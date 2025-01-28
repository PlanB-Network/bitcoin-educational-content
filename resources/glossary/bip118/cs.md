---
term: BIP118

---
Návrh na vylepšení Bitcoinu zaměřený na zavedení dvou nových modifikátorů SigHash Flag: `SIGHASH_ANYPREVOUT` a `SIGHASH_ANYPREVOUTANYSCRIPT`. Tyto funkce rozšiřují možnosti transakcí Bitcoinu, zejména pokud jde o chytré smlouvy a překryvná řešení, jako je Lightning Network. BIP118 by zejména umožnil používání Eltoo. Hlavní výhodou `SIGHASH_ANYPREVOUT` je umožnění opakovaného použití podpisů napříč více transakcemi, což nabízí větší flexibilitu. Konkrétně tyto SigHashe umožňují podpis, který nepokrývá žádný ze vstupů transakce.