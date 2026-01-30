---
term: Myntval
definition: Process genom vilken en plånbok väljer vilka UTXOs som ska användas som ingångar i en transaktion.
---

Den process genom vilken en Bitcoin Wallet-programvara väljer vilka UTXO:er som ska användas som input för att uppfylla outputen i en transaktion. Metoden för myntval är viktig eftersom den har konsekvenser för kostnaden för en transaktion och användarens integritet. Syftet är ofta att minimera antalet inputs som används för att minska transaktionsstorleken och tillhörande avgifter, samtidigt som man försöker bevara integriteten genom att undvika att slå samman mynt från olika källor (CIOH). Det finns flera metoder för myntval, t.ex. *Knapsack Solver* eller *Branch-and-Bound*. När myntvalet utförs manuellt av användaren kallas det "*Coin Control*".


