from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# from .managers import PublishedManager


# class IpModel(models.Model):
#     ip = models.CharField(max_length=100)

#     def __str__(self):
#         return self.ip


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(verbose_name="Kategoriya", max_length=150)

    def __str__(self):
        return self.name


class News(models.Model):

    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(verbose_name="Sarlavha", max_length=250)
    slug = models.SlugField(max_length=250)
    # slug = AutoSlugField(populate_from=title, unique=True, null=True, default=None)
    body = models.TextField(verbose_name='Yangilik matni')
    image = models.ImageField(verbose_name="Rasm", upload_to="news/images")
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_time = models.DateTimeField(verbose_name="Yuklagan vaqti", default=timezone.now)
    created_time = models.DateTimeField(verbose_name="Yaratilgan vaqti", auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name="Tahrirlangan vaqti", auto_now=True)
    status = models.CharField(verbose_name="Holati", max_length=2, choices=Status.choices,
                              default=Status.Draft
                              )
    # views = models.ManyToManyField(IpModel, related_name='news_views', blank=True)
    objects = models.Manager()
    published = PublishedManager()
    # comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-published_time"]

    def __str__(self):
        return self.title

    # def total_views(self):
    #     return self.views.count()

    def get_absolute_url(self):
        return reverse("news_detail", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(verbose_name='Ism', max_length=100)
    email = models.EmailField(verbose_name="Email", max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


# class Youtobe(models.Model):
#     chanel_name = models.CharField(verbose_name='Kanal nomi', max_length=150)
#     lesson_link = models.CharField(verbose_name='Dars havolasi', max_length=700)
#
#     def __str__(self):
#         return self.chanel_name

