import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # PING
    @discord.slash_command(name = "ping", description = "Replies with pong!")
    async def ping(self, ctx):
        ping = discord.Embed(
            title = "Pong 🏓",
            description = f"Time : {round(self.client.latency * 1000)}ms"
        )
        await ctx.respond(embed = ping)

    # MEMBERCOUNT
    @discord.slash_command(name = "membercount", description = "Shows the number of members in the server")
    async def membercount(self, ctx):
        mc = discord.Embed(
            title = "Membercount",
            description = f"We currently have {ctx.guild.member_count} members in our server"
        )
        await ctx.respond(embed = mc)

    # AVATAR
    @discord.slash_command(name = "avatar", description = "Shows the avatar of a user")
    async def avatar(self, ctx, user: discord.Member):
        try:
            avatar = user.avatar.url
            av = discord.Embed(title = "Avatar")
            av.set_image(url = f"{avatar}")
            await ctx.respond(embed = av)
        except:
            await ctx.respond("User has no avatar.")

def setup(client):
    client.add_cog(Basic(client))