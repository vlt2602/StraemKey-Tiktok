import os
import requests
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption

intents = nextcord.Intents.default()
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập với tên: {bot.user}")

@bot.slash_command(name="getkey", description="Lấy TikTok Stream Key mới nhất")
async def getkey(interaction: Interaction):
    sessionid = os.getenv("SESSIONID")
    sid_tt = os.getenv("SID_TT")

    headers = {
        "cookie": f"sessionid={sessionid}; sid_tt={sid_tt};",
        "referer": "https://www.tiktok.com/",
        "user-agent": "Mozilla/5.0"
    }

    try:
        res = requests.get("https://livecenter.tiktok.com/webcast/room/create/", headers=headers)
        data = res.json()

        stream_url = data['data']['push_url']
        stream_key = stream_url.split("/")[-1]
        rtmp_url = "/".join(stream_url.split("/")[:-1])

        await interaction.response.send_message(
            f"**TikTok Stream Key**\n🔑 Key: `{stream_key}`\n🌐 RTMP: `{rtmp_url}`\n⏰ Hiệu lực ~2h"
        )
    except Exception as e:
        await interaction.response.send_message(f"❌ Lỗi lấy key: {e}")

bot.run(os.getenv("DISCORD_TOKEN"))
