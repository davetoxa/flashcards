from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Card

def index(request):
    latest_card_list = Card.objects.order_by('-id')[:5]

    context = {'latest_card_list': latest_card_list}
    return render(request, 'cards/index.html', context)

def detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/detail.html', {'card': card})

# def check(request, card_id):
#     response = "You're checking the card %s."
#     return HttpResponse(response % card_id)
