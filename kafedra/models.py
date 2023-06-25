from django.urls import reverse
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(status=KafedraTeacher.Status.Published)


class KafedraCategory(models.Model):
    name = models.CharField(verbose_name='Kafedra', max_length=200)

    def __str__(self):
        return self.name


class KafedraTeacher(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, related_name="kafedra")
    fish = models.CharField(verbose_name="O'qituvchi (FISH)", max_length=150)
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    birthday = models.DateField(verbose_name='Tugilgan sana')
    graduated_education = models.CharField(verbose_name="Ta'lim olgan oliy talim", max_length=200)
    deegre = models.CharField(verbose_name="Daraja", max_length=100)
    direction = models.CharField(max_length=250, verbose_name='Mutaxasisligi', null=True, blank=True)
    description = models.TextField(verbose_name='Ustoz haqida...', null=True, blank=True)
    teacher_images = models.ImageField(verbose_name="O'qituvchi rasmi", upload_to="teacher_images/")
    created_time = models.DateTimeField(verbose_name="Yaratilgan vaqti", auto_now_add=True)
    published_time = models.DateTimeField(verbose_name="Yuklagan vaqti", default=timezone.now)
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
        return self.fish

    # def total_views(self):
    #     return self.views.count()

    def get_absolute_url(self):
        return reverse("teacher_detail", args=[self.slug])


class KafedraLife(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, related_name='kafedrasi',
                                verbose_name='Kafedra')
    title = models.CharField(max_length=250, verbose_name='Sarlavha')
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    body = models.TextField(verbose_name='Yangilik matni')
    image = models.ImageField(verbose_name="Rasm", upload_to="news/images", null=True, blank=True)
    created_time = models.DateTimeField(verbose_name="Yaratilgan vaqti", auto_now_add=True)
    published_time = models.DateTimeField(verbose_name="Yuklagan vaqti", default=timezone.now)
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
        return reverse("life_detail", args=[self.slug])


class KafedraSince(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, verbose_name='Kafedra')
    name = models.CharField(max_length=250, verbose_name="Ilmiy yo'nalish nomi")
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    description = models.TextField(verbose_name="Matni", help_text="Mana shu yo'nalish haqida ma'lumot")
    image = models.ImageField(upload_to='since/', verbose_name='Rasmi')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    published_time = models.DateTimeField(default=timezone.now, verbose_name='Yuklangan vaqti')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')
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
        return self.name

    # def total_views(self):
    #     return self.views.count()

    def get_absolute_url(self):
        return reverse("since_detail", args=[self.slug])


class KafedraGrant(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, verbose_name='Kafedra')
    name = models.CharField(max_length=250, verbose_name="Garnt nomi")
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    description = models.TextField(verbose_name="Matni", help_text="Mana shu grant haqida ma'lumot")
    image = models.ImageField(upload_to='grant/', verbose_name='Rasmi')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    published_time = models.DateTimeField(default=timezone.now, verbose_name='Yuklangan vaqti')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')
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
        return self.name

    # def total_views(self):
    #     return self.views.count()

    def get_absolute_url(self):
        return reverse("grant_detail", args=[self.slug])


class KafedraCultural(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, verbose_name='Kafedra')
    title = models.CharField(max_length=250, verbose_name="Sarlavhasi")
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    description = models.TextField(verbose_name="Matni", help_text="Mana shu Manaviy-ma'rifiy ish haqida ma'lumot")
    image = models.ImageField(upload_to='cultural/', verbose_name='Rasmi')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    published_time = models.DateTimeField(default=timezone.now, verbose_name='Yuklangan vaqti')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')
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
        return reverse("cultural_detail", args=[self.slug])


class KafedraInternational(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, verbose_name='Kafedra')
    name = models.CharField(max_length=250, verbose_name="Nomi", help_text='Tashkilot yoki universitet nomi')
    district = models.CharField(max_length=250, verbose_name="Hamkorlik yo'nalishi",
                                help_text='hamkorlik qaysi soha boyicha')
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    description = models.TextField(verbose_name="Matni", help_text="Mana shu hamkorlik haqida ma'lumot")
    image = models.ImageField(upload_to='international/', verbose_name='Rasmi')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    published_time = models.DateTimeField(default=timezone.now, verbose_name='Yuklangan vaqti')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')
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
        return self.name

    # def total_views(self):
    #     return self.views.count()

    def get_absolute_url(self):
        return reverse("international_detail", args=[self.slug])


class KafedraTeachersUpdate(models.Model):
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "published"

    kafedra = models.ForeignKey(KafedraCategory, on_delete=models.CASCADE, verbose_name='Kafedra')
    fish = models.ForeignKey(KafedraTeacher, on_delete=models.CASCADE, verbose_name="O'qituvchi ismi (FISH)")
    slug = models.SlugField(max_length=250, verbose_name='Url manzil :) ')
    image = models.ImageField(upload_to='update/', verbose_name='Rasmi')
    teacher_updated_time = models.DateField(verbose_name='Malaka oshirish sanasi')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')
    published_time = models.DateTimeField(default=timezone.now, verbose_name='Yuklangan vaqti')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Tahrirlangan vaqti')
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
        return self.fish.fish

    # def total_views(self):
    #     return self.views.count()

    def get_absolute_url(self):
        return reverse("teacher_update_detail", args=[self.slug])