import datetime

def year(request):
    request = datetime.datetime.today()
    year = request.year
    print (year)
    return {
        'year': request.year
    }
