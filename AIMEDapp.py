import streamlit as st
from fpdf import FPDF
import base64
import openai
import csv
from io import StringIO

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Home", "Decision Classification Tool", "AIMED Process Walkthrough"])

# Styling: Custom CSS for consistent colors and layout
st.markdown("""
<style>
    body {
        background-color: #D7E8E7;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    h1, h2, h3, h4 {
        color: #FF6F61;
    }
    .stButton>button {
        background-color: #FF6F61;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #E05A50;
    }
    .stSidebar {
        background-color: #FF6F61;
        color: white;
    }
    .stSidebar .css-1e5imcs {
        color: white !important;
    }
    .stTextInput, .stTextArea, .stSelectbox {
        border: 1px solid #FF6F61;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# AI Advice Function
def get_ai_advice(user_inputs):
    openai.api_key = st.secrets["openai"]["api_key"]  # Securely fetch the API key from Streamlit secrets
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Use the latest supported model
        messages=[
            {"role": "system", "content": "You are an expert providing decision-making advice."},
            {"role": "user", "content": f"Analyze the following decision-making inputs and provide advice:\n\n{user_inputs}\n\nAdvice:"}
        ],
        max_tokens=500,
        temperature=0.7
    )
    # Convert response to dictionary and access content
    return response.choices[0].message.content.strip()

# PDF Export Function
def export_to_pdf(problem_description, business_alignment, possible_solutions, data_needs, scenarios, risks, selected_option, implementation_plan, ai_advice=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="AIMED Process Walkthrough Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt="1. Assess the Situation", ln=True)
    pdf.multi_cell(0, 10, f"Problem Description: {problem_description}")
    pdf.multi_cell(0, 10, f"Business Alignment: {business_alignment}")
    pdf.ln(5)

    pdf.cell(200, 10, txt="2. Investigate Options", ln=True)
    pdf.multi_cell(0, 10, f"Possible Solutions: {possible_solutions}")
    pdf.multi_cell(0, 10, f"Data Needs: {data_needs}")
    pdf.ln(5)

    pdf.cell(200, 10, txt="3. Model the Outcomes", ln=True)
    pdf.multi_cell(0, 10, f"Scenarios: {scenarios}")
    pdf.multi_cell(0, 10, f"Risks: {risks}")
    pdf.ln(5)

    pdf.cell(200, 10, txt="4. Execute the Decision", ln=True)
    pdf.multi_cell(0, 10, f"Selected Option: {selected_option}")
    pdf.multi_cell(0, 10, f"Implementation Plan: {implementation_plan}")
    pdf.ln(5)

    if ai_advice:
        pdf.cell(200, 10, txt="AI-Generated Advice", ln=True)
        pdf.multi_cell(0, 10, ai_advice)
        pdf.ln(5)

    pdf_output = "AIMED_Report.pdf"
    pdf.output(pdf_output)

    with open(pdf_output, "rb") as pdf_file:
        b64 = base64.b64encode(pdf_file.read()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="AIMED_Report.pdf">Download PDF</a>'
        st.markdown(href, unsafe_allow_html=True)


if menu == "Home":
    # Page Title
    st.title("AIMED Decision Framework for Construction Leaders")

    # Homepage
    st.header("Welcome to the AIMED Decision Framework App")
    st.write("This tool helps construction leaders make smarter decisions using the AIMED framework, ensuring confidence in tackling complexity and uncertainty.")
    st.markdown("[Read the full article here](#)")  # Placeholder hyperlink

    # Home Content
    st.subheader("About the AIMED Framework")
    st.write("The AIMED framework guides construction leaders through a structured decision-making process. Its five steps ensure decisions are both robust and adaptable:")
    st.markdown("""
    1. **Assess the Situation**: Define the problem and align it with business goals.
    2. **Investigate Options**: Explore and test solutions in controlled environments.
    3. **Model the Outcomes**: Run scenarios and stress-test decisions.
    4. **Execute the Decision**: Implement with clarity and feedback mechanisms.
    5. **Debrief and Improve**: Review outcomes and institutionalise insights.
    """)

    st.subheader("Antifragility Principles")
    st.write("Adopting antifragility ensures systems thrive under stress, turning challenges into opportunities for growth.")
    st.markdown("""
    - **Stress-Test Scenarios**: Simulate extreme conditions to identify vulnerabilities.
    - **Feedback Loops**: Build adaptive processes that evolve in real-time.
    - **Diversity and Redundancy**: Incorporate backups and alternatives to reduce risk.
    - **Experimentation**: Use controlled tests before fully committing to solutions.
    - **Opportunities in Uncertainty**: Reframe challenges as opportunities for innovation.
    """)

elif menu == "Decision Classification Tool":
    st.header("Decision Classification Tool")
    st.write("Evaluate your decision as Reversible/Low Stakes or Irreversible/High Stakes.")

    # Input Form
    impact_duration = st.selectbox("Impact Duration", ["1 day to 1 month", "1 month to 1 year", "More than 1 year"])
    cost_of_reversal = st.selectbox("Cost of Reversal", ["Minimal effort or cost", "Moderate effort or cost", "Significant effort or cost"])
    stakeholder_involvement = st.selectbox("Stakeholder Involvement", ["Internal team only", "Internal and some external", "Broad external involvement"])

    # Classification
    if impact_duration == "More than 1 year" or cost_of_reversal == "Significant effort or cost" or stakeholder_involvement == "Broad external involvement":
        st.write("This decision is classified as **Irreversible/High Stakes**.")
    else:
        st.write("This decision is classified as **Reversible/Low Stakes**.")

elif menu == "AIMED Process Walkthrough":
    st.header("AIMED Process Walkthrough")
    st.write("Use this guided process to walk through the AIMED framework for your decision-making.")

    # Step 1: Assess the Situation
    st.subheader("1. Assess the Situation")
    problem_description = st.text_area("Describe the problem or decision context", "")
    business_alignment = st.text_area("How does this align with your business goals?", "")

    # Step 2: Investigate Options
    st.subheader("2. Investigate Options")
    possible_solutions = st.text_area("List possible solutions or approaches", "")
    data_needs = st.text_area("What data or information do you need to evaluate these options?", "")

    # Step 3: Model the Outcomes
    st.subheader("3. Model the Outcomes")
    scenarios = st.text_area("Describe the scenarios you want to model (best-case, worst-case, etc.)", "")
    risks = st.text_area("What risks have you identified for each option?", "")

    # Step 4: Execute the Decision
    st.subheader("4. Execute the Decision")
    selected_option = st.text_input("Which option are you implementing?", "")
    implementation_plan = st.text_area("Outline your implementation plan", "")

    # Step 5: Debrief and Improve
    st.subheader("5. Debrief and Improve")
    st.write("While this app does not require a response for this step, remember to reflect on the outcomes and lessons learned to continuously improve your decision-making processes.")

    # Restrict AI Advice to One Request Per Session
    if "ai_requested" not in st.session_state:
        st.session_state["ai_requested"] = False

    ai_advice = None

    # AI Advice Section
    if not st.session_state["ai_requested"] and all([problem_description, business_alignment, possible_solutions, data_needs, scenarios, risks, selected_option, implementation_plan]):
        if st.button("Get AI Advice"):
            with st.spinner("Analyzing inputs..."):
                user_inputs = f"""
                Problem Description: {problem_description}
                Business Alignment: {business_alignment}
                Possible Solutions: {possible_solutions}
                Data Needs: {data_needs}
                Scenarios: {scenarios}
                Risks: {risks}
                Selected Option: {selected_option}
                Implementation Plan: {implementation_plan}
                """