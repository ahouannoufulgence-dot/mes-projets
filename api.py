from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def accueil():
    return {"message": "Mon API fonctionne !"}

@app.get("/bonjour/{nom}")
def bonjour(nom: str):
 return {"message": "Bonjour " + nom + " !"}