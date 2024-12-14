import streamlit as st
import backend as bk
def show_title_generator(input_text):
    st.subheader("🖋️ Creative Title Generator")
    if st.button("Generate Titles"):
        if input_text:
            titles = bk.generate_creative_titles(input_text)
            st.subheader("Creative Titles:")
            for idx, title in enumerate(titles, 1):
                st.markdown(f"**Title {idx}:** {title}")
        else:
            st.warning("Please enter some text or select an example prompt.")
