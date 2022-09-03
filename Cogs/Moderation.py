import discord
from discord.ext import commands
import os

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # PURGE
    @discord.slash_command(name = "purge", description = "Purges messages")
    @commands.has_permissions(administrator = True)
    async def purge(self, ctx, limit: int):
        if limit > 999:
            await ctx.respond("You cannot delete more than 999 messages at a time.")
            return
        else:
            await ctx.delete()
            await ctx.channel.purge(limit = limit)

    @purge.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You don't have the permission to purge messages.")
        else:
            raise error

    # KICK
    @discord.slash_command(name = "kick", description = "Kick someone")
    @commands.has_permissions(administrator = True)
    async def kick(self, ctx, user: discord.Member, reason):
        await user.kick()
        kick = discord.Embed(
            title = f"{user} has been kicked from the server",
            description = f"Reason : {reason}"
        )
        await ctx.respond(embed = kick)

    @kick.error
    async def clear_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.respond("You don't have the permission to kick members")

def setup(client):
    client.add_cog(Moderation(client))