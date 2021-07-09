from django.shortcuts import render
from cloud.models import FileModel

# Create your views here.

def index(response):
    file_list = FileModel.objects.all()
    total_files = len(file_list)
    return render(response, 'cloud/index.html', {'total_files':total_files, 'file_list':file_list})

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
                print(f"File name: {uploaded_file.name}, File size: {uploaded_file.size}")
                new_file = FileModel(name=uploaded_file.name, file=uploaded_file)
                new_file.save()
            else:
                print("No file.")

        if response.POST.get("download_file"):
            print("Downloading file")
            file_id = response.POST["download_file"][3:]

        if response.POST.get("delete_file"):
            print("Deleting file")
            file_id = response.POST["delete_file"][3:]
            file = FileModel.objects.get(id=file_id)
            file_object = file.file
            file_object.delete()
            file.delete()
        

    return render(response, 'cloud/files.html', {'file_list':file_list})