# Teste Target Sistemas
## Respostas
### 1:  
O valor da variável SOMA será 77  
### 2:  
a) 9  
b) 128  
c) 64  
d) 10000  
e) 13  
f) 200  
### 3:
A resposta está no arquivo ['teste3.py'](./teste3.py)  
### 4:
A resposta está no arquivo 'teste4.txt'
### 5:  
Para resolver podemos calcular a distância percorrida por cada veículo até o momento em que ambos se encontram e   
depois disso comparar a distância com a distância total entre as cidades. 
Usando a equação D = VxT, onde   
D é distância,  
V é velocidade,  
T é tempo  
e assumindo que os veículos irão se encontrar depois de T horas, temos então   
1 -> D(carro) = 90xT   
2 -> D(caminhão) = 80xT  
Não podemos esquecer que existem pedágios e, assumindo que o carro já passou por 3 pedágios   
tempo gasto nos pedagios TP = 3 x 15 minutos = 3 x (15 minutos/ 60 minutos) = 0,25 horas  
Assumindo que a velocidade média do carro é de 90km/h em uma aceleração constante e que o carro vai perder 0,25 horas nos pedágios, 
então precisamos incluir o tempo gasto nos pedágios ao tempo total que o carro vai demorar para percorrer todo o trajeto  
tempo total gasto pelo carro = 125/90 = 1,39 Horas  
Acrescentando 0,25 horas ao tempo total do trajeto, temos  
velocidade média = 125/(1,39 + 0,25) = 76,22 km/h  
Como a soma das distâncias percorridas por cada um dos veículos é igual à distância total entre as duas cidades, podemos concluir que  
76,22xT + 80xT = 125 km  
156,22T = 125 km  
T = 125/156,22  
T = 0,709 horas  
T é o tempo que os veículos vão demorar para se encontrar.  
Sabendo agora o tempo em que o encontro vai ocorrer, substituimos T em 1 e 2 por 0,709:  
1 -> D(carro) = 76,22x0,709 = 54,04 km  
2 -> D(caminhão) = 80x0,709 = 56,72 km  
Assumindo que o carro partiu de Ribeirão Preto e o caminhão partiu de Barretos, podemos concluir que  
O carro está a 54,04km de Ribeirão Preto  
O caminhão está a 56,72km de Barretos   
Sabendo que o carro saiu de Ribeirão Preto e o carro terá percorrido 54,04km até encontrar o caminhão e o caminhão,  
saindo de Barretos, terá percorrido 56,72km até encontrar o carro e sabendo também que a distância entre as cidades é de 125km então  
podemos concluir que faltam 125km - 56,72 km para o caminhão chegar até Ribeirão Preto, o que resulta em 68,28 km.  
Como 68,28 km é maior que 54,04 km, podemos concluir que o carro está mais perto de Ribeirão Preto no momento em que ambos os veículos se cruzarem.



