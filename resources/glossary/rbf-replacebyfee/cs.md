---
term: RBF (REPLACE-BY-FEE)
---

Transakční mechanismus, který umožňuje odesílateli nahradit jednu transakci jinou tím, že zaplatí vyšší poplatky, aby urychlil její potvrzení. Pokud se transakce s příliš nízkými poplatky zasekne, odesílatel může použít *Replace-By-Fee* k zvýšení poplatků a k prioritnímu zařazení své náhradní transakce do mempoolů.

RBF je použitelné, dokud je transakce v mempoolech; jakmile je v bloku, již nemůže být nahrazena. Při původním odeslání musí transakce specifikovat svou dostupnost k nahrazení úpravou hodnoty `nSequence` na číslo menší než `0xfffffffe`. To je známé jako RBF "flag". Toto nastavení signalizuje možnost aktualizace transakce po jejím vysílání, což následně umožňuje RBF. Někdy je však možné nahradit transakci, která RBF neoznámila. Uzly používající konfigurační parametr `mempoolfullrbf=1` přijímají tuto náhradu i v případě, že nebyl RBF původně signalizován.

Na rozdíl od CPFP (*Child Pays For Parent*), kde může příjemce jednat, aby urychlil transakci, RBF (*Replace-By-Fee*) umožňuje odesílateli vzít iniciativu k urychlení vlastní transakce zvýšením poplatků.