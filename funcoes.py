# soma = 0
# def soma(a, b):
#     soma = a+b
#     return soma 

# banana = soma(2,10)
# print(banana)

# print(soma)


#                                           Função com *args
# def copa_do_mundo(pais, *anos):
#     print(f'País: {pais}' )

#     for year in anos:
#         print(f'Ano: {year}')

# copa_do_mundo('Brasil', '58', '62', '70', '94', '02')

# def copa_do_mundo(pais, **kargs):
#     sede = kargs.get('sede')
#     ano = kargs.get('ano')

#     if sede:
#         print(f'Sede: {sede}')
#     else:
#         print('n tem sede')

#     if ano:
#         print(f'Ano: {ano}')

#     print(pais)

# copa_do_mundo('Brasil', ano='62')