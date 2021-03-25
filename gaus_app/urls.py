from django.urls import path
from .views import Index, Count_Matrix, Get_matrix, Change_dir

urlpatterns = [
    path('dim/', Index, name='index'),
    # path('data/', Count_PDF),
    path('matrix/', Count_Matrix, name='matrix'),
    # path('eliminate/', G_Elimination, name='eliminate'),
    path('', Get_matrix, name='get_matrix'),
    path('change_dir/', Change_dir, name='change_dir'),
]