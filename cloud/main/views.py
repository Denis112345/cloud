from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.http import urlquote
import os
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView
from django.shortcuts import get_object_or_404
from .forms import DocumentForm
from .models import Document

def index(request):
    return render(request, 'main/index.html')

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'main/document_detail.html'
    slug_field = 'slug'
    context_object_name = 'document'

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'main/document.html'

def DocumentUpload(request):
    if request.method == 'POST':
        print('!!!!!')
        print(request.POST)
        print(request.FILES)
        slug = str(request.FILES['document']) + request.POST['descriptions']
        form = DocumentForm(request.POST, request.FILES, slug)
        if form.is_valid():
            print('+++++++=')
            print(form)
            form.save()
            return redirect('indexView')
    else:
        form = DocumentForm()
    return render(request, 'main/upload_view.html', {
        'form': form
    })

def DocumentAll(request):
    download_list = Document.objects.all()

    return render(request, 'main/document_all_views.html', {'download_list': download_list})

def DocumentDownload(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(), content_type='aplication/document')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response