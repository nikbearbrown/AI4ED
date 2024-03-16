# Multilanguage Invoice Extractor 
 
## Project Objective 
The Multilanguage Invoice Extractor is designed to simplify the processing of invoice images by extracting relevant information using the Google Gemini Pro Vision model. This Streamlit-based web application supports multiple languages, making it easier for users globally to handle invoices from different regions and in various formats. 

## Requirements 
- Python 3.8 or above 
- Streamlit 
- A Google Cloud account with Gemini Pro Vision API access 
- Other dependencies listed in `requirements.txt`  

## Installation Steps
Clone this repository to your local machine: 

    git clone https://your-repository-link.git 
    cd your-repository-directory
    pip install -r requirements.txt

## Setting Up Your Environment

Set up your environment variables before running the application:

1.  Create a `.env` file in the root directory of the project.
    
2.  Add your Google API key to the `.env` file:
    
    arduinoCopy code
    
    `GOOGLE_API_KEY='your_google_api_key_here'` 
    

Replace `'your_google_api_key_here'` with your actual Google API key.

## Running the Application

To start the Streamlit app, navigate to the project directory in your terminal and run:
`streamlit run app.py` 

Open the provided URL in a web browser to access the application.


  
Certainly! Here's a complete README.md content for your Multilanguage Invoice Extractor project. You can copy this into your README.md file and adjust any details as necessary:

markdownCopy code

``# Multilanguage Invoice Extractor

## Project Objective
The Multilanguage Invoice Extractor is designed to simplify the processing of invoice images by extracting relevant information using the Google Gemini Pro Vision model. This Streamlit-based web application supports multiple languages, making it easier for users globally to handle invoices from different regions and in various formats.

## Requirements
To run this project, you will need:

- Python 3.8 or above
- Streamlit
- A Google Cloud account with Gemini Pro Vision API access
- Other dependencies listed in `requirements.txt`

## Installation
Clone this repository to your local machine:

    ```bash
    git clone https://your-repository-link.git
    cd your-repository-directory`` 

Install the required Python packages:

`pip install -r requirements.txt` 

## Setting Up Your Environment

Set up your environment variables before running the application:

1.  Create a `.env` file in the root directory of the project.
    
2.  Add your Google API key to the `.env` file:
    
    arduinoCopy code
    
    `GOOGLE_API_KEY='your_google_api_key_here'` 
    

Replace `'your_google_api_key_here'` with your actual Google API key.

## Running the Application

To start the Streamlit app, navigate to the project directory in your terminal and run:

bashCopy code

`streamlit run app.py` 

Open the provided URL in a web browser to access the application.

## Usage

To use the Multilanguage Invoice Extractor, follow these steps:

1.  **Input Prompt**: Enter the specific details or questions you want to extract from the invoice.
2.  **Upload Invoice**: Click on 'Choose an image of the invoice' to upload an invoice image. Supported formats are JPG, JPEG, and PNG.
3.  **Generate Information**: After uploading the image, click on the 'Tell me about the invoice' button to extract information from the uploaded invoice based on your input prompt.
