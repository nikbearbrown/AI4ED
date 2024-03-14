# Chat with any Website

Chat with any Website is a project created by Agash Uthayasuriyan that utilizes Pinecone, OpenAI Embeddings, OpenAI LLM, and Streamlit to create a chat interface integrated with a website. This project aims to demonstrate the integration of advanced language models and embeddings to facilitate engaging and responsive interactions within a website.

## Problem Statement
GPTs such as ChatGPT are unable to give information about latest updates happening in the world. When there is a tech. product or a news that is released, current GPTs are unable to give reliable information about the same. This project aims to bridge the gap and presents a conversational bot between the user and the website. This would be beneficial for the user to quickly pull information from the website without spending much time in reading the entire content.

## Technologies Used
- Pinecone
- OpenAI Embeddings
- OpenAI LLM
- Streamlit

## Demo
Check out the demo of the project on [YouTube](https://www.youtube.com/watch?v=SucwaESC34s).

## Installation and Setup
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Chat-with-Website.git
   cd Chat-with-Website
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Unix/macOS
    venv\Scripts\activate      # For Windows
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialise environment variables:

   Create .env file in the root directory and initialize the keys for OpenAI and Pinecone as shown in dummyenv file

4. Run the Streamlit Application:
   ```bash
   streamlit run app.py
   ``` 
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
