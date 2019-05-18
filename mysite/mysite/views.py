from django.shortcuts import reverse
from django.shortcuts import redirect

def index(request):
    return redirect(reverse('booket:index'))
