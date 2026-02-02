---
term: Konsolidering
definition: Transaktion som slår samman flera små UTXOer till en enda större för att minska framtida avgifter.
---

En specifik transaktion där flera små UTXO:er slås samman till en input för att bilda en enda större UTXO som output. Denna operation är en transaktion som görs till ens egen Wallet. Målet med konsolidering är att dra nytta av perioder när avgifterna i Bitcoin-nätverket är låga för att slå samman flera små UTXO:er till en som är större i värde. På så sätt förutser man obligatoriska utgifter vid avgiftshöjningar, vilket möjliggör besparingar på framtida transaktionsavgifter.


Transaktioner med många inmatningar är tyngre och följaktligen dyrare. Utöver de besparingar som kan göras på transaktionsavgifter är konsolidering också en form av långsiktig planering. Om din Wallet innehåller mycket små UTXO:er kan dessa bli oanvändbara om Bitcoin-nätverket går in i en längre period med höga avgifter. Om du till exempel behöver spendera en UTXO på 10 000 Sats men de lägsta Mining-avgifterna uppgår till 15 000 Sats, skulle kostnaden överstiga värdet på själva UTXO. Dessa små UTXO:er blir då ekonomiskt irrationella att använda och förblir oanvändbara så länge avgifterna inte minskar. Dessa UTXO:er kallas vanligen för "Dust" Genom att regelbundet konsolidera dina små UTXO:er minskar du denna risk i samband med avgiftshöjningar.


Det är dock viktigt att notera att konsolideringstransaktioner är igenkännliga under en kedjeanalys. En sådan transaktion indikerar en Common Input Ownership Heuristic (CIOH), vilket innebär att inputs i konsolideringstransaktionen ägs av en enda enhet. Detta kan ha konsekvenser när det gäller användarens integritet.


