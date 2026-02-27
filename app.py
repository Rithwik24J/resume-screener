import streamlit as st
import pdfplumber
import docx
from resume_processor import get_match_score, get_missing_keywords, get_matching_keywords

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# Page configuration
st.set_page_config(page_title="Resume Screener", page_icon="📄", layout="wide")

st.title("📄 AI Resume Screener")
st.markdown("Upload your resume and paste the job description to see how well you match!")

# Two column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Job Description")
    job_description = st.text_area("Paste the job description here", height=300)

with col2:
    st.subheader("📎 Upload Resume")
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
    resume_text = ""
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            resume_text = extract_text_from_docx(uploaded_file)
        st.success("Resume uploaded successfully!")

# Analyze button
if st.button("🔍 Analyze Match", use_container_width=True):
    if not job_description:
        st.error("Please paste a job description!")
    elif not resume_text:
        st.error("Please upload your resume!")
    else:
        score = get_match_score(job_description, resume_text)
        missing = get_missing_keywords(job_description, resume_text)
        matching = get_matching_keywords(job_description, resume_text)

        st.markdown("---")
        st.subheader("📊 Results")

        # Score display
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Match Score", f"{score}%")
        with col_b:
            st.metric("Matching Keywords", len(matching))
        with col_c:
            st.metric("Missing Keywords", len(missing))

        # Score feedback
        if score >= 70:
            st.success("Great match! Your resume aligns well with this job.")
        elif score >= 40:
            st.warning("Moderate match. Consider adding more relevant keywords.")
        else:
            st.error("Low match. Your resume needs significant improvements for this role.")

        # Keywords
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("✅ Matching Keywords")
            if matching:
                st.write(", ".join(matching))
            else:
                st.write("No matching keywords found.")

        with col4:
            st.subheader("❌ Missing Keywords")
            if missing:
                st.write(", ".join(missing))
            else:
                st.write("No missing keywords!")

        st.markdown("---")
        st.subheader("💡 Suggestions")
        if missing:
            st.write(f"Consider adding these keywords to your resume: **{', '.join(missing[:10])}**")
        else:
            st.write("Your resume covers all the key terms from the job description!")