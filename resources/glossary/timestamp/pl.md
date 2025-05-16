---
term: HORODATAGE
---

Znacznik czasu (ang. timestamping, Timestamp) to mechanizm umożliwiający powiązanie precyzyjnego znacznika czasu ze zdarzeniem, danymi lub wiadomością. W ogólnym kontekście systemów komputerowych znaczniki czasu są używane do określania chronologicznej kolejności operacji i weryfikacji integralności danych w czasie.


W konkretnym przypadku Bitcoin, znaczniki czasu są wykorzystywane do ustalenia chronologii transakcji i bloków. Każdy blok w Blockchain zawiera Timestamp wskazujący przybliżony czas jego utworzenia. W Satoshi Nakamoto mówi nawet o "serwerze Timestamp" w swojej Białej Księdze, aby opisać to, co dziś nazwalibyśmy "Blockchain". Rolą znacznika czasu na Bitcoin jest określenie chronologii transakcji, tak aby bez interwencji organu centralnego można było ustalić, która transakcja dotarła jako pierwsza. Mechanizm ten pozwala każdemu użytkownikowi zweryfikować nieistnienie transakcji w przeszłości, a tym samym uniemożliwić złośliwemu użytkownikowi dokonanie podwójnego wydatku. Mechanizm ten został uzasadniony przez Satoshi Nakamoto w jego Białej Księdze słynnym zdaniem: " *Ten standard opiera się na czasie uniksowym, który reprezentuje całkowitą liczbę sekund, które upłynęły od 1 stycznia 1970 roku.


> znaczniki czasu bloków są stosunkowo elastyczne w Bitcoin, ponieważ aby Timestamp został uznany za ważny, musi być po prostu większy niż mediana czasu 11 poprzedzających go bloków (MTP) i mniejszy niż mediana czasów zwróconych przez węzły (czas dostosowany do sieci) plus 2 godziny