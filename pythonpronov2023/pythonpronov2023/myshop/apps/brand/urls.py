from django.urls import re_path
from apps.product.views import BrandView


urlpatterns = [
    re_path(r'^$', BrandView.as_view(), name='brands')
]