import streamlit as st
from resume_parser import extract_resume_text
from grading_engine import check_length, check_keywords, check_sections

def calculate_ats_score(length, section_found, section_total, keyword_matched, keyword_total):
    score = 0

    # Section Score (40 pts)
    section_score = (len(section_found) / section_total) * 40
    score += section_score

    # Word Count Score (20 pts)
    if 400 <= length <= 800:
        score += 20
    elif 300 <= length < 400 or 800 < length <= 1000:
        score += 10
    else:
        score += 5

    # Keyword Match Score (40 pts)
    keyword_score = (len(keyword_matched) / keyword_total) * 40
    score += keyword_score

    return round(score, 1)


st.set_page_config(page_title="AI Resume Grader", page_icon="🧠")

st.title("🧠 AI Resume Grader")
st.markdown("Upload your resume to get instant feedback on structure, length, and keyword match.")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type="pdf")
 
if not uploaded_file:
    st.info("👈 Upload a PDF resume using the uploader on the left to begin.")
    st.image("https://cdn-icons-png.flaticon.com/512/3208/3208707.png", width=200)

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    text = extract_resume_text("temp_resume.pdf")

    st.subheader("📋 Resume Preview")
    st.text(text[:300] + "...")

    st.subheader("🧠 Grading Results")

    # Word count
    length = check_length(text)
    st.write(f"📝 **Word Count:** {length}")

    # Sections
    found, missing = check_sections(text)
    st.success(f"✅ Found Sections: {', '.join(found)}") if found else st.warning("No key sections found.")
    st.error(f"❌ Missing Sections: {', '.join(missing)}") if missing else st.success("All key sections included!")

    # Keyword match
    job_keywords = ["Python", "JavaScript", "SEO", "Cybersecurity", "Figma", "SQL"]
    count, matched = check_keywords(text, job_keywords)
    st.write(f"🔍 **Matched Keywords ({count}):** {', '.join(matched)}")

    # --- ATS SCORE ---
    ats_score = calculate_ats_score(
        length,
        found,
        6,  # Total expected sections
        matched,
        len(job_keywords)
        )
    st.subheader(f"📊 ATS Score: {ats_score}/100")
    if ats_score >= 85:
        st.success("Excellent! Your resume is well-optimized.")
    elif ats_score >= 60:
        st.warning("Good. But some improvements can boost your score.")
    else:
        st.error("Low ATS score. Improve keyword usage or structure.")


    if count < len(job_keywords) // 2:
        st.warning("⚠️ Try to include more job-relevant keywords.")
    else:
        st.success("✅ Great keyword usage!")

