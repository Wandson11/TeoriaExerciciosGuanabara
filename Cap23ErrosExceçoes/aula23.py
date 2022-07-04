try:
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
#except:
    #print('Infelizmente tivemos problemas :(')

else:
    print(f'O valor da divisão foi de {r}')

finally:
    print('Volte sempre')