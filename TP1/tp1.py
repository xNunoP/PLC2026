import re

# A ER com âncoras para garantir a correspondência exata
er = r"^1*(0|01)*$"

# Lista com todos os casos de teste
testes = [
    "010101010",
    "0110011",
    "000000000",
    "110000000",
    "11111111010",
    "11110110000",
    "000000000001"
]

print("=== RESULTADOS DOS TESTES DE VALIDAÇÃO ===")
for t in testes:
    valido = bool(re.fullmatch(er, t))
    resultado = "ACEITE" if valido else "REJEITADO (Contém '011')"
    print(f"{t:<15} -> {resultado}")
