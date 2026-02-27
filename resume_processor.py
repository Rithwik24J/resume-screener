import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

from nltk.corpus import stopwords

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return ' '.join(words)

def get_match_score(job_description, resume_text):
    # Preprocess both texts
    processed_jd = preprocess_text(job_description)
    processed_resume = preprocess_text(resume_text)
    
    # Calculate similarity using TF-IDF
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([processed_jd, processed_resume])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score * 100, 2)

def get_missing_keywords(job_description, resume_text):
    # Extract keywords from job description not in resume
    jd_words = set(preprocess_text(job_description).split())
    resume_words = set(preprocess_text(resume_text).split())
    missing = jd_words - resume_words
    # Filter short words
    missing = [w for w in missing if len(w) > 3]
    return sorted(missing)

def get_matching_keywords(job_description, resume_text):
    # Extract keywords that match
    jd_words = set(preprocess_text(job_description).split())
    resume_words = set(preprocess_text(resume_text).split())
    matching = jd_words & resume_words
    matching = [w for w in matching if len(w) > 3]
    return sorted(matching)