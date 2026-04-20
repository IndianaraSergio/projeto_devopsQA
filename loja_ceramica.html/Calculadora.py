def calcular_custo_peca(gramas_argila, horas_forno):
    if gramas_argila <= 0:
        return 0
    
    # QA Inteligente: O forno não pode operar mais de 12h por segurança
    if horas_forno > 12:
        return "Erro: Limite de horas do forno excedido"
        
    return (gramas_argila * 0.02) + (horas_forno * 4.0)