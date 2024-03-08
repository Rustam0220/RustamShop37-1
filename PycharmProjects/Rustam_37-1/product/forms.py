from django import forms

from product.models import Product, Review, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['rate', 'comments']

        labels = {
            'name': 'Название',
            'description': 'Описание',
            'image': 'Картинка'
        }
        help_texts = {
            'name': 'Some useful help text'
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if "python" in name.lower():

            raise forms.ValidationError("Python is not allowed")

        return name.capitalize()

    def clean_description(self):
        description = self.cleaned_data['description']
        if "django" in description.lower():
            raise forms.ValidationError("Django is not allowed")

        return description

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and description:
            if name.lower() == description.lower():
                raise forms.ValidationError("Name and description must be different")

        return cleaned_data


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {
            'text': 'Отзыв'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Категория'
        }

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'categories']
