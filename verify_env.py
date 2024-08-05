from dotenv import load_dotenv
import os

load_dotenv()

serper_api_key = os.getenv("SERPER_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

print(f"SerpApi Key: {serper_api_key}")
print(f"OpenAI Key: {openai_api_key}")