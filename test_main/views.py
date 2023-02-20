from django.shortcuts import render


def main(request):
    return render(request, 'test_main/main.html')


def about(request):
    return render(request, 'test_main/about.html')


def activity(request):
    return render(request, 'test_main/activity.html')


def fot_con(request):
    return render(request, 'test_main/footer_contact.html')