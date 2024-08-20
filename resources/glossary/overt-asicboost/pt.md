---
term: OVERT ASICBOOST
---

A versão aberta e transparente do AsicBoost. AsicBoost é uma técnica de otimização algorítmica usada na mineração de Bitcoin. Os mineradores que utilizam a versão Overt manipulam o campo `nVersion` do bloco candidato e usam essa modificação como um nonce adicional. Este método deixa o campo `Nonce` real do bloco inalterado durante cada tentativa de hash, reduzindo assim os cálculos necessários para cada SHA256, mantendo alguns dados iguais entre as tentativas. Esta versão é publicamente detectável e não esconde suas modificações do resto da rede, ao contrário da versão Covert do AsicBoost.