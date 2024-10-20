from django import forms

class UserForm(forms.Form):
    name = forms.CharField(
        label="Имя клиента",
        max_length=15,
        help_text="ФИО не более 15 символов",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        label="Возраст клиента",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    basket = forms.BooleanField(
        label="Положить товар в корзину?",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    vyb = forms.NullBooleanField(
        label="Вы поедите в Сочи?",
        widget=forms.NullBooleanSelect(attrs={'class': 'form-select'})
    )
    email = forms.EmailField(
        label="Электронный адрес",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    regex = forms.RegexField(
        label="Введите текст",
        regex=r'^\w+$',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    url_text = forms.URLField(
        label="Введите URL",
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )
    file_path = forms.FilePathField(
        label="Выберите файл",
        path="C:/Users/sanme/OneDrive/Документы",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    file = forms.FileField(
        label="Файл",
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )