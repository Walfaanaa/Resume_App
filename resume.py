import streamlit as st
from datetime import datetime
from fpdf import FPDF
from PyPDF2 import PdfMerger
import requests
from io import BytesIO

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Walfaanaa Resume", page_icon="📄", layout="centered")

# ================= DATE =================
today_date = datetime.today().strftime("%B %d, %Y")

# ================= FILE LINKS =================
BASE_URL = "https://raw.githubusercontent.com/Walfaanaa/Resume_App/main/"

files = {
    "MSc Certificate": BASE_URL + "MSc_certificate.pdf",
    "MBA Certificate": BASE_URL + "MBA_certificate.pdf",
    "BSc Certificate": BASE_URL + "BSc_certificate.pdf",
}

exp_files = {
    "Experience Proof": BASE_URL + "Experience.pdf"
}

# ================= HEADER =================
st.markdown(f"""
### 📄 Curriculum Vitae  
**Date:** {today_date}  
**Walfaanaa Magarsaa**  
📞 +251912861288 | 📧 walfanamegersa3@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/walfaanaa-magarsaa/
""")

st.divider()

# ================= APPLICATION =================
st.subheader("📨 Job Application")

company = st.text_input("🏢 Company Name")
position = st.text_input("💼 Position")

application_text = st.text_area("✍️ Write Application", height=150)

if st.button("✨ Generate Application"):
    application_text = f"""
I am writing to apply for the position of {position or 'the role'} at {company or 'your organization'}.

With strong skills in SQL, Python, BI tools, and Machine Learning, I can contribute effectively.

I have experience in data analytics, dashboards, and ETL processes.

Thank you for your consideration.
"""

# ================= PREVIEW =================
st.subheader("📄 Preview")

st.write(f"Date: {today_date}")
st.write(f"To: {company or '________'}")
st.write(f"Position: {position or '________'}")

st.write("Dear Hiring Manager,")

st.write(application_text or "Your application will appear here...")

st.write("Sincerely,")
st.write("Walfaanaa Magarsaa")

st.divider()

# ================= PROFILE =================
col1, col2 = st.columns([1, 3])

with col1:
    st.image("1728453971208.jpg", width=140)

with col2:
    st.title("Walfaanaa Magarsaa")
    st.write("Data Analyst | Data Scientist | BI Developer")

st.divider()

# ================= EDUCATION =================
st.subheader("🎓 Education")
st.write("""
- MSc Computational Data Science (2024)
- MBA Business Administration (2020)
- BSc Statistics (2016)
""")

st.markdown("### 📄 View Certificates")
for name, url in files.items():
    st.link_button(f"📄 {name}", url)

# ================= EXPERIENCE =================
st.subheader("💼 Experience")
st.write("""
- Cooperative Bank of Oromia
- INSA Data Analytics
- CSA Supervisor
""")

st.markdown("### 📄 Experience Evidence")
for name, url in exp_files.items():
    st.link_button(f"📄 {name}", url)

st.divider()

# ================= SKILLS =================
st.subheader("🧠 Skills")
st.write("""
- SQL, Python
- Power BI, Tableau, Excel
- Machine Learning
""")

st.divider()

# ================= CREATE CV PDF =================
def create_cv_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    lines = [
        "Curriculum Vitae",
        f"Date: {today_date}",
        "",
        "Walfaanaa Magarsaa",
        "Email: walfanamegersa3@gmail.com",
        "Phone: +251912861288",
        "",
        "APPLICATION",
        f"To: {company or ''}",
        f"Position: {position or ''}",
        "",
        application_text or "",
        "",
        "EDUCATION",
        "MSc Computational Data Science",
        "MBA Business Administration",
        "BSc Statistics",
        "",
        "EXPERIENCE",
        "Cooperative Bank of Oromia",
        "INSA Data Analytics",
        "CSA Supervisor",
        "",
        "SKILLS",
        "SQL, Python, BI Tools, Machine Learning"
    ]

    for line in lines:
        pdf.multi_cell(0, 8, line)

    return pdf.output(dest="S").encode("latin-1")

# ================= MERGE PDF =================
def merge_all_pdfs():
    merger = PdfMerger()

    # Add CV
    merger.append(BytesIO(create_cv_pdf()))

    # Add certificates
    for url in files.values():
        try:
            response = requests.get(url)
            merger.append(BytesIO(response.content))
        except:
            pass

    # Add experience
    for url in exp_files.values():
        try:
            response = requests.get(url)
            merger.append(BytesIO(response.content))
        except:
            pass

    output = BytesIO()
    merger.write(output)
    merger.close()

    return output.getvalue()

# ================= DOWNLOAD SECTION =================
st.subheader("⬇️ Download")

# CV only
cv_pdf = create_cv_pdf()
st.download_button(
    "📄 Download CV (PDF)",
    data=cv_pdf,
    file_name="Walfaanaa_CV.pdf",
    mime="application/pdf"
)

# Full package
full_pdf = merge_all_pdfs()
st.download_button(
    "📦 Download FULL Package (CV + Certificates)",
    data=full_pdf,
    file_name="Walfaanaa_Full.pdf",
    mime="application/pdf"
)
