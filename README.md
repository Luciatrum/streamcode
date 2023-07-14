This repository is a catalogue of all the code we've used on streams in the past.

This explanation is assuming you've had some past experience with using Python and/or IDEs in the past and will not go into details on how to install the necessary libraries. (Don't get discouraged, it's really easy to do)

# Azurebot {Deprecated}
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

# mp3download
This is what was used to obtain the pure mp3 files we used for our background music. Effectively, this allows you to bulk download any YouTube playlist and save the audio on your local machine!

  ## Pre-requisites
    - Update the directory
That's it, just paste the URL of a playlist or video, and it'll download.


# FAQ
1. What IDE should I use?
      - It's up to your preference. I personally use Visual Studio Code to run the code, but any IDE will do.

2. The code doesn't work after following all the instructions! What do I do now?
      - Over time, some of these libraries will update, which may cause things to go wrong. You can either report a bug here or in our discord server and I'll look into it if possible.
  
3. Why does some of the code say Deprecated? What does that mean?
      - Deprecated code signifies code is no longer in use and is not actively supported. Any script with this tag will not be fixed in the case of any new bugs or defects.
  
4. Why even keep deprecated code up?
      - Valid question. That's because this code may still work, and even if it doesn't it can still give insight on other functionality. In the future, we may move all Deprecated code to its own repository, but until then, just be conscious whenever using deprecated code.
  
5. Why do I need to setup environmental variables? Can't I just add the tokens directly into the code?
      - You can, of course, put the tokens into the code directly. However, this is very unsecure and is not recommended as these tokens can be used by anyone who has access.

6. When can I expect INSERT_NEW_CODE to be added here?
      - Whenever I build new code, it's put through the wringer a few times to sift out all the bugs and clean things up. So there's no set timeframe for when code will be released here at this time The answer is "When I think it's ready"



 
