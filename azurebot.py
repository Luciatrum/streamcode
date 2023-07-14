import os
import random
from voices import voices
import azure.cognitiveservices.speech as speechsdk
from twitchio.ext import commands

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_key = os.environ.get('SPEECH_KEY')
speech_region = os.environ.get('SPEECH_REGION')
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)


# Default voice style and degree
DEFAULT_VOICE_STYLE = 'Neutral'
DEFAULT_VOICE_DEGREE = '1'

# Available voice styles
VOICE_STYLES = {
    'Neutral': 'Neutral',
    'Angry': 'Angry',
    'Cheerful': 'Cheerful',
    'Sad': 'Sad',
    'Excited': 'Excited',
    'Friendly': 'Friendly',
    'Terrified': 'Terrified',
    'Shouting': 'Shouting',
    'Whispering': 'Whispering',

    # Add more voices if needed
}

# Create the speech synthesis client
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(token=os.environ['TWITCH_TOKEN'], prefix='!', initial_channels=['CHANNEL_NAME'])
        self.assigned_voices = {}  # Store assigned voices for users


    async def event_message(self, message):
        print(f'Incoming message: {message.content}')

        # Ignore messages starting with "Changed voice to:"
        if message.content.startswith('Changed voice to:'):           
            return
        if message.echo or message.author.name.lower() == 'soundalerts':
            return

        text_to_speech(message.content, message.author)  # Pass the message object to text_to_speech method
        await self.handle_commands(message)


    async def event_ready(self):
        print(f'Bot is ready: {self.nick}')

    async def command_hello(self, ctx):
        await ctx.send(f'Hello, {ctx.author.name}!')

    async def command_echo(self, ctx):
        await ctx.send(ctx.content)

    async def command_assign(self, ctx):
        parts = ctx.content.split(' ')
        if len(parts) > 1:
            user = ctx.author.name.lower()
            voice = parts[1]
            if voice == 'Guy':
                self.assigned_voices[user] = 'en-US-GuyNeural'
            elif voice == 'Davis':
                self.assigned_voices[user] = 'en-US-DavisNeural'
            else:
                voice = random.choice(list(voices.keys()))
                self.assigned_voices[user] = voice
            await ctx.send(f'Assigned voice: {self.assigned_voices[user]}')
        else:
            await ctx.send('Invalid command usage. Please provide a voice.')

    async def command_voice(self, ctx):
        voice = ctx.content.split(' ')[1]
        if voice in voices:
            self.assigned_voices[ctx.author.name.lower()] = voice  # Assign the voice to the user
            await ctx.send(f'Changing voice to: {voice}')
        else:
            await ctx.send(f'Invalid voice: {voice}')

    @commands.command(name='voicehelp')
    async def command_voicehelp(self, ctx):
        help_message = """
        Voices:
        Jane,
        Guy,
        Davis |
        
        Emotions:
        Angry,
        Cheerful,
        Sad,
        Excited,
        Friendly,
        Terrified,
        Shouting |

        Example:
        !voice Jane |
        *terrified* We're all going to die!
        
        """
        await ctx.send(help_message)

    @commands.command(name='voice')
    async def command_voice(self, ctx):
        user = ctx.author.name.lower()
        parts = ctx.message.content.split(' ')
        if len(parts) > 1:
            voice = parts[1]
            if voice.lower() == 'jane':
                new_voice = 'en-US-JaneNeural'
            elif voice.lower() == 'guy':
                new_voice = 'en-US-GuyNeural'
            elif voice.lower() == 'davis':
                new_voice = 'en-US-DavisNeural'
            else:
                await ctx.send(f'Invalid voice: {voice}')
                return
        else:
            if user in self.assigned_voices:
                current_voice = self.assigned_voices[user]
                if current_voice == 'en-US-JaneNeural':
                    new_voice = 'en-US-GuyNeural'
                elif current_voice == 'en-US-GuyNeural':
                    new_voice = 'en-US-DavisNeural'
                elif current_voice == 'en-US-DavisNeural':
                    new_voice = 'en-US-JaneNeural'
                else:
                    await ctx.send(f'Invalid assigned voice: {current_voice}')
                    return
            else:
                new_voice = 'en-US-JaneNeural'

        self.assigned_voices[user] = new_voice
        await ctx.send(f'Changed voice to: {new_voice}')


def text_to_speech(text, author):
    if text.startswith('!voice'):
        return  # Skip speech synthesis for the '!voice' command

    if author is None:
        print('Author object is None')
        return

    voice, style, message = parse_message(text, author)  # Pass the author object to parse_message method

    if voice not in voices:
        print(f'Invalid voice: {voice}')
        return

    if style and style not in voices[voice]:
        print(f'Invalid style: {style}')
        return

    if style:
        ssml_content = voices[voice][style].format(message=message)
    else:
        style = 'Default'
        ssml_content = '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="{voice}">
                    {message}
                </voice>
            </speak>
        '''.format(voice=voice, message=message)


    result = synthesizer.speak_ssml_async(ssml_content).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print('Speech synthesized successfully')
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f'Speech synthesis canceled: {cancellation_details.reason}')
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f'Error details: {cancellation_details.error_details}')


def parse_message(text, author):
    parts = text.split(' ', 1)
    if len(parts) > 1:
        command, message = parts
        if command.startswith('*') and command.endswith('*'):
            style = command[1:-1].capitalize()
            voice = get_assigned_voice(author)
            return voice, style, message
    return get_assigned_voice(author), None, text


def get_assigned_voice(author):
    if isinstance(author, str):
        username = author.lower()
    elif author is not None:
        username = author.name.lower()
    else:
        print('Author object is None')
        return 'en-US-JaneNeural'  # Default voice if no voice is assigned

    # Check if the user has an assigned voice
    user_voice = bot.assigned_voices.get(username)
    if user_voice:
        return user_voice
    return 'en-US-JaneNeural'  # Default voice if no voice is assigned

if __name__ == '__main__':
    bot = MyBot()
    bot.run()
