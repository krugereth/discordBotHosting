import discord
import webserver
import os

DISCORD_TOKEN = os.environ['discordkey']
intents = discord.Intents.default()
intents.message_content = True  # NOQA

client = discord.Client(intents=intents)


KAWHI_IMAGE_URL = "https://raw.githubusercontent.com/krugereth/discordHostingBot/master/kawhiolympics.jpg"
MIKE_TOMLIN_IMAGE_URL = "https://raw.githubusercontent.com/krugereth/discordHostingBot/master/miketomlin.jpg"
WESTBROOK_IMAGE_URL = "https://raw.githubusercontent.com/krugereth/discordHostingBot/master/westbrook.jpg"


@client.event
async def on_message(message):
    # Ignores messages from the bot itself
    if message.author == client.user:
        return

    if "dmoi hodge" in message.content.lower():
        await message.channel.send("that's me, the toughest hooper in LA! From the tent to the pent!")

    if "kawhi" in message.content.lower():
        await message.channel.send(file=discord.File(fp=KAWHI_IMAGE_URL))

    if "kai jones" in message.content.lower():
        await message.channel.send("Yuh Yuh Yuh Yuh Yuh I got infinity money Yuh Yuh Yuh Yuh Yuh I got infinity money Yuh Yuh Yuh Yuh Yuh I got infinity money")

    keywords = {"mike", "tomlin", "steelers"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(fp=MIKE_TOMLIN_IMAGE_URL))

    keywords = {"westbrook", "midrange"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(fp=WESTBROOK_IMAGE_URL))

    if "hawad midrange" in message.content.lower():
        await message.channel.send(file=discord.File(fp=WESTBROOK_IMAGE_URL))

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
