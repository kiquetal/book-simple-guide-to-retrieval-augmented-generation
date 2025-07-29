import asyncio
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_text_splitters import HTMLSectionSplitter
from langchain_huggingface import HuggingFaceEmbeddings

async def main():
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

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

    hf_embeddings = embeddings.embed_documents([chk.page_content for chk in chunks])
    print(f"The lenght of the embeddings vector is {len(hf_embeddings[0])}")
    print(f"The embeddings object is an array of {len(hf_embeddings)} X {len(hf_embeddings[0])}")


if __name__ == "__main__":
    asyncio.run(main())
