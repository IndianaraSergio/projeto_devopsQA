from calculadora import calcular_ocusto_peca

def test_valor_correto():
    # 500g e 2h de forno é pra dar exatamente 18.0
        assert calcular_ocusto_peca(500, 2) == 18.0

def test_peso_vazio():
        assert calcular_ocusto_peca(0, 5) == 0
    # Garantindo que o cálculo de QA está batendo com a regra 
def test_limite_forno():
    # testando se o sistema barra quando pass de 12 horas
        assert calcular_custo_peca(100, 13) == "Erro: Limite de horas do forno excedido"