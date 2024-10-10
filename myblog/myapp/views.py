from django.shortcuts import render


def home_screen(request):
    print(request.headers)


    context = {
        "some_string": "This is some string 2",
    }


    return render(request, 'personal/home.html', context)
