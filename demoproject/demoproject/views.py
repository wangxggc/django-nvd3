from django.shortcuts import render_to_response


def home(request):
    """
    Home page
    """
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]

    return render_to_response('home.html',
                              {'test': 1, xdata: xdata, ydata: ydata})
