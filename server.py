import grpc
from concurrent import futures

import glossary_pb2
import glossary_pb2_grpc
from db import SessionLocal, Base, engine
from initial_terms import INITIAL_TERMS
from models import TermModel


def init_db():
    Base.metadata.create_all(bind=engine)


def db_init_terms():
    db = SessionLocal()
    try:
        for term_data in INITIAL_TERMS:
            term = db.query(TermModel).filter(TermModel.term == term_data["term"]).first()
            if not term:
                db.add(TermModel(**term_data))
        db.commit()
    finally:
        db.close()


class DictionaryService(glossary_pb2_grpc.GlossaryServiceServicer):
    def GetAllTerms(self, request, context):
        db = SessionLocal()
        terms = db.query(TermModel).all()
        db.close()
        return glossary_pb2.TermsList(
            terms=[glossary_pb2.Term(id=t.id, term=t.term, definition=t.definition) for t in terms]
        )

    def GetTerm(self, request, context):
        db = SessionLocal()
        term = db.query(TermModel).filter(TermModel.term == request.term).first()
        db.close()
        print(term)
        if term:
            return glossary_pb2.Term(
                term=glossary_pb2.Term(id=term.id, term=term.term, definition=term.definition)
            )
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Термин не найден")
        return glossary_pb2.Term()

    def AddTerm(self, request, context):
        db = SessionLocal()
        new_term = TermModel(
            term=request.term.term,
            definition=request.term.definition,
        )
        db.add(new_term)
        db.commit()
        db.close()
        return glossary_pb2.MessageResponse(message="Термин добавлен")

    def UpdateTerm(self, request, context):
        db = SessionLocal()
        term = db.query(TermModel).filter(TermModel.term == request.term.term).first()
        if term:
            term.term = request.term.term
            term.definition = request.term.definition
            db.commit()
            db.close()
            return glossary_pb2.MessageResponse(message="Термин обновлён")
        db.close()
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Термин не найден")
        return glossary_pb2.MessageResponse(message="Термин не найден")

    def DeleteTerm(self, request, context):
        db = SessionLocal()
        term = db.query(TermModel).filter(TermModel.term == request.term).first()
        if term:
            db.delete(term)
            db.commit()
            db.close()
            return glossary_pb2.MessageResponse(message="Термин удалён")
        db.close()
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("Term not found")
        return glossary_pb2.MessageResponse(message="Термин не найден")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    glossary_pb2_grpc.add_GlossaryServiceServicer_to_server(DictionaryService(), server)
    server.add_insecure_port("[::]:50051")
    print("gRPC server is running on port 50051")
    init_db()
    db_init_terms()
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
