---
term: BIP0352
---

Predlog za poboljšanje od strane Josibake i Ruben Somsen koji uvodi Silent Payments, metodu korišćenja statičkih Bitcoin adresa za primanje uplata bez ponovne upotrebe Address, interakcije i bez vidljive On-Chain veze između različitih uplata. Ova tehnika eliminiše potrebu za generate novim, neiskorišćenim adresama za primanje za svaku transakciju, čime se izbegavaju uobičajene interakcije u Bitcoin gde primalac mora da obezbedi novi Address platiocu.


U ovom sistemu, platiša koristi javni ključ primaoca i svoj privatni ključ da bi generate svež Address za svaku uplatu. Samo primalac, sa svojim privatnim ključem, može izračunati privatni ključ koji odgovara ovom Address. ECDH (*Elliptic-Curve Diffie-Hellman*), kriptografski algoritam ključa Exchange, koristi se za uspostavljanje zajedničke tajne koja se zatim koristi za izvođenje primajućeg Address i privatnog ključa (samo na strani primaoca). Da bi identifikovali Tihе Uplate namenjene njima, primaoci moraju skenirati Blockchain i ispitati svaku transakciju koja odgovara kriterijumima za Tihе Uplate. Za razliku od BIP47, koji koristi obaveštavajuću transakciju za uspostavljanje kanala plaćanja, Tihе Uplate eliminišu ovaj korak, štedeći transakciju. Međutim, kompromis je da primalac mora skenirati sve potencijalne transakcije da bi utvrdio, primenom ECDH, da li su upućene njima.