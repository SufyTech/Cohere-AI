import streamlit as st  
import backend as bk  # Your backend functions for AI integration  
from content_generator import show_content_generator   
from mood_based_content import show_mood_based_content  
from title_generator import show_title_generator    
from feedback import show_feedback  # Assuming feedback is in its own file  

# Set page config  
st.set_page_config(page_title="Gen AI Project", layout="wide")  

# Title and description on the main page  
st.title("🌟 Sophisticated AI Toolkit")  
st.markdown("### Generate insightful content using AI! Select a feature from the sidebar.")  

# Sidebar for different sections  
st.sidebar.header("Features")  
section = st.sidebar.radio(  
    "Choose a Section:",  
    ["Content Generator", "Mood-Based Content", "Title Generator", "Feedback"]  
)  

# Initialize session state variables  
if 'input_text' not in st.session_state:  
    st.session_state.input_text = ""  
    
if 'previous_section' not in st.session_state:  
    st.session_state.previous_section = None  # Initialize to None  

# Reset input text when changing features  
if st.session_state.previous_section != section:  
    st.session_state.input_text = ""  

# Update the previous section in session state  
st.session_state.previous_section = section    

# Sidebar for example prompts  
example_prompts = st.sidebar.selectbox(  
    "Choose an Example Prompt:",   
    ["Wikipedia of Tom Cruise", "Future Technology", "Climate Change Effects"]  
)  

# Allow the user to use an example prompt or enter their own  
if st.sidebar.button("Use Example Prompt"):  
    st.session_state.input_text = example_prompts  
else:  
    st.session_state.input_text = st.text_input("Enter Your Own Topic Here:", value=st.session_state.input_text)  

# Display the content based on the section selected  
if section == "Content Generator":  
    show_content_generator(st.session_state.input_text)  
elif section == "Mood-Based Content":  
    show_mood_based_content(st.session_state.input_text)  
elif section == "Title Generator":  
    show_title_generator(st.session_state.input_text)  
elif section == "Word Cloud":  
    show_word_cloud(st.session_state.input_text)  
elif section == "Feedback":  
    show_feedback()  

# Footer  
st.markdown("<style> .footer { font-size: 15px; text-align: center; } </style>", unsafe_allow_html=True)  
st.markdown("<p class='footer'>👨‍💻 Developed with ❤️ by Sufiyan Khan</p>", unsafe_allow_html=True)

