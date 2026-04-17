import streamlit as st
from datetime import datetime
import os

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Walfaanaa Resume", page_icon="📄", layout="centered")

# ================= AUTO DATE =================
today_date = datetime.today().strftime("%B %d, %Y")

# ================= HEADER =================
st.markdown(f"""
### 📄 Curriculum Vitae  
**Date:** {today_date}  
**Walfaanaa Magarsaa**  
📞 +251912861288 | 📧 walfanamegersa3@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/walfaanaa-magarsaa/
""")

st.divider()

# ================= APPLICATION SECTION =================
st.subheader("📨 Job Application")

company = st.text_input("🏢 Company Name")
position = st.text_input("💼 Position Applying For")

st.markdown("### ✍️ Brief Application")

application_text = st.text_area(
    "Write your short application message",
    height=150,
    placeholder="I am writing to apply for the position..."
)

# Auto generate option
if st.button("✨ Generate Professional Application"):
    application_text = f"""
I am writing to apply for the position of {position if position else 'the role'} at {company if company else 'your organization'}. 
With my strong background in Data Analysis, SQL, Python, and Machine Learning, 
I am confident in my ability to contribute effectively to your team.

I have hands-on experience in data analytics, dashboard development, and ETL processes, 
and I am eager to bring value to your organization.

Thank you for your time and consideration.
"""

# Preview
st.markdown("### 📄 Application Preview")
st.write(f"**Date:** {today_date}")
st.write(f"**To:** {company if company else '__________'}")
st.write(f"**Position:** {position if position else '__________'}")

st.write("Dear Hiring Manager,")

if application_text:
    st.write(application_text)
else:
    st.write("Your application message will appear here...")

st.write("Sincerely,")
st.write("**Walfaanaa Magarsaa**")

st.divider()

# ================= PROFILE =================
col1, col2 = st.columns([1, 3])

with col1:
    st.image("1728453971208.jpg", width=150)

with col2:
    st.title("Walfaanaa Magarsaa")
    st.subheader("Data Analyst | Data Scientist | BI Developer")
    st.write("Experienced in SQL, Python, BI tools, and Machine Learning.")

st.divider()

# ================= EDUCATION =================
st.subheader("🎓 Education")

st.write("""
- MSc Computational Data Science (2024)  
- MBA Business Administration (2020)  
- BSc Statistics (2016)
""")

st.markdown("### 📄 Education Evidence")

files = {
    "MSc Certificate": "MSc_certificate.pdf",
    "MBA Certificate": "MBA_certificate.pdf",
    "BSc Certificate": "BSc_certificate.pdf",
}

for name, path in files.items():
    if os.path.exists(path):
        with open(path, "rb") as f:
            st.download_button(f"Download {name}", f, file_name=path)
    else:
        st.warning(f"{name} not found")

st.divider()

# ================= EXPERIENCE =================
st.subheader("💼 Experience")

st.write("""
- Cooperative Bank of Oromia (Present)  
- INSA Data Analytics  
- CSA Supervisor  
""")

st.markdown("### 📄 Experience Evidence")

exp_files = {
    "Experience Proof": "Experience.pdf"
}

for name, path in exp_files.items():
    if os.path.exists(path):
        with open(path, "rb") as f:
            st.download_button(f"Download {name}", f, file_name=path)
    else:
        st.warning(f"{name} not found")

st.divider()

# ================= SKILLS =================
st.subheader("🧠 Skills")

st.write("""
- SQL, Python  
- Power BI, Tableau, Excel  
- SPSS, R, MATLAB, C++  
- ETL Tools (Talend, etc.)  
- Machine Learning & Deep Learning  
""")

st.divider()

# ================= CONTACT =================
st.subheader("📞 Contact")
st.write("📧 Email: walfanamegersa3@gmail.com")
st.write("📱 Phone: +251912861288")

st.success("✅ This CV & Application is ready to share as a live link.")