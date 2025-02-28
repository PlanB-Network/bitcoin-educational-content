---
term: FORMATO DE IMPORTAÇÃO DE CARTEIRA (WIF)

---
Um método para codificar uma chave privada Bitcoin de forma que ela possa ser importada ou exportada mais facilmente entre diferentes carteiras. O WIF é baseado na codificação `Base58Check`, que inclui informações sobre a versão, a compressão da chave pública correspondente e uma soma de verificação para deteção de erros na digitação. Uma chave privada WIF começa com os caracteres `5` para chaves não comprimidas, ou `K` e `L` para chaves comprimidas, e contém todos os caracteres necessários para reconstruir a chave privada original. O formato WIF fornece um meio padronizado para transferir uma chave privada entre diferentes softwares de carteira.