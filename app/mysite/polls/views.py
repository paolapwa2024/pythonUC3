from django.shortcuts import render

def index(request):
    mensagem = ""
    if request.method == "POST":
        idade = int(request.POST.get("idade", 0))
        if idade >= 18:
            mensagem = f"Acesso liberado! Você tem {idade} anos."
        else:
            mensagem = f"Acesso negado. Você tem {idade} anos."
    return render(request, "polls/index.html", {"mensagem": mensagem})