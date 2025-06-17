from resume_parser import extract_resume_text
from grading_engine import check_length, check_keywords, check_sections

# Load your resume text
text = extract_resume_text("sample_resume.pdf")

# 1. Word count
length = check_length(text)
print(f"📝 Word Count: {length}")

# 2. Sections check
found, missing = check_sections(text)
print(f"✅ Found Sections: {found}")
print(f"❌ Missing Sections: {missing}")

# 3. Keyword match check
job_keywords = ["Python", "JavaScript", "SEO", "Cybersecurity", "Figma", "SQL"]
count, matched = check_keywords(text, job_keywords)
print(f"🔍 Keywords Matched ({count}): {matched}")
