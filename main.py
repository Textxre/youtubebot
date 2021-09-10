import discord
import typing
from discord.ext import commands


prefix = "!"
client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
  print("I'm Alive")


@client.command()
async def ban(ctx, user: discord.Member=None, *, reason=None):
  if user == None:
    await ctx.send("Please mention a user!")
    return
  if reason == None:
    reason = "No reason provided."
    await ctx.guild.ban(user, reason=reason)
    await ctx.send(f"Succesfully banned {user}.\n**Reason:** {reason}")


@client.command()
async def unban(ctx, id: typing.Union[int, None]):
  if id == None:
    await ctx.send("Please provide a user ID!")
    return
  if id is not None:
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f"Unbanned {user} from this guild!")
  else:
    await ctx.send("This user is not banned from this guild!")


client.run(token)
