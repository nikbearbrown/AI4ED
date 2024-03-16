# Blog Generation Project

## Project Objective
The Blog Generation Project leverages the LLaMA 2 language model to automate the creation of blogs across different styles and topics. Utilizing the Streamlit framework, this application offers a user-friendly interface for generating tailored blog content, making it easier for writers, researchers, and data scientists to produce relevant and engaging articles efficiently.

## Requirements
To run this project, the following are required:

- Python 3.8 or above
- Streamlit
- LangChain
- Other dependencies listed in `requirements.txt`

## Installation
To set up this project locally:

1. Clone this repository to your local machine:

   ```bash
   git clone https://your-repository-link.git
   cd your-project-directory`` 

2.  Install the necessary Python packages:
    
    `pip install -r requirements.txt` 
    

## Running the Application

Execute the following command within the project directory to start the Streamlit app:

`streamlit run app.py` 

Then, navigate to the provided URL to access the web interface.

## Usage

Follow these steps to generate blog content:

1.  **Enter the Blog Topic**: Input the main topic or title of your desired blog post.
2.  **Specify the Number of Words**: Input the desired length of your blog post.
3.  **Choose the Blog Style**: Select the target audience or style of the blog from the dropdown (e.g., Researchers, Data Scientist, Common People).
4.  **Generate**: Click the 'Generate' button to produce the blog content based on your specifications.

## Customization

The application uses the LLaMA 2 model for content generation. You can adjust the model settings, such as `max_new_tokens` and `temperature`, to fine-tune the generated content's length and creativity.
