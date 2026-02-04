---
term: Gossip
definition: Protokół P2P służący do rozprzestrzeniania informacji między węzłami w sposób epidemiczny.
---

Gossip to rozproszony algorytm typu peer-to-peer (P2P) służący do epidemicznego rozpowszechniania informacji wśród wszystkich agentów sieci. W przypadku Bitcoin, Lightning i innych systemów rozproszonych, protokół ten umożliwia wymianę i synchronizację Global State węzłów w zaledwie kilku cyklach. Każdy węzeł propaguje informacje do jednego lub więcej losowych lub nielosowych sąsiadów, którzy z kolei propagują informacje do innych sąsiadów i tak dalej, aż do osiągnięcia stanu globalnej synchronizacji.


W Lightning plotka jest protokołem komunikacji między węzłami w celu udostępniania informacji o bieżącym stanie i topologii sieci. Protokół plotek umożliwia węzłom poznanie dynamicznego stanu kanałów płatności i innych węzłów, aby ułatwić kierowanie transakcji w sieci bez konieczności bezpośrednich połączeń między wszystkimi węzłami.


