from django.urls import path
from .views import polls_home_view, detail_view, ResultsView, vote_view


app_name = "polls"
urlpatterns = [
    path('', polls_home_view, name='polls_home'),
    path('<int:q_id>', detail_view, name='detail'),
    path('<int:pk>/result', ResultsView.as_view(), name='result'),
    path('<int:q_id>/votes', vote_view, name='votes'),
]