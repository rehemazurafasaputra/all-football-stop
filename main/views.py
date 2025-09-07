from django.shortcuts import render

def show_main(request):
    context =  {
        'npm': "2406432072",
        'nama': "Rehema Zurafa Saputra"
    }
    return render(request,"main.html",context)


