from django.views.generic import ListView, CreateView
from django.urls import reverse, reverse_lazy
from rest_framework import viewsets
from .models import StorageItem
from .serializers import StorageItemSerializer


class ItemList(ListView):
    model = StorageItem


class ItemCreate(CreateView):
    model = StorageItem
    fields = '__all__'
    success_url = reverse_lazy('index')


class StorageItemView(viewsets.ModelViewSet):
    serializer_class = StorageItemSerializer
    queryset = StorageItem.objects.all()