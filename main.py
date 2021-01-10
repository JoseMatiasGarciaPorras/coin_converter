import conversor

if __name__ == '__main__':
    try:
        print('********** COIN CONVERTER **********')
        initial_coin = int(input('''
        Ingresa el índice de la moneda que quieres convertir: 
            [1] Dolar.
            [2] Euro.
            [3] Libra.
        Elección: '''))
        print('*******************************')
        final_coin = int(input('''
        Ingresa el índice de la moneda que quieres obtener:
            [1] Dolar.
            [2] Euro.
            [3] Libra.
        Elección: '''))
        print('*******************************')
        mount = int(input('Ingresa la cantidad a convertir: '))
        conversor.change(initial_coin, final_coin, mount)
    except:
        print('********** ERROR **********')
        print('Solo se admiten valores numéricos')
