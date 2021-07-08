from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='customer')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			Customer.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

	context = {'form':form}
	return render(request, 'register.html', context)