from flask import Blueprint, request, render_template
from app.services.geometrie import generer_motif

geogen_bp = Blueprint('geogen', __name__)

@geogen_bp.route('/')
def index():
    return render_template('index.html')

@geogen_bp.route('/generer_motif', methods=['POST'])
def generer_motif_route():
    try:
        # Récupérer les données envoyées par le formulaire
        cotes = int(request.form['cotes'])
        profondeur = int(request.form['profondeur'])
        taille = int(request.form['taille'])
        angle_rotation = int(request.form['angle_rotation'])
        couleur = request.form['couleur']

        # Appeler la fonction generer_motif avec les paramètres reçus
        fichier_image = generer_motif(cotes, profondeur, taille, angle_rotation, couleur)
        
        # Renvoie le chemin de l'image générée, ou rediriger vers une page de confirmation
        return f"<img src='/{fichier_image}' alt='Motif généré' />"
    
    except Exception as e:
        # Gérer les erreurs
        return f"Une erreur est survenue : {str(e)}"