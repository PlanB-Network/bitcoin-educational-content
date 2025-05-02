---
term: OBIETTIVO
---

Nei portafogli deterministici e gerarchici (HD), lo scopo, definito dal BIP43, rappresenta uno specifico livello di derivazione. Questo indice, situato alla prima profondità dell'albero di derivazione (`m / purpose' /`), identifica lo standard di derivazione adottato dal portafoglio, per facilitare la compatibilità tra diversi software di gestione del portafoglio. Ad esempio, nel caso degli indirizzi SegWit (BIP84), lo scopo è indicato come `/84'/`. Questo metodo consente di organizzare in modo efficiente le chiavi tra diversi tipi di Address all'interno di un singolo portafoglio HD. Gli indici standard utilizzati sono :




- Per P2PKH: `44'` ;
- Per P2WPKH annidato in P2SH: `49'` ;
- Per P2WPKH: `84'` ;
- Per P2TR: `86'`.