from datetime import datetime
from django.views import View
from .models import Chat
from .forms import ChatForm
from django.shortcuts import render, redirect
from transformers import AutoTokenizer, TFBlenderbotForConditionalGeneration


model_name = "facebook/blenderbot-400M-distill"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFBlenderbotForConditionalGeneration.from_pretrained(model_name)

class MainView(View):
    def __init__(self):
        self.chat = Chat
        self.chat_form = ChatForm
        self.date = datetime.now()

    def get(self, request):
        form = self.chat_form()
        chat_history = self.chat.objects.all().order_by('timestamp')
        return render(request, 'chat_app/main.html', {'date': self.date, 'form': form, 'chat_history': chat_history})

    def post(self, request):
        if 'clear' in request.POST:
            self.clear_chat()
            return redirect('chat:main')

        form = self.chat_form(request.POST)
        if form.is_valid():
            user_msg = form.cleaned_data['msg']
            input = tokenizer(user_msg, return_tensors="tf")
            output = model.generate(**input)
            bot_msg = tokenizer.decode(output[0], skip_special_tokens=True).strip()

            self.chat.objects.create(user_msg=user_msg, bot_msg=bot_msg)
            return redirect('chat:main')
        
        chat_history = self.chat.objects.all().order_by('timestamp')
        return render(request, 'chat_app/main.html', {'form': form, 'chat_history': chat_history, 'date': self.date})

    def clear_chat(self):
        self.chat.objects.all().delete()
