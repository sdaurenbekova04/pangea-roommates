from django.contrib import admin
from django.core.mail import EmailMessage
# Register your models here.
from posts.models import Post, Favorite

class PostPublish(admin.ModelAdmin):
    list_display = ['title', 'published']
    actions = ['publish_with_notify', 'not_publish_description', 'not_publish_image']
    
    @admin.action(description='Опубликовать с уведомлением')
    def publish_with_notify(self, request, queryset):
        queryset.update(published = True)
        to = queryset.get()
        to = list(str(to).split(" "))
        subject, from_email = "Pangea-roommates | Пост прошёл модерацию", "pangea.roommates@yandex.kz"
        html_text = "<p>Test</p><h1>Test h1</h1>"
        msg = EmailMessage(subject, html_text, from_email, to)
        msg.content_subtype = "html"
        msg.send()
    
    @admin.action(description='Отказать в публикации с уведомлением [Описание]')
    def not_publish_description(self, request, queryset):
        to = queryset.get()
        to = list(str(to).split(" "))
        subject, from_email = "Pangea-roommates | Пост не прошёл модерацию", "pangea.roommates@yandex.kz"
        html_text = "<p>Test</p><h1>Описание</h1>"
        msg = EmailMessage(subject, html_text, from_email, to)
        msg.content_subtype = "html"
        msg.send()

    @admin.action(description='Отказать в публикации с уведомлением [Картинка]')
    def not_publish_image(self, request, queryset):
        to = queryset.get()
        to = list(str(to).split(" "))
        subject, from_email = "Pangea-roommates | Пост не прошёл модерацию", "pangea.roommates@yandex.kz"
        html_text = "<p>Test</p><h1>Картинка</h1>"
        msg = EmailMessage(subject, html_text, from_email, to)
        msg.content_subtype = "html"
        msg.send()


admin.site.register(Post, PostPublish)
admin.site.register(Favorite)