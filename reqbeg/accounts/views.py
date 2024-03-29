from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
def signuppage(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('persons:abf')
	else:		
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})
def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			return redirect('persons:abf')
	else:
		form = AuthenticationForm()
		return render(request,'accounts/login.html', {'form':form})	
# Create your views here.
def logoutpage(request):
	logout(request)
	return redirect('persons:abf')