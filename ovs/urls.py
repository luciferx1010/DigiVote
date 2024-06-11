from django.contrib import admin
from django.urls import path
from poll import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexview, name='index'),
    path('home/', views.homeView, name='home'),
    path('register/', views.registrationView, name='registration'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('logout/', views.logoutView, name='logout'),
    path('position/', views.positionView, name='position'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('result/', views.resultView, name='result'),
    path('changepass/', views.changePasswordView, name='changepass'),
    path('editprofile/', views.editProfileView, name='editprofile'),
    path('verifyotp/',views.verifyemail,name='verifyotp'),
    path('login/forgotemail.html/',views.forgotemail,name='forgotemail'),
    path('forgotemailverifyotp/',views.verifyforgotemail,name='verifyforgotemail'),
    path('changePasswordforgotemail/',views.changePasswordverifyforgotemail,name='changePasswordforgotemail'),
    path('emailvoting/',views.emailvotingview,name='emailvoting'),
    path('verifyemailvoting/',views.verifyemailvotingview,name='verifyemailvoting'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "DIGI-VOTE"
admin.site.index_title = "Welcome to online voting system admin panel"
admin.site.site_title = "OVS"
