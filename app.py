import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="GyanSetu AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 GyanSetu AI")
st.subheader("AI-Based Student Learning Gap Detection System")

st.sidebar.title("Student Portal")
student_name = st.sidebar.text_input("Enter your name")
semester = st.sidebar.selectbox(
    "Select Semester",
    list(range(1, 9))
)

st.header("📊 Student Performance Dashboard")

st.write(
    "Enter your marks to identify learning gaps "
    "and receive personalized study recommendations."
)

subjects = [
    "Mathematics",
    "Programming",
    "Data Structures",
    "Database Management Systems",
    "Machine Learning"
]

marks = {}

for subject in subjects:
    marks[subject] = st.slider(
        f"{subject} Marks",
        min_value=0,
        max_value=100,
        value=50
    )

if st.button("Analyze My Performance"):
    if not student_name.strip():
        st.warning("Please enter your name.")
    else:
        st.success(f"Analysis completed for {student_name}!")

        average = sum(marks.values()) / len(marks)

        col1, col2 = st.columns(2)

        col1.metric("Average Marks", f"{average:.1f}%")
        col2.metric("Semester", semester)

        st.subheader("Subject Performance")

        df = pd.DataFrame({
            "Subject": list(marks.keys()),
            "Marks": list(marks.values())
        })

        st.bar_chart(df.set_index("Subject"))

        weak_subjects = {
            subject: score
            for subject, score in marks.items()
            if score < 60
        }

        st.subheader("🧠 Learning Gap Analysis")

        if weak_subjects:
            for subject, score in weak_subjects.items():
                st.warning(
                    f"{subject}: {score}/100. "
                    "Revise the basics and practice more questions."
                )
        else:
            st.success(
                "No major learning gaps detected "
                "using the current 60-mark threshold."
            )

        st.subheader("📚 Personalized Recommendations")

        if weak_subjects:
            for subject in weak_subjects:
                st.write(
                    f"- Study {subject} for 30 minutes daily "
                    "and solve practice questions."
                )
        else:
            st.write(
                "Continue revising and practice advanced questions."
            )

        st.info(
            "This initial version uses rule-based analysis. "
            "Machine learning can be integrated in a future version."
        )