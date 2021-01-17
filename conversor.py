# ''' pesos = input('¿Cuántos pesos colombianos tienes? ')
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos/valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print('Tienes {}$'.format(dolares)) '''


def operation(mount, valor):
    result = 0
    result = mount * valor
    return result

def change(coin1, coin2, mount):
    if coin1 == 1 and coin2 == 1:
        valor = 1
        print('{} dolares equivalen a {} dolares'.format(mount, operation(mount, valor)))
    elif coin1 == 1 and coin2 == 2:
        valor = 0.82
        print('{} dolares equivalen a {} euros'.format(mount, operation(mount, valor)))
    elif coin1 == 1 and coin2 == 3:
        valor = 0.74
        print('{} dolares equivalen a {} libras'.format(mount, operation(mount, valor)))
    elif coin1 == 2 and coin2 == 1:
        valor = 1.22
        print('{} euros equivalen a {} dolares'.format(mount, operation(mount, valor)))
    elif coin1 == 2 and coin2 == 2:
        valor = 1
        print('{} euros equivalen a {} euros'.format(mount, operation(mount, valor)))
    elif coin1 == 2 and coin2 == 3:
        valor = 0.90
        print('{} euros equivalen a {} libras'.format(mount, operation(mount, valor)))
    elif coin1 == 3 and coin2 == 1:
        valor = 1.36
        print('{} libras equivalen a {} dolares'.format(mount, operation(mount, valor)))
    elif coin1 == 3 and coin2 == 2:
        valor = 1.11
        print('{} libras equivalen a {} euros'.format(mount, operation(mount, valor)))
    elif coin1 == 3 and coin2 == 3:
        valor = 1
        print('{} libras equivalen a {} libras'.format(mount, operation(mount, valor)))
    else:
        print('Solo se admiten los valores prefijados')





