#Exercício 1 Programa para verificação se um número pertence a sequência de Fibonacci

def fibonacci(n):
    a,b = 0,1
    while b < n:
        a,b = b, a + b
    return b == n

numero = int(input("Digite um número: \n"))
if fibonacci(numero):
    print("o número pertence a sequência de Fibonacci!\n")
else:
    print("O número não pertence a sequência de Fibonacci.\n")



# Exercício 2 Programa para verificar a presença e frequência da letra 'a' em um texto, mesmo se for em letra maiúscula.
def verificar_a(string):
    string = string.lower()
    count_a = string.count("a")
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vezes.\n")
    else:
        print("A letra 'a' não foi encontrada.\n")
    
texto = input("Digite uma palavra ou frase: \n")
verificar_a(texto)

# Exercício 3
INDICE = 12
SOMA = 0
K = 1
while K<INDICE:
    K = K+1
    SOMA = SOMA+K
print(SOMA)

#Exercício 4
""""
4) Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___ -> 9
b) 2, 4, 8, 16, 32, 64, ____ -> 128
c) 0, 1, 4, 9, 16, 25, 36, ____ -> 49
d) 4, 16, 36, 64, ____ -> 100
e) 1, 1, 2, 3, 5, 8, ____ -> 13
f) 2,10, 12, 16, 17, 18, 19, ____ -> 200
"""


#Exercício 5
""""
Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, 
mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir,
usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

Resposta:
Supondo que a lâmpada esquentaria ao ficar alguns minutos acesa, na primeira ida, ligaria qualquer um dos interrupotores e esperaria um pouco para dar tempo de aquecer 
Desligaria o interrputor e ligaria outro, ao voltar para a sala de lâmpadas, teria uma lâmpada acesa, correspondendo ao segundo interrputor, uma lâmmpada apagada, mas quente,
correspondendo ao primeiro interruptor. E também teria uma lâmpada apagada e fria, que corresponderia ao terceiro interruptor.
"""