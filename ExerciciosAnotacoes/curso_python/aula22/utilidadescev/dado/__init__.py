def leiaDinheiro(msg):
    """
    Função que valida a entrada de um valor monetário.
    :param msg: Mensagem a ser exibida ao usuário.
    :return: Retorna o valor monetário como float.
    """
    while True:
        valor = input(msg).strip().replace(',', '.')
        if valor.replace('.', '').isdigit():
            return float(valor)
        else:
            print(f'\033[0;31mERRO: "{valor}" é um preço inválido!\033[m')