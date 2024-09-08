from flask import Flask, render_template, request, jsonify, session, url_for,redirect, Blueprint
import requests
import os 
from check_key import *
import git



app = Flask(__name__)

# Variables globales

app.secret_key = os.urandom(24)
license_key = ""
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process-data', methods=['POST'])
def process_data():
    from discord_main import username, discord_id
   
    from discord_send import send_webhook, send_webhook_error
    """Met à jour la clé de licence et retourne une réponse au client."""
    
    # Récupérer les données envoyées par JavaScript
    data = request.json
    input_key = data.get('key')
    
    # Assigner input_key à license_key
    license_key = input_key

    # # Log de la clé côté serveur
    # print(f"Clé reçue: {input_key}")
    # print(f"Current license key: {license_key}")

    # Appeler la fonction de vérification
    check_response = main_check_key(license_key)
    User, discord_id_1, key_acces = check_response
    # Vérifier le code de statut de la réponse de l'API externe
    try:
        if discord_id_1 == discord_id:
                    from write_in_json import writter_key
                    # Traitement réussi
                    send_webhook(discord_id, license_key, key_acces, discord_id_1)
                    writter_key(license_key)
                    return jsonify({"message": "SUCCES AUTH KEY!", "status": "success"}), 200
        else:
                    send_webhook_error(discord_id, license_key, key_acces, discord_id_1)
                    return jsonify({"message": "ERROR AUTH KEY!", "status": "error"}), 404  
    except Exception as e:
        # Gérer les exceptions
        print(f"Erreur: {e}")
        return jsonify({"message": "INTERNAL SERVER ERROR", "status": "error"}), 500

# Route pour la page de connexion
@app.route('/login')
def login_1():
    from discord_main import login
    return login()

@app.route('/callback')
def callback_1():
    from discord_main import callback
    return callback()

@app.route("/confirmation_key")
def home1():
    return render_template('index_verif.html')

@app.route("/check_update", methods=['GET'])
def downloadUpdate():
    from pull_update import fetch_update

    test = fetch_update()
    local_commit, remote_commit, repo_url, repo = test

    if local_commit == remote_commit:
        print("Le dépôt est déjà à jour")
        # return jsonify({"status": "success"}), 200
        return redirect("/")
    else:
        print("Le dépôt va être mis à jour")
        # return jsonify({"status": "waiting"}), 200
        return redirect("/download_update")

    
@app.route("/download_update")
def page():
    return render_template('index_update.html')
    
def download():
    from pull_update import repo,repo_url
    # Faire un git pull
    print(f"Pull du dépôt {repo_url}...")
    repo.remotes.origin.pull()

    print("Pull effectué avec succès.")
    return jsonify({"message": "repo be update", "status": "success"}), 200

    


      
if __name__ == '__main__':
    app.run(debug=True)
