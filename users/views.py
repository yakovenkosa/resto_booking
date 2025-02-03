from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class RegisterViews(CreateView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("restaurant:home")

    def form_valid(self, form):
        user = form.save()
        user.save()
        return super().form_valid(form)
