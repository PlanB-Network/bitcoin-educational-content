---
term: WALLET IMPORT FORMAT (WIF)
---

Um método para codificar uma chave privada Bitcoin de maneira que ela possa ser importada ou exportada mais facilmente entre diferentes carteiras. O WIF é baseado na codificação `Base58Check`, que inclui informações sobre a versão, a compressão da chave pública correspondente e um checksum para detecção de erros na digitação. Uma chave privada WIF começa com os caracteres `5` para chaves não comprimidas, ou `K` e `L` para chaves comprimidas, e contém todos os caracteres necessários para reconstruir a chave privada original. O formato WIF fornece um meio padronizado para transferir uma chave privada entre diferentes softwares de carteira.