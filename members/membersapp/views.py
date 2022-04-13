from urllib import request
# from xml.dom.minidom import Identified
from django.shortcuts import render, redirect
# from .forms import  PostForm 
from .models import member

# Create your views here.


def index(request):  #新增資料，資料不作驗證
	# form = PostForm()
	if request.method == "POST"	: #如果是以POST方式才處理
		Name = request.POST['Name'] #取得表單輸入資料
		Sex =  request.POST['Sex']
		Birthday =  request.POST['Birthday']
		Email = request.POST['Email']
		Phone =  request.POST['Phone']
		Addr =  request.POST['Addr']
        #新增一筆記錄
		unit = member.objects.create(Name=Name, Sex=Sex, Birthday=Birthday, Email=Email,Phone=Phone, Addr=Addr) 
		unit.save()  #寫入資料庫
		return redirect('/index/')	
	# context = { 
    #     'form':form 
    # }    
	members = member.objects.all().order_by('id')
	return render(request, "members/index.html", locals())
	# return render(request, "members/index1.html", context)	


# def edit(request,id):
# 	members = member.objects.get(id=id)
# 	form = PostForm()
# 	if request.method == 'POST':
# 		form = PostForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('/index/')
# 	context = {
		
#         'form': form
#     }
# 	return render(request, 'members/edit.html', context)


def edit(request,id=None,mode=None):  
	if mode == "edit":  # 由 edit.html 按 submit
		unit = member.objects.get(id=id)  #取得要修改的資料記錄	
		unit.Name=request.GET['Name']
		unit.Sex=request.GET['Sex']
		unit.Birthday=request.GET['Birthday']
		unit.Email=request.GET['Email']
		unit.Phone=request.GET['Phone']
		unit.Addr=request.GET['Addr']		
		unit.save()  #寫入資料庫
		return redirect('/index/')	
	else: 
		try:
			unit = member.objects.get(id=id)  #取得要修改的資料記錄
			strdate=str(unit.Birthday)
			strdate2=strdate.replace("年","-")
			strdate2=strdate.replace("月","-")
			strdate2=strdate.replace("日","-")
			unit.Birthday = strdate2
		except:
			message = "此id不存在"
		return render(request, "members/edit.html", locals())


def delete(request,id=None):  #刪除資料
	members  = member.objects.get(id=id)
	if request.method == "POST":  #如果是以POST方式才處理
		members.delete()
		return redirect('/index')
	context = {
		'member':member ,
	}	
	return render(request, "members/delete.html", context)	

# def delete(request,id=None):  #刪除資料
# 	if id!=None:
# 		if request.method == "POST":  #如果是以POST方式才處理
# 			id=request.POST['Id'] #取得表單輸入的編號
# 		try:
# 			unit = member.objects.get(id=id)  
# 			unit.delete()
# 			return redirect('/index/')
# 		except:
# 			message = "讀取錯誤!"			
# 	return render(request, "members/delete.html", locals())	



		





#