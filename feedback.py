import streamlit as st  
import backend as bk  

def show_feedback():  
    st.title("Feedback Section 📝")  
    st.write("We appreciate your feedback and strive to improve our services. Please take a moment to rate the AI output and provide additional comments.")  

    # Rating Section  
    st.subheader("Rate the AI Output:")  
    rating = st.slider("How would you rate the AI output?", 1, 5, step=1, format="%d")  
    
    # Additional Feedback Section  
    st.subheader("What did you think?")  
    feedback_comments = st.text_area("Share your thoughts or suggestions:", height=100)  
    
    # Feedback Category/Type  
    st.subheader("Type of Feedback:")  
    feedback_type = st.selectbox("Select a feedback category:", ["General Comments", "Bugs", "Feature Requests",""])  
    
    # Optional Email Input  
    st.write("If you'd like to receive updates or follow-up about your feedback, please provide your email address:")  
    email = st.text_input("Email (optional):")  

    # Submit Button  
    if st.button("Submit Feedback"):  
        # Here you can include the backend call to save feedback  
        bk.submit_feedback(rating, feedback_comments, feedback_type, email)  
        st.success("Thank you for your feedback! We value your input and will use it to improve.")  

    st.markdown("---")  
    st.write("✨ Your feedback helps us enhance our service! If you have any immediate concerns, feel free to **contact us** at: suzkhan135@gmail.com.")