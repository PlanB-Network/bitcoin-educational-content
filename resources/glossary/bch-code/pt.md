---
term: CÓDIGO BCH
---

Uma classe de códigos de correção de erros utilizada para detetar e corrigir erros numa sequência de dados. Por outras palavras, os códigos de correção de erros BCH são utilizados para encontrar e corrigir erros aleatórios na informação transmitida, para garantir que esta chega intacta ao seu destino. O acrónimo "BCH" representa as iniciais dos nomes dos inventores destes códigos: Bose, Ray-Chaudhuri e Hocquenghem.


Esta ferramenta é utilizada em muitos domínios da informática, incluindo SSD, DVD e códigos QR. Por exemplo, graças a estes códigos de correção de erros, mesmo que um código QR esteja parcialmente coberto, continua a ser possível recuperar a informação que codifica.


Como parte do Bitcoin, os códigos BCH são utilizados para a soma de controlo nos formatos Bech32 e Bech32m (pós-SegWit) Address. Representam um melhor compromisso entre o tamanho da soma de controlo e a capacidade de deteção de erros do que as funções Hash simples anteriormente utilizadas nos endereços Legacy. No contexto do Bitcoin, os códigos BCH são utilizados apenas para a deteção de erros e não para a correção de erros. Assim, o software da carteira Bitcoin identificará e comunicará ao utilizador quaisquer erros num Address recetor, mas não alterará automaticamente o Address incorreto. Esta escolha é motivada pelo facto de a integração da correção de erros afetar inevitavelmente as capacidades de deteção de erros do algoritmo.