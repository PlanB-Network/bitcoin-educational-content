---
term: CISA
---

Zkratka pro "Cross-Input Signature Aggregation". Jedná se o technický návrh, jehož cílem je optimalizovat velikost transakcí Bitcoin snížením počtu podpisů potřebných k jejich ověření.


V současné době musí mít v systému Bitcoin každý vstup v transakci individuální podpis, aby mohl být spotřebován. Tím se prokazuje, že vlastník daného UTXO transakci autorizoval. Cílem CISA je spojit podpisy všech vstupů jedné transakce do jediného podpisu zahrnujícího všechny vstupy. To by umožnilo zmenšit velikost transakcí s mnoha vstupy, a tím i snížit jejich náklady. To by bylo užitečné zejména pro ty, kdo provádějí spojování mincí nebo konsolidace, a zároveň by to umožnilo potvrdit více transakcí na Bitcoin, aniž by se změnila velikost bloků nebo intervaly. CISA je založena na Schnorrově protokolu, který umožňuje lineární agregaci podpisů. To znamená, že jeden podpis může prokázat vlastnictví několika nezávislých klíčů.


Implementace CISA v systému Bitcoin je však velmi složitá, protože vyžaduje zásadní změny ve způsobu práce se skripty. V současné době se ověřování skriptů v systému Bitcoin provádí po jednotlivých vstupech. Přechod na model, kdy se kontroluje celá transakce najednou, jak navrhuje CISA, není zdaleka triviální změnou.