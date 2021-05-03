from django.shortcuts import render


def profile_detail_view(request, username, *args, **kwargs):
    return render(request, "profiles/details.html", {"username": username})



