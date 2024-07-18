from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from langchain.llms import GooglePalm
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


llm = GooglePalm(google_api_key="AIzaSyAfufg_BdiAuEuBPr6BjlLYgopRmPuaSao", temperature=0.8)


embeddings = HuggingFaceEmbeddings()
# documents = [Document(page_content=row.page_content, metadata=row.metadata) for row in data]

# loader = CSVLoader(file_path="/Users/Medhansh Jindal/OneDrive/Desktop/Python files/music.csv", encoding='latin1',source_column='track_name')
# data = loader.load()
# vectordb = FAISS.from_documents(documents=data, embedding = embeddings)


def chain(quest):
    loader = CSVLoader(file_path="/Users/Medhansh Jindal/OneDrive/Desktop/Python files/music.csv", encoding='latin1',
                       source_column='track_name')
    data = loader.load()
    vectordb = FAISS.from_documents(documents=data, embedding=embeddings)

    retriever = vectordb.as_retriever(score_threhold=0.7)
    prompt_template = """Given the context of the question, understand the feeling or expression based on the information from the documents provided and accordingly generate an answer
    CONTEXT : {context}
    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=['context','question']
    )
    chains= RetrievalQA.from_chain_type(
        llm = llm,
        chain_type="stuff",
        input_key="query",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )

    resp = chains(quest)
    return resp
