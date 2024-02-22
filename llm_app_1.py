import streamlit as st
import openai
import json

# Function to parse the LLM response into a structured format
def parse_llm_output(llm_output):
    # This function parses the output from the LLM
    # It assumes each transaction is separated by a newline
    # and each detail within a transaction is separated by a comma
    transactions = []
    for line in llm_output.split('\n'):
        if line.strip():  # Ensure the line contains data
            try:
                parts = line.split(',')
                transaction = {
                    "symbol": parts[0].strip(),  # Extract symbol
                    "strike_price": parts[1].strip(),  # Extract strike price
                    "call_put": parts[2].strip(),  # Extract call/put
                    "date": parts[3].strip(),  # Extract date
                    "price": parts[4].strip()  # Extract price
                }
                transactions.append(transaction)
            except IndexError:
                continue  # Skip lines that don't fit the expected format
    return transactions

# Function to extract trading details using OpenAI's GPT
def extract_trading_details_with_gpt(messages, api_key):
    openai.api_key = api_key
    # Prompt instructs the model to extract trading details and format them
    # Each transaction should be separated by a newline and details by commas
    prompt = f"Extract the symbol, strike price, call/put, date, and price from each trading call message and format each as 'Symbol, Strike Price, Call/Put, Date, Price':\n\n{messages}"
    
    try:
        response = openai.completions.create(
            engine="gpt-3.5-turbo-instruct",  # Engine for the completion
            prompt=prompt,  # Provide the prompt
            temperature=0.1,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        llm_output = response.choices[0].text.strip()  # Get LLM output
        return parse_llm_output(llm_output)  # Parse LLM output
    except Exception as e:
        return f"An error occurred: {e}"


# Streamlit app layout
st.title("Trading Calls Details Extractor")
st.sidebar.header("API Key")
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")  # Input API key

message_input = st.text_area("Enter the trading call messages below:", height=200)  # Input messages
if st.button("Extract Details"):  # Button to trigger extraction
    if not api_key:  # Check if API key is provided
        st.warning("Please enter your OpenAI API key in the sidebar.")
    elif not message_input:  # Check if messages are provided
        st.warning("Please enter some messages to extract details from.")
    else:
        # Extract trading details using OpenAI's GPT
        extracted_details = extract_trading_details_with_gpt(message_input, api_key)
        if extracted_details:
            st.success("Extracted Details:")
            for detail in extracted_details:
                st.json(detail)  # Display each transaction's details
        else:
            st.error("No details were extracted. Please check your input and try again.")
