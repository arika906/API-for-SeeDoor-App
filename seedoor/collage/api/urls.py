from django.urls import path,include
from collage.api import views
from collage.api.views import(
      api_create_collage_view,
     # api_update_collage_view,
     # api_delete_collage_view,
      StudentListView
)

app_name = 'collage'

urlpatterns = [
   
    path('list', StudentListView.as_view(), name="list"),
	path('create', api_create_collage_view, name="create"),
	#path('update/<pk>', api_update_collage_view, name="update"),
	#path('delete/<pk>',api_delete_collage_view, name ="delete")

]