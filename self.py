import os
import selfcord
import traceback
from dotenv import load_dotenv
load_dotenv()
OWNER = os.getenv('OWNER')
TOKEN = os.getenv('TOKEN')

if not OWNER or not TOKEN:
    raise Exception('Missing OWNER or TOKEN in .env file')
else:
    OWNER = int(OWNER)

class Nerd:
    def __init__(self):
        self.nerds: list[int] = []

    async def execute(self, mention: str):
        if mention == "list": # if the argument was "list", and not a mention
            # return the list of nerds, turn userid into username
            print("\n[Nerds]")
            for nerd in self.nerds:
                print(f" * {nerd}: {str(client.get_user(nerd))}\n") 
            return

        userid = int(mention.removeprefix('<@').removesuffix('>')) # remove mention formatting

        if userid not in self.nerds:
            self.nerds.append(userid)
            print('Added a nerd!', userid)
        else:
            self.nerds.remove(userid)
            print('Removed a nerd!', userid)

    async def on_message(self, message):
        if message.author.id in self.nerds:
            return await message.reply('"' + message.content + '"' + ' - 🤓')


class Client(selfcord.Client):
    def __init__(self):
        super().__init__()
        self.COMMANDS = {
            "nerd": Nerd(),
        }

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        try:
            # handle commands, only allow the owner to use commands
            if message.author.id == OWNER and message.content.startswith('/'):
                args = message.content.split(' ') # spaces separate the command and any following arguments
                await message.delete() # delete the message after the bot processes it, to keep the chat clean
                await self.COMMANDS[args[0][1:]].execute(args[1]) # Search in the COMMANDS dict for the first argument, excluding the '/'. Call the function associated with the command and pass the arguments

            # on_message handler
            for command in self.COMMANDS.values():
                await command.on_message(message)

        # todo: print stack trace for errors occurring in other places as well, not just on_message
        except Exception as error:
            print(traceback.format_exc()) # always keep the bot running, print errors rather than crashing
            pass

client = Client()
client.run(TOKEN)
