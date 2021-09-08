from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    # Описать класс AboutAuthorView для страницы about/author
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    # Описать класс AboutTechView для страницы about/tech
    # В переменной template_name обязательно указывается имя шаблона,
    # на основе которого будет создана возвращаемая страница
    template_name = 'about/tech.html'
