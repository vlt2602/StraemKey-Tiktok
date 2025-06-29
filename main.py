import discord
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))

class CleanerBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)

    async def on_ready(self):
        guild = discord.Object(id=GUILD_ID)
        await self.tree.sync(guild=guild)
        commands = await self.tree.fetch_commands(guild=guild)

        print(f"🔍 Tìm thấy {len(commands)} slash command trong GUILD {GUILD_ID}")
        for cmd in commands:
            print(f"🗑️ Xoá: /{cmd.name}")
            await self.tree.remove_command(cmd.name, guild=guild)

        print("✅ Đã xoá toàn bộ lệnh (local cache) – hãy chờ Discord cập nhật.")
        await self.close()

bot = CleanerBot()
bot.run(TOKEN)