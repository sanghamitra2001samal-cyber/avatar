import asyncio
import edge_tts
import os

async def test_tts():
    text = "Hello, this is a test of the neural voice engine."
    voice = "en-US-GuyNeural"
    output_file = "test_audio.mp3"
    
    print(f"Generating audio for: '{text}'")
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        print(f"Success! Audio saved to {output_file}")
        
        # Verify file size
        if os.path.exists(output_file):
            size = os.path.getsize(output_file)
            print(f"File size: {size} bytes")
        else:
            print("Error: File was not created.")
            
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(test_tts())
