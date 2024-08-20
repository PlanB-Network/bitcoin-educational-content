---
term: PEER DISCOVERY
---

O processo pelo qual nós na rede Bitcoin se conectam a outros nós para obter informações. Quando um nó Bitcoin é inicialmente lançado, ele não possui informações sobre outros nós na rede. No entanto, ele deve estabelecer conexões para sincronizar com o blockchain que possui o maior trabalho acumulado. Vários mecanismos são usados para descobrir esses pares, em ordem de prioridade:
* O nó começa consultando seu arquivo local `peers.dat`, que armazena informações sobre nós com os quais interagiu anteriormente. Se o nó for novo, este arquivo estará vazio, e o processo passará para a próxima etapa;
* Na ausência de informações no arquivo `peers.dat` (o que é normal para um nó recém-lançado), o nó realiza consultas DNS para os seeds DNS. Esses servidores fornecem uma lista de endereços IP de nós presumivelmente ativos para estabelecer conexões. Os endereços dos seeds DNS são codificados diretamente no código do Bitcoin Core. Esta etapa geralmente é suficiente para completar a descoberta de pares;
* Se os seeds DNS não responderem dentro de 60 segundos, o nó pode então recorrer aos seed nodes. Estes são nós públicos do Bitcoin listados em uma lista estática de quase mil entradas integradas diretamente no código-fonte do Bitcoin Core. O novo nó usará esta lista para estabelecer uma primeira conexão com a rede e obter endereços IP de outros nós;
* No caso muito improvável de todos os métodos anteriores falharem, o operador do nó sempre tem a opção de adicionar manualmente endereços IP de nós para estabelecer uma primeira conexão.