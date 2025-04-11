---
term: DESCOBERTA POR PARES

---
O processo pelo qual os nós na rede Bitcoin se conectam a outros nós para obter informações. Quando um nó Bitcoin é lançado pela primeira vez, ele não tem informações sobre outros nós na rede. No entanto, ele deve estabelecer conexões para sincronizar com o blockchain que tem mais trabalho acumulado. Vários mecanismos são usados para descobrir esses pares, por ordem de prioridade:


- O nó começa por consultar o seu ficheiro local `peers.dat`, que armazena informação sobre os nós com os quais já interagiu anteriormente. Se o nó for novo, este ficheiro estará vazio, e o processo passará para o passo seguinte;
- Na ausência de informações no arquivo `peers.dat` (o que é normal para um nó recém-lançado), o nó realiza consultas DNS aos servidores DNS. Estes servidores fornecem uma lista de endereços IP de nós presumivelmente activos para estabelecer ligações. Os endereços dos DNS seeds são hardcoded no código do Bitcoin Core. Este passo é geralmente suficiente para completar a descoberta de pares;
- Se as sementes DNS não responderem dentro de 60 segundos, o nó pode então recorrer aos nós de sementes. Estes são nós Bitcoin públicos listados numa lista estática de quase mil entradas integradas diretamente no código fonte do Bitcoin Core. O novo nó usará essa lista para estabelecer uma primeira conexão com a rede e obter endereços IP de outros nós;
- No caso muito improvável de todos os métodos anteriores falharem, o operador do nó tem sempre a opção de adicionar manualmente os endereços IP dos nós para estabelecer uma primeira ligação.