from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
import os
os.environ['OPENAI_API_KEY'] = "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"
# Load the document, split it into chunks, embed each chunk and load it into the vector store.
def retrieve(Path_to_document,query):
	raw_documents =  PyPDFLoader(Path_to_document).load()
	text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
	documents = text_splitter.split_documents(raw_documents)
	db = Chroma.from_documents(documents, OpenAIEmbeddings())
	docs = db.similarity_search(query)
	text = ""
	for page in docs:
		text+=page.page_content
	return text
#print(retrieve("/home/anuj/Desktop/Testings/Books/Class 12/Chemistry/Chapter 1.pdf","Types of solution"))
