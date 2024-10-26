import discord
import webserver
import os

DISCORD_TOKEN = os.environ['discordkey']
intents = discord.Intents.default()
intents.message_content = True  # NOQA

client = discord.Client(intents=intents)


KAWHI_IMAGE_PATH = "Kawhiolympics.jpg"
MIKE_TOMLIN_IMAGE_PATH = "miketomlin.jpg"
WESTBROOK_IMAGE_PATH = "westbrook.jpg"
NETS_KG_VIDEO_PATH = "netskg.mp4"


@client.event
async def on_message(message):
    # Ignores messages from the bot itself
    if message.author == client.user:
        return

    if "dmoi hodge" in message.content.lower():
        await message.channel.send("that's me, the toughest hooper in LA! From the tent to the pent!")

    if "kawhi" in message.content.lower():
        await message.channel.send(file=discord.File(KAWHI_IMAGE_PATH))

    if "kai jones" in message.content.lower():
        await message.channel.send("Yuh Yuh Yuh Yuh Yuh I got infinity money Yuh Yuh Yuh Yuh Yuh I got infinity money Yuh Yuh Yuh Yuh Yuh I got infinity money")

    keywords = {"mike", "tomlin", "steelers"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(MIKE_TOMLIN_IMAGE_PATH))

    keywords = {"westbrook", "midrange"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(WESTBROOK_IMAGE_PATH))
        
    keywords = {"nets", "kg"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(NETS_KG_VIDEO_PATH))

    if "hawad midrange" in message.content.lower():
        await message.channel.send(file=discord.File(WESTBROOK_IMAGE_PATH))

    # Check if the message contains a Twitter link
    if "twitter.com" in message.content or "x.com" in message.content:
        # Modify the message to use fxtwitter.com instead
        modified_message = message.content.replace("twitter.com", "fxtwitter.com").replace("x.com", "fxtwitter.com")

        # Delete the original message and send the modified version
        try:
            await message.delete()  # Delete the original message
            await message.channel.send(f"{message.author.mention} posted: {modified_message}")
        except discord.Forbidden:
            print("No permission to delete")
        except discord.HTTPException as e:
            print(f"Failed to edit message: {e}")


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

def main():
    webserver.keep_alive()
    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
