from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField()
    tags = models.ManyToManyField("Tag", related_name="quotes")
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, default=None, null=True, related_name="quotes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote
