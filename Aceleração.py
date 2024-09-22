import numpy as np
import logging

logging.basicConfig (level=logging.INFO, filename="Log_Aceleracao.log", format="%(asctime)s - %(levelname)s - %(message)s")

#Min e Max são os valores em que vai variar a randomização de X, Y e Z dos vetores

Min = -10
Max = 10

#Quantidade é a quantidade desejada de vetores

Quantidade = 50

Vetores = np.random.randint(Min, Max, (Quantidade * 3)).reshape(Quantidade, 3)

logging.info(f"Quantidade de vetores gerados {Quantidade}")
logging.info("Vetores gerados:")
logging.info(Vetores)

Dimensões = ["X", "Y", "Z"]

Parada = True

while (Parada == True):
    print ("Qual acão deseja tomar?")

    print ("========================================================================")

    print ("Pressione 1 para imprimir toda a matriz dos vetores.")
    print ("Pressione 2 para re-gerar a matriz dos vetores.")
    print ("Pressione 3 para imprimir uma linha específica da matriz dos vetores.")
    print ("Pressione 4 para alterar manualmente uma linha específica da matriz dos vetores.")
    print ("Pressione 5 para calcular a força resultante.")
    print ("Pressione 6 para calcular a aceleração do objeto.")
    print ("Pressione 0 para terminar o programa.")

    print ("========================================================================")

    escolha = int(input ())

    logging.info(f"escolha tomada: {escolha}")

    match escolha:
        case 0:
            Parada = False
            logging.info("Programa encerrado")            

        case 1:
            print ("Segue a Matriz com os valores dos vetores:\n")
            print(Vetores)

            logging.info("Vetores atuais:")
            logging.info(Vetores)

            print ("\n\n")
    
        case 2:
            
            print ("Deseja alterar o valor mínimo e máximo do randomizador?")

            if (int(input("Em caso positivo, digite 1\n")) == 1):
                Min = input("Qual o valor mínimo?\n")
                Max = input ("Qual o valor máximo?\n")

            Vetores = np.random.randint(Min, Max, (Quantidade * 3)).reshape((Quantidade), 3)
            print ("Segue a Matriz com os valores re-gerados dos vetores:\n")
            print(Vetores)      

            print ("\n\n")

            logging.info (f"Valor atual de randomização:\n Min: {Min}\n Max: {Max}")
            logging.info ("Vetores atuais:")
            logging.info (Vetores)

        case 3:
            temp = int(input ("Insira a linha que deseja ver\n"))

            print ("\nLinha", temp, ":", Vetores[temp - 1], "\n\n")

            logging.info (f"Linha solicitada: {temp}")
            logging.info (f"Linha visualizada: {Vetores[temp - 1]}")

        case 4:
            Linha = int(input ("Insira a linha que deseja alterar\n"))

            for i in range (3):
                print ("Insira o valor desejado para", Dimensões[i])
                Vetores [Linha - 1][i] = input ()

            logging.info (f"Linha alterada: {temp}")
            logging.info (f"Nova linha: {Vetores[temp - 1]}")

            
        case 5:
            #Axis = 0 faz com que a função sum some todos os numeros de cada coluna
            #Axis = 1 soma todos os numeros de cada linha
            ForçaResultante = np.sum(Vetores, axis = 0)
            
            print ("\nA força resultante é:")

            for i in range(3):
                print (Dimensões[i],"=", ForçaResultante[i], "N")
                logging.info(f"Força Resultante {Dimensões [i]}: {ForçaResultante[i]}")

            print("\n\n")

            

        case 6:

            #Axis = 0 faz com que a função sum some todos os numeros de cada coluna
            #Axis = 1 soma todos os numeros de cada linha
            ForçaResultante = np.sum(Vetores, axis = 0)

            Massa = int(input ("\nQual a massa (em quilos) do objeto em questão?\n"))

            while (Massa <= 0):
                logging.warning(f"{Massa} não é um valor válido como massa")
                Massa = int(input("ERRO: Forneça um valor de massa válido: "))


            logging.info (f"Massa fornecida: {Massa}")

            Aceleração = [0, 0, 0]

            for i in range (3):

                Aceleração [i] = (ForçaResultante[i] / Massa)

            print ("\nA aceleração deste objeto é:")
            
            for i in range(3):
                print (Dimensões[i], "=", np.array(Aceleração[i]), "m/s²")
                logging.info (f"{Dimensões[i]} = {np.array(Aceleração[i])} m/s²")

            print("\n\n")
            
        case _:
            print ("\nValor inválido, insira novamente\n")
            logging.warning ("Valor inválido inserido")