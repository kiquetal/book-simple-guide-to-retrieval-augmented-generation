# Index

- [Prerequisites](#prerequisites)
- [File Explanations](#file-explanations)
- [Chunking](#chunking)

# Prerequisites

This project requires Python 3.7+ and the libraries listed in `requirements.txt`.

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

# File Explanations

- **app.py**: This is the main application file. It uses the `langchain` library to load a web page, extract its content, and print it to the console. This serves as a basic example of the data loading and transformation aspect of a RAG system.

- **requirements.txt**: This file lists the Python libraries required to run the project.

- **README.md**: This file contains the outline for the book "A simple guide to retrieval augmented Generation".

- **notes.md**: This file contains notes about the project, including this index and file explanations.

# Chunking

Chunking is the process of splitting a large piece of text into smaller, more manageable pieces called chunks. This is a crucial step in Retrieval-Augmented Generation (RAG) systems.

## `chunk_overlap`

The `chunk_overlap` parameter in text splitters, such as `CharacterTextSplitter`, specifies the number of characters that should overlap between adjacent chunks. This overlap helps to maintain context between chunks. For example, if a sentence is split across two chunks, the overlap ensures that the beginning of the second chunk contains the end of the first chunk, so the full sentence is preserved in one of the chunks. This is important for downstream tasks like question answering, where the model might need the full context of a sentence to provide an accurate answer.
