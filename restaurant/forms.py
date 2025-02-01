from django import forms
from django.forms import BooleanField
from restaurant.models import Booking
from restaurant.models import Table


class StyleFormMixin:
    """класс StyleFormMixin предназначен для добавления CSS-классов к полям формы в Django"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class TableForm(forms.ModelForm, StyleFormMixin):
    """Форма модели стола"""

    class Meta:
        model = Table
        exclude = ("views_counter",)

    def __init__(self, *args, **kwargs):
        super(TableForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование стола"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание стола"}
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите стоимость бронирования стола",
            }
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name.lower() and description.lower() in [
            "казино",
            "криптовалюта",
            "крипта",
            "биржа",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]:
            self.add_error("name", "запрещенное слово")
            self.add_error("description", "запрещенное слово")

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")

        if price is None:
            raise forms.ValidationError(
                "Стоимость бронирования стола должна быть указана."
            )

        if price < 0:
            raise forms.ValidationError(
                "Цена бронирования стола не может быть отрицательной."
            )

        return price


class BookingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "email", "date_time"]
        widgets = {
            "date_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
