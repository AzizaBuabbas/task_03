from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	"my_list": [ 
    	#restaurant_name1
    	{

    	"restaurant_name" : "Pizza hut",
    	"food_type" : "Pizza"


    	},
    	#restaurant_name2
    	{

    	"restaurant_name" : "Manhattan Burger",
    	"food_type" : "Burger"
    	}, 
    	 #restaurant_name3 
    	 {

    	 "restaurant_name" : "Shrimpy",
    	 "food_type" : "see food"

    	 }

    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":
    { 

    "restaurant_name" : "Pizza hut",
    	"food_type" : "Pizza"

    }



    }
    return render(request, 'detail.html', context)
