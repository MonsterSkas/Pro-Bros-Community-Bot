import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

from keep_alive import keep_alive

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(intents=intents)

test_server = 919202475276378174

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    print("..................................")

# HELP
@client.slash_command(name = "help", description = "Help for commands")
async def help(ctx: nextcord.Interaction):
    help = nextcord.Embed(
        title = "Help",
        description = "Hi, I'm the official bot of **SXI Masters** with simple features"
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

    help.set_author(name="Rayquaza")
    help.author.icon_url = "https://cdn.discordapp.com/avatars/1011260492486033419/e2c5accbcf86f0681ec45bd759c5e40a.png?size=1024"
    help.set_thumbnail(url="https://cdn.discordapp.com/avatars/1011260492486033419/e2c5accbcf86f0681ec45bd759c5e40a.png?size=1024")
    help.set_footer(text="Total commands: 3")
    await ctx.response.send_message(embed = help)

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

keep_alive()

#client.run(os.getenv("TOKEN"))

while True:
    try:
        client.run(os.environ["TOKEN"])
    except nextcord.errors.HTTPException as err:
        if err.status == 429:
            print("\n\nERROR 429")
            print("\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
            os.system("kill 1")