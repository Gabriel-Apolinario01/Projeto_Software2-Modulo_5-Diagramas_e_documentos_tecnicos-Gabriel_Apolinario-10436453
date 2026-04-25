from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CodeInput(BaseModel):
    code: str


@app.get("/")
def home():
    return {
        "message": "API do Módulo 5 funcionando",
        "status": "ok"
    }


@app.post("/generate-diagram")
def generate_diagram(input: CodeInput):
    try:
        # Simulação usando o código do usuário
        diagram = f"""
@startuml

' Diagrama gerado automaticamente

{input.code}

@enduml
"""

        return {
            "diagram": diagram,
            "message": "Diagrama gerado com sucesso",
            "status": "success"
        }

    except Exception as e:
        return {
            "message": "Erro ao gerar diagrama",
            "error": str(e),
            "status": "error"
        }
