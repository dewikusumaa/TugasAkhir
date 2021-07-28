from supplier.forms import SupplierForm
from django.shortcuts import render, redirect

# Create your views here.
def AddProductKeluar(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("")
    context = {
        "form": form,
    }
    return render(request, 'supplier/form.html' , context)