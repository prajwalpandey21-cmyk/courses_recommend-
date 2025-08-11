import streamlit as st
import pandas as pd

# -------- Load the Excel file --------
df = pd.read_excel("C:/Users/prajw/Downloads/indian_student_scores_dataset.xlsx")  # Make sure this path is correct

# -------- Show available columns for debugging (optional) --------
# st.subheader("🛠 Debug: Available Columns in Dataset")
# st.write(df.columns.tolist())  # Uncomment this to debug column names

# -------- Calculate average marks --------.0
subject_columns = df.columns.drop('Name')  # All columns except Name
df["Average Marks"] = df[subject_columns].mean(axis=1)

# -------- Sidebar for student selection --------
st.sidebar.title("🎓 Student Selection")
student_name = st.sidebar.selectbox("Select a Student", df["Name"])
student_row = df[df["Name"] == student_name].iloc[0]

# -------- Main title --------
st.title("📊 Learn & Earn - Student Performance Dashboard")

# -------- Section 1: Average Marks --------
st.subheader("1️⃣ Student's Average Marks")
st.metric(label="🎯 Average Marks", value=round(student_row["Average Marks"], 2))

# -------- Section 2: Interest Area Dropdown --------
st.subheader("2️⃣ Student's Area of Interest")

interest_options = [
    "Technology / IT",
    "Finance & Investment",
    "Entrepreneurship / Startups",
    "Healthcare / Medical",
    "Data Analytics / AI",
    "Design / UI-UX / Animation",
    "Marketing & Branding",
    "Government / Civil Services",
    "Education / Teaching",
    "Environment & Sustainability"
]

interest_area = st.selectbox("Select the student's interest area:", interest_options)

# -------- Section 3: Display All Scores --------
st.subheader("3️⃣ Student's Detailed Scores")

col1, col2, col3 = st.columns(3)
col1.metric("📘 Academic Marks", round(student_row["Academic"], 2))
col2.metric("📊 Skill Quotient (SQ)", round(student_row["SQ"], 2))
col3.metric("💖 Emotional Quotient (EQ)", round(student_row["EQ"], 2))

col4, col5, col6 = st.columns(3)
col4.metric("🧠 Intelligence Quotient (IQ)", round(student_row["IQ"], 2))
col5.metric("🌐 Social Intelligence (SI)", round(student_row["SI"], 2))
col6.metric("💼 Professional Intelligence (PI)", round(student_row["PI"], 2))

# -------- Section 4: Matching Area --------
st.subheader("4️⃣ Matching with Student's Interest Area")
st.markdown(f"✅ **Selected Interest Area:** `{interest_area}`")

# -------- Section 5: Trending Job Sector & Certifications --------
st.subheader("5️⃣ Choose a Trending Job Sector")

sectors = {
    "Artificial Intelligence (AI) & Machine Learning (ML)": [
        "Google AI Certification",
        "Deep Learning Specialization – Andrew Ng",
        "IBM ML Certificate",
        "TensorFlow Developer",
        "Azure AI Engineer Associate"
    ],
    "Data Science & Data Analytics": [
        "Google Data Analytics Certificate",
        "IBM Data Science Professional",
        "Python for Data Science – Harvard",
        "SQL for Data Science – UC Davis",
        "Tableau Certification"
    ],
    "Cybersecurity": [
        "Certified Ethical Hacker (CEH)",
        "CompTIA Security+",
        "IBM Cybersecurity Analyst",
        "Google Cybersecurity Certificate",
        "Cisco Certified CyberOps Associate"
    ],
    "Cloud Computing (AWS, Azure, Google Cloud)": [
        "AWS Certified Solutions Architect",
        "Microsoft Azure Fundamentals",
        "Google Associate Cloud Engineer",
        "Cloud DevOps Engineer – Udacity",
        "Certified Kubernetes Administrator (CKA)"
    ],
    "Digital Marketing": [
        "Google Digital Marketing Certificate",
        "Meta Digital Marketing Associate",
        "SEO Specialization – UC Davis",
        "HubSpot Content Marketing",
        "Google Ads Certification"
    ],
    "Financial Technology (FinTech)": [
        "FinTech Specialization – Michigan",
        "Blockchain in FinTech – Berkeley",
        "FMVA Certification – CFI",
        "Digital Banking Certificate – BSE",
        "Financial Markets – Yale"
    ],
    "Healthcare & Bioinformatics": [
        "Bioinformatics Specialization – UCSD",
        "AI in Healthcare",
        "Health Informatics – Georgia Tech",
        "Telemedicine Certification",
        "Medical Data Analytics – edX"
    ],
    "Sustainability & Green Energy": [
        "Renewable Energy Entrepreneurship – Duke",
        "Energy Principles – TU Delft",
        "ESG Investing Certificate – CFA",
        "Solar Engineering – Delft",
        "Sustainability & Development – Michigan"
    ],
    "Blockchain & Web3": [
        "Blockchain Specialization – Buffalo",
        "Ethereum & Solidity – Udemy",
        "Certified Blockchain Developer",
        "Web3 Fundamentals – Alchemy",
        "MIT Blockchain Course"
    ],
    "E-commerce & Logistics Technology": [
        "E-commerce Essentials – Google",
        "Supply Chain Management – MIT",
        "Digital Product Management – BU",
        "Amazon FBA Masterclass",
        "Logistics & Delivery – Delft"
    ]
}

selected_sector = st.selectbox("Select a Job Sector:", list(sectors.keys()))

if selected_sector:
    st.markdown("### 🏅 Recommended Certifications for This Sector:")
    for cert in sectors[selected_sector]:
        st.markdown(f"- {cert}")

# -------- Section 6: Personalized Course Recommendation --------
st.subheader("6️⃣ Personalized Course Recommendation")

def recommend_course(avg_marks, interest):
    interest = interest.lower()
    if avg_marks > 85:
        if "tech" in interest:
            return "Advanced Python & Machine Learning"
        elif "finance" in interest:
            return "Financial Modeling & Valuation"
        elif "design" in interest:
            return "UI/UX & Creative Tools Mastery"
        else:
            return "Leadership & Strategic Thinking"
    elif avg_marks > 70:
        if "tech" in interest:
            return "Data Analytics with Excel & SQL"
        elif "finance" in interest:
            return "Intro to Financial Markets"
        elif "design" in interest:
            return "Graphic Design Fundamentals"
        else:
            return "Communication & Soft Skills"
    else:
        return "Foundation Course: Skill Building Essentials"

recommended_course = recommend_course(student_row["Average Marks"], interest_area)
st.success(f"🎓 **Recommended Course:** {recommended_course}")

# -------- Footer --------
st.markdown("---")
st.caption("🚀 Created with ❤️ for the Learn & Earn Project using Streamlit")

# For run the code
# streamlit run "C:\Users\prajw\Desktop\python\work.py" 

