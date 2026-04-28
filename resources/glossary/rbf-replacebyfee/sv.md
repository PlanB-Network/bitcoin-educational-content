---
term: RBF (ersätt genom avgift)
definition: Mekanism som gör det möjligt att ersätta en obekräftad transaktion med en annan med högre avgift.
---

En transaktionsmekanism som gör det möjligt för avsändaren att ersätta en transaktion med en annan genom att betala högre avgifter, för att påskynda bekräftelsen. Om en transaktion med för låga avgifter fastnar kan avsändaren använda *Replace-by-fee* för att höja avgifterna och prioritera sin ersättningstransaktion i mempoolerna.


RBF gäller så länge som transaktionen finns i mempoolerna; när den väl finns i ett block kan den inte längre ersättas. Vid den första sändningen måste transaktionen ange att den är tillgänglig för ersättning genom att justera värdet `nSequence` till ett tal som är mindre än `0xfffffffe`. Detta är känt som en RBF "flagga". Denna inställning signalerar möjligheten att uppdatera transaktionen efter det att den har sänts, vilket i sin tur möjliggör en RBF. Det är dock ibland möjligt att ersätta en transaktion som inte har signalerat RBF. Noder som använder konfigurationsparametern `mempoolfullrbf=1` accepterar denna ersättning även om RBF inte ursprungligen signalerades.


Till skillnad från CPFP (*Child Pays For Parent*), där mottagaren kan agera för att påskynda transaktionen, tillåter RBF (*Replace-by-fee*) avsändaren att ta initiativ till att påskynda sin egen transaktion genom att höja avgifterna.