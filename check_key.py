import hashlib
import platform
import requests
import aiohttp
HWID = ""
api_key = "G0mUekOJOQ_wBVoBT-etbPebRJYwCgE8DZ5TAMD3Txk"
license_key = ""
key_acces = None
discord_id_1 = None
User = None


def generate_hwid():
    """Génère un HWID basé sur le nom de l'hôte."""
    return hashlib.sha256(platform.node().encode()).hexdigest().strip()
    

def validate_license(license_key, HWID):
    """Valide la clé de licence en appelant une API externe."""
    url = f"https://api.whop.com/api/v2/memberships/{license_key}/validate_license"
    
    payload = {"metadata": {"HWID": HWID}}
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}",  # Remplacez par votre clé API
        "content-type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print(f"Validation Response: {response.status_code}")

    if data.get('valid', True):
            user_details = data.get('discord', {})
            User = user_details.get('username', '')  
            discord_id_1 = user_details.get('id', '')
            key_acces = data.get('license_key', '')
            return User, discord_id_1, key_acces
    else:
        return {"valid": False, "error": "License not valid"}, None
    
def main_check_key(license_key):
    """Vérifie la clé de licence et retourne la réponse de l'API."""
    HWID = generate_hwid()
    response = validate_license(license_key, HWID)
    return response



