# ============================================================
# 🔐 DedSec Bot © 2025 — Created by Shane Green (ShaneYLad)
# 📜 All code is original and protected.
# Do NOT upload the same code but under a different name.
# ============================================================

import discord
from discord import app_commands
from discord.ext import commands
import secrets, string

# --- BOT SETUP ---
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree  # built-in slash command tree

# --- VARIABLES ----
ascii_logo = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠶⠶⠶⠶⠶⠤⠤⠤⢤⣤⣠⡶⠻⠉⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠀⢀⣀⡠⠤⠤⠤⠤⢄⣴⠟⠀⠀⠀⢀⣿⣿⣖⠶⠤⠤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⣀⣀⣀⣀⣀⣴⣿⠏⠀⠀⠀⡇⢘⣿⣿⣝⣧⣐⣒⣤⣬⠭⣉⣛⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠈⡍⠁⠀⠀⡾⢱⡟⠀⠀⠀⠀⡗⠈⢿⡿⠙⠚⢿⡄⠈⠉⠉⠓⠚⠿⢵⣖⣪⣭⣓⠢⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡜⠀⣷⠀⠀⢸⠃⣿⣇⠀⢀⢀⣈⣀⣀⡈⢷⣶⣷⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠶⠤⣉⡳⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡄⠸⡄⠀⢸⢠⣟⣧⣶⣿⣛⢿⣿⣿⣿⢷⣿⣿⡿⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠺⢷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡍⠀⣇⠀⣿⠻⣿⣿⣿⣿⣷⣦⡙⣿⣿⣿⣿⣯⣡⣤⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⢸⠀⣿⢼⣿⣿⠷⠋⡙⣟⣿⣉⠉⠹⢿⣿⣏⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠘⣆⣿⢸⣻⣿⣾⡏⣡⡄⣀⣉⣹⣶⣾⣿⡏⠟⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⢻⡿⣌⣿⣿⣿⣿⠟⢛⣉⠁⠈⣿⣿⡟⠁⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠁⠘⣧⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⡟⣤⣴⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⣿⣀⠀⢿⡏⢧⡈⣿⣿⣿⣿⣿⣿⣿⢿⠟⠛⠻⣿⠿⠙⣗⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠏⠁⢀⣿⡏⡀⢸⣷⣸⣿⡙⠿⣿⣿⣿⣿⣟⢮⡞⠀⠀⠋⠀⢘⣿⠟⠈⠉⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⣀⣀⣸⣿⣷⢷⠀⣿⣷⡱⣝⠒⣿⣿⢿⡿⣷⣿⠆⠀⣠⠂⢠⡟⡁⠀⠀⠈⠙⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣩⠠⠤⣀⣭⣿⣿⣞⡆⢹⣷⡿⣍⠓⠦⣼⣿⣿⡋⢁⣤⡞⣁⠴⠿⢋⣕⠀⡀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⠿⠏⢀⠀⠀⢸⣿⣿⣿⣿⢃⠀⣿⣿⠈⠣⡀⠨⣿⣿⣾⣛⣽⡟⠁⠛⣿⡿⠿⠀⡇⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠟⣿⠤⣄⠈⣳⣼⣿⣿⠝⠃⣿⣾⡀⢹⣌⡓⠦⠬⠿⠿⢿⣿⣯⣭⡔⠒⡛⠁⠀⡤⣠⣿⠀⡄⠀⢠⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡏⠀⡏⣴⣟⣿⣿⣿⡿⠏⠀⠀⠘⣷⣧⣀⣏⣛⡲⠤⠿⣿⣿⣯⣭⣽⣶⠞⠁⣠⢞⣽⣿⡟⢨⠁⠀⢸⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠁⣸⠃⠙⠛⣿⢦⣀⣀⣤⢶⣶⣿⣿⣿⣿⣶⣶⡏⠀⢀⠉⢻⣟⣫⠿⠊⢁⡾⠁⠉⣾⣿⣧⣾⣏⠀⢸⡇⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡯⢰⠋⠀⣰⣿⣿⣿⡿⣿⡏⡠⣯⡈⣹⣟⣿⣝⣙⡇⠈⢩⣭⣿⣿⠇⢀⡴⠋⠀⠀⠐⣻⣿⢿⣿⠃⠀⣿⡇⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡿⢠⠏⠀⢀⣻⣿⠏⢿⣿⣸⢸⠁⠸⣿⣿⣿⢿⠛⣿⣷⣿⣿⣿⣷⠶⠚⠉⠀⠀⠀⠀⠘⢿⣿⣿⡷⡄⢸⣹⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⢀⣴⣶⣾⣿⣿⡏⣰⢸⠇⣇⡏⠀⠀⠙⣿⣿⣟⡄⢹⡿⠿⠛⠛⣿⣶⣶⡦⠤⢔⣂⣀⠀⣾⡟⠻⡿⠁⢌⡿⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⣸⠿⠟⠟⠙⡿⠀⡇⡾⢠⣏⢣⣄⢲⣄⡘⣿⣿⣷⠘⣇⢀⣒⡯⠉⠉⠁⠈⠓⠿⣿⠟⢰⣿⡇⠴⠁⠀⣼⡽⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢘⣇⠉⠀⠀⣀⡼⠁⢸⣱⠇⢠⢻⡄⣿⣿⣿⣿⣿⣿⣏⠀⢻⣿⣷⣄⡄⠀⠀⢀⡤⠞⠁⢠⣿⣿⡀⠀⢀⣾⣵⡗⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠾⢾⣆⣰⣶⣷⡄⠀⢡⠏⠀⠀⠈⠀⠉⠙⢿⢱⠙⢿⣿⣄⡸⣿⣿⣿⣿⡿⠟⢉⡠⠆⣰⢿⣿⢿⠁⣠⠋⠐⣾⠇⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣌⠻⣿⡿⠿⣯⡶⠇⠀⠀⢠⠀⠀⠸⣿⠀⠀⣿⡏⠁⣿⠋⠁⣁⣤⠞⠉⠀⠰⢛⣿⠋⣠⡞⠁⢀⡀⠉⠀⢠⢿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠓⠧⣤⣄⣉⣀⣀⡈⠐⢪⣷⡄⠀⡇⣧⡀⣾⣧⠁⢻⣶⣾⣿⡄⠀⠀⠀⠀⣿⣯⣾⣿⡾⠛⢉⣀⡅⠀⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣟⣷⣦⣾⣷⠀⣿⣿⣧⣿⢿⣇⠀⣿⣿⠛⠀⡀⢀⠀⣠⣿⣫⣾⡽⠞⠛⠛⠾⠁⣸⢁⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢸⡟⣿⡿⣿⣷⢿⣿⣿⣿⡜⣷⠄⢸⡘⣊⣭⡾⢋⡾⣿⣿⣿⣵⠶⠚⠁⠀⠀⠀⣿⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⣧⢻⣷⢻⢿⣧⡻⣿⣿⢷⣽⡆⠈⣧⠡⢄⣼⡿⠞⣻⢿⡭⠆⠀⢀⣠⣴⠀⢰⣏⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⢸⡿⣟⣷⡻⣿⣿⣿⣟⣿⣿⡂⢹⣶⣿⣿⠀⢸⡟⠉⠀⠀⠻⣿⣞⠋⢠⠇⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

