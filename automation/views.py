from django.shortcuts import render
import os
import shutil

def home(request):
    return render(request, 'automation/index.html')

def organize_files(request):
    target_folder = os.path.expanduser("~/Downloads/AutomationFolder")

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    extensions = {
        "Images": ['.jpg', '.jpeg', '.png', '.gif'],
        "Documents": ['.pdf', '.docx', '.txt'],
    }

    for filename in os.listdir(target_folder):
        name, ext = os.path.splitext(filename)
        for folder, exts in extensions.items():
            if ext.lower() in exts:
                folder_path = os.path.join(target_folder, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(os.path.join(target_folder, filename), os.path.join(folder_path, filename))

    return render(request, 'automation/success.html')
