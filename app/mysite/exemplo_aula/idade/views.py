from django.shortcuts import render

def home(request):
    mensagem =""
    conteudo = False

    if request.method == "POST":
        idade = int(request.POST.get("idade"))

    if idade >= 18:
        conteudo = True
    else:
        mensagem = "Você não é maior de idade."

    
    return render(
        request, 'index.html', {'mensagem': mensagem, 'conteudo': conteudo})