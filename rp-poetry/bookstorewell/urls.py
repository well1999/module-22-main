
import debug_toolbar
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    pach('-- debug --/ ', include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path('bookstorewell/(?<version>(v1|v2))/',  include ('product.urls')),    
     re_path('bookstorewell/(?<version>(v1|v2))/', include ('product.urls')), 
     pach('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]

