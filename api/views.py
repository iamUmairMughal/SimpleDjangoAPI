from django.http import JsonResponse
from rest_framework.decorators import api_view
from .tesseract import img_to_text

@api_view(['POST'])
def post(image):
    text = img_to_text(image)
    return JsonResponse(text, safe=False)