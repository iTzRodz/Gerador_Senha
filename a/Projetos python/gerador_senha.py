import string
import secrets
senhas_geradas = []

tamanho_senha = int(input("Digite quantos caracteres você deseja em sua senha: "))
qnt_senha = int(input("Digite a quantidade de senhas que você quer gerar: "))
for k in range(qnt_senha): 
    alfabeto = string.ascii_letters + string.digits
    senha = ''.join(secrets.choice(alfabeto) for _ in range(tamanho_senha))
    senhas_geradas.append(senha)

print("_" * 30)
print("_" * 30)
print("Senhas geradas: ")

contador = 0 
i = 0
while contador < qnt_senha:
    i += 1
    print(f"\n{i} --->  {senhas_geradas[contador]}")
    contador += 1
    if contador == qnt_senha:
        print("_" * 20)
        if qnt_senha > 1:
            print(f"Programa finalizado!\nFoi gerada: {qnt_senha} senhas ao total.")
        else:
            print(f"Programa finalizado!\nFoi gerada: {qnt_senha} senha ao total.")