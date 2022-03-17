from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') and not form.cleaned_data.get('DELETE'):
                tag_count += 1

        if tag_count > 1:
            raise ValidationError('Основным может быть только один раздел')
        if tag_count < 1:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


