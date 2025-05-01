---
term: SELFISH Mining
---

Estrategia (o ataque) en Mining, en la que un Miner o grupo de mineros retiene intencionadamente bloques con un Proof of Work válido sin liberarlos inmediatamente a la red. El objetivo es adelantarse a otros mineros en términos de Proof of Work, lo que potencialmente les permitiría Miner varios bloques seguidos y publicarlos todos a la vez, maximizando así sus ganancias. En otras palabras, el grupo de mineros atacante no mina sobre el último bloque validado por toda la red, sino sobre un bloque que ellos mismos han creado y que difiere del validado por la red.


Este proceso genera una especie de rama secreta de la Blockchain, que permanece desconocida para toda la red hasta que esta cadena alternativa supera potencialmente a la Blockchain honesta. Una vez que la cadena secreta de los mineros atacantes se hace más larga (es decir, contiene más trabajo acumulado) que la cadena pública honesta, se difunde a toda la red. En ese momento, los nodos de la red que sigan la cadena más larga (con más trabajo acumulado) se sincronizarán con esta nueva cadena. Entonces se produce una reorganización.


El egoísmo de Mining es molesto para los usuarios, ya que reduce la seguridad del sistema al desperdiciar parte de la potencia de cálculo de la red. Si tiene éxito, también provoca reorganizaciones de Blockchain, lo que afecta a la fiabilidad de las confirmaciones de transacciones para los usuarios. Aún así, esta práctica sigue siendo arriesgada para el grupo atacante de mineros, ya que a menudo es más rentable Miner normalmente por encima del último bloque conocido públicamente que asignar potencia de cálculo a una rama secreta que probablemente nunca superará el honesto Blockchain. Cuanto mayor sea el número de bloques en la reorganización, menor será la probabilidad de que el ataque tenga éxito.