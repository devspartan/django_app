from django.urls import path
from .views import polls_home_view, detail_view, results_view, vote_view


app_name = "polls"
urlpatterns = [
    path('', polls_home_view, name='polls_home'),
    path('<int:q_id>', detail_view, name='detail'),
    path('<int:q_id>/result', results_view, name='result'),
    path('<int:q_id>/votes', vote_view, name='votes'),
]