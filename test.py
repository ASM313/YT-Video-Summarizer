from utility import *

transcript = ''

transcript = transcript_text("https://www.youtube.com/watch?v=kU0wCDiqfew")
# print(transcript)

print(generate_gemini_content(transcript, prompt))