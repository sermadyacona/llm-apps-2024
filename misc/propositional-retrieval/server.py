from fastapi import FastAPI
from langserve import add_routes
from propositional_retrieval import chain

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="Retriever and Generator for RAG Chroma Dense Retrieval",
)

add_routes(app, chain, path="/propositional-retrieval")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
