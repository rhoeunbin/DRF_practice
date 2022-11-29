from django.urls import path, include

urlpatterns = [
    # 로그인
    path('', include('dj_rest_auth.urls')),
    # 회원가입
    path('registration/', include('dj_rest_auth.registration.urls')),
]