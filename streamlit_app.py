import streamlit as st
from model import generate_response

st.set_page_config(page_title="Smart City Assistant", page_icon="🌆")

st.title("🌆 Sustainable Smart City Assistant")
st.write("Ask about traffic, pollution, water, waste management, or sustainability solutions.")

# Input prompt
prompt = st.text_input("💬 Ask something:", placeholder="How can we reduce traffic pollution?")

# Submit button
if st.button("Ask"):
    if prompt:
        with st.spinner("Generating response..."):
            response = generate_response(f"As a smart city assistant, answer: {prompt}")
            st.success("Here's the answer:")
            st.write(response)
    else:
        st.warning("Please enter a question.")
