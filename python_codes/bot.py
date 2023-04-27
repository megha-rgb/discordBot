import discord
import botResponses

class VeggieBot():
    def __init__(self, dictionary):
        self.responses = botResponses.BotResponse(dictionary)
        self.run_bot()
        
    def run_bot(self):

        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)

        

        @client.event
        async def on_ready():
            print(f'{client.user} is now running!')

        @client.event
        async def on_message(message):

            # # Get data about the user
            # username = str(message.author)
            # user_message = str(message.content)
            # channel = str(message.channel)
            # print(f"{username} said: '{user_message}' ({channel})")

            if message.author == client.user:
                return
            
            response = self.responses.getResponse(message.content)
            if response is not None:
                await message.channel.send(response)

        TOKEN = 'make ur own token'
        client.run(TOKEN)  #super secure, definitely no issue with having the key here


            

