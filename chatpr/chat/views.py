from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import FormModelMessage


from .models import MessageModel
# Create your views here.


class MessageView(ListView):
    model = MessageModel
    template_name = "message.html"
    context_object_name = "messager"

    def get_queryset(self):
        return MessageModel.objects.order_by("-id").all()[:1]


class MessageMaking(CreateView):
    model = MessageModel
    form_class = FormModelMessage
    template_name = "message_creator.html"
    success_url = reverse_lazy("message-viewer")
