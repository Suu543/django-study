from django.urls import path
from . import views

# urlpatterns = [
#     path("january", views.january_view),
#     path("february", views.febuary_view),
#     path("march", views.march_view),
#     path("<month>", views.monthly_challenge)
# ]

# Dynamic Path Segments & Captured Values Path Converters
# The Reverse Function & Named Urls
urlpatterns = [
    path("", views.index, name="index"), # /challenges/
    path("<int:month>", views.monthly_challenges_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
