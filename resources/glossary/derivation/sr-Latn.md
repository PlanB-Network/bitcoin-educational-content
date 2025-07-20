---
term: DERIVACIJA
---

Odnosi se na proces generisanja parova ključeva za decu iz roditeljskog para ključeva (privatni ključ i javni ključ) i lanca kodova unutar determinističkog i hijerarhijskog (HD) Wallet. Ovaj proces omogućava segmentaciju grana i organizaciju Wallet u različite nivoe sa brojnim parovima ključeva za decu, koji se svi mogu povratiti znajući samo osnovne informacije za oporavak (Mnemonic fraza i bilo koji potencijalni passphrase). Za izvođenje ključa za dete koristi se funkcija `HMAC-SHA512` sa roditeljskim lancem kodova i konkatenacijom roditeljskog ključa i 32-bitnog indeksa. Postoje dve vrste derivacija:


- Normalna derivacija, koja koristi roditeljski javni ključ kao osnovu za funkciju `HMAC-SHA512`;
- Ojačano izvođenje, koje koristi roditeljski privatni ključ kao osnovu za funkciju `HMAC-SHA512`;


Rezultat HMAC-SHA512 se deli na dva dela: prvih 256 bita postaju dečiji ključ (privatni ili javni nakon obrade kroz ECDSA), a preostalih 256 bita postaju dečiji lančani kod.