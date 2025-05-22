from scripts.transcription import transcribe_audio

audio_path = "data/sample_audio.wav"
transcription = transcribe_audio(audio_path)

print("\n--- Transcription ---\n")
print(transcription)


