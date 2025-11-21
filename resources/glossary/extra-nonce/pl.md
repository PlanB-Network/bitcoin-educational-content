---
term: EXTRA-Nonce
---

Pole używane w `scriptSig` Coinbase Transaction bloku, które pozwala na przetestowanie większej liczby możliwości w celu uzyskania Hash niższego niż docelowy poziom trudności, oprócz klasycznego Nonce, który znajduje się bezpośrednio w nagłówku każdego bloku.


Modyfikacja dodatkowego Nonce w Coinbase Transaction zmienia identyfikator tej transakcji, a tym samym Merkle Root wszystkich transakcji w bloku, co również modyfikuje nagłówek bloku. Pozwala to Miner na kontynuowanie wyszukiwania hashy, gdy zakres klasycznego Nonce jest już wyczerpany, bez zmiany struktury bloku kandydującego.


W pulach Mining dodatkowy Nonce jest często podzielony na dwie części: jedną generowaną przez pulę w celu identyfikacji każdego choppera, a drugą modyfikowaną przez choppera w poszukiwaniu ważnego udziału. Pozwala to różnym chopperom w puli pracować jednocześnie nad tym samym blokiem kandydującym z całym zakresem nonces, bez powielania tej samej pracy na poziomie puli.