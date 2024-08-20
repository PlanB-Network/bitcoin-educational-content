---
termo: DIFICULDADE
---

Um parâmetro ajustável que determina a complexidade da prova de trabalho necessária para adicionar um novo bloco à blockchain e ganhar a recompensa associada. Essa dificuldade é representada pelo alvo de dificuldade, um valor de 256 bits que estabelece o limite superior que o hash do cabeçalho do bloco deve atender para ser considerado válido. O objetivo é que o hash, alcançado por meio de uma execução dupla de SHA256 (SHA256d), seja menor ou igual a esse alvo. Para alcançar esse hash, os mineradores manipulam o `nonce` no cabeçalho do bloco. A dificuldade ajusta-se a cada 2016 blocos, ou aproximadamente a cada duas semanas, para manter o tempo médio de criação de bloco em cerca de 10 minutos.