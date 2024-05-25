import os
from decouple import config
import google.generativeai as genai

def generateResponse(text):

    genai.configure(api_key='')
    
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash"
    )

    chat_session = model.start_chat()
    response = chat_session.send_message(text)
    return response,chat_session.history

