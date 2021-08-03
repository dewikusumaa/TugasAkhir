from django.db.models.expressions import F
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User

# Create your views here.
def createUser(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/user/daftar/")
    context = {
        "form": form,
    }
    return render(request, 'user/form.html', context)


def users(request):
    users = User.objects.all()
    context = {
        "users": users, 
    }
    return render(request, 'user/users.html', context)


def updateUser(request, id):
	instance = get_object_or_404(User, id=id)
	form = UserForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("/user/daftar" )
	context = {
		"instance": instance,
		"form": form,
	}
	return render(request, 'user/form.html', context)


def deleteUser(request, id):
	instance = get_object_or_404(User, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/user/daftar")