import discord
import webserver
import os

DISCORD_TOKEN = os.environ['discordkey']
intents = discord.Intents.default()
intents.message_content = True  # NOQA

client = discord.Client(intents=intents)


@client.event
async def on_message(message):
    # Ignores messages from the bot itself
    if message.author == client.user:
        return

    if "dmoi hodge" in message.content.lower():
        await message.channel.send("that's me, the toughest hooper in LA ! From the tent to the pent !")

    if "kawhi" in message.content.lower():

        await message.channel.send(file=discord.File(r"C:\Users\Ayush\Desktop\kawhiolympics.jpg"))

    if "kai jones" in message.content.lower():
        await message.channel.send("Yuh Yuh Yuh Yuh Yuh I got infinity money Yuh Yuh Yuh Yuh Yuh I got infinity money Yuh Yuh Yuh Yuh Yuh I got infinity money")

    keywords = {"mike", "tomlin", "steelers"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(r"C:\Users\Ayush\Desktop\miketomlin.jpg"))

    keywords = {"westbrook", "midrange"}
    if all(keyword in message.content.lower() for keyword in keywords):
        await message.channel.send(file=discord.File(r"C:\Users\Ayush\Desktop\westbrook.jpg"))

    if "hawad midrange" in message.content.lower():
        await message.channel.send(file=discord.File(r"C:\Users\Ayush\Desktop\westbrook.jpg"))


    # Check if the message contains a twitter link
    if "twitter.com" in message.content or "x.com" in message.content:
        # Modify the message to use fxtwitter.com instead
        modified_message = message.content.replace("twitter.com", "fxtwitter.com").replace("x.com", "fxtwitter.com")

        # delete og message and send modified version
        try:
            await message.delete()  # Delete the original message
            await message.channel.send(f"{message.author.mention} posted : {modified_message}")
        except discord.Forbidden:
            print("No perm to delete")
        except discord.HTTPException as e:
            print(f"failed to edit message: {e}")


@client.event
async def on_ready():
    print(f'Logged in as {client.user}!')

def main():
    webserver.keep_alive()
    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()

