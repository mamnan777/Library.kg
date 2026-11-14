from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=150, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    published_year = models.PositiveIntegerField(verbose_name="Год издания")
    pages = models.PositiveIntegerField(verbose_name="Количество страниц")
    language = models.CharField(max_length=50, default="Русский", verbose_name="Язык")
    cover_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на обложку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    views_count = models.PositiveIntegerField(default=0)
    
    def str(self):
        return f"{self.title} — {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


