class TableFlipper:
    def __init__(self):
        self.table_flippers: list[int] = []

    async def execute(self, mention: str):
        if mention == "list":
            print("[Table Flippers]")
            for table_flipper in self.table_flippers:
                print(f"\t* {table_flipper}: {str(client.get_user(table_flipper))}\n") 
            return

        userid = int(mention.removeprefix('<@').removesuffix('>'))

        if userid not in self.table_flippers:
            self.table_flippers.append(userid)
            print('Added a table flipper!', userid)
        else:
            self.table_flippers.remove(userid)
            print('Removed a table flipper!', userid)

    async def on_message(self, message):
        if message.author.id in self.table_flippers:
            upside_down_tables = [
                "┻━┻",
                "┻",
                "ㅛ",
                "ㅗ",
                "╚",
                "╝",
                "┗",
                "┛",
                "|",
                "_",
                "ⵡ",
                "Ц",
            ]
            for table in upside_down_tables:
                if table in message.content:
                    return await message.reply("┬─┬ノ( º _ ºノ)")\

class Yapper:
    def __init__(self):
        self.yappers: list[int] = []

    async def execute(self, mention: str):
        if mention == "list":
            print("[Yappers]")
            for yapper in self.yappers:
                print(f"\t* {yapper}: {str(client.get_user(yapper))}\n") 
            return

        userid = int(mention.removeprefix('<@').removesuffix('>'))

        if userid not in self.yappers:
            self.yappers.append(userid)
            print('Added a yapper!', userid)
        else:
            self.yappers.remove(userid)
            print('Removed a yapper!', userid)

    async def on_message(self, message):
        if message.author.id in self.yappers:
            return await message.reply("🫸😝🫷 LALALA I CANT HEAR YOU") 
