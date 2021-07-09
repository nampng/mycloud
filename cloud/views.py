from django.shortcuts import render
from cloud.models import FileModel
import os
from django.http import HttpResponse, Http404

# Create your views here.

def index(response):
    file_list = FileModel.objects.all()
    total_files = len(file_list)
    recent_files = []
    if file_list:
        recent_files = file_list.order_by('-id')[:5]
        for file in recent_files:
            print(f"Recent file: {file.name}")
    return render(response, 'cloud/index.html', {'total_files':total_files, 'recent_files':recent_files})

def files(response):

    file_list = FileModel.objects.all()

    if response.method == 'POST':
        print(f"POST: {response.POST}")
        if response.POST.get("submit_file"):
            print("Submitting file")
            if response.FILES:
                print(response.FILES)
                print("There's a file!")
                uploaded_file = response.FILES['uploaded_file']
                uploaded_file.name = uploaded_file.name.replace(' ', '_')
                print(f"File name: {uploaded_file.name}, File size: {uploaded_file.size}")
                new_file = FileModel(name=uploaded_file.name, file=uploaded_file)
                new_file.save()
            else:
                print("No file.")

        if response.POST.get("download_file"):
            print("Downloading file")
            file_id = response.POST["download_file"][3:]
            file = FileModel.objects.get(id=file_id)
            with open(file.name, 'rb') as f:
                http_response = HttpResponse(f.read())
                http_response['Content-Disposition'] = 'attachment; filename= ' + file.name
                return http_response

        if response.POST.get("delete_file"):
            print("Deleting file")
            file_id = response.POST["delete_file"][3:]
            file = FileModel.objects.get(id=file_id)
            file_object = file.file
            file_object.delete()
            file.delete()
        

    return render(response, 'cloud/files.html', {'file_list':file_list})