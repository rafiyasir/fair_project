from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='claims'),
    path('<int:claim_id>', views.claim, name='claim'),
]