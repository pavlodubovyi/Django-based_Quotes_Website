"""Цей скрипт переносить дані з MongoDB до PostgreSQL"""

import os
import django
from pymongo import MongoClient

# from django.db import connection

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes_site.settings")
django.setup()

from quotes.models import Author, Quote, Tag

# Подальший блок для того, щоб нумерація завжди починалась з 1
# # Видалити всі записи з таблиць
# Author.objects.all().delete()
# Tag.objects.all().delete()
# Quote.objects.all().delete()
#
# # Скинути послідовності
# with connection.cursor() as cursor:
#     cursor.execute("ALTER SEQUENCE quotes_author_id_seq RESTART WITH 1;")
#     cursor.execute("ALTER SEQUENCE quotes_tag_id_seq RESTART WITH 1;")
#     cursor.execute("ALTER SEQUENCE quotes_quote_id_seq RESTART WITH 1;")

client = MongoClient("mongodb+srv://userweb21:567234@cluster0.vkwfwwg.mongodb.net/")
db = client.get_database("PD_homework_8")

authors = db.authors.find()

for author in authors:
    print(f"Transferring author {author['fullname']}...")
    Author.objects.get_or_create(
        fullname=author["fullname"],
        born_date=author["born_date"],
        born_location=author["born_location"],
        description=author["description"],
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    quote_exists = Quote.objects.filter(quote=quote["quote"]).exists()

    if not quote_exists:
        print(f"Transferring quote {quote['quote']}...")
        author = db.authors.find_one({"_id": quote["author"]})

        a = Author.objects.get(fullname=author["fullname"])
        q = Quote.objects.create(
            quote=quote["quote"],
            author=a,
        )
    for tag in tags:
        q.tags.add(tag)
