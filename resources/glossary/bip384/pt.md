---
term: BIP384

---
Introduz a função `combo(KEY)` para descritores. Esta função descreve um conjunto de possíveis scripts de saída para uma determinada chave pública. Assim, ela cobre vários tipos de scripts ao mesmo tempo, incluindo P2PK, P2PKH, P2WPKH e P2SH-P2WPKH. Se a chave fornecida estiver comprimida, são testados todos os 4 tipos de guiões e, se não estiver, apenas são testados os 2 tipos de guiões legados. O objetivo é simplificar a representação de chaves em descritores, fornecendo um único método para gerar diferentes variantes de scripts de saída com base na mesma chave pública. O BIP384 foi implementado junto com todos os outros BIPs relacionados a descritores (exceto o BIP386) na versão 0.17 do Bitcoin Core.