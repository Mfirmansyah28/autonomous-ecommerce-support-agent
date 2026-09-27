import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def main():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY belum ditemukan di file .env")

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0,
        api_key=api_key,
    )

    response = llm.invoke(
        "Jelaskan apa itu Costumer support dalam satu kalimat."
    )

    print(response.content)

if __name__=="__main__":
    main()