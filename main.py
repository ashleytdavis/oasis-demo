import random
import webbrowser

meme_list = [
    "https://imgflip.com/s/meme/Drake-Hotline-Bling.jpg",
    "https://imgflip.com/s/meme/Two-Buttons.jpg",
    "https://imgflip.com/s/meme/Distracted-Boyfriend.jpg",
    "https://imgflip.com/s/meme/Buff-Doge-vs-Cheems.png",
    "https://imgflip.com/s/meme/Left-Exit-12-Off-Ramp.jpg",
    "https://imgflip.com/s/meme/Expanding-Brain.jpg",
    "https://imgflip.com/s/meme/Always-Has-Been.png",
    "https://imgflip.com/s/meme/Surprised-Pikachu.jpg"

]

def get_random_meme():
    return random.choice(meme_list)

meme_url = get_random_meme()
webbrowser.open(meme_url)
