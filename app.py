"""
AI_Resume_Builder
AI-Based Resume Enhancement & Portfolio Builder
Single-file Streamlit App (Classical NLP, No LLMs)
Deployable on Streamlit Cloud
"""

import streamlit as st
import PyPDF2
import re
from fpdf import FPDF
from sklearn.feature_extraction.text import TfidfVectorizer


# ======================================================
# Resume Parser (merged from resume_parser.py)
# ======================================================
def fix_text_spacing(text: str) -> str:
    """Fix spacing issues in PDF-extracted text by adding spaces between words"""
    if not text:
        return text
    
    # Add space before capital letters that follow lowercase letters or numbers
    text = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', text)
    
    # Add space after capital letters before lowercase (for acronyms like "AI" followed by word)
    text = re.sub(r'([A-Z]{2,})([a-z])', r'\1 \2', text)
    
    # Add space around special characters that should have spaces
    text = re.sub(r'([a-zA-Z0-9])([&|/])([a-zA-Z0-9])', r'\1 \2 \3', text)
    
    # Add space before numbers that follow letters
    text = re.sub(r'([a-zA-Z])(\d)', r'\1 \2', text)
    
    # Add space after numbers that precede letters
    text = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', text)
    
    # Normalize multiple spaces to single space
    text = re.sub(r'\s+', ' ', text)
    
    # Fix common patterns
    text = text.replace('&', ' & ')
    text = re.sub(r'\s+', ' ', text)  # Normalize again after replacements
    
    return text.strip()


def extract_text_from_pdf(uploaded_file) -> str:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    # Fix spacing issues in extracted text
    text = fix_text_spacing(text)
    return text.strip()


# ======================================================
# AI / NLP Logic (merged from resume_ai.py)
# ======================================================
def enhance_resume(resume_text: str) -> str:
    resume_text = " ".join(resume_text.split())

    if not resume_text:
        return (
            "Motivated student seeking opportunities to apply skills, "
            "gain professional experience, and contribute effectively to organizational goals."
        )

    vectorizer = TfidfVectorizer(stop_words="english", max_features=40)
    tfidf = vectorizer.fit_transform([resume_text])
    keywords = vectorizer.get_feature_names_out()

    top_keywords = list(keywords[:8]) if len(keywords) >= 8 else list(keywords)

    if not top_keywords:
        top_keywords = ["problem solving", "communication", "teamwork"]

    summary = (
        "Results-driven student with practical exposure to "
        + ", ".join(top_keywords)
        + ". Possesses strong analytical thinking, adaptability, and a continuous learning mindset. "
          "Actively seeking opportunities to contribute to impactful projects and grow professionally."
    )

    return summary


# ======================================================
# PDF Generator (merged from pdf_generator.py)
# ======================================================
def sanitize_text_for_pdf(text: str) -> str:
    """Remove or replace Unicode characters that can't be encoded in latin-1"""
    if not text:
        return ""
    # Replace common Unicode characters with ASCII equivalents
    replacements = {
        '\uf10b': '',  # Remove problematic characters
        '\u2013': '-',  # En dash
        '\u2014': '--',  # Em dash
        '\u2018': "'",  # Left single quotation mark
        '\u2019': "'",  # Right single quotation mark
        '\u201c': '"',  # Left double quotation mark
        '\u201d': '"',  # Right double quotation mark
        '\u2026': '...',  # Ellipsis
    }
    result = text
    for unicode_char, replacement in replacements.items():
        result = result.replace(unicode_char, replacement)
    # Remove any remaining non-ASCII characters that can't be encoded
    try:
        result.encode('latin-1')
        return result
    except UnicodeEncodeError:
        # If still has issues, remove all non-ASCII characters
        return result.encode('ascii', 'ignore').decode('ascii')


def create_enhanced_pdf(name, email, summary, resume_text) -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Sanitize all text inputs for PDF encoding
    safe_name = sanitize_text_for_pdf(name) if name else "Candidate Name"
    safe_email = sanitize_text_for_pdf(email) if email else "email@example.com"
    safe_summary = sanitize_text_for_pdf(summary) if summary else ""
    
    safe_text = sanitize_text_for_pdf(resume_text.strip() if resume_text else "")
    if len(safe_text) > 6000:
        safe_text = safe_text[:6000] + "\n\n[Content truncated for readability]"

    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, safe_name, ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(0, 8, safe_email, ln=True)

    pdf.ln(6)

    # Summary Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Enhanced Professional Summary", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 7, safe_summary)

    pdf.ln(4)

    # Resume Content Section
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "Extracted & Refined Resume Content", ln=True)

    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 6, safe_text if safe_text else "No resume text available.")

    output_file = "Enhanced_AI_Resume.pdf"
    pdf.output(output_file)
    return output_file


# ======================================================
# Streamlit UI (merged & cleaned app.py)
# ======================================================
st.set_page_config(
    page_title="AI Resume Enhancement & Builder",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Resume Enhancement & Portfolio Builder")
st.caption("Classical NLP (TF-IDF) + Rule-Based AI | No LLMs | Streamlit Cloud Ready")

st.info(
    "This application enhances resumes using **classical NLP techniques**. "
    "No Large Language Models, no paid APIs, and fully explainable AI."
)

option = st.radio(
    "Choose how you want to build your resume:",
    ["Upload Existing Resume (PDF)", "Create New Resume (Manual Input)"]
)

# ------------------------------------------------------
# Option 1: Upload Existing Resume
# ------------------------------------------------------
if option == "Upload Existing Resume (PDF)":
    uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
    name = st.text_input("Your Name")
    email = st.text_input("Email Address")

    if st.button("Enhance Resume"):
        if not uploaded_file:
            st.error("Please upload a PDF resume.")
        else:
            resume_text = extract_text_from_pdf(uploaded_file)
            enhanced_summary = enhance_resume(resume_text)
            pdf_path = create_enhanced_pdf(name, email, enhanced_summary, resume_text)

            st.subheader("AI-Enhanced Professional Summary")
            st.write(enhanced_summary)

            with open(pdf_path, "rb") as f:
                st.download_button(
                    "⬇️ Download Enhanced Resume (PDF)",
                    data=f,
                    file_name="Enhanced_AI_Resume.pdf",
                    mime="application/pdf"
                )

# ------------------------------------------------------
# Option 2: Create Resume from Scratch
# ------------------------------------------------------
else:
    st.subheader("Enter Your Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    skills = st.text_area("Skills (comma separated)")
    projects = st.text_area("Projects / Experience")

    if st.button("Generate Resume"):
        combined_text = f"{skills}\n{projects}".strip()
        enhanced_summary = enhance_resume(combined_text)
        pdf_path = create_enhanced_pdf(name, email, enhanced_summary, combined_text)

        st.subheader("Generated Professional Summary")
        st.write(enhanced_summary)

        with open(pdf_path, "rb") as f:
            st.download_button(
                "⬇️ Download Resume (PDF)",
                data=f,
                file_name="AI_Resume.pdf",
                mime="application/pdf"
            )
