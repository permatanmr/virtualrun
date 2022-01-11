from django.shortcuts import render
import requests

# Create your views here.
def handleAuth(request):
    #mengambil dari url parameter yang dilempar oleh Strava Auth system
    code = request.GET.get('code', '')# <-- masukan ini ke DB untuk di simpen
    print('CINTA')
    print(code)
    #URL format https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&code=your_code_from_previous_step&grant_type=authorization_code
    url_strava = 'https://www.strava.com/oauth/token?client_id=75955&client_secret=f76ea9ae9e60bcaabf96145bf2c7ae0f3d08a134&code='+code+'&grant_type=authorization_code'
    x = requests.post(url_strava)
    print('AKU PADAMU')# <-- data response yang diperoleh dari Strava
    print(x.text)
    responses = x.json()
    access_token = responses['access_token']# <-- masukan ini ke DB untuk di simpen
    refresh_token = responses['refresh_token']# <-- masukan ini ke DB untuk di simpen
    print(access_token)

    #URL format https://www.strava.com/api/v3/athlete/activities?access_token=access_token_from_previous_step
    url_get_activities = 'https://www.strava.com/api/v3/athlete/activities?access_token='+access_token
    x = requests.get(url_get_activities)# <-- masukan ini ke DB untuk di simpen
    print('CINTAA LAGI')
    print(x.text)
    ## masukan ke DB
    content = ''
    if code == '':
        content = ''
    else:
        content = 'KONEKSI BERHASIL'
    context = {'status': content}
    return render(request, 'authstrava.html', context)
    #Code to filter products whose price is less than price_lte i.e. 5000
