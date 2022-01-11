from django.shortcuts import render

# Create your views here.
def handleAuth(request):
    code = request.GET.get('code', '')
    print(code)
    content = ''
    if code == '':
        content = ''
    else:
        content = 'KONEKSI BERHASIL'
    context = {'status': content}
    return render(request, 'authstrava.html', context)
    #Code to filter products whose price is less than price_lte i.e. 5000
