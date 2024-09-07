from discord_webhook import DiscordEmbed, DiscordWebhook
from datetime import datetime

import socket
from main_flask import license_key

ROLE_ID = "1270076476842049617"
# Obtenir l'heure actuelle
current_version = "v.00"
current_time = datetime.now().strftime('%Y-%m-%d : %H:%M:%S')
discord_id = ""

def send_webhook(discord_id, license_key, key_acces, discord_id_1):
    from discord_main import discord_id
    host = socket.gethostname()
    url_webhook = "https://discord.com/api/webhooks/1280993848541319198/Nlb8j7njEMyCIOLnVITwH-t5JPuoB4CG36hurSti2uZNaqwRI8qxRG7FIVmTGfxStj6_"
    print(discord_id_1, key_acces, "1")
    webhook = DiscordWebhook(url=url_webhook)

    embed = DiscordEmbed(
        title="",
        description=f"""**DISCORD :**\n-------\n**USER** : <@{discord_id}>\n**ID** : {discord_id}\n**HOST** :{host}\n\n**KEY** : {license_key}
        \n\n-----------------------------------\n\n**WHOP :**\n-------\n**USER** : <@{discord_id_1}>\n**ID** : {discord_id_1}\n**KEY** : {key_acces}\n\n\n   **AUTHORIZED**""",
        color= '130042'
    )    
    embed.set_footer(text=f'{current_time}'+'\n\n'+'v.00')
    
    webhook.add_embed(embed)
    webhook.execute()

def send_webhook_error(discord_id, license_key, key_acces, discord_id_1):
    from discord_main import discord_id
    host = socket.gethostname()
    url_webhook = "https://discord.com/api/webhooks/1280993848541319198/Nlb8j7njEMyCIOLnVITwH-t5JPuoB4CG36hurSti2uZNaqwRI8qxRG7FIVmTGfxStj6_"
    print(discord_id_1, key_acces, "1")
    webhook = DiscordWebhook(url=url_webhook,content=f"<@&{ROLE_ID}>")
    embed = DiscordEmbed(
        title="",
        description=f"""**DISCORD :**\n-------\n**USER** : <@{discord_id}>\n**ID** : {discord_id}\n**HOST** :{host}\n\n**KEY** : {license_key}
        \n\n-----------------------------------\n\n**WHOP :**\n-------\n**USER** : <@{discord_id_1}>\n**ID** : {discord_id_1}\n**KEY** : {key_acces}\n\n\n   **INSTRUSIF** """,
        color= '990040'
    )    
    
    embed.set_footer(text=f'{current_time}'+'\n\n'+'v.00')
    
    webhook.add_embed(embed)
    webhook.execute()
