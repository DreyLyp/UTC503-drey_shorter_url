import uuid
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import drey_link_saved

# This function will inform our django that the index.html page is our page that will be hosted
def index(request):
    return render(request, 'index.html')

# This function will create the idd of the long link
# The idd is a sequence of 8 characters that will point to our long link in the database
def create_shorter_url(request):
    if request.method == 'POST':
        url_long = request.POST['link'] # Allows you to retrieve the link entered on index.html
        url_string = str(uuid.uuid4())[:8] # Create a idd of 8 characters
        new_link = drey_link_saved(url = url_long, idd = url_string)
        new_link.save() # Save the long link and the idd in the data base named drey_link_saved
        return HttpResponse(url_string)

# This function will make the link between our idd and the long link
# like that by entering our localhost:8000 and our idd we will come across the long link
def redirect_to_real_link(request, pk):
    real_link = drey_link_saved.objects.get(idd=pk) # Retrieves the entity from the database corresponding to the idd
    return redirect(real_link.url) # We return the long link