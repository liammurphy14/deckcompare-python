# Deckcompare

Paste two Hearthstone deck codes and see which cards are only in the first deck, only in the
second, or in both. Built between 2018 and 2020 as a Django web app, which ran at deckcompare.com.

Built by [Floris van Rijn](https://github.com/florisvanrijn) and
[Liam Murphy](https://github.com/liammurphy14).

## How it works

A deck code is a base64 string. Decoded, it holds a short header, the hero, and two lists of
card IDs stored as varints: the cards with one copy and the cards with two. The app decodes both
decks, sorts every card by how many copies each deck has, and looks up the names in the
[HearthstoneJSON](https://hearthstonejson.com/) card data.

The [write-up](docs/Deckcompare.com%20writeup.pdf) walks through the decoding byte by byte.

## Running it locally

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install django requests
cd compare && python jsonConvert.py && cd ..   # downloads the card data to ./cardData
DJANGO_DEBUG=1 python manage.py runserver
```

Then open http://127.0.0.1:8000. Without `DJANGO_SECRET_KEY` set, a random secret key is
generated at startup, which is fine for local use. Tested with Django 6.1 on Python 3.13.
