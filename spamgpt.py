import openai
import base64
import clipboard

# Read API key from file (assumes key is stored in "api_key.txt" or "api_key.base64")
try:
    with open("api_key.txt", "r") as f:
        api_key = f.read().strip()
except FileNotFoundError:
    with open("api_key.base64", "r") as f:
        api_key = base64.b64decode(f.read().strip()).decode("utf-8")

# Set the OpenAI API key
openai.api_key = api_key

# Get user input
spamprompt = input("Please enter your spam prompt: ")

# Create prompt with user input
prompt = f"Hey Ada, please generate a 1000-word copypasta based on the following prompt: {spamprompt}"

# Generate copypasta
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=prompt,
  max_tokens=3000,
  n=1,
  stop=None,
  temperature=1.5,
)

# Extract copypasta from response
copypasta = response.choices[0].text.strip()

# Print copypasta
print(copypasta)

# Prompt user to copy copypasta to clipboard
copy_to_clipboard = input("Would you like to copy the copypasta to your clipboard? (y/n) ")

if copy_to_clipboard.lower() == "y":
    clipboard.copy(copypasta)
    print("Copied to clipboard!")
