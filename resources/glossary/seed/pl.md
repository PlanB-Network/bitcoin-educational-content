---
term: ZIARNO
---

W konkretnym kontekście hierarchicznego deterministycznego portfela Bitcoin, seed to 512-bitowy fragment informacji pochodzący ze zdarzenia losowego. Jest on używany do deterministycznego i hierarchicznego generate zestawu kluczy prywatnych i odpowiadających im kluczy publicznych dla portfela Bitcoin. seed jest często mylony z samą frazą odzyskiwania. Nie jest to jednak to samo. seed jest uzyskiwany przez zastosowanie funkcji `PBKDF2` do frazy Mnemonic i dowolnego passphrase.


seed został wynaleziony wraz z BIP32, który zdefiniował podstawy hierarchicznego portfela deterministycznego. W tym standardzie seed mierzył 128 bitów. Pozwala to na uzyskanie wszystkich kluczy w portfelu z jednej informacji, w przeciwieństwie do portfeli JBOK (*Just a Bunch Of Keys*), które wymagają nowych kopii zapasowych dla każdego wygenerowanego klucza. BIP39 zaproponował następnie kodowanie tego seed, aby uprościć jego odczyt przez ludzi. Kodowanie to ma postać frazy, ogólnie określanej jako fraza Mnemonic lub fraza odzyskiwania. Standard ten pozwala uniknąć błędów podczas zapisywania seed, w szczególności dzięki zastosowaniu sumy kontrolnej.


Poza kontekstem Bitcoin, w kryptografii w ogóle, seed jest wartością początkową używaną do generate kluczy kryptograficznych lub szerzej, dowolnego typu danych generowanych przez generator liczb pseudolosowych. Ta wartość początkowa musi być losowa i nieprzewidywalna, aby zagwarantować bezpieczeństwo systemu kryptograficznego. Rzeczywiście, seed wprowadza entropię do systemu, ale następujący po nim proces generowania jest deterministyczny.


> w języku potocznym większość bitcoinerów odnosi się do frazy Mnemonic, gdy mówią o "seed", a nie do pośredniego stanu derywacji, który leży pomiędzy frazą Mnemonic a kluczem głównym