ascii_logo2 = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ██████╗ ███████╗██████╗ ███████╗███████╗ ██████╗
            ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝
            ██║  ██║█████╗  ██║  ██║███████╗█████╗  ██║     
            ██║  ██║██╔══╝  ██║  ██║╚════██║██╔══╝  ██║     
            ██████╔╝███████╗██████╔╝███████║███████╗╚██████╗
            ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚══════╝ ╚═════╝⠀⠀⠀⠀⠀⠀⠀⠀
"""

# --- ON READY ---
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await tree.sync()
        print(f"🔧 Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Sync error: {e}")


# =====================================================
#                   /warning group
# =====================================================

class WarningCommand(app_commands.Group):
    def __init__(self):
        super().__init__(name="_warning", description="⚠️ Important notice before using commands")

    @app_commands.command(name="readme", description="Read this before using any commands")
    async def readme(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**⚠️ WARNING — READ BEFORE USING DEDSEC BOT:**\n"
            "- This bot provides privacy and security advice. Use responsibly.\n"
            "- Do not share sensitive personal data in public channels.\n"
            "- Always verify links and tools independently.\n"
            "- Educational use only — not a substitute for professional cybersecurity services.\n"
            "- PLEASE USE THESE GUIDES AT YOUR OWN RISK AND DO YOUR RESEARCH (I AM NOT RELIABLE FOR ANY DOWNLOADS YOU MAKE)\n\n"
            "*Stay safe. Stay private. Stay incognito.*",
            ephemeral=True
        )

tree.add_command(WarningCommand())

# =====================================================
#                   /privacy group
# =====================================================
class PrivacyCommands(app_commands.Group):
    def __init__(self):
        super().__init__(name="privacy", description="Privacy & security tools")

    @app_commands.command(name="tips", description="Get practical privacy tips")
    async def tips(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🧠 Privacy Tips:**\n"
            "- Use strong, unique passwords.\n"
            "- Enable 2FA (authenticator app preferred).\n"
            "- Limit personal info shared online.\n"
            "- Use privacy-focused browsers (Brave, Firefox).\n"
            "- Review app permissions regularly.\n"
        )

    @app_commands.command(name="helpguides", description="Useful OSINT and privacy resources")
    async def helpguides(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🔍 OSINT & Privacy Resources:**\n"
            "- [OSINT Framework](https://osintframework.com)\n"
            "- [Privacy Guides](https://www.privacyguides.org)"
        )

    @app_commands.command(name="password_strength", description="Analyze password strength locally")
    async def password_strength(self, interaction: discord.Interaction, password: str):
        entropy = len(set(password)) * 4 + len(password) * 2
        verdict = "Strong 💪" if entropy > 50 else "Weak ⚠️"
        await interaction.response.send_message(
            f"🔐 Entropy score: **{entropy}**\nVerdict: **{verdict}**\n"
            "*(Local check only. Your password is never stored.)*",
            ephemeral=True
        )

    @app_commands.command(name="make_pass", description="Generate a secure password")
    async def make_pass(self, interaction: discord.Interaction, length: int = 16):
        charset = string.ascii_letters + string.digits + "!@#$%^&*()"
        password = ''.join(secrets.choice(charset) for _ in range(length))
        await interaction.response.send_message(f"🧾 Your password:\n`{password}`", ephemeral=True)

    @app_commands.command(name="2fa_guide", description="Learn how to set up Two-Factor Authentication")
    async def two_fa(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🔑 2FA Guide:**\n"
            "- Use apps like **Authy**, **Aegis**, or **Google Authenticator**.\n"
            "- Avoid SMS-based 2FA.\n"
            "- Backup recovery codes securely.\n"
            "- [Setup Guide](https://www.privacyguides.org/en/multi-factor-authentication/)"
        )

    @app_commands.command(name="vpn_advice", description="Advice on choosing a safe VPN")
    async def vpn_advice(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🌐 VPN Advice:**\n"
            "- No-logs policy, independent audits, open-source clients.\n"
            "- Prefer providers outside 5/9/14 Eyes.\n"
            "- VPNs hide IP, not identity.\n"
            "- [VPN Comparison](https://www.privacyguides.org/en/vpn/)"
        )

    @app_commands.command(name="secure_messaging", description="Learn about secure messaging apps")
    async def secure_messaging(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**📱 Secure Messaging Options:**\n"
            "- **Signal**: open-source, encrypted, trusted.\n"
            "- **Molly (Android)**: Signal but you can route your connection to TOR, have unused RAM data securely shredded and more.\n"
            "- **SimpleX Chat**: instant messenger that doesn't depend on any unique identifiers such as phone numbers or usernames\n"
            "- [Messaging Guide](https://www.privacyguides.org/en/real-time-communication/)"
        )

    @app_commands.command(name="breach_check", description="Learn how to check if your email was in a data breach")
    async def breach_check(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🔐 Breach Check Guide**\n"
            "\n"
            "🔍 **Step 1:** Visit [HaveIBeenPwned](https://haveibeenpwned.com)\n"
            "🔗 You can manually check if your email has been exposed in a data breach.\n"
            "\n"
            "**If your email appears in a breach:**\n"
            "• Change your password immediately\n"
            "• Enable 2FA on affected accounts\n"
            "• Use a password manager to generate and store strong passwords\n"
            "• Watch for phishing emails or suspicious activity\n"
        )



tree.add_command(PrivacyCommands())

# =====================================================
#                   /guides group
# =====================================================
class GuidesCommands(app_commands.Group):
    def __init__(self):
        super().__init__(name="guides", description="Learning paths & resources")

    @app_commands.command(name="cyber_security", description="Cyber security learning path")
    async def cyber_security(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🧠 Cyber Security Guide:**\n"
            "- Learn networking (TCP/IP), Linux, and basic CLI.\n"
            "- Explore ethical hacking: Nmap, Wireshark, Metasploit.\n"
            "- Try platforms like TryHackMe, HackTheBox.\n"
            "- [Intro Course](https://academy.tryhackme.com/)\n"
            "- [Linux Basics](https://linuxjourney.com/)"
        )

    @app_commands.command(name="web_dev", description="Web development guide")
    async def web_dev(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🌐 Web Dev Guide:**\n"
            "- Frontend: HTML, CSS, JS, React.\n"
            "- Backend: Python (Flask/Django), Node.js.\n"
            "- Learn Git, APIs, databases.\n"
            "- [Frontend Roadmap](https://roadmap.sh/frontend)\n"
            "- [Backend Roadmap](https://roadmap.sh/backend)"
        )

    @app_commands.command(name="software_engineer", description="Software engineering roadmap")
    async def software_engineer(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**💻 Software Engineering Guide:**\n"
            "- Learn Python, Java, or C++.\n"
            "- Study algorithms, data structures, OOP.\n"
            "- Practice on LeetCode, HackerRank.\n"
            "- [CS50 Course](https://cs50.harvard.edu/)\n"
            "- [CodeCamp Roadmap](https://www.freecodecamp.org/news/how-to-become-a-software-engineer-2023-roadmap/)"
        )

    @app_commands.command(name="data_analyst", description="Data analysis roadmap")
    async def data_analyst(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**📊 Data Analyst Guide:**\n"
            "- Learn Excel, SQL, Python (pandas, matplotlib).\n"
            "- Understand data visualization & statistics.\n"
            "- Use tools like Tableau, Power BI.\n"
            "- [SQL Tutorial](https://www.w3schools.com/sql/)\n"
            "- [Python Data Course](https://www.datacamp.com/)"
        )
        
    @app_commands.command(name="digital_forensics", description="Digital forensics learning path")
    async def digital_forensics(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🕵️ Digital Forensics Guide:**\n"
            "- Learn file systems: FAT32, NTFS, ext4 — especially how Linux handles metadata and journaling.\n"
            "- Get comfortable with Linux: CLI tools like `dd`, `grep`, `strings`, `hexdump`, and `mount` are essential.\n"
            "- Use forensic tools: **Autopsy**, **FTK Imager**, **Volatility**, **The Sleuth Kit**, **Plaso**, and **Wireshark**.\n"
            "- Wireshark helps analyze packet captures (PCAPs) to investigate suspicious network activity and data exfiltration.\n"
            "- Study memory, disk, and mobile forensics.\n"
            "- Understand chain of custody, evidence integrity, and legal procedures.\n"
            "- Try forensic Linux distros: **Arch**, **Kali**, **Parrot OS**, **Ubuntu**.\n"
            "- [DFIR Youtube Roadmap](https://www.youtube.com/watch?v=eekzaI0UFDA)\n"
            "- [Autopsy](https://www.sleuthkit.org/index.php)\n"
            "- [Wireshark Labs](https://www.wireshark.org/learn.html)\n"
            "- [Linux Journey](https://linuxjourney.com/) — great for CLI basics"
        )

    @app_commands.command(name="cli_basics", description="Command-line interface (CLI) basics")
    async def cli_basics(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            "**🖥️ CLI Basics Guide:**\n"
            "- Learn navigation: `cd`, `ls`, `pwd`, `mkdir`, `rm`, `touch`.\n"
            "- File inspection: `cat`, `less`, `head`, `tail`, `grep`.\n"
            "- Permissions: `chmod`, `chown`, `sudo`.\n"
            "- Networking: `ping`, `curl`, `netstat`, `traceroute`.\n"
            "- [Learn Shell](https://learnshell.org/)\n"
            "- [Explainshell](https://explainshell.com/)"
        )

tree.add_command(GuidesCommands())

# =====================================================
#                   /dedsec group
# =====================================================
class DedSecCommands(app_commands.Group):
    def __init__(self):
        super().__init__(name="dedsec", description="DedSec identity & style")

    @app_commands.command(name="logo", description="Show DedSec logo and a quote")
    async def logo(self, interaction: discord.Interaction):
        quote = "*'Privacy isn't hiding something. It's staying away from unlawful surveillance.'*"
        await interaction.response.defer()

        await interaction.followup.send(f"```{ascii_logo}```", ephemeral=False)
        await interaction.followup.send(f"```{ascii_logo2}```", ephemeral=False)
        await interaction.followup.send(quote, ephemeral=False)


tree.add_command(DedSecCommands())

# =====================================================
#                   RUN BOT
# =====================================================
bot.run("YOUR_TOKEN_HERE")
