import numpy as np
import sympy as sp
import logging
logging.basicConfig (level=logging.INFO, filename="Log_Derivada.log", format="%(asctime)s - %(levelname)s - %(message)s")


# Definindo a variável
x = sp.symbols('x')

# Definindo a função que você deseja derivar

#indica o maior n para indicar o grau da função
Grau = int(input ("Informe qual o valor mais alto da exponenciação: "))

Função = []
f = 0

for i in range(Grau + 1):
    Função.append(float(input (f"insira a constante que multiplica x**{Grau - i}: ")))
    logging.info(f"Constante inserido para x^{i}: {Função[i]}")
    f += Função[i]*(x**(Grau - i))
    logging.info("f(x) atualmente:")
    logging.info(f)


# Calculando a derivada
derivada = sp.diff(f, x)
logging.info(derivada)

# Exibindo o resultado
print(f"A derivada de {f} em relação a x é: {derivada}")




