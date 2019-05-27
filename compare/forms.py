from django import forms

class CodeForm(forms.Form):
    deckCode1 = forms.CharField(label='Deck 1', max_length=300, initial="AAECAZ8FBr2GA6CAA5GAA/H+AoT8AvQFDLSbA76YA/mTA+yGA+H+Avz8ArT2 AvYHzwaTBNwDjAEA")
    deckCode2 = forms.CharField(label='Deck 2', max_length=300, initial="AAECAZ8FCtqdA4qaA/mTA72GA6CAA5GAA/H+AsD9AoT8AvQFCrSbA+yGA+H+ Avz8ArT2AvYHzwaTBNwDjAEA")
