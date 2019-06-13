import discord
import asyncio
from discord.ext import commands
from logger import get_logger
from config import loadconfig

__author__ = "NotThatSiri"
__version__ = "0.0.2"

logger = get_logger(__name__)

class mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ban'])
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def dracarys(self, ctx, member: discord.Member=None, *reason):
        '''ban a member with a reason (MOD ONLY)
        Example:
        -----------
        d/ dracarys @bob#1234
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.ban(reason=reason)
            description = "**{}** Went up in flames.".format(member)
            embed=discord.Embed(description=description, color=0xff8040)
            embed.set_image(url="https://media1.tenor.com/images/4bacffc46ccbc06bd97ab1b531b4bdac/tenor.gif")
            await ctx.send(embed=embed)
        else:
            await ctx.send('**:no_entry:** No Users found')

    @commands.command(aliases=['ress','unban'])
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def resurrect(self, ctx, user: discord.User=None, *reason):
        '''unban a member with a reason (MOD ONLY)
        example:
        -----------
        d/ unban 102815825781596160
        '''
        if user is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await ctx.guild.unban(user, reason=reason)
            await ctx.send('{} have been resurrected.'.format(user))
        else:
            await ctx.send('**:no_entry:** No user specified!')

    @commands.command(aliases=['prune'])
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def purge(self, ctx, *limit):
        '''delete amount of messages (MOD ONLY)
        Example:
        -----------
        d/ purge 100
        '''
        try:
            limit = int(limit[0])
        except IndexError:
            limit = 1
        deleted = 0
        while limit >= 1:
            cap = min(limit, 100)
            deleted += len(await ctx.channel.purge(limit=cap, before=ctx.message))
            limit -= cap
        tmp = await ctx.send(f'**:white_check_mark:** {deleted} Messages deleted')
        await asyncio.sleep(5)
        await tmp.delete()
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *reason):
        '''Kick a member with a reason (MOD ONLY)
        example:
        -----------
        !dl kick @bob#1234
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await member.kick(reason=reason)
        else:
            await ctx.send('**:no_entry:** No user specified!')

def setup(bot):
    bot.add_cog(mod(bot))
