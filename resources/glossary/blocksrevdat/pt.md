---
term: BLOCKS/REV*.DAT
---

Nome dos arquivos no Bitcoin Core que armazenam as informações necessárias para potencialmente reverter as alterações feitas no conjunto de UTXOs pelos blocos anteriormente adicionados. Cada arquivo é identificado por um número único que é o mesmo do arquivo blk*.dat ao qual corresponde. Os arquivos rev*.dat contêm os dados de reversão correspondentes aos blocos armazenados nos arquivos blk*.dat. Esses dados são essencialmente uma lista de todos os UTXOs gastos como entradas em um bloco. Esses arquivos de reversão permitem que o nó volte a um estado anterior em caso de uma reorganização da blockchain que cause a descarte de blocos previamente validados.