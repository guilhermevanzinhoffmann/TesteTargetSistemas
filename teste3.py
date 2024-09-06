def mediana(vetor):
    primeiro = vetor[0]
    meio = vetor[len(vetor) // 2]
    ultimo = vetor[-1]
    return sorted([primeiro, meio, ultimo])[1]

def quicksort(vetor):
    if len(vetor) <= 1:
        return vetor
    else:
        pivo = mediana(vetor)
        menor = [x for x in vetor if x < pivo]
        igual = [x for x in vetor if x == pivo]
        maior = [x for x in vetor if x > pivo]
        return quicksort(menor) + igual + quicksort(maior)

def resultados(vetor):
    vetor_ordenado = quicksort(vetor)
    vetor_sem_zeros = [ x for x in vetor_ordenado if x > 0]

    media = sum(vetor_sem_zeros)/len(vetor_sem_zeros)
    indice = -1
    for i in vetor_sem_zeros:
        indice = indice + 1
        if(media < i):
            break

    menor_valor_faturamento = vetor_sem_zeros[0]
    maior_valor_faturamento = vetor_sem_zeros[-1]
    total_dias_valor_faturamento_maior_media_anual = len(vetor_sem_zeros) - indice
    print(f'O menor valor de faturamento ocorrido em um dia do ano é de : {menor_valor_faturamento} reais')
    print(f'O maior valor de faturamento ocorrido em um dia do ano é de : {maior_valor_faturamento} reais')
    print(f'Número de dias no ano em que o valor de faturamento diário foi superior à média anual : {total_dias_valor_faturamento_maior_media_anual} dia(s)')

vetor = [5,2,3,1,0,0,4,5,6,7,2,31, 2, 67, 89, 0, 32]
resultados(vetor)