import nextcord
from nextcord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    # PURGE
    @nextcord.slash_command(name = "purge", description = "Purges messages")
    @commands.has_permissions(administrator = True)
    async def purge(self, ctx: nextcord.Interaction, limit: int):

        if limit > 999:
            await ctx.response.send_message("You cannot delete more than 999 messages at a time.")
            return
        else:
            await ctx.response.send_message(f"Deleting {limit} message(s)")
            await ctx.delete_original_message()
            await ctx.channel.purge(limit=limit)
            await ctx.channel.send(f"Deleted {limit} message(s)")
            await ctx.delete_original_message(delay=2.0)

    @purge.error
    async def clear_error(self, ctx: nextcord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.response.send_message("You don't have the permission to purge messages")
        else:
            raise error

    # KICK
    @nextcord.slash_command(name = "kick", description = "Kick someone")
    @commands.has_permissions(administrator = True)
    async def kick(self, ctx: nextcord.Interaction, user: nextcord.Member, reason):

        if ctx.user.top_role <= user.top_role:
            await ctx.response.send_message("The user you're trying to kick probably has a role higher than or equal to yours")
            return

        await user.kick(reason = reason)
        kick = nextcord.Embed(
            title = f"{user} has been kicked from the server",
            description = f"Reason = {reason}"
        )
        await ctx.response.send_message(embed = kick)

    @kick.error
    async def clear_error(ctx: nextcord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.response.send_message("You don't have the permission to kick members")

    # BAN
    @nextcord.slash_command(name = "ban", description = "Ban someone")
    @commands.has_permissions(administrator = True)
    async def ban(self, ctx: nextcord.Interaction, user: nextcord.Member, reason):

        if ctx.user.top_role <= user.top_role:
            await ctx.response.send_message("The user you're trying to ban probably has a role higher than or equal to yours")
            return

        await user.ban(reason = reason)
        ban = nextcord.Embed(
            title = f"{user} has been banned from the server",
            description = f"Reason = {reason}"
        )
        await ctx.response.send_message(embed = ban)

    @ban.error
    async def clear_error(ctx: nextcord.Interaction, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.response.send_message("You don't have the permission to ban members")

def setup(client):
    client.add_cog(Moderation(client))