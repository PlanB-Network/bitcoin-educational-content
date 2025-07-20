---
term: NABÍDKA
---

V aplikaci BOLT12 jsou *nabídky* statické QR kódy pro provedení více plateb na Lightning Network. Na rozdíl od běžných faktur lze *offers* používat opakovaně. Mohou být použity k vícenásobným žádostem generate a Invoice. Když uživatel naskenuje QR kód obsahující *nabídku*, odešle zprávu s požadavkem na nový Invoice do přidruženého uzlu Lightning. Uzel odpoví nabídkou Invoice, kterou může plátce použít. *Nabídky* tak poskytují jedinečný identifikátor pro příjem více plateb od různých uživatelů v systému Lightning.