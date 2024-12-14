import streamlit as st
import backend as bk
def show_content_generator(input_text):
    st.subheader("🤖 AI-Powered Content Generator")
    if st.button("Generate Content"):
        if input_text:
            output = bk.get_text_output(input_text)
            st.subheader("Generated Content:")
            st.markdown(output)
        else:
            st.warning("Please enter some text or select an example prompt.")