from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CodeInput(BaseModel):
    code: str


@app.get("/")
def home():
    return {"message": "API do Módulo 5 funcionando"}


@app.post("/generate-diagram")
def generate_diagram(input: CodeInput):
    # Simulação de diagrama UML
    diagram = """
    @startuml
    class User
    class Order
    User --> Order
    @enduml
    """

    return {
        "diagram": diagram,
        "message": "Diagrama gerado com sucesso"
    }