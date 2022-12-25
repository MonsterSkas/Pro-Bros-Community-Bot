import nextcord
from nextcord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # PING
    @nextcord.slash_command(name = "ping", description = "Replies with pong!")
    async def ping(self, ctx: nextcord.Interaction):
        ping = nextcord.Embed(
            title = "Pong 🏓",
            description = f"Time : {round(self.client.latency * 1000)}ms"
        )
        await ctx.response.send_message(embed = ping)

    # MEMBERCOUNT
    @nextcord.slash_command(name = "membercount", description = "Shows the number of members in the server")
    async def membercount(self, ctx: nextcord.Interaction):
        mc = nextcord.Embed(
            title = "Membercount",
            description = f"We currently have {ctx.guild.member_count} members in our server"
        )
        await ctx.response.send_message(embed = mc)

    # AVATAR
    @nextcord.slash_command(name = "avatar", description = "Shows the avatar of a user")
    async def avatar(self, ctx: nextcord.Interaction, user: nextcord.Member):
        try:
            avatar = user.avatar.url
            av = nextcord.Embed(title = "Avatar")
            av.set_image(url = f"{avatar}")
            await ctx.response.send_message(embed = av)
        except:
            await ctx.response.send_message("User has no avatar.")

    # ADDROLE
    @nextcord.slash_command(name = "addrole", description = "Assigns a role to you")
    async def addrole(self, ctx: nextcord.Interaction, role: nextcord.Role):
        user = ctx.user

        if role.name == "new role":
            await user.add_roles(role)
            await ctx.response.send_message(f"Gave you {role} role")
        else:
            await ctx.response.send_message("Can't give you that role")

    # REMOVEROLE
    @nextcord.slash_command(name = "removerole", description = "Removes a role from you")
    async def removerole(self, ctx: nextcord.Interaction, role: nextcord.Role):
        user = ctx.user

        if(user.get_role(role.id) == False):
            await ctx.response.send_message("You don't have that role")
        else:
            await user.remove_roles(role)
            await ctx.response.send_message(f"Removed {role} role")

def setup(client):
    client.add_cog(Basic(client))