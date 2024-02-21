# Using an LLM to Extract Structured Data

## Python Regular Expression
---

### This code defines a Streamlit app that takes in a block of text, which can contain multiple messages, and extracts financial trading call or put option details from it using a regular expression. The app then displays these details in a structured format.

## Open AI LLM model
---

### This code defines a Streamlit app that incorporates the functionality to extract trading details using OpenAI's GPT model. The app allows users to input their OpenAI API key via a sidebar for security reasons and to input the messages from which they want to extract details.

### For a task that involves extracting specific structured information from text, like trading call details from messages, using a Large Language Model (LLM) such as GPT-3.5 effectively requires crafting a prompt that clearly instructs the model on what to do. Below is an example of how you might set up a Python script to use OpenAI's GPT (assuming you're using GPT-3.5 or a similar version) for this task. This approach involves sending a prompt to the model that asks it to extract and list the details (symbol, strike price, call/put, date, and price) from each trading call message.

## Important Notes:
---
**API Key Security:** The api_key should be kept secure and not hard-coded in production scripts. Consider using environment variables or secure vaults for storing such sensitive information.

**Model Choice:** At the time of writing, "text-davinci-003" was an example. You should use the latest and most appropriate model version available.

**Prompt Engineering:** The effectiveness of this script heavily relies on the crafted prompt. You may need to refine the prompt based on the actual responses you get from the model to ensure it accurately extracts the information as intended.

**Handling the Model's Response:** The script assumes the model will format its response in a straightforward way that can be directly used. However, you might need to parse the model's response if it doesn't match your exact needs.

### This example demonstrates a basic application of GPT-3.5 for extracting structured information from unstructured text. The success of the extraction depends on both the quality of the prompt and the model's current capabilities.

**Parsing Logic:** The parse_llm_output function is crucial here and needs to be tailored to the specific output format of your LLM. The provided example assumes a very structured and simplistic output format for demonstration purposes.

**LLM Prompt:** Ensure your prompt to the LLM clearly asks for the output in a structured format that can be easily parsed (e.g., comma-separated values for each detail of a transaction).

**Displaying Results:** The app displays each transaction's details as JSON for clear, structured visualization. You might adjust this based on your preference or requirements.

### This script assumes a specific output format from the LLM, so you'll likely need to adjust the parsing logic to match the actual output you receive from your LLM prompts.








