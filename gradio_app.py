import gradio as gr
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
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",  # Engine for the completion
            prompt=prompt,  # Provide the prompt
            # model="gpt-3.5-turbo-instruct", # Specify the model
            temperature=0.1,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        llm_output = response.choices[0].text.strip()  # Get LLM output
        return parse_llm_output(llm_output)  # Parse LLM output
    except Exception as e:
        return [{"error": str(e)}]  # Return error message as JSON

# Function to display the result
def display_result(messages, api_key):
    extracted_details = extract_trading_details_with_gpt(messages, api_key)
    if extracted_details:
        return json.dumps(extracted_details, indent=2)  # Return the details as JSON
    else:
        return "No details were extracted. Please check your input and try again."

# Gradio interface
iface = gr.Interface(
    fn=display_result,
    inputs=["text", "text"],
    outputs="text",
    title="Trading Calls Details Extractor",
    description="Enter the trading call messages and your OpenAI API key to extract details."
)
iface.launch(share=True)
