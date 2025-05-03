import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import numpy as np
import datetime
import os

def generer_motif(cotes, profondeur, taille, angle_rotation, couleur='blue'):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    for i in range(0, profondeur):
        angle_debut = np.radians(i * angle_rotation)
        angles = np.linspace(0, 2 * np.pi, cotes + 1) + angle_debut
        x = taille * np.cos(angles)
        y = taille * np.sin(angles)
        ax.plot(x, y, color=couleur)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    DOSSIER_IMAGES = "app/static/images/generated"
    os.makedirs(DOSSIER_IMAGES, exist_ok=True)

    nom_fichier = f"motif_{timestamp}.png"
    chemin_complet = os.path.join(DOSSIER_IMAGES, nom_fichier)
    plt.savefig(chemin_complet)

    plt.close()

    return "static/images/generated/" + nom_fichier