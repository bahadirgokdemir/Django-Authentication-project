from django.shortcuts import render
from django.conf import settings
import psycopg2  
from django.contrib.auth.models import User

def kullanici_listesi(request):
    kullanicilar = User.objects.all()
    return render(request, 'adminpage/list.html', {'user_list': kullanicilar})



def get_data_view(request):
    db_settings = settings.DATABASES['default']

    connection = psycopg2.connect(
        database=db_settings['NAME'], 
        user=db_settings['USER'],
        password=db_settings['PASSWORD'],
        host=db_settings['HOST'],
        port=db_settings['PORT']
    )

    cursor = connection.cursor()
    cursor.execute("SELECT username, first_name, last_name, email, date_joined, last_login FROM auth_user")
    
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return render(request, 'adminpage/userlist.html', {'results': results})

