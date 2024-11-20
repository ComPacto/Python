<<<<<<< HEAD
import whois  # Importa o módulo python-whois

dominio = input('Digite o domínio: ')

try:
    # Consulta o whois do domínio
    resultado = whois.whois(dominio)

    # Mostra o resultado
    print(resultado)
except Exception as e:
    print(f'Ocorreu um erro: {e}')
=======
import whois # 👉️ Import whois module

dominio = input('Digite o domínio: ')

print(whois.whois(dominio))
>>>>>>> d090b9a51ca850f704ae22acb51c1c49921bfc2a
