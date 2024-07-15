# import asyncio
# import os
# from langflow.load import run_flow_from_json
# import nest_asyncio

# # Set the OpenAI API key
# os.environ['OPENAI_API_KEY'] = 'sk-proj-RPwWpkjMpNfJKeTSaVJHT3BlbkFJv5NTVALMN2mVqEl85iqq'

# # Apply nest_asyncio
# nest_asyncio.apply()

# def main():
#     result = run_flow_from_json(flow="faqAI.json", input_value="INPUT HERE")
#     print(result[0].outputs[0].results['message'])
#     print("--------------------------------")
#     print(result[0].outputs[0].results['message']['text'])

# if __name__ == "__main__":
#     main()


import asyncio
import os
from langflow.load import run_flow_from_json
import nest_asyncio
import streamlit as st
from dotenv import load_dotenv


load_dotenv()
# Set the OpenAI API key
#os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
#os.environ['OPENAI_API_KEY'] = 'sk-proj-RPwWpkjMpNfJKeTSaVJHT3BlbkFJv5NTVALMN2mVqEl85iqq'

# Apply nest_asyncio
nest_asyncio.apply()

def run_flow(input_value):
    result = run_flow_from_json(flow="faqAI.json", input_value=input_value)
    print(result[0].outputs[0].results['message'].text)
    message_text = result[0].outputs[0].results['message'].text
    return message_text

def main():
    st.title("FAQ AI Interface")
    
    # Text input for "INPUT HERE"
    user_input = st.text_input("Enter your question:")
    
    # Button to submit
    if st.button("Submit"):
        with st.spinner("Processing..."):
            result = run_flow(user_input)
            st.success("Result:")
            st.write(result)

if __name__ == "__main__":
    main()
