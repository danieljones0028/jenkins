age = input("Entre com sua idade: ")
age = int(age)
se_tem_carro = input("Voce e maior de 21 e possui carro? (y/n): ")

if (age > 21) and (se_tem_carro == 'y'):
    print ("vc e maior de 21 e tem carro")

if (age > 21) and (se_tem_carro == 'n'):
    print ("vc nao e maior de 21 e nao tem carro")

if (age == 21) and (se_tem_carro == 'y'):
        print ("vc tem 21 e tem carro")

if (age == 21) and (se_tem_carro == 'n'):
        print ("vc tem 21 e nao tem carro")

if (age < 21) and (se_tem_carro == 'y'):
        print ("vc e menor de 21 e tem carro")

if (age < 21) and (se_tem_carro == 'n'):
        print ("vc nao e menor de 21 e nao tem carro")
