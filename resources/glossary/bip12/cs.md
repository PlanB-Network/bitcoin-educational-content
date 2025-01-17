---
term: BIP12

---
Návrh Gavina Andresena na zvýšení flexibility a soukromí transakčních skriptů Bitcoinu. Tento BIP navrhuje implementaci nového opkódu skriptu s názvem `OP_EVAL`, který umožňuje vyhodnocení skriptu obsaženého v datech `scriptSig` během procesu validace transakce. Hlavní změnou BIP12 je umožnění začlenění jednoho skriptu uvnitř jiného skriptu. Tato technika umožňuje vytvářet složitější podmínky, které lze ověřit v okamžiku utrácení, aniž by je bylo nutné prozrazovat uživatelům odesílajícím bitcoiny na použitou adresu. BIP12 byl později nahrazen bezpečnějšími návrhy, zejména BIP16 (P2SH), který nabízí jinou metodu k dosažení stejných cílů jako `OP_EVAL`.