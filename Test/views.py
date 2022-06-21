from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import StringForm
# Create your views here.
def String_Find(request):

    form=StringForm(request.POST)
    if request.method =='POST':

        #Getting Values From Form
        ##############################################################################################
        master_string=request.POST.get('Master_String')
        string1=request.POST.get('String1')
        string2=request.POST.get('String2')
        string3=request.POST.get('String3')
        string4=request.POST.get('String4')

        #To Convert String Into List
        ##############################################################################################

        master_list=list(master_string)
        string1_list=list(string1)
        string2_list=list(string2)
        string3_list=list(string3)
        string4_list=list(string4)

        #To Count Characters Of Each Sub String Using Count Variables
        ###############################################################################################

        string1_count=0
        string2_count=0
        string3_count=0
        string4_count=0
       
        if form.is_valid():

            #Input String1 Operation
            ###########################################################################################

            for i in string1_list:
                if i in master_list:
                    master_list.remove(i)
                    string1_count=string1_count+1
            if string1_count<len(string1_list):
                string1_status='No'
                print(string1_status)
            else:
                string1_status='Yes'
                print(string1_status)
           
           #Input String2 Operation
            ###########################################################################################

            for i in string2_list:
                if i in master_list:
                    master_list.remove(i)
                    string2_count=string2_count+1
            if string2_count<len(string2_list):
                string2_status='No'
                print(string2_status)
            else:
                string2_status="Yes"
                print(string2_status)

            #Input String3 Operation
            ###########################################################################################

            for i in string3_list:
                if i in master_list:
                    master_list.remove(i)
                    string3_count=string3_count+1
            if string3_count<len(string3_list):
                string3_status="No"
                print(string3_status)
            else:
                string3_status="Yes"
                print(string3_status)

            #Input String4 Operation
            ###########################################################################################

            for i in string4_list:
                if i in master_list:
                    master_list.remove(i)
                    string4_count=string4_count+1
            if string4_count<len(string4_list):
                string4_status="No"
                print(string4_status)
            else:
                string4_status="Yes"
                print(string4_status)
           
            
            form.save()
            
            return HttpResponse(string1 +':' + string1_status + "<br>"+string2 + ':'+string2_status +"<br>"+string3 + ':'+ string3_status +"<br>"+string4+':'+string4_status)

    return render(request,'form.html',{'form':form})
