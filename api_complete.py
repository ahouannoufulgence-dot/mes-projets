from fastapi import FastAPI

app = FastAPI()

# Notre base de données temporaire (une liste)
utilisateurs = []

# Voir tous les utilisateurs
@app.get("/utilisateurs")
def voir_utilisateurs():
    return utilisateurs

# Ajouter un utilisateur
@app.post("/utilisateurs")
def ajouter_utilisateur(nom: str, email: str):
    utilisateur = {"nom": nom, "email": email}
    utilisateurs.append(utilisateur)
    return {"message": "Utilisateur ajouté !", "utilisateur": utilisateur}