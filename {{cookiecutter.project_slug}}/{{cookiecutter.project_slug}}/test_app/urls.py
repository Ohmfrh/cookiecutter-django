from django.urls import path

from {{ cookiecutter.project_slug }}.test_app.views import home_page_view

app_name = "users"
urlpatterns = [
    path("", view=home_page_view, name="home"),
]
