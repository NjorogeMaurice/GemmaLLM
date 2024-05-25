from django.shortcuts import render
from rest_framework.response import Response
from django.http import BadHeaderError, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from .gemini import generateResponse
import json

@api_view(['POST'])
def index(request):
    # text = request.POST['text']
    data = json.loads(request.body)
    text = data.get('text')
    result,chat_history = generateResponse(text)
    response_data = {
        'text': result.text
    }
    print(chat_history)
    return Response(response_data)
