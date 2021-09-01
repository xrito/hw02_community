from django.contrib.auth.views import LogoutView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        # Прямо в описании обработчика укажем шаблон,
        # который должен применяться для отображения возвращаемой страницы.
        # Да, во view-классах так можно! Как их не полюбить.
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
]
