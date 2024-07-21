from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import FileForm
from .models import File


class MainView(View):
    def get(self, request):
        file = FileForm()
        return render(request, 'uploadfile_app/main.html', {'file': file})

    def post(self, request):
        submit_file = FileForm(request.POST, request.FILES)

        if submit_file.is_valid():
            file = File(file=request.FILES['file'])
            file.save()
            return HttpResponseRedirect("/file")

        return render(request, 'uploadfile_app/main.html', {'file': submit_file})
