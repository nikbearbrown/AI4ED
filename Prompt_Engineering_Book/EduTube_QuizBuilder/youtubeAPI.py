import os
import streamlit as st
import openai
from dotenv import load_dotenv
from pytube import YouTube, Playlist
from youtube_transcript_api import YouTubeTranscriptApi

# Load the environment variables from .env file
load_dotenv()

# Access your API key
openai_api_key = os.getenv('OPENAI_API_KEY')

# For example, setting the OpenAI API key
openai.api_key = openai_api_key

def fetch_transcript_for_video(video_url):
    video_id = video_url.split("watch?v=")[-1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return compile_transcript(transcript)
    except Exception as e:
        print(f"An error occurred while fetching the transcript: {e}")
        return "Transcript could not be fetched."

def compile_transcript(transcript):
    output = ''
    for x in transcript:
        sentence = x['text']
        output += f' {sentence}\n'
    return output.strip()

def process_video(url):
    video_id = url.split("watch?v=")[-1]
    yt = YouTube(url)
    video_title = yt.title
    # print(f"Fetching transcript for video: {video_title}")
    transcription = fetch_transcript_for_video(video_id)
    return {video_title: transcription}

def download_and_transcribe_selected_videos(playlist_url, selected_titles):
    playlist = Playlist(playlist_url)
    transcriptions = {}

    for video_url in playlist.video_urls:
        yt = YouTube(video_url)
        video_title = yt.title

        if video_title in selected_titles:
            # print(f"Fetching transcript for video: {video_title}")
            transcription = fetch_transcript_for_video(video_url)
            transcriptions[video_title] = transcription

    return transcriptions

def summarize_text(text, openai_api_key):
    openai.api_key = openai_api_key
    prompt = (
        "Summarize the text below and give me a list of bullet points with key insights and the most important facts of the following video content:\n\n"
        # "Create a concise, informative summary suitable for professors, students, and general audiences that provides a comprehensive overview of the following video content:\n\n"
        f"{text}"
    )

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000  # Adjust the number of tokens as needed
    )
    return response.choices[0].text.strip()

def generate_quiz_questions(api_key, context, difficulty, number_of_questions):
    openai.api_key = api_key

    formatted_prompt = (
        f"Create {number_of_questions} advanced, master's level standard questions based on the following {difficulty} text. "
        "Each MCQ question should:\n\n"
        "1. Be based on the context provided and it should have 4 options show 4 options on 4 new lines.\n"
        "2. Include a variety of question types:\n"
        "3. Provide correct answer and display it on a new line\n\n"
        "4. Provide explanation of correct answer and display it on a new line\n\n"
        "Context for questions:\n\n" + context
    )
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=formatted_prompt,
        max_tokens=250 * number_of_questions
    )
    return response.choices[0].text.strip()

def generate_lesson_plan(api_key, transcription, topic):
    openai.api_key = api_key

    # Construct the prompt for generating the lesson plan
    prompt = f"""
    Given the following transcription of a YouTube video on {topic}, create a detailed lesson plan for Master's students. The lesson plan should include:

    1. An engaging introduction to the topic.
    2. A breakdown of the main concepts covered in the video, organized into sections.
    3. Learning objectives for each section.
    4. Questions for discussion or reflection.
    5. Activities or assignments to reinforce the learning objectives.
    6. A summary of key takeaways.

    Transcription: {transcription}
    """

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  
        prompt=prompt,
        temperature=0.8,
        max_tokens=1500,  
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return response.choices[0].text.strip()

def generate_student_notes(api_key, transcription, topic):
    openai.api_key = api_key

    # Construct the prompt for generating student notes
    prompt = f"""
    Given the following transcription on {topic}, create a concise, easy-to-understand notes for students and write it in bullet points in student friendly manner.

    Transcription: {transcription}
    """

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct", 
        prompt=prompt,
        temperature=0.8,
        max_tokens=1500,  
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    return response.choices[0].text.strip()



