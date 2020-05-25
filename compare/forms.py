from django import forms

class CodeForm(forms.Form):
    deckCode1 = forms.CharField(
                        label='',
                        max_length=300,
                        initial="AAECAZ8FBr2GA6CAA5GAA/H+AoT8AvQFDLSbA76YA/mTA+yGA+H+Avz8ArT2 AvYHzwaTBNwDjAEA",
                        widget=forms.TextInput(
                                attrs={
                                    "class": "col"
                                }
                            )
                        )
    deckCode2 = forms.CharField(
                        label='',
                        max_length=300,
                        initial="AAECAZ8FCtqdA4qaA/mTA72GA6CAA5GAA/H+AsD9AoT8AvQFCrSbA+yGA+H+ Avz8ArT2AvYHzwaTBNwDjAEA",
                        widget=forms.TextInput(
                                attrs={
                                    "class": "col"
                                }
                            )
                        )
