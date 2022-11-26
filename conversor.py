from string import ascii_uppercase

def coletar_e_validar_input(mensagem, base=10):
    ''' Coleta o input e checa se é válido '''
    while True:
        inp = input(mensagem).replace(',','.').upper()
        if base > 10 and inp.count('.') <= 1:
            # Pode conter letras
            if inp.replace('.','').isalnum():
                return inp
        else:
            # Não pode conter letras
            if inp.replace('.','').isnumeric():
                return inp
        print('Número Inválido!')

def separar_inteiro_e_decimal(num: str):
    ''' 12.234 -> ([1,2], [2,3,4]) '''
    ponto_index = num.find('.')
    decimal = (False if ponto_index == -1 else True)
    chars_decimal = list()
    
    if decimal:
        chars_inteiro = list(num[:ponto_index])
        chars_decimal = list(num[ponto_index+1:])
    else:
        chars_inteiro = list(num)
    return (chars_inteiro, chars_decimal)

def contar_digitos(num: int):
    ''' Retorna quantidade de dígitos em um inteiro '''
    contagem = 0
    while num > 0:
        num //= 10
        contagem += 1
    return contagem
        
def x_para_decimal(base_origem: int, numero: str) -> int:
    ''' Retorna o número na base 10 '''
    
    chars_inteiro, chars_decimal = separar_inteiro_e_decimal(numero)
    resultado_inteiro, resultado_decimal = 0, 0
    
    ''' 
    1. Letra para Numero (A -> 10, B -> 11, C -> 13...)
    2. Computar Resultado
    '''
    
    # Parte Inteira
    for index, char in enumerate(chars_inteiro):
        if char.isalpha():
            chars_inteiro[index] = letras[char]    
    for index, num in enumerate(chars_inteiro):
        resultado_inteiro += base_origem ** index * int(num)
    
    # Parte Decimal
    if chars_decimal:
        for index, char in enumerate(chars_decimal):
            if char.isalpha():
                chars_decimal[index] = letras[char]
        for index, num in enumerate(chars_decimal):
            resultado_decimal += base_origem ** -(index + 1) * int(num)
    
    return resultado_inteiro + resultado_decimal

def decimal_para_x(base_destino, numero):
    ''' Retorna o decimal na base x '''

    chars_inteiro, chars_decimal = separar_inteiro_e_decimal(numero)
    inteiro = ''.join(chars_inteiro)
    decimal = ''.join(chars_decimal)

    resultado_inteiro, resultado_decimal = list(), list()
    
    if inteiro != '':
        inteiro = int(inteiro)
        while inteiro >= base_destino:
            resultado_inteiro.append( inteiro % base_destino )
            inteiro //= base_destino
        resultado_inteiro = ( resultado_inteiro + [inteiro] )[::-1]
    
    if decimal != '':
        decimal = float('.' + decimal)
        last_result = None
        while decimal != 0:
            decimal *= base_destino
            if decimal >= 1:
                if decimal == last_result:
                    break
                last_result = decimal
                resultado_decimal.append( int(decimal) )
                decimal = decimal - int(decimal)

    for resultado in (resultado_inteiro, resultado_decimal):
        for index, num in enumerate(resultado):
            if num >= 10:
                resultado[index] = numeros[num]
            else:
                resultado[index] = str(num)  
    
    if resultado_decimal:
        return ''.join(resultado_inteiro) + '.' + ''.join(resultado_decimal)
    return ''.join(resultado_inteiro)
        
# A: 10, B: 11, C: 12...
letras = {
    letra: ord(letra) - 55 for letra in ascii_uppercase
}

# 10: A, 11: B, 12: C...
numeros = {
    value:key for key, value in letras.items()
}

def main():
    base_origem = round( float(coletar_e_validar_input('Base de Origem: ')) )
    numero = coletar_e_validar_input('Número: ', base_origem )
    base_destino = round( float(coletar_e_validar_input('Base de Destino: ')) )

    if base_origem != 10:
        numero = x_para_decimal(base_origem, numero)

    print(decimal_para_x(base_destino, numero))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saindo...\n')
        exit()