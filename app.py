import streamlit as st

from agent import financial_react_agent


# Streamlit UI
st.title("Financial Analyst")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    st.write(f"{message['role']}: {message['content']}")

# User input
user_input = st.text_input("You: ", "")

if user_input:
    st.session_state.messages.append({"role": "User", "content": user_input})

    # Get response from the agent
    response = financial_react_agent.chat(user_input)
    st.session_state.messages.append({"role": "Agent", "content": response})

    # Clear user input
    st.experimental_rerun()
