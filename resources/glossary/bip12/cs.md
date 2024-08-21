---
term: BIP12
---

Návrh od Gavina Andresena na zvýšení flexibility a soukromí Bitcoinových transakčních skriptů. Tento BIP navrhuje implementaci nového skriptového operátoru, pojmenovaného `OP_EVAL`, který umožňuje vyhodnocení skriptu obsaženého v datech `scriptSig` během procesu validace transakce. Hlavní modifikace BIP12 spočívá v možnosti zahrnutí jednoho skriptu do druhého skriptu. Tato technika umožňuje vytváření složitějších podmínek, které lze ověřit v době utrácení, aniž by bylo nutné je odhalovat uživatelům posílajícím bitcoiny na použitou adresu. BIP12 byl později nahrazen bezpečnějšími návrhy, zejména BIP16 (P2SH), který nabízí jinou metodu pro dosažení stejných cílů jako `OP_EVAL`.