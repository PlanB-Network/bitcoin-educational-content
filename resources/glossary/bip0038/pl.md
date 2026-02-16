---
term: BIP0038
definition: Standard szyfrowania kluczy prywatnych Bitcoin za pomocą hasła, używany w szczególności do zabezpieczania portfeli papierowych.
---

Propozycja ulepszenia Bitcoin, która wprowadza mechanizm szyfrowania w celu dodania dodatkowej ochrony do kluczy prywatnych poprzez passphrase. BIP38 gwarantuje, że nawet jeśli strona trzecia fizycznie uzyska zaszyfrowany klucz prywatny, nie będzie mogła go użyć bez znajomości jego passphrase. Dodaje to dodatkowy Layer bezpieczeństwa w celu ochrony bitcoinów przed kradzieżą, szczególnie w przypadku bezpieczeństwa starych portfeli papierowych.


> chociaż niniejsza propozycja jest określana jako "passphrase", ważne jest, aby nie mylić jej z passphrase wspomnianym w BIP39, który jest znacznie częściej używany. Jednak podstawowa koncepcja pozostaje podobna: podczas gdy BIP38 ma na celu zabezpieczenie indywidualnego klucza prywatnego, BIP39 zapewnia ochronę całego HD Wallet