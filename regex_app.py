# Import necessary libraries
import streamlit as st
import re

# Define a function to extract details from messages
def extract_message_details(messages):
    # Define a regex pattern to match the structure of the trading messages
    # This pattern captures:
    # 1. Symbol (e.g., CVS)
    # 2. Strike price
    # 3. Option type (CALL or PUT)
    # 4. Date (with optional year)
    # 5. Price
    pattern = r'\$(\w+)\s+(\d+)\s+(CALL|PUT)\s+(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s+@\s+(\d+\.\d{2})'
    
    # Initialize an empty list to store the details of each match
    details = []
    
    # Split the input text by double newlines to process multiple messages
    for message in messages.split('\n\n'):
        # Use finditer to find all matches in the message, enabling multiline processing
        matches = re.finditer(pattern, message, re.MULTILINE)
        for match in matches:
            # Destructure the match object to get the captured groups
            symbol, strike, option_type, date, price = match.groups()
            
            # Check if the date includes a year, append a default year if not
            if '/' not in date[-3:]:  # Year is missing if no '/' in the last 3 characters
                date += '/2024'  # Append a default year
            
            # Add the extracted details to the details list
            details.append({
                "symbol": symbol,
                "strike": strike,
                "option_type": option_type,
                "date": date,
                "price": price
            })
    return details

# Streamlit UI components
st.title("Message Details Extractor")

# Create a text area for user input
message_input = st.text_area("Enter the message(s) here:", height=300)

# Define a button and its action
if st.button("Extract Details"):
    if message_input:
        # Call the extract_message_details function with the user input
        details = extract_message_details(message_input)
        if details:
            st.write("Extracted Details:")
            # Loop through the details and display them in the app
            for detail in details:
                st.json(detail)  # Use st.json to nicely format the output
        else:
            st.write("No details extracted. Ensure the messages are formatted correctly.")
    else:
        st.write("Please input some messages to extract details from.")
