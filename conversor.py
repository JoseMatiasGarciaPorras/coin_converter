''' pesos = input('¿Cuántos pesos colombianos tienes? ')
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos/valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print('Tienes {}$'.format(dolares)) '''


def change(coin1, coin2, mount):
    result = 0
    if coin1 == 1 and coin2 == 1:
        result = mount * 1
        print('{} dolares equivalen a {} dolares'.format(mount, result))
    elif coin1 == 1 and coin2 == 2:
        result = mount * 0.82
        print('{} dolares equivalen a {} euros'.format(mount, result))
    elif coin1 == 1 and coin2 == 3:
        result = mount * 0.74
        print('{} dolares equivalen a {} libras'.format(mount, result))
    elif coin1 == 2 and coin2 == 1:
        result = mount * 1.22
        print('{} euros equivalen a {} dolares'.format(mount, result))
    elif coin1 == 2 and coin2 == 2:
        result = mount * 1
        print('{} euros equivalen a {} euros'.format(mount, result))
    elif coin1 == 2 and coin2 == 3:
        result = mount * 0.90
        print('{} euros equivalen a {} libras'.format(mount, result))
    elif coin1 == 3 and coin2 == 1:
        result = mount * 1.36
        print('{} libras equivalen a {} dolares'.format(mount, result))
    elif coin1 == 3 and coin2 == 2:
        result = mount * 1.11
        print('{} libras equivalen a {} euros'.format(mount, result))
    elif coin1 == 3 and coin2 == 3:
        result = mount * 1
        print('{} libras equivalen a {} libras'.format(mount, result))
    else:
        print('Solo se admiten los valores prefijados')





