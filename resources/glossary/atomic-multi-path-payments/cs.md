---
term: ATOMOVÉ VÍCECESTNÉ PLATBY
---

Vylepšená verze MPP (*Multi-Path Payments*), kde má každý fragment platby samostatné dílčí tajemství, což zajišťuje, že transakce je zúčtována atomicky, tj. v plné výši nebo vůbec.


MPP jsou platební techniky v systému Lightning, které umožňují rozdělit transakci na několik menších částí a směrovat ji různými cestami. Jinými slovy, každá část platby jde jinou cestou přes uzel. Tím se obchází omezení likvidity na jediném kanálu v trase. V základních MPP sdílí každá platební frakce stejné tajemství, a tedy i stejný Hash v HTLC. Díky tomu může být transakce dohledatelná, pokud je pozorovatel přítomen na několika trasách, protože může všechny tyto identické tajenky spojit dohromady. A co víc, protože tajemství je jedinečné pro všechny části platby, není atomické. To znamená, že některé části platby mohou být provedeny úspěšně, zatímco jiné mohou selhat.


V systému AMP se pro každý zlomek používají jedinečné dílčí tajemství. Po obdržení všech dílčích tajemství může příjemce rekonstruovat původní obecné tajemství a požadovat celou platbu. Tato metoda znemožňuje částečné vypořádání platby, protože k odblokování celé platby je nutné vlastnit všechny dílčí tajemství. Tím je zajištěno, že platba je plně úspěšná nebo plně neúspěšná (tj. atomická). AMP také zlepšuje důvěrnost, protože již neexistují žádné viditelné vazby mezi různými cestami.


Jednou z výhod AMP je, že fungují i v případě, že tuto metodu má implementovanou pouze příjemce a odesílatel. Zprostředkující uzly zpracovávají tyto platby jako běžné transakce pomocí HTLC, aniž by si uvědomovaly, že zpracovávají zlomky větší platby.