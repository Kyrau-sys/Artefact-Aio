from flask import Flask, render_template, request, jsonify, session, url_for,redirect, Blueprint
import requests
import os 
from check_key import main_check_key

app = Flask(__name__)
username = ""
# Variables globales

app.secret_key = os.urandom(24)

CLIENT_ID = "1279882913441255517"
CLIENT_SECRET = "SRK5rPkVuSS6BStyrtOrb0dr0mvTckvX"
REDIRECT_URI = "http://localhost:5000/callback"
GUILD_ID = "1258099019045929111"
discord_id = ""


def login():
    # Construction de l'URL d'authentification Discord 
    discord_auth_url = (
        "https://discord.com/oauth2/authorize?client_id=1279882913441255517&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000%2Fcallback&scope=guilds+email+identify"
        
    )
    # Redirige l'utilisateur vers l'URL d'authentification Discord
    return redirect(discord_auth_url)




def callback():
    code = request.args.get('code')
    
    if not code:
        return redirect("http://localhost:5000")
    
    token_url = 'https://discord.com/api/oauth2/token'
    
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(token_url, data=data, headers=headers)
    
    if response.status_code != 200:
        # Affichez le message d'erreur pour le débogage
        return f'Erreur lors de l\'authentification. Code HTTP: {response.status_code}, Réponse: {response.text}', 400
    
    response_data = response.json()
    access_token = response_data.get('access_token')

    user_guilds = requests.get(
        'https://discord.com/api/users/@me/guilds',
        headers={'Authorization': f'Bearer {access_token}'}
    ).json()
    

    is_member = any(guild['id'] == GUILD_ID for guild in user_guilds)
    
    if not access_token:
        return 'Erreur lors de l\'authentification.', 400

    user_info = get_user_info(access_token)
    print(user_info)
    

    if is_member:
        return redirect(f"http://localhost:5000/check_update")

    else:
        return redirect('http://localhost:5000')



def get_user_info(access_token):
    global discord_id
    user_url = 'https://discord.com/api/v10/users/@me'
    
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(user_url, headers=headers)
    user_data = response.json()
    
    # Récupérez l'ID Discord et le nom d'utilisateur
    discord_id = user_data.get('id')
    username = user_data.get('username')
    
    if not discord_id:
        return 'Erreur : impossible de récupérer les informations de l\'utilisateur.', 400

    
    return discord_id


    