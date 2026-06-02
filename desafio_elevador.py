def calcular_elevador(chamadas, estrategia="chegada"):
    andar_atual = 0
    tempo_total = 0
    deslocamento_total = 0
    ordem_atendimento = []
    
    chamadas_pendentes = chamadas.copy()
    
    while chamadas_pendentes:
        if estrategia == "mais_proximo":
            # ESTRATÉGIA B: Olha só para quem está esperando mais perto
            proxima_chamada = min(chamadas_pendentes, key=lambda c: abs(c[0] - andar_atual))
            
        elif estrategia == "menor_deslocamento":
            # ESTRATÉGIA C: Olha para o custo da viagem inteira (ir buscar + levar)
            proxima_chamada = min(chamadas_pendentes, key=lambda c: abs(c[0] - andar_atual) + abs(c[1] - c[0]))
            
        else:
            # ESTRATÉGIA A: Ordem de chegada
            proxima_chamada = chamadas_pendentes[0]
            
        origem, destino = proxima_chamada
        
        # Cálculos de tempo e distância
        distancia_vazia = abs(origem - andar_atual)
        tempo_vazio = distancia_vazia * 3
        
        distancia_cheia = abs(destino - origem)
        tempo_cheio = distancia_cheia * 3
        
        tempo_portas = 10 
        
        # Atualiza métricas
        deslocamento_total += (distancia_vazia + distancia_cheia)
        tempo_total += (tempo_vazio + tempo_cheio + tempo_portas)
        
        # Atualiza o estado
        andar_atual = destino
        ordem_atendimento.append(proxima_chamada)
        chamadas_pendentes.remove(proxima_chamada)

    return ordem_atendimento, tempo_total, deslocamento_total

# --- Entradas ---
chamadas_entrada = [(0,4), (2,1), (3,0), (4,2)]

# --- Execução ---
ordem_A, t_A, d_A = calcular_elevador(chamadas_entrada, "chegada")
ordem_B, t_B, d_B = calcular_elevador(chamadas_entrada, "mais_proximo")
ordem_C, t_C, d_C = calcular_elevador(chamadas_entrada, "menor_deslocamento")

print(f"ESTRATÉGIA A (Chegada): Ordem: {ordem_A} | Deslocamento: {d_A} | Tempo: {t_A}s")
print(f"ESTRATÉGIA B (Próximo): Ordem: {ordem_B} | Deslocamento: {d_B} | Tempo: {t_B}s")
print(f"ESTRATÉGIA C (Menor):   Ordem: {ordem_C} | Deslocamento: {d_C} | Tempo: {t_C}s")
