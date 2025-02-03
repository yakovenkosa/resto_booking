from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

from restaurant.forms import TableForm
from restaurant.models import Table, Booking
from .forms import BookingForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View

from .services import send_messages


class TableListViews(ListView):
    model = Table
    template_name = "restaurant/table_list.html"


class TableDetailViews(DetailView):
    model = Table
    template_name = "restaurant/table_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "restaurant/table_create.html"
    success_url = reverse_lazy("restaurant:table_list")


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = "restaurant/table_create.html"
    success_url = reverse_lazy("restaurant:table_list")

    def get_success_url(self):
        return reverse("restaurant:table_detail", args=[self.kwargs.get("pk")])


class TableDeleteView(DeleteView):
    model = Table
    template_name = "restaurant/table_delete.html"
    success_url = reverse_lazy("restaurant:table_list")


class RestaurantContactsView(View):
    def get(self, request):
        return render(request, "restaurant/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


def home(request):
    return render(request, "restaurant/home.html")


def book_table(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Сохраняем бронирование
            send_messages(
                booking.name, booking.date_time, booking.email
            )  # Отправляем email-уведомление
            return redirect(
                "restaurant:booking_success"
            )  # Перенаправляем на страницу успеха
    else:
        form = BookingForm()
    return render(request, "restaurant/book_table.html", {"form": form})


def booking_success(request):
    booking = Booking.objects.latest("created_at")
    return render(request, "restaurant/booking_success.html", {"booking": booking})
