from django.shortcuts import render


def blog(request):
    print('Blog')
    return render(
        request,
        'blog.html'
    )


def exemplo(request):
    print('Blog')
    return render(
        request,
        'exemplo.html'
    )
