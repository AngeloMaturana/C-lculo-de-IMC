def calculo_de_imc_Lambert(p, a):
    '''
    Fórmula que mostra o IMC (índice de massa corporal) da pessoa,
    que é igual ao peso dela dividivo pela altura ao quadrado
    O round( ) é apenas para delimitar o número de casas decimais do imc, mostrando apenas 1.
    '''
    return round(p / pow(a, 2), 1)


def calculo_de_imc_Nick(p, a):
    '''
     Essa fórmula é quase igual à primeira, porém multiplica-se o valor do peso com um valor
     constante (1.3), e a altura é elevada à 2.5 em vez de 2
    '''
    return round(1.3 * p / pow(a, 2.5), 1)


def classificacao_do_peso(imc):
    '''
    Função de simplemente compara o valor do imc com outros valores
    e retorna diferentes respostas para cada valor
    '''
    if imc < 18.5:
        return 'Magreza'
    elif 18.5 <= imc <= 24.9:
        return 'peso Normal'
    elif 25 <= imc <= 29.9:
        return 'Sobrepeso'
    elif 30 <= imc <= 34.9:
        return 'Obesidade de grau I'
    elif 35 <= imc <= 39.9:
        return 'Obesidade de grau II'
    elif imc > 40:
        return 'Obesidade de grau III'


def main():

    '''
    Criação das variáveis que recebem valores digitados
    pelo usuário e esses valores são convertidos em float
    '''
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

    '''
    Criação das variáveis que recebem e guardam os valores das funções
    com os parâmetros peso e altura
    '''
    resultado_do_imc_Lambert = calculo_de_imc_Lambert(peso, altura)
    resultado_do_imc_Nick = calculo_de_imc_Nick(peso, altura)

    '''
    Criação das variáveis que recebem e guardam o valor da função que 
    recebe como parâmetro o valor do imc
    '''
    tipo_de_peso_lambert = classificacao_do_peso(resultado_do_imc_Lambert)
    tipo_de_peso_Nick = classificacao_do_peso(resultado_do_imc_Nick)

    '''
    Aqui apenas mostra na tela todos os resultados
    '''
    print(f"\nSeu IMC com a fórmula de Lambert é de {resultado_do_imc_Lambert}.")
    print(f"De acordo com o cálculo, você está com {tipo_de_peso_lambert}")

    print(f"Seu IMC com a fórmula de Nick é de {resultado_do_imc_Nick}.")
    print(f"De acordo com o cálculo, você está com {tipo_de_peso_Nick}")


if __name__ == '__main__':
    main()
