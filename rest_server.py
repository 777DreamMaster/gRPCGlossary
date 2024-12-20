import os

from fastapi import FastAPI, HTTPException
import grpc
import glossary_pb2
import glossary_pb2_grpc
from typing import List

from schemas import TermOut, TermCreate, MessageResponse

app = FastAPI()

host = os.getenv("GRPC_SERVER_HOST", "localhost")
port = os.getenv("GRPC_SERVER_PORT", "50051")
channel = grpc.insecure_channel(f"{host}:{port}")
stub = glossary_pb2_grpc.GlossaryServiceStub(channel)


@app.get("/terms/", response_model=List[TermOut])
async def get_terms():
    response = stub.GetAllTerms(glossary_pb2.Empty())

    return [TermOut(id=term.id, term=term.term, definition=term.definition) for term in response.terms]


@app.get("/term/{term_name}", response_model=TermOut)
async def get_term(term_name: str):
    print(111111)
    grpc_response = stub.GetTerm(glossary_pb2.TermNameRequest(term="API"))
    print(222222)
    if grpc_response.term:
        term = grpc_response.term
        print(333333)
        return TermOut(term=TermOut(id=term.id, term=term.term, definition=term.definition))
    raise HTTPException(status_code=404, detail="Term not found")


@app.post("/terms", response_model=MessageResponse)
async def add_term(term: TermCreate):
    grpc_term = glossary_pb2.Term(
        term=term.term,
        definition=term.definition,
    )
    response = stub.AddTerm(glossary_pb2.Term(term=grpc_term))
    return MessageResponse(message=response.message)


@app.put("/terms", response_model=MessageResponse)
async def update_term(term: TermCreate):
    try:
        grpc_term = glossary_pb2.Term(
            term=term.term.term,
            definition=term.term.definition,
        )
        response = stub.UpdateTerm(glossary_pb2.Term(term=grpc_term))
        return MessageResponse(message=response.message)
    except grpc.RpcError as e:
        raise HTTPException(status_code=404 if e.code() == grpc.StatusCode.NOT_FOUND else 500, detail=e.details())


@app.delete("/term/{term_name}", response_model=MessageResponse)
async def delete_term(term_name: str):
    try:
        response = stub.DeleteTerm(glossary_pb2.TermNameRequest(term=term_name))  # Передаем ID
        return MessageResponse(message=response.message)
    except grpc.RpcError as e:
        raise HTTPException(status_code=404 if e.code() == grpc.StatusCode.NOT_FOUND else 500, detail=e.details())
