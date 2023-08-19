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
spamlength = int(input("Please enter the number of words you want in your spam: "))
spamprompt = input("Please enter your spam prompt: ")

# Create prompt with user input
prompt = (f"Hey buddy, please generate a {spamlength}-word copypasta based on the following prompt: {spamprompt}"
          f"Please ensure that the generated copypasta is exactly {spamlength} words long")

# Generate copypasta
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": prompt}]
)

# Extract copypasta from response
copypasta = response.choices[0].message.content

# Print copypasta
print(copypasta)

# Prompt user to copy copypasta to clipboard
copy_to_clipboard = input("Would you like to copy the copypasta to your clipboard? (y/n) ")

if copy_to_clipboard.lower() == "y":
    clipboard.copy(copypasta)
    print("Copied to clipboard!")
