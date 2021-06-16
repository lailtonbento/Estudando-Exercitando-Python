real = float(input('Quanto você tem na carteira em R$ ? '))
dolar = real / 5.04
eur = real / 6.11
libra = real / 7.12
rublo = real / 0.70
pesoargentino = real / 0.053
dolaraustraliano = real / 3.89
francosuiço = real / 5.61
yuanschineses = real / 0.79
print('Com R${:.2f} você pode comprar: \nUS$ {:.2f}\nEUR$ {:.2f}\n£$ {:.2f}\nRUB {:.2f}\nARS$ {:.2f}\nAUD$ {:.2f}\nCHF$ {:.2f}\nCNY$ {:.2f} '.format(real, dolar, eur, libra, rublo, pesoargentino, dolaraustraliano, francosuiço, yuanschineses))



