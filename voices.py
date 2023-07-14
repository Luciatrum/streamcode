# Define the available voices and their corresponding SSML templates
voices = {
    'en-US-JaneNeural': {
        'Angry': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="angry" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Cheerful': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="cheerful" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Sad': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="sad" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Excited': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="excited" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Friendly': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="friendly" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Terrified': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="terrified" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Shouting': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="shouting" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Whispering': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="whispering" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Unfriendly': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="unfriendly" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Hopeful': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-JaneNeural">
                    <mstts:express-as style="hopeful" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
    },
    'en-US-DavisNeural': {
        'Angry': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="angry" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Cheerful': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="cheerful" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Sad': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="sad" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Excited': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="excited" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Friendly': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="friendly" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Terrified': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="terrified" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Shouting': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="shouting" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Whispering': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="whispering" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Unfriendly': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="unfriendly" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Hopeful': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-DavisNeural">
                    <mstts:express-as style="hopeful" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
    },
    'en-US-GuyNeural': {
        'Angry': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="angry" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Cheerful': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="cheerful" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Sad': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="sad" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Excited': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="excited" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Friendly': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="friendly" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Terrified': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="terrified" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Shouting': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="shouting" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Whispering': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="whispering" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Unfriendly': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="unfriendly" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
        'Hopeful': '''
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
                   xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
                <voice name="en-US-GuyNeural">
                    <mstts:express-as style="hopeful" styledegree="2">
                        {message}
                    </mstts:express-as>
                </voice>
            </speak>
        ''',
    }
}
