
# translation_app/views.py
from django.shortcuts import render
from .models import Translation
import requests

def index(request):
    return render(request, 'index.html')

def translate(request):
    if request.method == 'POST':
        text_to_translate = request.POST['text_to_translate']
        source_lang = request.POST['source_lang']
        target_lang = request.POST['target_lang']

        api_url = "https://655.mtis.workers.dev/translate"
        params = {
            'text': text_to_translate,
            'source_lang': source_lang,
            'target_lang': target_lang
        }

        response = requests.get(api_url, params=params)
        data = response.json()

        translated_text = data['response']['translated_text']

        Translation.objects.create(
            text_to_translate=text_to_translate,
            source_lang=source_lang,
            target_lang=target_lang,
            translated_text=translated_text
        )

        return render(request, 'index.html', {
            'text_to_translate': text_to_translate,
            'translated_text': translated_text
        })

