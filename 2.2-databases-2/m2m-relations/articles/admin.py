from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                counter += 1
        if counter == 0:
            raise ValidationError('Необходимо указать основной раздел')
        if counter > 1:
            raise ValidationError('Основной раздел может быть только один')
        return super().clean()

        # В form.cleaned_data будет словарь с данными
        # каждой отдельной формы, которые вы можете проверить

        # вызовом исключения ValidationError можно указать админке о наличие ошибки
        # таким образом объект не будет сохранен,
        # а пользователю выведется соответствующее сообщение об ошибке


class ScopeInlaine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInlaine]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [ScopeInlaine, ]
