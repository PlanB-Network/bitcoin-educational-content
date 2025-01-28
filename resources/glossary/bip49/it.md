---
term: BIP49

---
Il BIP49 è un BIP informativo che introduce il metodo di derivazione utilizzato per generare indirizzi SegWit annidati in un portafoglio HD. Il percorso di derivazione proposto segue gli standard di BIP43 e BIP44, con l'indice `49'` (derivazione rafforzata) alla profondità dell'obiettivo. Ad esempio, il primo indirizzo di un conto P2SH-P2WPKH verrebbe derivato dal percorso: `m/49'/0'/0'/0/0`. Gli script SegWit annidati sono stati inventati al momento del lancio di SegWit per facilitarne l'adozione. Permettono di utilizzare questo nuovo standard anche su portafogli non ancora nativamente compatibili con SegWit.