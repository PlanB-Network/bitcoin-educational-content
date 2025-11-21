---
term: VÍCECESTNÉ PLATBY (MPP)
---

Obecný termín pro všechny platební techniky v systému Lightning, které umožňují rozdělit transakci na několik menších částí a směrovat ji různými cestami. Jinými slovy, každá část platby jde jinou uzlovou cestou. To umožňuje obejít omezení likvidity na jednom kanálu v trase.


Vícecestné platby mají také mírné výhody z hlediska důvěrnosti, protože pro pozorovatele je obtížnější spojit každý fragment platby s celou transakcí. V základní verzi však všechny fragmenty sdílejí stejné tajemství pro HTLC, což může umožnit dohledání transakce, pokud je pozorovatel přítomen na několika trasách. A co víc, protože tajemství je jedinečné pro všechny zlomky platby, není atomické. To znamená, že některé části platby mohou být provedeny úspěšně, zatímco jiné mohou selhat. Tyto nevýhody jsou odstraněny pomocí funkce "Atomic Multi-Path Payment".