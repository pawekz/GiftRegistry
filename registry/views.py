from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from registry.models import Gift

app_name = 'registry'
# Create your views here.

def index(request):
    gift_list = Gift.objects.all()
    return render(request, 'registry/index.html', {'gift_list': gift_list})
def detail(request, gift_id):
    gift = Gift.objects.get(pk=gift_id)
    return render(request, 'registry/details.html', {'gift': gift})

@require_POST
def purchase(request, gift_id):
    gift = Gift.objects.get(pk=gift_id)
    gift.purchased = True
    gift.save()
    return redirect('registry:index')



