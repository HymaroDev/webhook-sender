from discord_webhook import DiscordWebhook, DiscordEmbed

hook=DiscordWebhook("https://discord.com/api/webhooks/xxxxxxxxx/xxxxxxxxxxxxxx")

title= input("Coloque o Titulo da Embed: ")
description= input("Coloque a descricao da embed: ")
footer= input("Coloque o footer: ")

embed= DiscordEmbed(title=f"{title}", description=f"{description}")

embed.set_footer(text=f"{footer}")

hook.add_embed(embed)
response = hook.execute()
