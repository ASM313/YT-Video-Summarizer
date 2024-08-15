import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """Act as youtube video summarizer, Video transcript text will provide to you. So your task is to summarize entire video and return the detailed summary in 5000 words and give response in HTML code. The transcript text will be appended here: 
"""

## Extract transcript

def transcript_text(url):
    
    try:
        video_id = url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript=''
        
        for i in transcript_text:
            transcript += ' '+i["text"]
            
        return transcript     
        
    except Exception as e:
        raise e

## Communicate with Gemini
def generate_gemini_content(transcript, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript)
    
    return response.text


