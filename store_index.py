from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_doc,text_split,download_embedding
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY= os.environ.get('GOOGLE_API_KEY')


extracted_data=load_pdf_files(data='data/')
filter_data = filter_to_minimal_doc(extracted_data)
text_chunks=text_split(filter_data)

embeddings=download_embedding()

pinecone_api_key=PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)



index_name='medical-chatbot'

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, # Dimension of Embeddings
        metric='cosine', # COsine Similarity
        spec=ServerlessSpec(cloud='aws',region='us-east-1')
    )

index=pc.Index(index_name)



doc_search= PineconeVectorStore.from_documents(
    documents=text_chunk,
    embedding=embedding,
    index_name=index_name 
)