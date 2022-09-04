import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents)

test_server = 919202475276378174

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("..................................")

# HELP
@client.slash_command(name = "help", description = "Help for commands")
async def help(ctx):
    help = discord.Embed(
        title = "Pro Bros Community Bot",
        description = "It is the official Bot of the **Pro Bros Community** with simple utility features. More features coming soon."
    )
    help.add_field(
        name = "ping",
        value = "A random command for checking the stats=us of the bot"
    )
    help.add_field(
        name = "membercount",
        value = "Shows the current number of members in the server"
    )
    help.add_field(
        name = "avatar",
        value = "Gives the avatar of an user"
    )
    help.add_field(
        name = "purge",
        value = "Bulk delete messages"
    )
    help.add_field(
        name = "Kick",
        value = "Kick members"
    )
    help.add_field(
        name = "Ban",
        value = "Ban members"
    )
    await ctx.respond(embed = help)

# LOADING COGS
initial_extensions = []

for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        initial_extensions.append(f"Cogs.{filename[:-3]}")

print("Cogs")
print("..................................")
print(initial_extensions)
print("..................................")

if __name__ == "__main__":
    for extensions in initial_extensions:
        client.load_extension(extensions)
# LOADING DONE

client.run(os.getenv("TOKEN"))