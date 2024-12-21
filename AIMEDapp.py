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
    impact_duration = st.selectbox("Impact Duration", ["Short-term (days or weeks)", "Long-term (months or years)"])
    cost_of_reversal = st.selectbox("Cost of Reversal", ["Minimal effort or cost", "Significant effort or cost"])
    stakeholder_involvement = st.selectbox("Stakeholder Involvement", ["Internal team", "External stakeholders"])

    # Classification
    if impact_duration == "Long-term (months or years)" or cost_of_reversal == "Significant effort or cost" or stakeholder_involvement == "External stakeholders":
        st.write("This decision is classified as **Irreversible/High Stakes**.")
    else:
        st.write("This decision is classified as **Reversible/Low Stakes**.")

elif menu == "Case Study Builder":
    st.header("Build Your Own Case Study")
    st.write("Document your decision-making process using the AIMED framework.")

    # Input Fields
    case_title = st.text_input("Case Study Title", "")
    decision_context = st.text_area("Describe the Decision Context", "")
    steps_taken = st.text_area("Steps Taken (using AIMED)", "")
    outcomes = st.text_area("Outcomes and Lessons Learned", "")

    if st.button("Generate Case Study"):
        st.subheader("Your Case Study")
        st.write(f"### {case_title}")
        st.write(f"**Context:** {decision_context}")
        st.write(f"**Steps Taken:** {steps_taken}")
        st.write(f"**Outcomes:** {outcomes}")

# Footer
st.write("Developed to support construction leaders in smarter decision-making using the AIMED framework.")
