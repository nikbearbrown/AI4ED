# EduTube QuizBuilder

EduTube QuizBuilder is an innovative tool designed to leverage the power of OpenAI and YouTube for educational purposes. This Python-based application utilizes the Streamlit framework to provide a user-friendly interface, enabling educators, students, and content creators to fetch, transcribe, summarize, create comprehensive lesson plans and even create notes for students from YouTube videos or playlists. Additionally, it offers a unique feature to generate quiz questions based on video transcriptions, making it an invaluable resource for enhancing learning experiences.

## Features

- **Video Transcription**: Automatically transcribe YouTube videos or entire playlists, providing accessible written content for further analysis or study.
- **Content Summarization**: Utilize OpenAI's GPT model to summarize video content, extracting key insights and important facts in a concise format.
- **Lesson Plan Creation**: Generate detailed lesson plans from video transcriptions, tailored for Master's level education, including learning objectives, discussion questions, and activities.
- **Student Notes Generation**: Leverage OpenAI's GPT model to produce concise, easy-to-understand notes from video transcriptions. This feature focuses on distilling the most important points and concepts into student-friendly notes, aiding in revision and comprehension.
- **Quiz Question Generation**: Create advanced, customizable quiz questions based on video transcriptions, supporting different difficulty levels and educational standards.

## Installation

To use EduTube QuizBuilder, follow these steps:

1. **Clone the repository**:

   ```
   git clone <repository-url>
   ```

2. **Install the required packages**:

   ```
   pip install -r requirements.txt
   ```

   This command installs Streamlit, OpenAI, PyTube, the YouTube Transcript API, and other dependencies.

3. **Set up environment variables**:

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=<Your-OpenAI-API-Key>
   ```

   To create and activate a virtual environment, follow these steps. This process is crucial for managing dependencies and ensuring that your project's packages don't conflict with those of other Python projects on your system.
   
    **Creating a Virtual Environment**
   
   1. **Navigate to your project directory**:
   
      Open a terminal or command prompt and navigate to the directory where you've cloned or placed the EduTube QuizBuilder project.
   
      ```
      cd path/to/EduTubeQuizBuilder
      ```
   
   2. **Create the virtual environment**:
   
      - **For Windows**:
   
        ```
        python -m venv venv
        ```
   
      - **For macOS and Linux**:
   
        ```
        python3 -m venv venv
        ```
   
      This command creates a new directory named `venv` in your project folder, where the virtual environment files are stored.
4. **Activating the Virtual Environment**:

     After creating the virtual environment, you need to activate it to use it for your project.
   
   - **For Windows**:
   
     ```
     .\venv\Scripts\activate
     ```
   
   - **For macOS and Linux**:
   
     ```
     source venv/bin/activate
     ```
   
   You'll know that your virtual environment is activated because your terminal's prompt will now include `(venv)`, indicating that any Python or pip commands you use will now affect only this virtual environment.
5. **Installing Dependencies**:

   With the virtual environment activated, install the project dependencies using pip:
   
   ```
   pip install -r requirements.txt
   ```
   
   This ensures that all the required Python packages, including Streamlit, OpenAI, PyTube, and others, are installed within the virtual environment.

6. **Usage**

   To run EduTube QuizBuilder, execute the following command:
   
   ```
   streamlit run app.py
   ```
   
   Upon launching, you'll be greeted by the Streamlit interface where you can choose between processing a single YouTube video or a playlist. Depending on your selection, you can transcribe the video(s), generate summaries, create lesson plans, or generate quiz questions based on the content.

### Key Functionalities:

- **Transcribe YouTube Videos/Playlists**: Input the URL of the video or playlist you wish to transcribe.
- **Summarize Video Content**: After transcription, opt to summarize the content to highlight key points.
- **Generate Lesson Plans**: Create comprehensive lesson plans based on video transcriptions, suitable for advanced educational settings.
- **Create Notes**: Create concise notes for studnets based on video transcriptions.
- **Create Quiz Questions**: Generate quiz questions from the transcriptions, tailored to various difficulty levels.

## Contributing

Contributions to EduTube QuizBuilder are welcome! If you have suggestions for improvements or encounter any issues, please feel free to open an issue or submit a pull request.

## License

EduTube QuizBuilder is released under the MIT License. See the LICENSE file for more details.
