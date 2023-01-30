from django.urls import path
from . import views

urlpatterns = [
    path('select_department/', views.select_department, name='select_department'),
    path('select_doctor/', views.select_doctor, name='select_doctor'),
    path('confirm_token/', views.confirm_token, name='confirm_token'),
    path('generate/<int:doctor_id>/', views.generate_token, name='generate_token'),
    path('reset/', views.reset_tokens, name='token_reset'),
    path('download_pdf/<int:token_id>/', views.download_pdf, name='download_pdf'),
]
