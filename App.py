from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

def get_answer(input_txt, client):
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful translation assistant. Use a friendly welcome message in a friendly tone in the target language as the first thing you say. Try to detect if there is no target language given. If no target language is given, then show an error message saying this."
            },
            {
                "role": "user",
                "content": input_txt
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    response_str = ""
    for chunk in completion:
        response_str += chunk.choices[0].delta.content or ""
    
    return response_str

def main():
    st.title("Translate ANYTHING !!")
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
        )
    # User input
    st.write("Hi, I am a Translation Assistant. Ask me anything but dont forget to add a language!")
    location = st.text_input("Type in your question")

    # Ask me button
    if st.button("Ask me"):
        # Check if location is provided
        if location:
            # Get current weather
            response = get_answer(location,client)
            # Display weather details
            # st.json(response)
            st.write(response)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
