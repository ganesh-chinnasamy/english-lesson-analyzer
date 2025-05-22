import whisper

def transcribe_audio(audio_path):
    print("Transcribing audio with Whisper...")
    model = whisper.load_model("large")  # or "small", "medium", "large"
    result = model.transcribe(audio_path)
    return result["text"]



