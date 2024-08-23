import numpy as np

Min = -10
Max = 10
Vetores = np.random.randint(Min, Max, 150).reshape(50, 3)

Dimensões = ["X", "Y", "Z"]

Parada = True

while (Parada == True):
    print ("Qual acão deseja tomar?")

    print ("========================================================================")

    print ("Pressione 1 para imprimir toda a matriz dos vetores.")
    print ("Pressione 2 para re-gerar a matriz dos vetores.")
    print ("Pressione 3 para imprimir uma linha específica da matriz dos vetores.")
    print ("Pressione 4 para alterar uma linha específica da matriz dos vetores.")
    print ("Pressione 5 para calcular a força resultante.")
    print ("Pressione 6 para calcular a aceleração do objeto.")
    print ("Pressione 0 para terminar o programa.")

    print ("========================================================================")

    escolha = int(input ())

    match escolha:
        case 0:
            Parada = False

        case 1:
            print ("Segue a Matriz com os valores dos vetores:\n")
            print(Vetores)

            print ("\n\n")

        case 2:
            
            print ("Deseja alterar o valor mínimo e máximo do randomizador?")

            if (int(input("Em caso positivo, digite 1\n")) == 1):
                Min = input("Qual o valor mínimo?\n")
                Max = input ("Qual o valor máximo?\n")

            Vetores = np.random.randint(Min, Max, 150).reshape(50, 3)
            print ("Segue a Matriz com os valores re-gerados dos vetores:\n")
            print(Vetores)      

            print ("\n\n")

        case 3:
            temp = int(input ("Insira a linha que deseja ver\n"))

            print ("\nLinha", temp, ":", Vetores[temp - 1], "\n\n")

        case 4:
            Linha = int(input ("Insira a linha que deseja alterar\n"))

            for i in range (3):
                print ("Insira o valor desejado para", Dimensões[i])
                Vetores [Linha - 1][i] = input ()

            

        case 5:
            #Axis = 0 faz com que a função sum some todos os numeros de cada coluna
            #Axis = 1 soma todos os numeros de cada linha
            ForçaResultante = np.sum(Vetores, axis = 0)
            
            print ("\nA força resultante é:")

            for i in range(3):
                print (Dimensões[i],"=", ForçaResultante[i], "N")

            print("\n\n")

        case 6:

            #Axis = 0 faz com que a função sum some todos os numeros de cada coluna
            #Axis = 1 soma todos os numeros de cada linha
            ForçaResultante = np.sum(Vetores, axis = 0)

            Massa = int(input ("\nQual a massa (em quilos) do objeto em questão?\n"))

            Aceleração = [0, 0, 0]

            for i in range (3):

                Aceleração [i] = (ForçaResultante[i] / Massa)

            print ("\nA aceleração deste objeto é:")
            
            for i in range(3):
                print (Dimensões[i], "=", np.array(Aceleração[i]), "m/s²")

            print("\n\n")
            

        case _:
            print ("\nValor inválido, insira novamente\n")