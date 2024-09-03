from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from .models import Quote, Author
from .forms import AuthorForm, QuoteForm


def main(request, page=1):
    quotes = Quote.objects.all()
    paginator = Paginator(quotes, 10)
    quotes_on_page = paginator.get_page(page)
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page})


def author_detail(request, id):
    try:
        id = int(id)
    except ValueError:
        raise Http404("Author not found")

    author = get_object_or_404(Author, id=id)
    quotes = Quote.objects.filter(author=author)
    return render(
        request,
        "quotes/author_detail.html",
        context={"author": author, "quotes": quotes},
    )


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            quote_text = form.cleaned_data["quote"]
            if quote_text:
                Quote.objects.create(author=author, quote=quote_text)
            return redirect("quotes:root")
    else:
        form = AuthorForm()
    return render(request, "quotes/add_author.html", {"form": form})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("quotes:root")
    else:
        form = QuoteForm()
    return render(request, "quotes/add_quote.html", {"form": form})


def tag_quotes(request, tag_name):
    quotes = Quote.objects.filter(tags__name=tag_name)
    return render(
        request,
        "quotes/tag_quotes.html",
        context={"quotes": quotes, "tag_name": tag_name},
    )
