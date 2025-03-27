import asyncio
import discord
from discord.ext import commands
from discord import app_commands

import os

DEV_GUILD = discord.Object(id=int(os.getenv("DEV_GUILD_ID"))) 

users_map = {}
LIMIT = 7
DIFF = 5

class SpamModeration(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    ## EVENTS ---------------------------------------------------------------------------------------------
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        user_id = message.author.id
        current_time = message.created_at.timestamp()

        if user_id in users_map:
            user_data = users_map[user_id]
            last_message_time = user_data["last_message_time"]
            msg_count = user_data["msg_count"]

            difference = current_time - last_message_time
            print(difference)
        
            if difference > DIFF:
                user_data["msg_count"] = 1
                user_data["last_message_time"] = current_time
                users_map[user_id] = user_data

                async def remove_user():
                    await asyncio.sleep(DIFF)
                    users_map.pop(user_id, None)
                    print("Removed from map.")
            
                asyncio.create_task(remove_user())
            else:
                msg_count += 1
                if msg_count >= LIMIT:
                    await message.channel.send("Warning: Spamming in this channel is forbidden.")
                    deleted = await message.channel.purge(limit=LIMIT)
                    print(f"Deleted {len(deleted)} messages.")
                else:
                    user_data["msg_count"] = msg_count
                    users_map[user_id] = user_data
        else:
            users_map[user_id] = {
                "msg_count": 1,
                "last_message_time": current_time
            }
        
            async def remove_user():
                await asyncio.sleep(DIFF)
                users_map.pop(user_id, None)
                print("Removed from map.")
        
            asyncio.create_task(remove_user())
    
    ## SLASH COMMANDS ---------------------------------------------------------------------------------------------
    

# Add the cog
async def setup(bot):
    await bot.add_cog(SpamModeration(bot))