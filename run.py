from app import create_app  # Assumons que 'create_app' est une fonction dans '__init__.py'

app = create_app()  # Crée l'application Flask

if __name__ == '__main__':
    app.run(debug=True)  # Démarre le serveur en mode debug
