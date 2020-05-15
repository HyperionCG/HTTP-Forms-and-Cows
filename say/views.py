from django.shortcuts import render

from say.models import Input
from say.forms import InputForm

import subprocess
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Input.objects.create(text=data['text'])
            DaCow = subprocess.run(['cowsay'] + data['text'].split(),
            capture_output=True).stdout.decode()

        return render (request, 'index.html', {'DaCow': DaCow, 'form': form})

    form = InputForm()
    return render(request, 'index.html', {'form': form})

def historyview(request):
    data = list(Input.objects.all())
    last_ten = data[-10:]

    return render (request, 'history.html', {'last_ten': last_ten})