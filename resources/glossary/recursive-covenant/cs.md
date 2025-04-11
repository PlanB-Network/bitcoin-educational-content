---
term: REKURZIVNÍ (SMLOUVA)

---
Rekurzivní smlouva v Bitcoinu je typ chytré smlouvy, která ukládá podmínky nejen pro aktuální transakci, ale také pro budoucí transakce, které utrácejí výstupy této transakce. To umožňuje vytvářet řetězce transakcí, kde každá musí dodržovat určitá pravidla definovaná první v řetězci. Rekurzivita vytváří posloupnost transakcí, kde každá dědí omezení od své nadřazené transakce. To by umožnilo komplexní a dlouhodobou kontrolu nad tím, jak lze bitcoiny utrácet, ale zároveň by to přineslo rizika týkající se svobody utrácení a zaměnitelnosti.

Shrneme-li to, nevratná smlouva by se omezovala pouze na transakci, která bezprostředně následuje po transakci, která stanovila pravidla. Naproti tomu rekurzivní dohoda má možnost ukládat konkrétní podmínky pro bitcoin neomezeně dlouho. Transakce mohou následovat jedna po druhé, ale daný bitcoin si vždy zachová původní podmínky, které jsou s ním spojeny. Technicky vzato, k vytvoření nerekurzivní smlouvy dochází, když `scriptPubKey` UTXO definuje omezení `scriptPubKey` výstupů transakce, která utrácí zmíněné UTXO. Naproti tomu k vytvoření rekurzivní smlouvy dochází, když `scriptPubKey` UTXO definuje omezení na `scriptPubKey` výstupů transakce, která utrácí uvedené UTXO, a na všechny `scriptPubKey`, které budou následovat po utracení tohoto UTXO.

Obecněji se v informatice nazývá "rekurzivita" schopnost funkce volat samu sebe a vytvářet tak jakousi smyčku.