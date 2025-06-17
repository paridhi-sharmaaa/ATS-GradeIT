from resume_parser import extract_resume_text

resume_text = extract_resume_text("sample_resume.pdf")
print(resume_text[:])  # print first 500 characters
