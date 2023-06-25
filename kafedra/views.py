from django.shortcuts import render, get_list_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView
from .models import KafedraTeacher, KafedraCategory, KafedraGrant, KafedraCultural, KafedraInternational, KafedraLife, \
    KafedraSince, KafedraTeachersUpdate


def kafedrateachersview(request):
    teacher = KafedraTeacher.objects.all().order_by('-published_time')
    category = KafedraCategory.objects.all()
    at_category = KafedraTeacher.objects.filter(kafedra__name='AT-Servis')
    ki_category = KafedraTeacher.objects.filter(kafedra__name='Kompyuter Injiniringi')
    context = {
        "teacher": teacher,
        "category": category,
        "at_category": at_category,
        "ki_category": ki_category,
    }
    return render(request, 'kafedra/teacher.html', context)


class AtTeachersView(ListView):
    model = KafedraTeacher
    template_name = 'kafedra/at-teachers.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atteachersview(request):
#     teacher = KafedraTeacher.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 3)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-teachers.html', context)


class KiTeachersView(ListView):
    model = KafedraTeacher
    template_name = 'kafedra/ki-teachers.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kiteachersview(request):
#     teacher = KafedraTeacher.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-teachers.html', context)


def teachersdetailview(request, teacher):
    teacher = get_list_or_404(KafedraTeacher, slug=teacher, status=KafedraTeacher.Status.Published)
    related = KafedraTeacher.objects.filter(status=KafedraTeacher.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/teachers-detail.html', context)


def teacherssearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraTeacher.objects.filter(
            Q(fish__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/teachers-search.html', context)
    else:
        return render(request, 'kafedra/teachers-search.html')


class AtGrantView(ListView):
    model = KafedraGrant
    template_name = 'kafedra/at-grant.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atgrantview(request):
#     teacher = KafedraGrant.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-grant.html', context)


class KiGrantView(ListView):
    model = KafedraGrant
    template_name = 'kafedra/ki-grant.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kigrantview(request):
#     teacher = KafedraGrant.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-grant.html', context)


def grantdetailview(request, grant):
    teacher = get_list_or_404(KafedraGrant, slug=grant, status=KafedraGrant.Status.Published)
    related = KafedraGrant.objects.filter(status=KafedraGrant.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/grant-detail.html', context)


class AtSinceView(ListView):
    model = KafedraSince
    template_name = 'kafedra/at-ilmiy.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atsinceview(request):
#     teacher = KafedraSince.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-ilmiy.html', context)


class KiSinceView(ListView):
    model = KafedraSince
    template_name = 'kafedra/ki-ilmiy.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kisinceview(request):
#     teacher = KafedraSince.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-ilmiy.html', context)


def sincedetailview(request, since):
    teacher = get_list_or_404(KafedraSince, slug=since, status=KafedraSince.Status.Published)
    related = KafedraSince.objects.filter(status=KafedraSince.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/ilmiy-detail.html', context)


class AtLifesView(ListView):
    model = KafedraLife
    template_name = 'kafedra/at-hayoti.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atlifesview(request):
#     teacher = KafedraLife.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-hayoti.html', context)


class KiLifesView(ListView):
    model = KafedraLife
    template_name = 'kafedra/ki-hayoti.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kilifesview(request):
#     teacher = KafedraLife.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-hayoti.html', context)


def lifedetailview(request, life):
    teacher = get_list_or_404(KafedraLife, slug=life, status=KafedraLife.Status.Published)
    related = KafedraLife.objects.filter(status=KafedraLife.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/hayoti-detail.html', context)


class AtCulturalView(ListView):
    model = KafedraCultural
    template_name = 'kafedra/at-manaviy.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atculturalview(request):
#     teacher = KafedraCultural.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-manaviy.html', context)


class KiCulturalView(ListView):
    model = KafedraCultural
    template_name = 'kafedra/ki-manaviy.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kiculturalview(request):
#     teacher = KafedraCultural.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-manaviy.html', context)


def culturaldetailview(request, cultural):
    teacher = get_list_or_404(KafedraCultural, slug=cultural, status=KafedraCultural.Status.Published)
    related = KafedraCultural.objects.filter(status=KafedraCultural.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/manaviy-detail.html', context)


class AtInternationalView(ListView):
    model = KafedraInternational
    template_name = 'kafedra/at-hamkorlik.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atinternationalview(request):
#     teacher = KafedraInternational.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-hamkorlik.html', context)


class KiInternationalView(ListView):
    model = KafedraInternational
    template_name = 'kafedra/ki-hamkorlik.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kiinternationalview(request):
#     teacher = KafedraInternational.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-hamkorlik.html', context)


def internationaldetailview(request, international):
    teacher = get_list_or_404(KafedraInternational, slug=international, status=KafedraInternational.Status.Published)
    related = KafedraInternational.objects.filter(status=KafedraInternational.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/hamkorlik-detail.html', context)


class AtTeachersUpdateView(ListView):
    model = KafedraTeachersUpdate
    template_name = 'kafedra/at-malaka.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="AT-Servis")
        return teacher


# def atteachersupdateview(request):
#     teacher = KafedraTeachersUpdate.objects.filter(kafedra=1)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/at-malaka.html', context)


class KiTeachersUpdateView(ListView):
    model = KafedraTeachersUpdate
    template_name = 'kafedra/ki-malaka.html'
    context_object_name = 'teacher'
    paginate_by = 6

    def get_queryset(self):
        teacher = self.model.published.all().filter(kafedra__name="Kompyuter Injiniringi")
        return teacher


# def kiteachersupdateview(request):
#     teacher = KafedraTeachersUpdate.objects.filter(kafedra=2)
#     paginator = Paginator(teacher, 6)
#     page_num = request.GET.get('page')
#     page = paginator.get_page(page_num)
#     context = {
#         "teacher": teacher,
#         "news": page
#     }
#
#     return render(request, 'kafedra/ki-malaka.html', context)


def teachersupdatedetailview(request, teacher_update):
    teacher = get_list_or_404(KafedraTeachersUpdate, slug=teacher_update, status=KafedraTeachersUpdate.Status.Published)
    related = KafedraTeachersUpdate.objects.filter(status=KafedraTeachersUpdate.Status.Published)[:5]
    context = {
        "teacher": teacher,
        "related": related,
    }
    return render(request, 'kafedra/malaka-detail.html', context)


def lifesearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraLife.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/life-search.html', context)
    else:
        return render(request, 'kafedra/life-search.html')


def sincesearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraSince.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/since-search.html', context)
    else:
        return render(request, 'kafedra/since-search.html')


def grantsearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraGrant.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/grant-search.html', context)
    else:
        return render(request, 'kafedra/grant-search.html')


def culturalsearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraCultural.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/cultural-search.html', context)
    else:
        return render(request, 'kafedra/cultural-search.html')


def internationalsearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraInternational.objects.filter(
            Q(name__icontains=query) | Q(district__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/international-search.html', context)
    else:
        return render(request, 'kafedra/international-search.html')


def teacherupdatesearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = KafedraTeachersUpdate.objects.filter(
            Q(teacher_updated_time__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'kafedra/teacher-update-search.html', context)
    else:
        return render(request, 'kafedra/teacher-update-search.html')