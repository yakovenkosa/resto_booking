from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from restaurant.apps import RestaurantConfig
from restaurant.views import (
    TableListViews,
    TableDetailViews,
    RestaurantContactsView,
    TableCreateView,
    TableUpdateView,
    TableDeleteView,
    book_table,
    booking_success,
)

app_name = RestaurantConfig.name

urlpatterns = [
    path("home/", views.home, name="home"),
    path("table_list/", TableListViews.as_view(), name="table_list"),
    path("table/create/", TableCreateView.as_view(), name="table_create"),
    path("table/<int:pk>/detail", TableDetailViews.as_view(), name="table_detail"),
    path("table/<int:pk>/update", TableUpdateView.as_view(), name="table_update"),
    path("table/<int:pk>/delete", TableDeleteView.as_view(), name="table_delete"),
    path("book_table", book_table, name="book_table"),
    path("booking/success/", booking_success, name="booking_success"),
    path("contacts/", RestaurantContactsView.as_view(), name="contacts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
