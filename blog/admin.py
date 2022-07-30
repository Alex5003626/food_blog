from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInLine(admin.StackedInline):  # для PostAdmin --> inlines
    model = models.Recipe
    extra = 1  # один рецепт


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]
    inlines = [RecipeInLine]  # Позволяет добавлять рецепт прям во время редактирования Post
    save_as = True  # добавляет поле "сохранить как новый объект
    save_on_top = True


@admin.register(models.Recipe)  # указываем модель, которую мы хотим подключить
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)
# admin.site.register(models.Post, PostAdmin) <-- можно делать так, если НЕ с декоратором
# admin.site.register(models.Recipe, RecipeAdmin) <-- можно делать так, если НЕ с декоратором

