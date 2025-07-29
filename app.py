import asyncio
import os
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_text_splitters import HTMLSectionSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS

async def main():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    folder_path = "./Assets/Data"
    index_name = "CWC_index"
    faiss_index_path = os.path.join(folder_path, f"{index_name}.faiss")

    if os.path.exists(faiss_index_path):
        print("Loading existing vector store...")
        vector_store = FAISS.load_local(folder_path=folder_path, embeddings=embeddings, index_name=index_name, allow_dangerous_deserialization=True)
        print("Vector store loaded.")
    else:
        print("Creating new vector store...")
        urls = ["https://en.wikipedia.org/wiki/2023_Cricket_World_Cup"]
        loader = AsyncHtmlLoader(urls)
        docs = await loader.aload()

        headers_to_split_on = [
            ("h1", "Header 1"),
            ("h2", "Header 2"),
            ("table", "Table"),
        ]

        html_splitter = HTMLSectionSplitter(headers_to_split_on=headers_to_split_on)
        chunks = html_splitter.split_text(docs[0].page_content)
        print(f"The number of chunks created : {len(chunks)}")

        hf_embeddings = embeddings.embed_documents([chk.page_content for chk in chunks])
        print(f"The lenght of the embeddings vector is {len(hf_embeddings[0])}")
        print(f"The embeddings object is an array of {len(hf_embeddings)} X {len(hf_embeddings[0])}")

        index = faiss.IndexFlatIP(len(hf_embeddings[0]))

        vector_store = FAISS(
            embedding_function=embeddings,
            index=index,
            docstore=InMemoryDocstore(),
            index_to_docstore_id={},
        )

        vector_store.add_documents(documents=chunks)
        vector_store.save_local(folder_path=folder_path, index_name=index_name)
        print("New vector store created and saved.")

    query = "Who won the World Cup final?"
    docs = vector_store.similarity_search(query)
    print(docs[0].page_content)

if __name__ == "__main__":
    asyncio.run(main())
