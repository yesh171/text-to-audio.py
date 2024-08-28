from gtts import gTTS  # Corrected import statement
from playsound import playsound

# Text you want to convert to speech
text = "Hello, i am mali yeshwanth reddy."

# Create the gTTS object
tts = gTTS(text=text, lang='en')

# Save the audio file
audio = "speed.mp3"
tts.save(audio)

# Play the audio file
playsound(audio)