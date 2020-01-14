from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list": [
    {'restaurant_name': 'nino',
    'food_type': 'pasta',
    },
    {'restaurant_name': 'bf',
    'food_type': 'burger',
    },
    {'restaurant_name': 'pizzahut',
    'food_type': 'pizza',
    }]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object": {'restaurant_name': 'nino',
    'food_type': 'pasta',
    }

    }
    return render(request, 'detail.html', context)
