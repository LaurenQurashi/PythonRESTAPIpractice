from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here. A View is a function that takes in a request and returns a response. 

@api_view(['GET', 'POST'])
# this @api_view decorator is a wrapper that REST provides. It helps with some additional functionality.
#  The get and post methods are decalred methods that this view function can use. 
def snippet_list(request, format=None):
    #  Here we define the name of the view function, and pretty much they always take a request as a param. 
    #  This function is a bit like a controller, it's python code used to format the data whether it's going to or from the API.
    #  The format suffix gives us URLs that explicitly refer to a given format, so our API can deal with a route such as
    # http://example.com/api/items/4.json
    
    """
    This view function makes sure we list all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        # sets a variable name to a request for all the snippets from the DB
        serializer = SnippetSerializer(snippets, many=True)
        #  sets a variable name to the outcome of calling the snippet serialiser.
        return Response(serializer.data)
        #  All view methods should return a response object, and this is a response with all our data in it. 

    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        # sets a variable name to the outcome of calling the snippetSerializer on the request.
        #  Request and Response are REST provided levelled up versions of HttpRequest and HttpResponse. The additional 
        # functionality means that they can automatically know what format to put the data in (JSON or PythonNative depending on
        #  which way the data is going).
        if serializer.is_valid():
            serializer.save()
            #  If the data is valid, it gets saved. The code for this is set in the serializers file. If you're using a 
            # model Serializer then It's done by unseen magic. If you've made your own generic one, the code will be there. 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #  These HTTP codes are provided by the api wrapper above. They help set the status to an easily read
            #  variable name for the HTTP codes. 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  All view functions are reponsible for returning a response. 

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)