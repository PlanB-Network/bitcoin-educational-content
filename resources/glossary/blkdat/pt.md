---
term: BLK*.DAT
---

Nome dos arquivos no Bitcoin Core que armazenam os dados brutos dos blocos da blockchain. Cada arquivo é identificado por um número único em seu nome. Assim, os blocos são registrados em ordem cronológica, começando com o arquivo blk00000.dat. Quando este arquivo atinge sua capacidade máxima, os blocos seguintes são registrados em blk00001.dat, depois blk00002.dat, e assim por diante. Cada arquivo blk tem uma capacidade máxima de 128 mebibytes (MiB), o que é equivalente a um pouco mais de 134 megabytes (MB). Esses arquivos foram movidos para a pasta `/blocks` desde a versão 0.8.0.