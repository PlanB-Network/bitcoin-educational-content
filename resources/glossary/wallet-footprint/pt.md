---
term: PEGADA DE CARTEIRA
---

Um conjunto de características distintas observáveis em transações feitas pela mesma carteira Bitcoin. Essas características podem incluir semelhanças no uso de tipos de script, reutilização de endereços, a ordem dos UTXOs, o posicionamento de saídas de troco, o sinalizar de RBF (*Replace-by-Fee*), o número da versão, o campo `nSequence` e o campo `nLockTime`.

As pegadas de carteira são usadas por analistas para rastrear as atividades de uma entidade específica na blockchain, identificando padrões recorrentes em suas transações. Por exemplo, um usuário que sistematicamente envia seu troco para endereços P2TR (`bc1p…`) cria uma pegada distintiva que pode ser usada para rastrear suas futuras transações.

Como LaurentMT explica no Space Kek #19 (um podcast francófono), a utilidade das pegadas de carteira em análise de cadeia aumenta significativamente com o tempo. De fato, o crescente número de tipos de script e a implantação cada vez mais gradual dessas novas funcionalidades pelo software de carteira acentuam as diferenças. É até possível identificar com precisão o software usado pela entidade rastreada. Portanto, é importante entender que estudar a pegada de uma carteira é particularmente relevante para transações recentes, mais do que para aquelas iniciadas no início dos anos 2010.