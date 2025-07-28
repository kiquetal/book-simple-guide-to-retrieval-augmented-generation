import asyncio
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer

async def main():
    urls = ["https://en.wikipedia.org/w/index.php?search=World+cup+cricket+2024"]
    loader = AsyncHtmlLoader(urls)
    docs = await loader.aload()
    bs_transformer = BeautifulSoupTransformer()
    docs_transformed = bs_transformer.transform_documents(docs, tags_to_extract=["p", "li", "div", "a"])
    print(docs_transformed[0].page_content)

if __name__ == "__main__":
    asyncio.run(main())