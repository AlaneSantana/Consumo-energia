# Entrada 
aparelho_eletronico = input("Digite o nome do aparelho: ") 
potencia = float(input("Digite a potência em watts(W): ")) 
horasDia = float(input("Digite o tempo médio de uso em horas: ")) 

# Processamento 
consumoMensal = (potencia*horasDia*30)/1000

#Saída
print(f"Consumo estimado: KWh {consumoMensal:.2f}")