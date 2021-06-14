import discord
from discord.ext import commands, tasks
import random
from discord.ext.commands import cooldown, BucketType
import asyncio
import DiscordUtils

embed_author_url = "https://cdn.discordapp.com/attachments/802962665772285985/813039519473467402/cave.png"

embedcolor = 0x800080 #purple

id_1 = 853261137835327519

id_2 = 853261139462848522

id_3 = 853261141316730890

id_4 = 853261142952771625

id_5 = 853261144973770762

id_6 = 853261159791591445

list = [id_1, id_2, id_3, id_4, id_5, id_6]


class Ticket(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ticket ready")
        
#await channel.set_permissions(ctx.guild.default_role, read_messages = False, send_messages = False)
        
        
        


    @commands.command()
    @commands.has_role(767001286360825866)
    #@cooldown(1, 60, BucketType.user)
    async def ticket(self, ctx):
        helper = ctx.guild.get_role(820318090574168104)
        category = self.client.get_channel(807317077521334303).category
        
        embed_1 = discord.Embed(title = "Life RP", description = "To create a ticket react with 📩", color = embedcolor)
        t1 = await ctx.send(embed = embed_1)
        await t1.add_reaction("📩")
        t1_id = t1.id
        
        embed_2 = discord.Embed(title = "Semi-Vanilla", description = "To create a ticket react with 📩", color = embedcolor)
        t2 = await ctx.send(embed = embed_2)
        await t2.add_reaction("📩")
        t2_id = t2.id
        
        embed_3 = discord.Embed(title = "Staff Report", description = "To create a ticket react with 📩", color = embedcolor)
        t3 = await ctx.send(embed = embed_3)
        await t3.add_reaction("📩")
        t3_id = t3.id
        
        embed_4 = discord.Embed(title = "Donator Inquiries", description = "To create a ticket react with 📩", color = embedcolor)
        t4 = await ctx.send(embed = embed_4)
        await t4.add_reaction("📩")
        t4_id = t4.id
        
        embed_5 = discord.Embed(title = "Report", description = "To create a ticket react with 📩", color = embedcolor)
        t5 = await ctx.send(embed = embed_5)
        await t5.add_reaction("📩")
        t5_id = t5.id
       
        embed_6 = discord.Embed(title = "Other", description = "To create a ticket react with 📩", color = embedcolor)
        t6 = await ctx.send(embed = embed_6)
        await t6.add_reaction("📩")
        t6_id = t6.id
        
        
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.id == self.client.user.id:
            return
        else:
            if payload.message_id in list:
                if payload.message_id == id_1:
                    choice = "Life RP"
                if payload.message_id == id_2:
                    choice = "Semi-Vanilla"
                if payload.message_id == id_3:
                    choice = "Staff Report"
                if payload.message_id == id_4:
                    choice = "Donator Inquiries"
                if payload.message_id == id_5:
                    choice = "Report"
                if payload.message_id == id_6:
                    choice = "Other"
                 
            else:
                return
                
            find_guild = discord.utils.find(lambda guild: guild.id == payload.guild_id, self.client.guilds)
            
            helper = discord.utils.get(find_guild.roles, name='Ticket Support')
            
            category = discord.utils.get(find_guild.categories, id=737451094556541028)
            
            channel = await category.create_text_channel(f"Ticket-{payload.member}")
            
            await channel.set_permissions(find_guild.default_role, read_messages = False, send_messages = False)
            await channel.set_permissions(payload.member, send_messages=True, view_channel=True)
            await channel.set_permissions(helper, send_messages=True, view_channel=True)
            await channel.send(f"Welcome {payload.member.mention}")
            
            embed = discord.Embed(title = "", description=f"{choice} \n\nPlease enter the reason of this ticket, support will be here shortly.", color = embedcolor)
            embed.set_author(name=f"Ticket", icon_url = payload.member.avatar_url)
            
            re = await channel.send(embed = embed)
            
            await re.add_reaction("🔒")
            
            re_id = re.id
            
            def check(reaction, user):
                return user != self.client.user and str(reaction.emoji) == "🔒"
            
            okay = True
            while okay == True:
                reaction, user = await self.client.wait_for('reaction_add', check=check)
                
            
                if reaction.emoji == "🔒":
                    if reaction.message.id != re_id:
                        return
                    else:
                        pass
                    msg = reaction.message
                    channel_true = msg.channel
                    
                    sec = 5
                    em2 = discord.Embed(title = "Closing ticket", description=f"Closing ticket in {sec} seconds!", color = embedcolor)
                    ed = await channel.send(embed = em2)
                    await asyncio.sleep(1)
                    sec = 4
                    em3 = discord.Embed(title = "Closing ticket", description=f"Closing ticket in {sec} seconds!", color = embedcolor)
                    await ed.edit(embed = em3)
                    await asyncio.sleep(1)
                    sec = 3
                    em4 = discord.Embed(title = "Closing ticket", description=f"Closing ticket in {sec} seconds!", color = embedcolor)
                    await ed.edit(embed = em4)
                    await asyncio.sleep(1)
                    sec = 2
                    em5 = discord.Embed(title = "Closing ticket", description=f"Closing ticket in {sec} seconds!", color = embedcolor)
                    await ed.edit(embed = em5)
                    await asyncio.sleep(1)
                    sec = 1
                    em6 = discord.Embed(title = "Closing ticket", description=f"Closing ticket in {sec} seconds!", color = embedcolor)
                    await ed.edit(embed = em6)
                    await asyncio.sleep(1)
                    sec = 0
                    em6 = discord.Embed(title = "Closing ticket", description=f"Closing ticket in {sec} seconds!", color = embedcolor)
                    await ed.edit(embed = em6)
                    await asyncio.sleep(0.5)
                    await channel_true.delete()
                    test = False
                    
                    
                else:
                    test = True
                    
            
            
            
            
            
            


            
            
            
         
            
def setup(client):
    client.add_cog(Ticket(client))






#discord.errors.Forbidden: 403 Forbidden (error code: 60003): Two factor is required for this operation
#Ignoring exception in on_raw_reaction_add
#Traceback (most recent call last):
  #File "/home/container/discord/client.py", line 343, in _run_event
    #await coro(*args, **kwargs)
  #File "/home/container/cogs/ticket.py", line 165, in on_raw_reaction_add
    #await channel_true.delete()
  #File "/home/container/discord/abc.py", line 574, in delete
    #await self._state.http.delete_channel(self.id, reason=reason)
  #File "/home/container/discord/http.py", line 248, in request
    #raise Forbidden(r, data)
