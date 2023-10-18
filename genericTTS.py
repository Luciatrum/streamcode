import os
import sounddevice as sd
import soundfile as sf
import pyttsx3
from twitchio.ext import commands

# List of terms to filter out
filter_terms = ['luciat2', 'agentj26', 'emote2', 'emote3']

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
        if ctx.echo or ctx.author.name.lower() in ['soundalerts', 'nightbot', 'streamelements','luciatrum']:
            return

        # Ignore any message that starts with '!'
        if ctx.content.startswith('!'):
            return

        # Check if the message sender is a subscriber
        if ctx.author.is_subscriber:
            # Filter out specified terms from the message content
            filtered_content = ' '.join(word for word in ctx.content.split() if not any(term in word for term in filter_terms))

            if filtered_content.strip():  # Check if there's content left after filtering
                await self.read_message(filtered_content)

    async def read_message(self, content):
        # Generate the TTS audio using your preferred TTS library
        generate_tts(content)

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
