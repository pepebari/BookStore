from django.urls import include, path, re_path
from rest_framework import routers
from Books import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'stock', views.StockViewSet)
router.register(r'book', views.BookViewSet)
router.register(r'Purchase', views.PurchaseViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^user/(?P<username>.+)/$', views.UserList.as_view())
]
