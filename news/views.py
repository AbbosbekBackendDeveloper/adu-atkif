from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, HttpResponse, redirect
from .models import News, Category, Contact
from .forms import ContactForm
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.


def home(request):
    news = News.objects.all().order_by('-published_time')[:3]
    context = {
        "news": news,
    }
    return render(request, 'home.html', context)


def newslistview(request):
    newss = News.objects.all()
    categories = Category.objects.all()
    s_category = News.objects.filter(category__name="Sport").order_by("-published_time")[:4]
    i_category = News.objects.filter(category__name="Ilmiy").order_by("-published_time")[:4]
    m_category = News.objects.filter(category__name="Madaniy-ma'rifiy").order_by("-published_time")[:4]
    d_category = News.objects.filter(category__name="Dunyo").order_by("-published_time")[:4]
    paginator = Paginator(newss, 6)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        # return HttpResponse("<h3> Xabaringiz uchun tashakkur! </h3>")
        return redirect('/')
    context = {
        "newss": newss,
        "category": categories,
        "s_category": s_category,
        "i_category": i_category,
        "d_category": d_category,
        "m_category": m_category,
        "newss": page,
    }
    return render(request, 'news-list.html', context)


class SportNewsView(ListView):
    model = News
    template_name = 'sport.html'
    context_object_name = 'sport_news'
    paginate_by = 2

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Sport")
        return news


class SinceNewsView(ListView):
    model = News
    template_name = 'ilmiy.html'
    context_object_name = 'ilmiy_news'
    paginate_by = 2

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Ilmiy")
        return news


class CulturalNewsView(ListView):
    model = News
    template_name = 'madaniy.html'
    context_object_name = 'madaniy_news'
    paginate_by = 2

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Madaniy-ma'rifiy")
        return news


class ForeignNewsView(ListView):
    model = News
    template_name = 'xorij.html'
    context_object_name = 'xorij_news'
    paginate_by = 2

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="Dunyo")
        return news


def newsdetailview(request, news):
    news = get_list_or_404(News, slug=news, status=News.Status.Published)
    related = News.objects.filter(status=News.Status.Published)[:5]
    context = {
        "news": news,
        "related": related,
    }
    return render(request, 'news-detail.html', context)


def newssearchview(request):
    if request.method == 'POST':
        query = request.POST['query']
        search = News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        context = {
            "query": query,
            "search": search
        }
        return render(request, 'news-search.html', context)
    else:
        return render(request, 'news-search.html')


def contactview(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h3> Xabaringiz uchun tashakkur! </h3>")
    context = {
        "form": form,
    }

    return render(request, 'contact.html', context)

# class SaidbarNewsView(ListView):
#     news = News
#     template_name = 'news-detail.html'
#     context_object_name = 'all_news'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return News.objects.filter(
#             Q(title__icontains=query) | Q(body__icontains=query)
#         )
