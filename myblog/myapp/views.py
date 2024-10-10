from django.shortcuts import render


def home_screen(request):
    print(request.headers)
    context = {}
    list_var = []
    list_var.append("Value 1")
    list_var.append("Value 2")
    list_var.append("Value 3")
    context["list_var"] = list_var


    return render(request, 'personal/home.html', context)
