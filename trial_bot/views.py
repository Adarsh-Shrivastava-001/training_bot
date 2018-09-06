import json
from django.shortcuts import render
from . models import Chats
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def train(request):
	return render(request,'./train.html')

@csrf_exempt
def save_conv(request):
	chat=Chats()
	if request.method=='POST':
		print(request)
		req=json.loads(request.body)
		print(req)
		chat.que=req['que']
		chat.pro_ans=req['pro_ans']
		chat.sug_ans=req['sug_ans']
		if req['user']!="":
			chat.name=req['user']
		else:
			chat.name="anonymous"

		chat.save()

		print("success")
		return JsonResponse({
			'status': 'success',
			'msg': 'recieved the 3 things'
		})



def analyse(request):
	chat=Chats.objects.all()
	sug_chats=[]
	unsug_chats=[]
	for i in chat:
		if i.sug_ans=="":
			unsug_chats.append(i)
		else:
			sug_chats.append(i)

	if not request.POST._mutable:
   		request.POST._mutable = True

	context={'sug_chats':sug_chats,'unsug_chats':unsug_chats,'nsug_chats':len(sug_chats),'nunsug_chats':len(unsug_chats),
	'pnsug_chats':(len(unsug_chats)*100/len(chat)),'psug_chats':(len(sug_chats)*100/len(chat))
	}
	print(context)
	return render(request,"analyse.html",context)