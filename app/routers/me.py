from fastapi import APIRouter

router = APIRouter()

@router.get("/me")

def me():
    return {"nome" : "Pedro Henrique Barboza da Silva",
            "email" : "email.escolar174@gmail.com",
            "curso" : "Sistemas de Informação",
            "github" : "https://github.com/stingy-namake/",
            "cidade" : "Brejo Santo CE",
            "interesses" : "League of Legends, Genshin Impact, Arch Linux"}