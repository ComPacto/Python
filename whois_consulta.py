import whois  # Importa o módulo python-whois

dominio = input('Digite o domínio: ')

try:
    # Consulta o whois do domínio
    resultado = whois.whois(dominio)

    # Mostra o resultado
    print(resultado)
except Exception as e:
    print(f'Ocorreu um erro: {e}')
teste = 0