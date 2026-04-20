def calcular_custo_peca(gramas_argila, horas_forno):
    if gramas_argila <= 0:
        return 0
    
    # R$ 0,02 por grama + R$ 4,00 por hora de forno hipotético prpra ser mais fácil 
    return (gramas_argila * 0.02) + (horas_forno * 4.0)