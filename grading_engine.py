import nltk
nltk.data.path.append("/Users/paridhisharma/nltk_data")  # ✅ your punkt path

from nltk.tokenize import word_tokenize  # ✅ THIS was missing

def check_length(text):
    words = word_tokenize(text)
    return len(words)

def check_keywords(text, keywords):
    matched = [kw for kw in keywords if kw.lower() in text.lower()]
    return len(matched), matched

def check_sections(text):
    expected = ['Objective', 'Education', 'Skills', 'Projects', 'Experience', 'Certifications']
    found = [sec for sec in expected if sec.lower() in text.lower()]
    missing = list(set(expected) - set(found))
    return found, missing
