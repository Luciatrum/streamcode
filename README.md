This repository is a catalogue of all the code we've used on streams in the past.

This explanation is assuming you've had some past experience with using Python and/or IDEs in the past and will not go into details on how to install the necessary libraries. (Don't get discouraged, it's really easy to do)

# Azurebot
Azurebot is a TTS tool using Azure Cognitive voices to read out incoming twitch messages and allow users to define emotions to their messages. The voices in the code are what were available at the time of usage so the list of voices may need to be updated in the future.
The voices in the code all come with the listed Voice Styles (emotions). Make sure you check the Azure Speech Studio when adding voices to ensure a voice style is supported.

IMPORTANT - You will need the voices.py file along with the azurebot to work, without it the code will fail. Make sure they are in the same directory.

  ## Pre-requisites
    - Create a Virtual Environment in your IDE of choice (Optional)
    - Have a Twitch Account
      - Obtain your Oauth token
      - Create an Environmental Variable called TWITCH_TOKEN
    - Create a Microsoft Azure account
      - Create a Cognitive Service resource in Azure
      - Create a Speech Service
      - Obtain the Speech Key and Speech Region
      - Create an Environmental Variable for SPEECH_KEY and SPEECH_REGION

  When you run the command, it should take a few seconds to connect to your Twitch account. From here, you can type directly into your chat to test if it works. To turn it off, just kill the script.

# genericTTS
If Azurebot is too complicated, we also built a very basic bot that reads out all text in your standard robotic TTS voice.

  ## Pre-requisites
    - Have a Twitch Account
      - Obtain your Oauth token
      - Create an Environmental Variable called TWITCH_TOKEN
    - Define the Device that will be outputting the Audio. (Ex. VIRTUAL_AUDIO_CABLE)

  Similar to before, you can just run it, and test it using chat.
