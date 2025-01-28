---
term: BIP68

---
Zavedena možnost používat relativní časy uzamčení pomocí pole `nSequence`. To umožňuje transakci zadat relativní prodlevu, než může být zařazena do bloku. Toto zpoždění lze definovat jako počet bloků nebo jako násobek 512 sekund (tj. reálného času). Všimněte si, že tato nová interpretace pole `nSequence` je platná pouze v případě, že pole `nVersion` je větší nebo rovno `2`. K této interpretaci pole `nSequence` dochází na úrovni pravidel konsensu Bitcoinu. Relativní časový zámek nastavuje zpoždění počínaje přijetím předchozí transakce, zatímco absolutní časový zámek určuje přesný okamžik, před kterým nemůže být transakce zařazena do bloku. BIP68 byl zaveden prostřednictvím soft forku 4. července 2016 spolu s BIP112 a BIP113, které byly poprvé aktivovány metodou BIP9.