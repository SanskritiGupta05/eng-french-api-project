from django.db import models

class Translation(models.Model):
    text_to_translate = models.TextField()
    source_lang = models.CharField(max_length=10)
    target_lang = models.CharField(max_length=10)
    translated_text = models.TextField()
