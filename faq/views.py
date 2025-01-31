from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the FAQ API</h1><p>Use <code>/api/faqs/</code> to fetch FAQs.</p>")

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    data = [
        {
            "question": faq.get_translation(lang),
            "answer": faq.answer
        } for faq in faqs
    ]
    return Response(data)
