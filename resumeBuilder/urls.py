from django.urls import path
from resumeBuilder import views
from .views import generate_pdf_resume

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signupPage, name='signupPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutPage, name='logoutPage'),
   # path('addResume/', views.addResume, name='add_resume'),  # Define URL pattern for addResume view
    path('addResume', views.addResume, name='addResume'),
    path('listResume', views.listResume, name='listResume'),
    #path('editResume', views.editResume, name='edit_resume'),
    #path('download_resume/', generate_pdf_resume, name='download_resume'),
    path('download', views.download, name='download'),
    path('deleteResume/', views.deleteResume, name='delete_resume'),

]