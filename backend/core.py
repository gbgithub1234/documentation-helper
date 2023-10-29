import os

from typing import Any, List, Dict

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone

from consts import INDEX_NAME

PINECONE_API_KEY='b32d298b-1cae-446f-9306-2d13539791df'
PINECONE_ENVIRONMENT_REGION='gcp-starter'

pinecone.init(
    api_key='b32d298b-1cae-446f-9306-2d13539791df',
    environment='gcp-starter',
    # api_key=os.environ["PINECONE_API_KEY"],
    # environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)

OPENAI_API_KEY='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'

def run_llm(query: str, chat_history: List[Dict[str, Any]]=[]) -> Any:
    embeddings = OpenAIEmbeddings(openai_api_key='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')
    docsearch = Pinecone.from_existing_index(
        index_name=INDEX_NAME, embedding=embeddings
    )
    chat = ChatOpenAI(verbose=True, temperature=0, openai_api_key='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')

    qa = ConversationalRetrievalChain.from_llm(
        llm=chat, retriever=docsearch.as_retriever(), return_source_documents=True
    )

    return qa({"question": query, "chat_history": chat_history})


if __name__ == "__main__":
    print(run_llm(query="What is LangChain?"))
