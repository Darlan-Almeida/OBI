while(True):    
    n = int(input())
    computadores = []
    precos = []
    qualidades = []

    i = 0

    for i in range(n): 
        computador = list(map(int, input().split()))
        [computadores.append(s) for s in computador]

    splited = []
    len_l = len(computadores)
    for i in range(n):
        start = int(i*len_l/n)
        end = int((i+1)*len_l/n)
        splited.append(computadores[start:end])
        preco = splited[i][0]
        qualidade = splited[i][1]
        qualidades.append(qualidade)
        precos.append(preco)

        menor_preco = min(precos)
        menor_pos = precos.index(menor_preco)
        maior_qualidade = max(qualidades)
        maior_pos = qualidades.index(maior_qualidade)




    if(menor_pos == maior_pos):
        print("YES")
        break

    else:
        print("NO")
        break



