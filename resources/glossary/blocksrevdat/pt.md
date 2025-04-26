---
term: BLOCOS/REV*.DAT

---
Nome dos arquivos no Bitcoin Core que armazenam as informações necessárias para potencialmente reverter as alterações feitas no conjunto UTXO por blocos adicionados anteriormente. Cada ficheiro é identificado por um número único que é o mesmo que o ficheiro blk*.dat a que corresponde. Os ficheiros rev*.dat contêm os dados de reversão correspondentes aos blocos armazenados nos ficheiros blk*.dat. Estes dados são essencialmente uma lista de todos os UTXOs gastos como entradas num bloco. Esses arquivos de reversão permitem que o nó reverta para um estado anterior no caso de uma reorganização da blockchain que faça com que blocos previamente validados sejam descartados.