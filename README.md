# Desafio de Programação: Elevador Inteligente da ETEC

## 1. O Algoritmo
O código fonte com a simulação do elevador está disponível no arquivo `desafio_elevador.py` neste repositório. Ele foi estruturado para calcular o deslocamento e o tempo de diferentes estratégias.

## 2. Justificativa da Estratégia Escolhida
Testei as estratégias A, B e C propostas no desafio. A estratégia que escolhi como a mais eficiente foi a **B (Atender o mais próximo primeiro)**. 

Ao garantir que o elevador sempre busque a origem de chamada mais próxima do seu andar atual, eliminei as grandes viagens vazias cruzando o prédio. Curiosamente, ela se mostrou mais eficiente até mesmo que a estratégia C (avaliar o menor trajeto total), provando que minimizar o tempo de busca do passageiro é o fator mais crítico nesta configuração.

## 3. Comparação de Estratégias
Utilizei as entradas `[(0,4), (2,1), (3,0), (4,2)]` para rodar meu algoritmo nas três lógicas.

**Métricas da Estratégia A (Ordem de Chegada):**
* Ordem: (0,4) -> (2,1) -> (3,0) -> (4,2)
* Deslocamento: 18 andares
* Tempo Total: 94 segundos

**Métricas da Estratégia B (Mais próximo primeiro):**
* Ordem: (0,4) -> (4,2) -> (2,1) -> (3,0)
* Deslocamento: 12 andares
* Tempo Total: 76 segundos

**Métricas da Estratégia C (Menor deslocamento total da viagem):**
* Ordem: (2,1) -> (0,4) -> (4,2) -> (3,0)
* Deslocamento: 14 andares
* Tempo Total: 82 segundos

## 4. Melhor Resultado
A estratégia **B (Mais próximo primeiro)** obteve o melhor resultado. Ela reduziu o tempo de operação em **18 segundos** em relação à ordem de chegada e poupou o elevador de percorrer **6 andares** extras, comprovando ser a solução mais inteligente.

*(Nota técnica: A saída gerada pela minha Estratégia B resulta na mesma ordem de atendimento sugerida no exemplo da imagem do desafio. No entanto, o cálculo mecânico real dessa rota gera 12 andares de deslocamento, e não 14).*
