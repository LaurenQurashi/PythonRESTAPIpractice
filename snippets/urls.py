from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

#  This file maps the urls to the view functions. the List below is jsut a big list containing the urls and what
#  functions get invoked when these urls are visited. If someone goes to the snippets/ path, then the 
#  snippest list view function in the views.py gets invoked. 
#  To access something from the url, use captioned brackets and include a converter otherwise any string etc excluding
#  a / is matched.

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
# The code above appends the format suffix patterns to the end of the urls. 