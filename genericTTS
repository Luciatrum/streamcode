import pyttsx3
import os
import sounddevice as sd
import soundfile as sf
from twitchio.ext import commands

# Create a TTS engine
engine = pyttsx3.init()

# Create a Twitch Chat Bot instance
class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['TWITCH_TOKEN'], prefix='?', initial_channels=['TWITCH_CHANNEL'])

    # Event handler for incoming chat messages
    async def event_message(self, ctx):
        # Check if the message is from a subscriber
        if ctx.author.is_subscriber:
            # Extract the message content
            message = ctx.content

            # Pass the message to pyttsx3 for speech synthesis
            engine.save_to_file(message, "temp.wav")
            engine.runAndWait()

            # Set the virtual audio cable device as the default output
            devices = sd.query_devices()
            for device in devices:
                if "VIRTUAL_AUDIO_CABLE" in device["name"]:
                    sd.default.device = device["name"]
                    break

            # Read the audio file
            audio_data, sample_rate = sf.read("temp.wav", dtype="float32")

            # Play the synthesized speech through the virtual audio cable
            sd.play(audio_data, sample_rate)

# Create an instance of the Bot class
bot = Bot()

# Run the Twitch Chat Bot
bot.run()
