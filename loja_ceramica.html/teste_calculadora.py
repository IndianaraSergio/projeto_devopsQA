from calculadora import calcular_ocusto_peca

def teste_valor_correto():
    # 500g e 2h de forno é pra dar exatamente 18.0
    assert calcular_ocusto_peca(500, 2) == 18.0

def teste_peso_vazio():
    assert calcular_ocusto_peca(0, 5) == 0