---
term: BLK*.DAT

---
Nome dos arquivos no Bitcoin Core que armazenam os dados brutos do bloco da blockchain. Cada ficheiro é identificado por um número único no seu nome. Assim, os blocos são registados por ordem cronológica, começando pelo ficheiro blk00000.dat. Quando este ficheiro atinge a sua capacidade máxima, os blocos seguintes são registados em blk00001.dat, depois em blk00002.dat, e assim sucessivamente. Cada ficheiro blk tem uma capacidade máxima de 128 mebibytes (MiB), o que equivale a um pouco mais de 134 megabytes (MB). Estes arquivos foram movidos para a pasta `/blocos` desde a versão 0.8.0.