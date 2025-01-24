# Chatbot with Gemini API

This project implements a Django-based chatbot that answers user questions by directly accessing documentation URLs of various Customer Data Platforms (CDPs) and using the Google Gemini API for general queries. The chatbot does not rely on local storage of documentation files, ensuring that responses are based on the latest data available online.

## Project Overview

This chatbot is designed to help users find information related to four different CDPs:

*   **Segment** ([https://segment.com/docs/](https://segment.com/docs/))
*   **mParticle** ([https://docs.mparticle.com/](https://docs.mparticle.com/))
*   **Lytics** ([https://docs.lytics.com/](https://docs.lytics.com/))
*   **Zeotap** ([https://docs.zeotap.com/](https://docs.zeotap.com/))

If the user's question does not specifically mention any of these CDPs, the chatbot leverages the Google Gemini API for a more general response.

## Key Features

*   **Direct Web Access:** The chatbot dynamically fetches and processes data from documentation websites, rather than relying on local storage.
*   **Dynamic Scraping:** Fetches and extracts the text from the website that is specified in the user query.
*   **Gemini API Integration:** Uses the Gemini API for answering general questions that do not pertain to a specific CDP.
*   **Sentence Embeddings:** Utilizes Sentence Transformer models for semantic similarity search.
*   **Real-time Updates:** The chatbot will have up to date information, because it accesses the latest versions of the documentation in real time.
*   **User-Friendly Interface:** Implemented using a simple chat interface in Django, for ease of use.

## Architecture

The project follows a Django project structure with the following key components:

*   `cdp_chatbot/`: Django project folder
    *   `cdp_chatbot/`: Contains the Django project's settings and configurations.
    *   `chatbot/`: Django app folder
        *   `views.py`: Handles the request and responses with the help of django
        *   `utils.py`: Implements the web-scraping, text-preprocessing, and text-embedding logic.
        *   `templates/`: Contains the HTML template for the chat interface.
        *   `static/`: Contains CSS files for styling.
        *   `urls.py`: Contains URL mappings of the application
    *   `manage.py`: For managing Django commands.

## Tech Stack

*   **Python:** The core programming language for the project.
*   **Django:** For building the web application.
*   **Beautiful Soup 4:** For parsing HTML content from web pages.
*   **Requests:** For making HTTP requests to web URLs.
*   **Sentence Transformers:** For generating sentence embeddings to measure similarity between the user queries and documentation text.
*   **Scikit-Learn:** For calculating cosine similarity between the vectors.
*   **NumPy:** For numeric operations in Python.
*   **Google Generative AI:** For integrating with the Gemini large language model.
*   **python-dotenv:** To manage secret keys and variables.
* **Gunicorn:** Application server for deployment

## Setup and Installation

1.  **Clone Repository:**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```
2.  **Create Virtual Environment:**
    ```bash
    python -m venv venv
    ```
3.  **Activate Virtual Environment:**
     * **On Windows (cmd.exe):**
        ```
        venv\Scripts\activate
        ```
     * **On Windows (PowerShell):**
         ```
        venv\Scripts\activate
        ```
     * **On Linux/macOS:**
       ```bash
        source venv/bin/activate
       ```
4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    The requirements file will install the following libraries:
        *   `Django==5.1.5`
        *   `beautifulsoup4==4.12.3`
        *   `requests==2.31.0`
        *   `sentence-transformers==2.2.2`
        *   `scikit-learn==1.4.0`
        *   `numpy==1.26.4`
        *   `google-generativeai==0.2.0`
        *   `python-dotenv==1.0.1`

5.  **Set Environment Variables:**
    *   **`GOOGLE_API_KEY`**: Obtain a Google Gemini API key and set it as an environment variable.
    * **`SECRET_KEY`**: Set a secret key for your Django project.
        *You can do this by creating a `.env` file in the root directory and populating it with `GOOGLE_API_KEY="..."` and `SECRET_KEY="..."`
        *If you prefer to manage secrets manually then, you can directly set them in cmd with set or powershell using $env:.

6.  **Apply Migrations**
    ```bash
      python manage.py makemigrations
      python manage.py migrate
    ```

7.  **Run Development Server:**
    ```bash
    python manage.py runserver
    ```
    Access the application in your web browser at `http://127.0.0.1:8000/`.

## Usage

1.  **Open the Chatbot Interface**
    *   Access the URL in your browser and type your question in the input box.

2.  **Ask Questions**
    *   Ask questions pertaining to one of the following CDPs : Segment, mParticle, Lytics, or Zeotap. For example, "How do I create a segment in Segment?" or "How to create user profile in mParticle?".
    *   If no CDP is mentioned, the chatbot will use Gemini API for answering the questions. For example, you can ask "What is a Customer Data Platform?".

3.  **Receive Response:**
    *   The chatbot will provide an answer by fetching the relevant information from the chosen website, or by responding using Gemini API.

## Deployment to Render

The following steps will guide you to deploy this application to Render:

1.  **Prepare Project**: Make sure that you have `Procfile`, `requirements.txt`, and your Django project configured as described in this README.
2.  **Github Repository**: Push all your code to your Git repository
3.  **Create an Account:** Create an account on [Render](https://render.com).
4.  **Create a Web Service:** Connect your Git repository to render and create a new web service.
5.  **Set Environment Variables:** In Render settings, set the `GOOGLE_API_KEY` and `SECRET_KEY` environment variables.
6.  **Configure the Build and Start Commands:**
    *   **Build Command:** `pip install -r requirements.txt`

## Contributing

Feel free to fork the repository and submit pull requests with improvements, bug fixes, or additional features.

