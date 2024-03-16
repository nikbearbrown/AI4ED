import os
import tempfile
from pytube import YouTube, Playlist
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import streamlit as st
import openai
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Access your API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# For example, setting the OpenAI API key
openai.api_key = openai_api_key

def download_and_transcribe_selected_videos(playlist_url, selected_titles):
    playlist = Playlist(playlist_url)
    transcriptions = {}

    for video_url in playlist.video_urls:
        yt = YouTube(video_url)
        video_title = yt.title

        if video_title in selected_titles:
            print(f"Downloading and transcribing video: {video_title}")
            audio_path = download_audio_from_youtube(video_url)
            transcription = get_large_audio_transcription_on_silence(audio_path)
            transcriptions[video_title] = transcription
            os.remove(audio_path)

    return transcriptions

def download_audio_from_youtube(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_path = tempfile.gettempdir()
    audio_stream.download(output_path=output_path)
    return os.path.join(output_path, audio_stream.default_filename)

def transcribe_audio(path):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio_listened = r.record(source)
        try:
            text = r.recognize_google(audio_listened)
            return text
        except sr.UnknownValueError as e:
            return "Error: " + str(e)
        except sr.RequestError as e:
            return "API Error: " + str(e)

def get_large_audio_transcription_on_silence(path):
    sound = AudioSegment.from_file(path)
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=sound.dBFS-14, keep_silence=500)

    folder_name = tempfile.mkdtemp()
    whole_text = ""
    for i, audio_chunk in enumerate(chunks, start=1):
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        text = transcribe_audio(chunk_filename)
        if not text.startswith("Error"):
            text = f"{text.capitalize()}. "
            whole_text += text

    # Clean up
    for file in os.listdir(folder_name):
        os.remove(os.path.join(folder_name, file))
    os.rmdir(folder_name)

    return whole_text

def summarize_text(text, openai_api_key):
    openai.api_key = openai_api_key
    prompt = (
        "Create a concise, informative summary suitable for professors, students and general audiences that provides a comprehensive overview of the following video content:\n\n"
        f"{text}"
    )

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=200  # Adjust the number of tokens as needed
    )
    return response.choices[0].text.strip()

def generate_quiz_questions(api_key, context, difficulty, number_of_questions):
    openai.api_key = api_key

    formatted_prompt = (
        f"Create {number_of_questions} advanced, master's level standard questions based on the following {difficulty} text. "
        "Each question should:\n\n"
        "1. Be based on the context provided.\n"
        "2. Include a variety of question types:\n"
        "   - Single correct option e.g., What is the capital of France? \nA. Berlin \n B. Madrid \n C. Paris \n D. London)\n"
        "   - Multiple correct options (e.g., Which of the following are European countries? \nA. Egypt \nB. Spain \nC. Italy \nD. Nigeria)\n"
        "   - Text entry (e.g., Who wrote 'Romeo and Juliet'?)\n"
        "   - Numeric entry (e.g., What is the square root of 144?)\n"
        "3. For multiple choice questions, include 4 options (labeled A to D, each option on new line), with one or more correct answers and plausible but incorrect alternatives.\n"
        "4. For text or numeric entry, require a specific, correct answer.\n"
        "5. Reflect high academic standards in both content and formulation.\n"
        "6. Provide correct answer and display it on a new line and provide a brief explanation for the correct answer, highlighting key concepts or reasoning and display it on new line.\n\n"
        "Context for questions:\n\n" + context
    )
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=formatted_prompt,
        max_tokens=250 * number_of_questions
    )
    return response.choices[0].text.strip()

def main():
    st.title("EduTube QuizBuilder")

    playlist_url = st.text_input("Enter the URL of the YouTube Playlist")

    if playlist_url:
        playlist = Playlist(playlist_url)
        video_titles = [YouTube(url).title for url in playlist.video_urls]

        # Session state for selected titles
        if 'selected_titles' not in st.session_state:
            st.session_state['selected_titles'] = []

        selected_titles = st.multiselect("Select videos to transcribe or summarize", video_titles, default=st.session_state['selected_titles'])

        # Update session state
        st.session_state['selected_titles'] = selected_titles

        # Transcription and summarization options
        user_choice = st.radio("Choose an action", ("Transcribe", "Summarize"))

        if st.button("Process Selected Videos"):
            with st.spinner('Processing selected videos...'):
                try:
                    transcriptions = download_and_transcribe_selected_videos(playlist_url, st.session_state['selected_titles'])
                    
                    if user_choice == "Summarize":
                        # Store summaries in session state
                        st.session_state['result'] = {title: summarize_text(text, openai_api_key) for title, text in transcriptions.items()}
                    else:
                        # Store transcriptions in session state
                        st.session_state['result'] = transcriptions

                    # Display results
                    for title, content in st.session_state['result'].items():
                        st.subheader(title)
                        st.write(content)

                except Exception as e:
                    st.error(f"An error occurred: {e}")

        # Quiz creation option
        if 'result' in st.session_state and st.checkbox("Create a quiz based on this content?"):
            difficulty = st.selectbox("Select difficulty level", ["Easy", "Moderate", "Difficult", "Master"])
            number_of_questions = st.number_input("Number of questions", min_value=1, value=5)

            if st.button("Generate Quiz"):
                # Aggregate all content for quiz context
                context = " ".join(st.session_state['result'].values())
                quiz_questions = generate_quiz_questions(openai_api_key, context, difficulty, number_of_questions)
                st.subheader("Quiz Questions")
                st.write(quiz_questions)

if __name__ == "__main__":
    main()