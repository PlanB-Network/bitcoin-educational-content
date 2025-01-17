---
term: DIFICULDADE

---
Um parâmetro ajustável que determina a complexidade da prova de trabalho necessária para adicionar um novo bloco à cadeia de blocos e ganhar a recompensa associada. Esta dificuldade é representada pelo objetivo de dificuldade, um valor de 256 bits que define o limite superior que o hash do cabeçalho do bloco deve cumprir para ser considerado válido. O objetivo é que o hash, obtido através de uma execução dupla de SHA256 (SHA256d), seja inferior ou igual a este objetivo. Para atingir este hash, os mineiros manipulam o `nonce` no cabeçalho do bloco. A dificuldade ajusta-se a cada 2016 blocos, ou aproximadamente a cada duas semanas, para manter o tempo médio de criação de blocos em cerca de 10 minutos.