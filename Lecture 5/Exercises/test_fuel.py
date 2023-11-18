from fuel import convert, gauge

def teste_fuel():
    entrada = convert("1/2")
    assert entrada[2] == 0.5
    assert gauge(entrada[2]) == "E"

    # # Testa a entrada de uma fração com numerador e denominador iguais
    entrada = convert("1/1")
    assert gauge(entrada[2]) == "100%"