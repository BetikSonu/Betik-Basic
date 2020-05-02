from gtts import gTTS
ses = gTTS(text="Merhabalar",lang="tr")
ses.save("ben_sesim.mp3")
