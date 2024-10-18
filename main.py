import discord
import os
import webserver




DISCORD_TOKEN = os.environ('discordkey')
intents = discord.Intents.default()
intents.message_content = True  # NOQA

client = discord.Client(intents=intents)

# Event triggered when a message is sent in the server
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message contains a Twitter link
    if "twitter.com" in message.content or "x.com" in message.content:
        # Modify the message to use fxtwitter.com instead
        modified_message = message.content.replace("twitter.com", "fxtwitter.com").replace("x.com", "fxtwitter.com")

        # Attempt to delete the original message and send a modified one
        try:
            await message.delete()  # Delete the original message
            await message.channel.send(f"{message.author.mention} posted : {modified_message}")
        except discord.Forbidden:
            print("Bot doesn't have permission to delete messages.")
        except discord.HTTPException as e:
            print(f"Failed to edit message: {e}")

# Event triggered when the bot is ready and connected
@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

def main():
    client.run(DISCORD_TOKEN)
    webserver.keep_alive()
if __name__ == "__main__":
    main()

