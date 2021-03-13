import json
import os
from .forms import JSONFileForm
from .models import JSONFile,JsonDetails
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def userdata(request):
    if request.method == 'POST':
        newfile = JSONFile(file=request.FILES['file'])
        newfile.save()
        file=str(request.FILES['file'])
        if file.endswith('.json'):
            json_data = open('./media/'+file)
            data = json.load(json_data)  # deserialises it
            for i in data:
                if i['userId'] and i['id'] and i['title'] and i['body']:
                    JsonDetails.objects.create(
                        userId=i['userId'],
                        id=i['id'],
                        title=i['title'],
                        body=i['body']

                    )
            json_data.close()
            os.remove('./media/'+str(file))
            return redirect('usersdata')

    else:
         form = JSONFileForm()
         return render(request,"uploadtask/upload.html",{"form":form})

@login_required(login_url='login')
def getall(request):
    queryset = JsonDetails.objects.all()
    context = {
        'object_list': queryset
    }
    print(context)
    return render(request, "uploadtask/dashbord.html", context)
