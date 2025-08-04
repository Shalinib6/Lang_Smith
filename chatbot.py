from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    input_variables=["Book"],
    template="""
    I want to read a summary of a book.
    Give *only* the summary of the book {Book} in about 500 words.
    """
)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
book_name = input("Which book do you want a summary of? ")
response = chain.invoke({"Book": book_name})
print("Book Summary:\n", response)
