import streamlit as st
import PyPDF2
import os
import io
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.set_page_config(page_title="Resume Analyzer", page_icon=":mag_right:", layout="wide")    

st.title("Resume Analyzer") 
st.markdown("Upload your resume in PDF format and get insights on its content.")    

google_api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)

upload = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

job_description = st.text_area("Enter the job description for comparison", height=200)

analyze_button = st.button("Analyze Resume")

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_text)
    return response.text

if analyze_button and upload:
    try:
        file_content = extract_text_from_pdf(upload)
        
        if not file_content.strip():
            st.error("The uploaded file is empty or could not be read. Please upload a valid PDF file.")
            st.stop()
        
        prompt = f"Analyze the following resume content and compare it with the job description:\n\nResume Content:\n{file_content}\n\nJob Description:\n{job_description}"
        
        response = get_gemini_response(prompt)
        
        st.markdown("### Analysis Result")
        st.markdown(response)
    except Exception as e:
        st.error(f"An error occurred while processing the resume: {e}")
