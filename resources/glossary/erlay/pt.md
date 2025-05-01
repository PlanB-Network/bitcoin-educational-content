---
term: ERLAY
---

Protocolo de rede proposto para melhorar a eficiência da retransmissão de transacções não confirmadas entre nós Bitcoin.


Atualmente, cada transação é propagada através de um sistema em que cada nó transmite a transação de que tem conhecimento a todos os seus pares. O problema é que isso leva a muita redundância e uso de largura de banda para duplicatas. Muitas transmissões de transacções são desnecessárias, uma vez que o destinatário já tem conhecimento dessas transacções, e cada nó só precisa de ter conhecimento de cada transação uma vez. Erlay propõe limitar por defeito a 8 o número de pares para os quais um nó envia diretamente transacções de que tem conhecimento, e depois usar um processo de reconciliação baseado na biblioteca minisketch para partilhar as transacções em falta de forma mais eficiente.


O Erlay reduziria o consumo de largura de banda em cerca de 40%, tornando o funcionamento do Full node mais acessível a utilizadores com ligações limitadas à Internet e promovendo assim uma melhor descentralização da rede. Este protocolo também manteria o consumo de largura de banda quase constante à medida que o número de conexões aumentasse. Isto significa que seria muito mais simples para os operadores de nós aceitarem um número muito elevado de ligações dos seus pares, o que aumentaria a segurança da rede Bitcoin ao reduzir o risco de particionamento, intencional ou acidental. Além disso, o Erlay tornaria mais difícil determinar o nó de origem de uma transação, aumentando assim a confidencialidade para os utilizadores de nós que não operam com o Tor.


Erlay é proposto em BIP330.