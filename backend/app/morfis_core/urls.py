from django.urls import include, path
from rest_framework import routers
from . import views


# router = routers.SimpleRouter()
# router.register(r'icd_codes', views.IcdCodeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('case/icd_codes/<int:pk>', views.ICDcodeViewSet.as_view()),
    # path('articles/<int:pk>', views.ICDcodeViewSet.as_view({'get': 'retrieve'})),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('case/', include(router.urls)),

    path('case/', views.CaseListViewSet.as_view()),
    path('case/<int:pk>/', views.CaseUpdateViewSet.as_view()),
    path('icd_codes/', views.IcdCodeListViewSet.as_view())
]