def main():
    st.title("EduTube QuizBuilder")
    # Asking user what they would like to input
    user_input_type = st.radio("Enter a YouTube Video or a YouTube Playlist URL?",
        ("YouTube Video", "YouTube Playlist"),
        key="input_type_selection"  # Unique key to avoid DuplicateWidgetID error
    )

    # if user_input_type == "YouTube Playlist":
    #     playlist_url = st.text_input("Enter the URL of the YouTube Playlist")

    #     if playlist_url:
    #         playlist = Playlist(playlist_url)
    #         video_titles = [YouTube(url).title for url in playlist.video_urls]

    #         if 'selected_titles' not in st.session_state:
    #             st.session_state['selected_titles'] = []

    #         selected_titles = st.multiselect("Select videos to transcribe or summarize", video_titles, default=st.session_state['selected_titles'])

    #         st.session_state['selected_titles'] = selected_titles

    #         user_choice = st.radio(
    #             "Choose an action",
    #             ("Transcribe", "Summarize"),
    #             key="action_selection"  # Another unique key
    #         )

    #         if st.button("Process Selected Videos"):
    #             with st.spinner('Processing selected videos...'):
    #                 try:
    #                     transcription_playlist = download_and_transcribe_selected_videos(playlist_url, st.session_state['selected_titles'])
                        
    #                     if user_choice == "Summarize":
    #                         st.session_state['result'] = {title: summarize_text(text, openai_api_key) for title, text in transcription_playlist.items()}
    #                     else:
    #                         st.session_state['result'] = transcription_playlist

    #                     for title, content in st.session_state['result'].items():
    #                         st.subheader(title)
    #                         st.write(content)

    #                 except Exception as e:
    #                     st.error("You have entered a video URL, please input a YouTube playlist URL instead.")

    # elif user_input_type == "YouTube Video":
    #     video_url = st.text_input("Enter the URL of the YouTube Video")

    #     if video_url:
    #         user_choice = st.radio(
    #             "Choose an action",
    #             ("Transcribe", "Summarize"),
    #             key="action_selection"  # Another unique key
    #         )
    #         if st.button("Process Video"):
    #             with st.spinner('Fetching video details...'):
    #                 try:
    #                     transcription_video = process_video(video_url)
    #                     # print(transcription_video)
    #                     if user_choice == "Summarize":
    #                             st.session_state['result'] = {title: summarize_text(text, openai_api_key) for title, text in transcription_video.items()}
    #                     else:
    #                         st.session_state['result'] = transcription_video


    #                     for title, content in st.session_state['result'].items():
    #                         st.subheader(title)
    #                         st.write(content)
    #                 except Exception as e:
    #                     st.error(f"{e}")
                    
    if user_input_type == "YouTube Playlist":
        playlist_url = st.text_input("Enter the URL of the YouTube Playlist")

        if playlist_url:
            playlist = Playlist(playlist_url)
            # print(playlist)
            video_titles = [YouTube(url).title for url in playlist.video_urls]
            
            if 'selected_titles' not in st.session_state:
                st.session_state['selected_titles'] = []

            selected_titles = st.multiselect("Select videos to transcribe, summarize, or create a lesson plan from",
                                             video_titles,
                                             default=st.session_state['selected_titles'])
            st.session_state['selected_titles'] = selected_titles

            user_choice = st.radio("Choose an action",
                                   ("Transcribe", "Summarize", "Create Lesson Plan", "Create Notes"),
                                   key="action_selection")

    elif user_input_type == "YouTube Video":
        video_url = st.text_input("Enter the URL of the YouTube Video")
        if video_url:
            user_choice = st.radio("Choose an action",
                                   ("Transcribe", "Summarize", "Create Lesson Plan","Create Notes"),  
                                   key="video_action_selection")

    if st.button("Process"):
        with st.spinner('Processing...'):
            try:
                if user_input_type == "YouTube Playlist" and playlist_url:
                    processed_data = download_and_transcribe_selected_videos(playlist_url, st.session_state['selected_titles'])
                elif user_input_type == "YouTube Video" and video_url:
                    processed_data = process_video(video_url)
                else:
                    processed_data = {}
                    st.error("Please enter a valid URL.")

                # Process based on the selected action
                if user_choice == "Summarize":
                    st.session_state['result'] = {title: summarize_text(text, openai_api_key) for title, text in processed_data.items()}
                elif user_choice == "Transcribe":
                    st.session_state['result'] = processed_data
                    st.session_state['transcription_for_quiz'] = processed_data
                elif user_choice == "Create Notes":
                    st.session_state['result'] = {
                        title: generate_student_notes(
                            openai_api_key,
                            text,
                            title
                        ) for title, text in processed_data.items()
                    }
                elif user_choice == "Create Lesson Plan":
                    st.session_state['result'] = {
                        title: generate_lesson_plan(
                            openai_api_key,
                            text,
                            title  # Topic is assumed to be the video title
                        ) for title, text in processed_data.items()
                    }

                for title, content in st.session_state['result'].items():
                    st.subheader(title)
                    st.write(content)

            except Exception as e:
                st.error(f"An error occurred: {e}")


    # Quiz creation option (this part remains common and should be outside the if-elif block if both input types allow for quiz creation)
    if 'transcription_for_quiz' in st.session_state and st.checkbox("Create a quiz based on this content?"):
        difficulty = st.selectbox("Select difficulty level", ["Easy", "Moderate", "Difficult", "Master"])
        number_of_questions = st.number_input("Number of questions", min_value=1, value=5)

        if st.button("Generate Quiz"):
            context = " ".join(st.session_state['transcription_for_quiz'].values())
            quiz_questions = generate_quiz_questions(openai_api_key, context, difficulty, number_of_questions)
            st.subheader("Quiz Questions")
            st.write(quiz_questions)

if __name__ == "__main__":
    main()