---
term: PEGADA DE CARTEIRA

---
Um conjunto de caraterísticas distintivas observáveis em transacções feitas pela mesma carteira Bitcoin. Essas caraterísticas podem incluir similaridades no uso de tipos de scripts, reutilização de endereços, a ordem dos UTXOs, a colocação de saídas de mudança, a sinalização de RBF (*Replace-by-Fee*), o número da versão, o campo `nSequence` e o campo `nLockTime`.

As pegadas de carteira são usadas por analistas para rastrear as atividades de uma determinada entidade na blockchain, identificando padrões recorrentes em suas transações. Por exemplo, um utilizador que envia sistematicamente os seus trocos para endereços P2TR (`bc1p...`) cria uma pegada distintiva que pode ser utilizada para rastrear as suas transacções futuras.

Como LaurentMT explica no Space Kek #19 (um podcast francófono), a utilidade das pegadas das carteiras na análise da cadeia aumenta significativamente com o tempo. De facto, o número crescente de tipos de scripts e a implementação cada vez mais gradual destas novas funcionalidades pelo software das carteiras acentuam as diferenças. É mesmo possível identificar com exatidão o software utilizado pela entidade rastreada. Por conseguinte, é importante compreender que o estudo da pegada de uma carteira é particularmente relevante para as transacções recentes, mais do que para as iniciadas no início da década de 2010.