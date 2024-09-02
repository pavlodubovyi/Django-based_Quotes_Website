from django.shortcuts import render
from django.core.paginator import Paginator
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    paginator = Paginator(list(quotes), 10)
    quotes_on_page = paginator.get_page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})
