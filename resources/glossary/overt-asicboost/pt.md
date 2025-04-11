---
term: OVERT ASICBOOST

---
A versão aberta e transparente do AsicBoost. AsicBoost é uma técnica de otimização algorítmica usada na mineração de Bitcoin. Os mineradores que usam a versão Overt manipulam o campo `nVersion` do bloco candidato e usam essa modificação como um nonce adicional. Este método deixa o campo `Nonce` real do bloco inalterado durante cada tentativa de hashing, reduzindo assim os cálculos necessários para cada SHA256, mantendo alguns dados iguais entre as tentativas. Esta versão é detetável publicamente e não esconde as suas modificações do resto da rede, ao contrário da versão Covert do AsicBoost.