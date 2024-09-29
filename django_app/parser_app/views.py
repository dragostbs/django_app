import re
import cv2
import numpy as np

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect, Http404
from .forms import FileForm
from .models import File
from django.contrib import messages
from pytesseract import pytesseract


class MainView(View):
    pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

    def process_img(self, file):
        file.seek(0)
        file_bytes = np.frombuffer(file.read(), np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        return img

    def extract_text(self, img):
        return pytesseract.image_to_string(img)

    def extract_amount(self, text):
        pattern = re.compile(r'\bTOTAL\b.*?(\d+(?:\.\d{1,2})?)')
        match = pattern.findall(text.upper())

        return match

    def delete_img(self):
        File.objects.last().delete()

    def get(self, request):
        file = FileForm()
        files = File.objects.all()
        amount = files.last().amount if files else 0

        return render(request, 'parser_app/main.html', {'files': files, 'file': file, 'amount': amount})

    def post(self, request):
        try:
            if 'clear' in request.POST:
                self.delete_img()
                return HttpResponseRedirect('/')

            submit_file = FileForm(request.POST, request.FILES)

            if submit_file.is_valid():
                uploaded_file = request.FILES['file']
                img = self.process_img(uploaded_file)
                text = self.extract_text(img)
                amount = self.extract_amount(text)

                file = File(file=request.FILES['file'], amount=amount[0])
                file.save()

                return HttpResponseRedirect('/')

            files = File.objects.all()
            return render(request, 'parser_app/main.html', {'files': files, 'file': submit_file})
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            files = File.objects.all()
            amount = files.last().amount if files else 0
            return render(request, 'parser_app/main.html', {'files': files, 'file': submit_file, 'amount': amount})
