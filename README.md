# Resume Analyzer

A Streamlit web application that analyzes a resume against a job description using the power of Google's Gemini API. This tool helps you to quickly assess the suitability of a candidate's resume for a particular job role.

## Features

*   **Resume Upload:** Upload resumes in PDF format.
*   **Job Description Input:** Paste the job description for comparison.
*   **AI-Powered Analysis:** Utilizes Google's Gemini API to provide a detailed analysis of the resume against the job description.
*   **User-Friendly Interface:** A simple and intuitive web interface built with Streamlit.

## Technologies Used

*   **Python:** The core programming language.
*   **Streamlit:** For building the interactive web application.
*   **Google Generative AI:** For the resume analysis and comparison.
*   **PyPDF2:** To extract text from PDF resumes.
*   **Dotenv:** To manage environment variables.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/resume-analyzer.git
    cd resume-analyzer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    # source .venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt # Assuming you have a requirements.txt, if not, create one from pyproject.toml
    ```

4.  **Create a `.env` file:**
    Create a file named `.env` in the root directory of the project and add your Google API key:
    ```
    GOOGLE_API_KEY=your-google-api-key
    ```
    You can get your Google API key from [Google AI Studio](https://aistudio.google.com/).

5.  **Run the application:**
    ```bash
    streamlit run main.py
    ```

## Usage

1.  Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
2.  Upload a resume in PDF format using the file uploader.
3.  Paste the job description into the text area.
4.  Click the "Analyze Resume" button to get the analysis.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
