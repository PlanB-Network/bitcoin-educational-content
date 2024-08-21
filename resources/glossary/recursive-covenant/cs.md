---
term: REKURZIVNÍ (COVENANT)
---

Rekurzivní covenant na Bitcoinu je typ chytrého kontraktu, který klade podmínky nejen na aktuální transakci, ale také na budoucí transakce, které utratí výstupy této transakce. To umožňuje vytváření řetězců transakcí, kde každá musí dodržovat určitá pravidla definovaná první transakcí v řetězci. Rekurzivita vytváří sekvenci transakcí, kde každá dědí omezení od své rodičovské transakce. To by umožnilo složité a dlouhodobé kontroly nad tím, jak lze bitcoiny utrácet, ale zároveň by to přineslo rizika týkající se svobody utrácení a zaměnitelnosti.

Shrnutí, ne-rekurzivní covenant by se omezil pouze na transakci, která bezprostředně následuje po té, která stanovila pravidla. Naopak, rekurzivní covenant má schopnost ukládat specifické podmínky na bitcoin na neurčito. Transakce mohou následovat jedna za druhou, ale dotčený bitcoin vždy zachová původní podmínky k němu připojené. Technicky, založení ne-rekurzivního covenantu nastane, když `scriptPubKey` UTXO definuje omezení na `scriptPubKey` výstupů transakce, která utratí dané UTXO. Na druhé straně, založení rekurzivního covenantu nastane, když `scriptPubKey` UTXO definuje omezení na `scriptPubKey` výstupů transakce, která utratí dané UTXO, a na všechny `scriptPubKey`, které budou následovat po utracení tohoto UTXO.

Obecněji, v informatice, se termínem "rekurzivita" rozumí schopnost funkce volat sama sebe, čímž vytváří jakýsi cyklus.