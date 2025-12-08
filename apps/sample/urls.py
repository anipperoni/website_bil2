from django.urls import path
from .views import StartupView


urlpatterns = [
    path(
        "",
        StartupView.as_view(template_name="index.html"),
        name="index",
    ),
    path(
        "about/",
        StartupView.as_view(template_name="about.html"),
        name="about",
    ),
    path(
        "programs/",
        StartupView.as_view(template_name="programs.html"),
        name="programs",
    ),
    path(
        "partners/",
        StartupView.as_view(template_name="partners.html"),
        name="partners",
    ),
    path(
        "news/",
        StartupView.as_view(template_name="news.html"),
        name="news",
    ),
    path(
        "events/",
        StartupView.as_view(template_name="events.html"),
        name="events",
    ),
    path(
        "startup673/",
        StartupView.as_view(template_name="startup673.html"),
        name="startup673",
    ),
    path(
        "contact/",
        StartupView.as_view(template_name="contact.html"),
        name="contact",
    ),
    # Legacy routes
    path(
        "service/",
        StartupView.as_view(template_name="programs.html"),
        name="service",
    ),
    path(
        "quote/",
        StartupView.as_view(template_name="quote.html"),
        name="quote",
    ),
]
