import os
import sounddevice as sd
import soundfile as sf
import pyttsx3
import asyncio
from twitchio.ext import commands

def generate_tts(text):
    engine = pyttsx3.init()
    engine.save_to_file(text, 'temp.wav')
    engine.runAndWait()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['TMI_TOKEN'], prefix='?', initial_channels=['luciatrum'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, ctx):
        if ctx.echo or ctx.author.name.lower() in ['soundalerts', 'nightbot', 'streamelements']:
            return

        # Ignore any message that starts with '!'
        if ctx.content.startswith('!'):
            return

        # Check if the message sender is a subscriber
        if ctx.author.is_subscriber:
            # Read out the incoming message
            await self.read_message(ctx)

    async def read_message(self, ctx):
        # Generate the TTS audio using your preferred TTS library
        generate_tts(ctx.content)

        # Save the audio to a temporary WAV file
        wav_file_path = 'temp.wav'
        audio_data, sample_rate = sf.read(wav_file_path, dtype="float32")

        # Set the virtual audio cable input device as the default input
        input_device = 'CABLE Input (VB-Audio Virtual Cable)'
        devices = sd.query_devices()
        input_device_index = None
        for i, device in enumerate(devices):
            if device['name'] == input_device:
                input_device_index = i
                break
        if input_device_index is None:
            print(f"Input device '{input_device}' not found.")
            return

        # Play the synthesized speech through the specified input device
        sd.play(audio_data, sample_rate, device=input_device_index)

        # Wait until playback is finished
        sd.wait()

        # Remove the temporary WAV file
        os.remove(wav_file_path)

bot = Bot()
bot.run()
