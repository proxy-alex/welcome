import amino

email = "liza24221@gmail.com"  # Set your own password here!
password = "sagar890"  # Set your own password here!
cid = "59449739"  # Community ID

client = amino.Client()
client.login(email=email, password=password)
print("Bot logged in")
sub = amino.SubClient(comId=cid, profile=client.profile)
print("Bot logged onto the community, id:", cid, "\nBot Name:", sub.profile.nickname)

join = """welcome in the chat"""

@client.callbacks.event('on_group_member_join')
def on_group_member_join(data):
        nick = data.message.author.nickname
        msg = {
        'message': f"{join}\n\n[CB]{nick} welcome 🌹🌹🌹🌹!!",
        'chatId': data.message.chatId,
        'mentionUserIds': [data.message.author.userId]
        }
        sub.send_message(**msg)
