# """drf URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api-auth/', include('rest_framework.urls'))
# ]

from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib import admin
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
# 앱 시리얼라이저 기본 모델
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # 사용할 테이블
        model = User
        # 시리얼라이저에 사용할 필드(=컬럼)
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
# 기본 뷰셋
# 뷰셋 과 제네릭뷰 차이를 인지하고 사용
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# 뷰셋 사용 시 사용하게 되는 라우터
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # 어드민 사이트 코드
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    # 로그인 버튼과 기능 코드
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]