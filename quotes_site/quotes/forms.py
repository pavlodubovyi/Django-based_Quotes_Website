from django import forms
from .models import Author, Quote


class AuthorForm(forms.ModelForm):
    quote = forms.CharField(
        label="Quote (optional)",
        required=False,
        widget=forms.Textarea(attrs={"rows": 4, "cols": 40}),
    )

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description", "quote"]


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["quote", "tags", "author"]
