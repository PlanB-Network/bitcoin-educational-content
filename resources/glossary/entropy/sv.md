---
term: Entropi
definition: Mått på oförutsägbarheten hos en datakälla, avgörande för generering av säkra nycklar.
---

Entropi är i samband med kryptografi och information ett kvantitativt mått på den osäkerhet eller oförutsägbarhet som är förknippad med en datakälla eller en slumpmässig process. Entropi spelar en avgörande roll för säkerheten i kryptografiska system, särskilt när det gäller generering av nycklar och slumptal. Hög entropi säkerställer att de genererade nycklarna är tillräckligt oförutsägbara och motståndskraftiga mot brute-force-attacker, där en angripare försöker gissa sig till nyckeln genom att prova alla möjliga kombinationer.


I samband med Bitcoin används entropi för att generate privata nycklar eller frön. När man skapar en deterministisk och hierarkisk Wallet görs konstruktionen av Mnemonic-frasen från ett slumpmässigt tal, som i sin tur härrör från en entropikälla. Frasen används sedan för att generate flera privata nycklar, på ett deterministiskt och hierarkiskt sätt, för att skapa utgiftsvillkor för UTXO:er.


Det är viktigt att ha en entropikälla av hög kvalitet för att garantera säkerheten i kryptografiska system. Entropikällor kan vara fysiska processer, t.ex. elektroniskt brus eller termiska variationer, eller mjukvaruprocesser, t.ex. generatorer av pseudoslumpmässiga tal.