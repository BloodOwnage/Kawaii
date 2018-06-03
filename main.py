import discord
import asyncio
import random
import secreto

TOKEN =  secreto.seu_token()
msg_id = None
msg_user = None

from discord import Client

client: Client = discord.Client()
COR = 0xFF00FF

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('----------Kawaii----------')

@client.event         #Reacts
async def on_message(message):
    if message.content.lower().startswith('bom dia'):
        await client.send_message(message.channel, "**Olá Bom Dia >.<**")

    if message.content.lower().startswith('kawaii'):
        await client.send_message(message.channel, "**Oieee >.<**")

    if message.content.lower().startswith('fdp'):
        await client.send_message(message.channel, "**Sem Palavrões boca suja >:(**")

    if message.content.lower().startswith('boa tarde'):
            await client.send_message(message.channel, "**Olá,tudo bem? Boa Tarde >.<**")
    if message.content.lower().startswith('boa noite'):
            await client.send_message(message.channel, "**Oie Boa Noite >.<**")

    if message.content.lower().startswith('arrombado'):
            await client.send_message(message.channel, "**Sem Palavrões boca suja >:(**")

    if message.content.lower().startswith('vai toma no cu'):
            await client.send_message(message.channel, "**Sem Palavrões boca suja >:(**")

    if message.content.lower().startswith('kawaii explica o dino que n é facil programar'):
        await client.send_message(message.channel, "**Dinao calma,Rlx o seu comando vai ficar pronto é só voce esperar**")

    if message.content.lower().startswith('blood'):
        await client.send_message(message.channel, "**Este é o meu mestre <@400380303220277278>**")

    if message.content.lower().startswith('biurifor'):
        await client.send_message(message.channel, "**Ia biurifor** https://i.ytimg.com/vi/l-DFmaVUzJY/hqdefault.jpg")

    if message.content.lower().startswith('a biurifor'):
        await client.send_message(message.channel, "**Ia biurifor** https://i.ytimg.com/vi/l-DFmaVUzJY/hqdefault.jpg")

    if message.content.lower().startswith('ia biurifor'):
        await client.send_message(message.channel, "**Ia biurifor** https://i.ytimg.com/vi/l-DFmaVUzJY/hqdefault.jpg")

    if message.content.lower().startswith('eu vo cai'):
        await client.send_message(message.channel, "**Eu vo Caiiii** https://www.youtube.com/watch?v=8Ppv4L_aokY")

    if message.content.lower().startswith('me derrubaro aqui o'):
        await client.send_message(message.channel, "**Me derrubaro aqui o** https://www.youtube.com/watch?v=8Ppv4L_aokY")

    if message.content.lower().startswith('e quem disse que isso é problema meu'):
        await client.send_message(message.channel, "http://img.ibxk.com.br/ns/rexposta/2018/05/20/20165358256463.png?watermark=neaki&w=600")

    if message.content.lower().startswith('e quem disse que isso e problema meu'):
        await client.send_message(message.channel, "http://img.ibxk.com.br/ns/rexposta/2018/05/20/20165358256463.png?watermark=neaki&w=600")

    if message.content.lower().startswith('$ajuda'):
        await client.send_message(message.channel, "```Olá eu sou a Kawaii e pelo o que eu vi você solicitou ajuda. Eu sou um bot de Animação ainda estou em desenvolvimento.Eu ainda tenho poucos comandos mas você pode me ajudar com sugestoes,ideias ,etc.Para contatar algum erro ou bug ou até mesmo dar ideias me chame no discord:Blood#1174 Ou entre no nosso grupo:https://discord.gg/aPj97Hf```")

    if message.content.lower().startswith('oi'):
        await client.send_message(message.channel, "**Oiee >.<**")

    if message.content.lower().startswith('tururu'):
        await client.send_message(message.channel, "**Tururu** https://www.youtube.com/watch?v=vh_EFU138j0")
	
# ===================================================
# Respostas por Embed | Imagens
# ===================================================

    if message.content.lower().startswith('kawaii help'):  # PREFIX DO COMANDO (Deste, no caso) Não escrever em Maiúsculo.
        fazer = discord.Embed(
            title="**Aqui estar os meus comando! >u<**",
            color=COR,
	    description="**COMANDOS**\n"
	            "- bom dia, boa tarde e boa noite \n"
                    "- oi, tururu \n"
                    "- blood, kawaii \n" 
                    "- $ajuda",)

        botmsg = await client.send_message(message.channel, embed=fazer)

        await client.send_message(message.channel, ">.<")	
	


@client.event                    #Entrada
async def on_member_join(member):
   canal = client.get_channel("426929175157407746")
   msg = "Bem Vindo {} espero que goste do nosso grupo >.<".format(member.mention)
   await client.send_message(canal, msg)

@client.event                    #Saida
async def on_member_remove(member):
   canal = client.get_channel("426929175157407746")
   msg = "Fico muito triste em saber que {} nos deixou...".format(member.mention)
   await client.send_message(canal, msg)




client.run(TOKEN)
