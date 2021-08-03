from django.shortcuts import render, redirect, get_object_or_404
from .forms import SupplierForm
from .models import Supplier

# Create your views here.
def suppliers(request):
	suppliers = Supplier.objects.all()
	context = {
		"suppliers":suppliers
	}
	return render(request, 'supplier/suppliers.html', context) 

def deleteSupplier(request, id):
	instance = get_object_or_404(Supplier, id=id)
	instance.delete()
	#messages.success(request, "Successfully Deleted")
	return redirect("/supplier/list/")

def addSupplier(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("/supplier/list/")
    context = {
        "form": form,
    }
    return render(request, 'supplier/form.html', context)