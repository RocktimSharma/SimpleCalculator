from django.shortcuts import render
from .forms import *

def home(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            first_number = form.cleaned_data["firstNumber"]
            second_number = form.cleaned_data["secondNumber"]
            operation = form.cleaned_data["operation"]
            if operation == '+':
                return render(request, 'index.html', context={'form': form, 'result': (first_number + second_number)})
            elif operation == '-':
                return render(request, 'index.html', context={'form': form, 'result': (first_number - second_number)})
            elif operation == 'x':
                return render(request, 'index.html', context={'form': form, 'result': (first_number * second_number)})
            else:
                return render(request, 'index.html', context={'form': form, 'result': (first_number / second_number)})

    else:
        form = CalculatorForm()
        return render(request, 'index.html', context={'form': form, 'result': ''})
