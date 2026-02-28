# 🤖 AI Resume Screener

An AI-powered Resume Screening Application that analyzes how well a candidate’s resume matches a given job description using Natural Language Processing (NLP) techniques.

🚀 **Live Demo:** https://rithwik-resume-screener.streamlit.app

---

## 📌 Project Overview

The AI Resume Screener helps recruiters and candidates evaluate resume-job description compatibility automatically.

The application:
- Extracts text from resumes (PDF/DOCX)
- Processes job descriptions
- Applies NLP techniques
- Calculates similarity score
- Displays match percentage

This project demonstrates practical implementation of:
- Text preprocessing
- Vectorization
- Cosine Similarity
- Streamlit web deployment

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Libraries Used:**
  - scikit-learn
  - nltk / spacy (if used)
  - PyPDF2 / docx
  - pandas
  - numpy
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

---

## 🧠 Working Architecture

1. User uploads resume (PDF/DOCX)
2. User pastes job description
3. Text extraction is performed
4. Text cleaning and preprocessing
5. TF-IDF Vectorization
6. Cosine Similarity calculation
7. Match score displayed

---

## 📊 Features

✔ Resume upload support (PDF, DOCX)  
✔ Job description input  
✔ Automatic text extraction  
✔ Similarity score calculation  
✔ Clean UI using Streamlit  
✔ Deployed web application  

---

## 📂 Project Structure

```
AI-Resume-Screener/
│
├── app.py
├── requirements.txt
├── README.md
└── sample_resumes/
```

---

## ⚙ Installation (Run Locally)

Clone the repository:

```
git clone https://github.com/Rithwik24J/AI-Resume-Screener.git
cd AI-Resume-Screener
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

## 📈 Future Improvements

- Keyword highlighting
- Skill gap detection
- Resume ranking for multiple candidates
- BERT-based semantic matching
- ATS compatibility scoring
- Dashboard analytics for recruiters

---

## 🎯 Use Cases

- HR Resume Shortlisting
- Candidate Self-Evaluation
- Campus Placement Filtering
- Internship Screening

---

## 👨‍💻 Author
M.Rithwik
Final Year – Computer Science (AI & ML)  
Interested in Machine Learning, NLP, and AI-based Systems.

---

