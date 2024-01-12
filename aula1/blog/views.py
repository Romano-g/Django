from django.shortcuts import render


def blog(request):
    print('Blog')
    return render(
        request,
        'blog/index.html'
    )


def exemplo(request):
    print('Blog')
    return render(
        request,
        'blog/example.html'
    )
