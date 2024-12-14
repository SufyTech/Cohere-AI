import streamlit as st
import backend as bk

def show_mood_based_content(input_text):
    st.subheader("🎭 Mood-Based Content Generator")
    mood = st.selectbox("Choose a Mood:", ["Happy", "Serious", "Motivational", "Sad", "Excited"])
    if st.button("Generate Mood-Based Content"):
        if input_text:
            mood_input = f"{input_text} in a {mood} tone"
            output = bk.get_text_output(mood_input)
            st.subheader(f"Generated Content in {mood} Mood:")
            st.markdown(output)
        else:
            st.warning("Please enter some text or select an example prompt.")
