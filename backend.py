import cohere
import os
import time
from dotenv import load_dotenv
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables for Cohere API key and email credentials
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")  # Your email to receive feedback

# Function to get the generated text content
def get_text_output(input_text):
    time.sleep(3)  # Simulate a delay for generating content
    response = co.generate(
        model="command-xlarge-nightly",  # Adjust the model if needed
        prompt=input_text,
        max_tokens=300,  # Limit the length of the output text
    )
    return response.generations[0].text

# Function to save feedback to a file
def save_feedback_to_file(rating, feedback_comments, feedback_type, email):
    feedback_entry = {
        "rating": rating,
        "comments": feedback_comments,
        "type": feedback_type,
        "email": email if email else "Not provided",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    try:
        feedback_file = "feedback.json"
        # Check if the feedback file exists
        if os.path.exists(feedback_file):
            with open(feedback_file, "r") as file:
                feedback_data = json.load(file)
        else:
            feedback_data = []

        # Append new feedback and save it back to the file
        feedback_data.append(feedback_entry)
        with open(feedback_file, "w") as file:
            json.dump(feedback_data, file, indent=4)
        print("Feedback saved successfully.")
    except Exception as e:
        print(f"Failed to save feedback: {e}")

# Function to send email
def send_email(subject, body):
    try:
        # Set up the email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the email server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:  # Using Gmail as an example
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to handle feedback submission
def submit_feedback(rating, feedback_comments, feedback_type, email):
    print(f"submit_feedback called with: Rating={rating}, Comments={feedback_comments}, Type={feedback_type}, Email={email}")

    # Save the feedback locally
    save_feedback_to_file(rating, feedback_comments, feedback_type, email)

    # Generate a thank-you note using Cohere
    prompt = f"Write a thank-you message for the following feedback:\nRating: {rating}\nComments: {feedback_comments}\nType: {feedback_type}"
    thank_you_message = get_text_output(prompt)
    print("Generated Thank-You Message:")
    print(thank_you_message)

    # Create email body
    email_body = f"""
    Feedback Received:
    -------------------
    Rating: {rating}
    Comments: {feedback_comments}
    Feedback Type: {feedback_type}
    Email: {email if email else "Anonymous"}

    Thank-You Message:
    -------------------
    {thank_you_message}
    """

    # Send email with feedback details and thank-you note
    send_email(subject="New Feedback Received", body=email_body)

# Example usage
if __name__ == "__main__":
    # Example data for testing
    test_rating = 5
    test_comments = "Great tool, very user-friendly!"
    test_feedback_type = "Positive"
    test_email = "user@example.com"  # Optional field for the feedback submitter

    submit_feedback(test_rating, test_comments, test_feedback_type, test_email)
