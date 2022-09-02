import discord
from discord.ext import commands

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

def setup(client):
    client.add_cog(Moderation(client))