from django import forms

class CodeForm(forms.Form):
    print("lm4")
    deckCode1 = forms.CharField(label='Deck 1', max_length=300)
    deckCode2 = forms.CharField(label='Deck 2', max_length=300)
