import json
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http.response import FileResponse, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.db.models import Q
from pathlib import Path
from django.conf import settings

from .forms import DocumentForm
from .models import Document


def documents_list(request):
    if not request.user.is_authenticated:
        documents = []
    else:
        documents = Document.objects.filter(Q(created_by=request.user)|Q(public=True))
    return render(request, 'main/documents_list.html',{
        'documents': documents
    })


@login_required
def filter_by_filename(request, file_name):
    documents = list(Document.objects.filter(Q(file_name=file_name) & (Q(created_by=request.user)|Q(public=True))))
    documents_forjson = [{'fileName': document.file_name,
                          'createdBy': document.created_by.username,
                          'createdAt': document.created_at.strftime("%m/%d/%Y - %H:%M:%S"),
                          'filePath': str(document.file.file)} for document in documents]
    return JsonResponse(documents_forjson, safe=False)


@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.created_by = request.user
            doc.save()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'main/upload_document.html', {
        'form': form
    })

@login_required
def download_document(request):
    if request.method == 'POST':
        try:
            file = Path(request.POST['file_path'])
        except:
            HttpResponseBadRequest('Bad Request, probably wrong path to sent')
        documents = list(Document.objects.filter(Q(file=str(file)) & (Q(created_by=request.user)|Q(public=True))))
        if not documents:
            return HttpResponseBadRequest('File Not Found')
        media_root = Path(settings.MEDIA_ROOT)
        full_path = media_root.joinpath(file)
        if not full_path.exists():
            return HttpResponseBadRequest('File Not Found')
        filename = documents[0].file_name
        response = FileResponse(open(full_path, 'rb'), as_attachment=True, filename='test.txt')
        return response
        # return HttpResponse(
        #     json.dumps({'success': 'true'}),
        #     content_type="application/json" ,           
        #     status='200'
        #     )
    else:
        return HttpResponseNotAllowed(['POST',], "405 - Not allowed")
