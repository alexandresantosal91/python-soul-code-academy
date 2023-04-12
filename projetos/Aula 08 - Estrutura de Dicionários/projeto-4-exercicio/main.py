diasDaSemana = {"Dia1":"Segunda-Feira", "Dia2":"Terca-Feira", "Dia3":"Quarta-Feira", "Dia4":"Quinta-Feira", "Dia5":"Sexta-Feira", "Dia6":"Sabado", "Dia7":"Domingo"}

diasDaSemana.popitem()
diasDaSemana.popitem()

del(diasDaSemana["Dia1"])

print(diasDaSemana.keys())
print(diasDaSemana.values())

print(diasDaSemana)