import streamlit as st

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Home", "Decision Classification Tool", "Case Study Builder"])

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

elif menu == "AIMED Template":
    st.header("AIMED Template")
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
    outcomes = st.text_area("What were the outcomes of your decision?", "")
    lessons_learned = st.text_area("What lessons did you learn that can improve future decisions?", "")
    st.write(f"**Outcomes:** {outcomes}")

# Footer
st.write("Developed to support construction leaders in smarter decision-making using the AIMED framework.")
