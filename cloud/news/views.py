from django.shortcuts import render, redirect
from .models import Artiсles
from .forms import ArtiсlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    news = Artiсles.objects.order_by('-date')[:5]
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Artiсles
    template_name = 'news/details_views.html'
    context_object_name = 'article'

def NewsUpdateView(request, slug):
    if request.method == 'POST':
        form = ArtiсlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
    else:
        form = ArtiсlesForm()
    return render(request, 'news/news_update.html', {
        'form': form
    })

class NewsDeleteView(DeleteView):
    model = Artiсles
    template_name = 'news/news_delete.html'
    success_url = '/news'


def create(request):
    error = ''
    if request.method == "POST":
        form = ArtiсlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верна'

    form = ArtiсlesForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'news/create.html', data)