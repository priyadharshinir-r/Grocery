from django.urls import path
from .views import GroceryListView,GroceryCreateView,GroceryDeleteView,GrocerySearchView,GroceryUpdateView

urlpatterns=[
    path('grocery/',GroceryListView.as_view(),name='grocery'),
    path('grocery/create/',GroceryCreateView.as_view(),name='grocery-create'),
    path('grocery/<int:pk>/update/',GroceryUpdateView.as_view(),name='grocery-update'),
    path('grocery/<int:pk>/delete/',GroceryDeleteView.as_view(),name='grocery-delete'),
    path('grocery/search/',GrocerySearchView.as_view(),name='grocery-search')

]