import streamlit as st
from datetime import datetime
from fpdf import FPDF
from PyPDF2 import PdfMerger
import requests
from io import BytesIO

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Walfaanaa Magarsaa | Resume",
    page_icon="📄",
    layout="centered"
)

# ============================================================
# DATE
# ============================================================
today_date = datetime.today().strftime("%B %d, %Y")

# ============================================================
# GITHUB FILE URLS
# ============================================================
BASE_URL = "https://raw.githubusercontent.com/Walfaanaa/Resume_App/main/"

PROFILE_IMAGE = BASE_URL + "1728453971208.jpg"

files = {
    "MSc Certificate": BASE_URL + "MSc_certificate.pdf",
    "MBA Certificate": BASE_URL + "MBA_certificate.pdf",
    "BSc Certificate": BASE_URL + "BSc_certificate.pdf",
    "Certification": BASE_URL + "Certification.pdf",
}

exp_files = {
    "Experience Proof": BASE_URL + "Experience.pdf"
}

# ============================================================
# SESSION STATE
# ============================================================
if "application_text" not in st.session_state:
    st.session_state.application_text = ""

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-top: 5px;
    }

    .contact {
        text-align: center;
        font-size: 15px;
        margin-top: 10px;
    }

    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 25px;
    }

    .preview-box {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        background-color: #fafafa;
    }

    .skill-box {
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ddd;
        margin-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================
st.markdown(
    '<div class="main-title">📄 Walfaanaa Magarsaa</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Data Analyst | Data Scientist | BI Developer</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="contact">
        📞 +251 912 861 288 &nbsp; | &nbsp;
        📧 walfanamegersa3@gmail.com
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="contact">
        🔗 <a href="https://www.linkedin.com/in/walfaanaa-magarsaa/" target="_blank">
        LinkedIn Profile
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(f"CV updated: {today_date}")

st.divider()

# ============================================================
# PROFILE
# ============================================================
col1, col2 = st.columns([1, 3])

with col1:
    try:
        response = requests.get(PROFILE_IMAGE, timeout=10)
        response.raise_for_status()
        st.image(BytesIO(response.content), width=140)
    except Exception:
        st.info("Profile image unavailable")

with col2:
    st.header("Walfaanaa Magarsaa")
    st.write(
        """
        Data professional with experience in data analytics, SQL,
        Python, Business Intelligence, reporting, ETL processes,
        dashboards, and Machine Learning.
        """
    )

st.divider()

# ============================================================
# JOB APPLICATION
# ============================================================
st.subheader("📨 Job Application")

company = st.text_input(
    "🏢 Company Name",
    placeholder="Enter company name"
)

position = st.text_input(
    "💼 Position",
    placeholder="Enter position"
)

application_text = st.text_area(
    "✍️ Application Letter",
    value=st.session_state.application_text,
    height=220,
    placeholder="Write your application letter here..."
)

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "✨ Generate Application",
        use_container_width=True
    ):
        st.session_state.application_text = f"""
I am writing to apply for the position of {position or 'the advertised position'} at {company or 'your organization'}.

I hold an MSc in Computational Data Science, an MBA in Business Administration, and a BSc in Statistics. I have professional experience in data analytics, SQL, Python, Business Intelligence, reporting, ETL processes, and Machine Learning.

My experience includes developing analytical solutions, preparing management reports, building dashboards, working with databases, and transforming data into actionable insights.

I am confident that my technical background, analytical skills, and professional experience would allow me to contribute effectively to your organization.

Thank you for considering my application. I would welcome the opportunity to discuss how my skills and experience can contribute to your team.

Sincerely,
Walfaanaa Magarsaa
"""

        st.rerun()

with col2:
    if st.button(
        "🗑️ Clear Application",
        use_container_width=True
    ):
        st.session_state.application_text = ""
        st.rerun()

# ============================================================
# PREVIEW
# ============================================================
st.subheader("📄 Application Preview")

preview_text = (
    st.session_state.application_text
    if st.session_state.application_text
    else application_text
)

st.markdown(
    f"""
    <div class="preview-box">

    <strong>Date:</strong> {today_date}<br><br>

    <strong>To:</strong> {company or "________________________"}<br>

    <strong>Position:</strong> {position or "________________________"}<br><br>

    Dear Hiring Manager,<br><br>

    {preview_text.replace(chr(10), "<br>") if preview_text else "Your application will appear here..."}

    <br><br>

    Sincerely,<br>
    <strong>Walfaanaa Magarsaa</strong>

    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ============================================================
# EDUCATION
# ============================================================
st.subheader("🎓 Education")

st.markdown(
    """
    **MSc Computational Data Science** — 2024

    **MBA Business Administration** — 2020

    **BSc Statistics** — 2016
    """
)

st.markdown("### 📄 Certificates")

for name, url in files.items():
    st.link_button(
        f"📄 {name}",
        url,
        use_container_width=True
    )

st.divider()

# ============================================================
# EXPERIENCE
# ============================================================
st.subheader("💼 Experience")

st.markdown(
    """
    **Cooperative Bank of Oromia**
    
    Data Analytics / Reporting

    **INSA**
    
    Data Analytics / Data Science Research

    **CSA**
    
    Supervisor
    """
)

st.markdown("### 📄 Experience Evidence")

for name, url in exp_files.items():
    st.link_button(
        f"📄 {name}",
        url,
        use_container_width=True
    )

st.divider()

# ============================================================
# SKILLS
# ============================================================
st.subheader("🧠 Technical Skills")

skills = [
    "SQL",
    "Python",
    "Power BI",
    "Tableau",
    "Microsoft Excel",
    "Machine Learning",
    "Data Analytics",
    "ETL",
    "Data Visualization",
    "Reporting",
    "Database Management"
]

cols = st.columns(3)

for i, skill in enumerate(skills):
    with cols[i % 3]:
        st.markdown(
            f'<div class="skill-box">🔹 {skill}</div>',
            unsafe_allow_html=True
        )

st.divider()

# ============================================================
# PDF HELPER
# ============================================================
def safe_text(text):
    """
    Convert text into characters supported by the default FPDF font.
    """
    if not text:
        return ""

    replacements = {
        "–": "-",
        "—": "-",
        "’": "'",
        "“": '"',
        "”": '"',
        "•": "-",
        "©": "(c)",
        "®": "(R)",
        "™": "(TM)",
        "✓": "[OK]",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text.encode("latin-1", "replace").decode("latin-1")


# ============================================================
# CREATE PROFESSIONAL CV PDF
# ============================================================
def create_cv_pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Page margins
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)

    # ========================================================
    # HEADER
    # ========================================================
    pdf.set_font("Arial", "B", 20)
    pdf.cell(
        0,
        12,
        "WALFAANAA MAGARSAA",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C"
    )

    pdf.set_font("Arial", "B", 11)
    pdf.cell(
        0,
        7,
        "Data Analyst | Data Scientist | BI Developer",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C"
    )

    pdf.set_font("Arial", size=9)

    pdf.cell(
        0,
        6,
        "Email: walfanamegersa3@gmail.com | Phone: +251 912 861 288",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C"
    )

    pdf.cell(
        0,
        6,
        "LinkedIn: linkedin.com/in/walfaanaa-magarsaa/",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C"
    )

    pdf.cell(
        0,
        6,
        f"Date: {today_date}",
        new_x="LMARGIN",
        new_y="NEXT",
        align="C"
    )

    pdf.ln(5)

    # ========================================================
    # PROFILE
    # ========================================================
    pdf.set_font("Arial", "B", 14)
    pdf.cell(
        0,
        8,
        "PROFESSIONAL PROFILE",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font("Arial", size=10)

    profile = (
        "Data professional with experience in data analytics, SQL, Python, "
        "Business Intelligence, reporting, ETL processes, dashboards, "
        "database management, and Machine Learning. Experienced in "
        "transforming data into meaningful insights and developing "
        "analytical solutions to support decision making."
    )

    pdf.multi_cell(
        180,
        6,
        safe_text(profile),
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(3)

    # ========================================================
    # EDUCATION
    # ========================================================
    pdf.set_font("Arial", "B", 14)
    pdf.cell(
        0,
        8,
        "EDUCATION",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font("Arial", size=10)

    education = [
        "MSc Computational Data Science - 2024",
        "MBA Business Administration - 2020",
        "BSc Statistics - 2016"
    ]

    for item in education:
        pdf.multi_cell(
            180,
            6,
            safe_text("- " + item),
            new_x="LMARGIN",
            new_y="NEXT"
        )

    pdf.ln(3)

    # ========================================================
    # EXPERIENCE
    # ========================================================
    pdf.set_font("Arial", "B", 14)
    pdf.cell(
        0,
        8,
        "PROFESSIONAL EXPERIENCE",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    experience = [
        ("Cooperative Bank of Oromia", "Data Analytics / Reporting"),
        ("INSA", "Data Analytics / Data Science Research"),
        ("CSA", "Supervisor")
    ]

    for organization, role in experience:

        pdf.set_font("Arial", "B", 10)

        pdf.cell(
            0,
            6,
            safe_text(organization),
            new_x="LMARGIN",
            new_y="NEXT"
        )

        pdf.set_font("Arial", size=10)

        pdf.cell(
            0,
            6,
            safe_text(role),
            new_x="LMARGIN",
            new_y="NEXT"
        )

        pdf.ln(2)

    pdf.ln(2)

    # ========================================================
    # SKILLS
    # ========================================================
    pdf.set_font("Arial", "B", 14)
    pdf.cell(
        0,
        8,
        "TECHNICAL SKILLS",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font("Arial", size=10)

    skill_text = (
        "SQL, Python, Power BI, Tableau, Microsoft Excel, "
        "Machine Learning, Data Analytics, ETL, Data Visualization, "
        "Reporting, Database Management"
    )

    pdf.multi_cell(
        180,
        6,
        safe_text(skill_text),
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(5)

    # ========================================================
    # APPLICATION
    # ========================================================
    pdf.set_font("Arial", "B", 14)
    pdf.cell(
        0,
        8,
        "APPLICATION",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.set_font("Arial", size=10)

    pdf.cell(
        0,
        6,
        safe_text(f"Company: {company or ''}"),
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.cell(
        0,
        6,
        safe_text(f"Position: {position or ''}"),
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.ln(4)

    application = (
        st.session_state.application_text
        or application_text
        or ""
    )

    if application.strip():

        pdf.multi_cell(
            180,
            6,
            safe_text(application),
            new_x="LMARGIN",
            new_y="NEXT"
        )

    pdf.ln(5)

    pdf.cell(
        0,
        6,
        "Sincerely,",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    pdf.cell(
        0,
        6,
        "Walfaanaa Magarsaa",
        new_x="LMARGIN",
        new_y="NEXT"
    )

    # ========================================================
    # RETURN PDF
    # ========================================================
    return pdf.output()

# ============================================================
# DOWNLOAD REMOTE PDF
# ============================================================
def download_pdf(url):
    """
    Download a PDF from GitHub.
    """
    response = requests.get(
        url,
        timeout=20
    )

    response.raise_for_status()

    return BytesIO(response.content)


# ============================================================
# MERGE FULL PACKAGE
# ============================================================
def merge_all_pdfs():

    merger = PdfMerger()

    # CV
    merger.append(
        BytesIO(create_cv_pdf())
    )

    # Certificates
    for name, url in files.items():

        try:
            pdf_file = download_pdf(url)
            merger.append(pdf_file)

        except Exception as e:
            st.warning(
                f"Could not add {name}: {e}"
            )

    # Experience documents
    for name, url in exp_files.items():

        try:
            pdf_file = download_pdf(url)
            merger.append(pdf_file)

        except Exception as e:
            st.warning(
                f"Could not add {name}: {e}"
            )

    output = BytesIO()

    merger.write(output)
    merger.close()

    output.seek(0)

    return output.getvalue()


# ============================================================
# DOWNLOAD SECTION
# ============================================================
st.subheader("⬇️ Download Documents")

# ---------------- CV ----------------
cv_pdf = create_cv_pdf()

st.download_button(
    label="📄 Download CV",
    data=cv_pdf,
    file_name="Walfaanaa_Magarsaa_CV.pdf",
    mime="application/pdf",
    use_container_width=True
)

# ---------------- FULL PACKAGE ----------------
with st.spinner("Preparing CV + certificates + experience documents..."):

    try:
        full_pdf = merge_all_pdfs()

        st.download_button(
            label="📦 Download Full Application Package",
            data=full_pdf,
            file_name="Walfaanaa_Magarsaa_Full_Application.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    except Exception as e:

        st.error(
            f"Could not create the full PDF package: {e}"
        )

st.divider()

# ============================================================
# FOOTER
# ============================================================
st.caption(
    "© Walfaanaa Magarsaa | CV & Job Application Portal"
)
