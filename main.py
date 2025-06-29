import discord
import os
import asyncio

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))

class CleanerBot(discord.Client):
    async def on_ready(self):
        app = await self.application_info()
        commands = await self.http.get_guild_application_commands(app.id, GUILD_ID)

        print(f"🔍 Found {len(commands)} command(s) in GUILD {GUILD_ID}")
        for cmd in commands:
            print(f"🗑️ Deleting: /{cmd['name']}")
            await self.http.delete_guild_application_command(app.id, GUILD_ID, cmd['id'])

        print("✅ All slash commands deleted.")
        await self.close()

intents = discord.Intents.default()
client = CleanerBot(intents=intents)
client.run(TOKEN)