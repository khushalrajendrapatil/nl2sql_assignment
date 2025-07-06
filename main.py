import os
import requests

# Constants
API_URL = "https://api-inference.huggingface.co/models/tscholak/optimum-nl2sql"
HF_TOKEN = os.getenv("HF_TOKEN")

# Check for token presence
if not HF_TOKEN:
    print("❌ Error: HF_TOKEN environment variable not set.")
    print("Please set it using: set HF_TOKEN=your_token_here (Windows) or export (Linux/macOS)")
    exit(1)

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def get_sql_from_nl(nl_query: str) -> str:
    payload = {"inputs": nl_query}
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            return f"❌ API Error {response.status_code}: {response.text}"
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif "error" in data:
            return f"❌ API Error: {data['error']}"
        else:
            return f"❌ Unexpected response format: {data}"
    except requests.exceptions.RequestException as err:
        return f"❌ Request failed: {err}"
    except Exception as ex:
        return f"❌ Unexpected error: {ex}"

if __name__ == "__main__":
    print("🧠 Natural Language to SQL Converter (Powered by Hugging Face API)")
    query = input("📥 Enter your natural language query: ")
    print("\n🔄 Processing...")
    result = get_sql_from_nl(query)
    print("\n✅ Generated SQL:")
    print(result)
