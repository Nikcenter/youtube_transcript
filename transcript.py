import sys
from youtube_transcript_api import YouTubeTranscriptApi

def transcribe(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang, 'en'])
    for entry in transcript:
        #print(f"{entry['start']} - {entry['duration']}: {entry['text']}")
        print(f"{entry['text']}")


if len(sys.argv) != 3:
    print("Usage: python transcribe.py <video_id> <language>")
else:
    video_id = sys.argv[1]
    lang = sys.argv[2]
    transcribe(video_id)
