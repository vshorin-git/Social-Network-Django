from django.views.generic import CreateView

from django.urls import reverse_lazy

from .forms import CreationForm, ContactForm
from django.shortcuts import redirect, render


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('/thank-you/')
        return render(request, 'post.html', {'form': form})
    form = ContactForm()
    return render(request, 'post.html', {'form': form})