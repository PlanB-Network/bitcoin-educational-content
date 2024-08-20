---
termo: BIP384
---

Introduz a função `combo(KEY)` para descritores. Esta função descreve um conjunto de possíveis scripts de saída para uma chave pública dada. Assim, cobre múltiplos tipos de scripts ao mesmo tempo, incluindo P2PK, P2PKH, P2WPKH e P2SH-P2WPKH. Se a chave dada for comprimida, todos os 4 tipos de scripts são testados, e se não for, apenas os 2 tipos de scripts Legacy são testados. O objetivo é simplificar a representação de chaves em descritores, fornecendo um único método para gerar diferentes variantes de scripts de saída baseados na mesma chave pública. O BIP384 foi implementado juntamente com todos os outros BIPs relacionados a descritores (exceto o BIP386) na versão 0.17 do Bitcoin Core.