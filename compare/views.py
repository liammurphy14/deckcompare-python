from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .newCompare import compare
from .forms import CodeForm
# Create your views here.

def index(request):
    template = loader.get_template('compare/index.html')

    code1 = 'AAECAf0ECoqeA5aaA4OWA6+HA6iHA6aHA6CAA8XzAooHigEKwpkD05gD55UD zYkDw/gC7AfhB6sEyQNNAA=='
    code2 = 'AAECAf0ECIqeA6CbA5aaA62HA6iHA6CAA77sAqsEC9OYA4OWA82JA5n/AsP4 AsXzAuwHywTJA4oBTQA='

    results = compare(code1,code2)

    context = {
    'one':results[0],
    'both':results[1],
    'two':results[2],
    }

    return render(request, 'compare/index.html', context)

'''def index2(request):
    print("lm5")
    if request.method == 'POST':

    else:
        template = loader.get_template('compare/index.html')

        code1 = 'AAECAf0ECoqeA5aaA4OWA6+HA6iHA6aHA6CAA8XzAooHigEKwpkD05gD55UD zYkDw/gC7AfhB6sEyQNNAA=='
        code2 = 'AAECAf0ECIqeA6CbA5aaA62HA6iHA6CAA77sAqsEC9OYA4OWA82JA5n/AsP4 AsXzAuwHywTJA4oBTQA='

        results = compare(code1,code2)

        context = {
        'one':results[0],
        'both':results[1],
        'two':results[2],
    }

    return render(request, 'compare/index.html', context)'''

def codeInput(request):
    if request.method == 'POST':
        print("lm2")
        form = CodeForm(request.POST)
        if form.is_valid():
            code1 = form.cleaned_data['deckCode1']
            code2 = form.cleaned_data['deckCode2']
            results = compare(code1,code2)
            print("lm3")
            context = {
            'one':results[0],
            'both':results[1],
            'two':results[2],
            }

            return render(request, 'compare/index.html', context)
    else:
        print("lm1")
        form = CodeForm()
    return render(request, 'compare/formtest.html', {'form': form})

def testPage(request):

    return render(request, 'compare/testpage.html')
