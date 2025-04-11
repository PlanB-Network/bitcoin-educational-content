---
term: RBF (REPLACE-BY-FEE)

---
Transakční mechanismus, který umožňuje odesílateli nahradit jednu transakci jinou tím, že zaplatí vyšší poplatky, aby urychlil její potvrzení. Pokud se transakce s příliš nízkými poplatky zasekne, může odesílatel použít *Replace-By-Fee*, aby zvýšil poplatky a upřednostnil jejich náhradní transakci v mempoolech.

RBF platí, dokud je transakce v mempoolech; jakmile je v bloku, nelze ji již nahradit. Při počátečním odeslání musí transakce určit svou dostupnost pro nahrazení úpravou hodnoty `nSequence` na číslo menší než `0xfffffffe`. To se nazývá "příznak" RBF. Toto nastavení signalizuje možnost aktualizace transakce po jejím odvysílání, což následně umožní RBF. Někdy je však možné nahradit transakci, která nesignalizovala RBF. Uzly používající konfigurační parametr `mempoolfullrbf=1` toto nahrazení akceptují, i když RBF původně signalizováno nebylo.

Na rozdíl od CPFP (*Child Pays For Parent*), kdy příjemce může jednat a urychlit transakci, RBF (*Replace-By-Fee*) umožňuje odesílateli převzít iniciativu a urychlit vlastní transakci zvýšením poplatků.