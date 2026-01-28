---
term: Witnessscript
definition: P2WSH veya P2SH-P2WSH UTXO'ları için harcama koşullarını tanımlayan betik, redeemScript'in SegWit karşılığı.
---

Bitcoinlerin P2WSH veya P2SH-P2WSH UTXO'lardan hangi koşullar altında harcanabileceğini belirten bir betik. Tipik olarak, `witnessScript` SegWit standardı altında çok imzalı bir Wallet'ün koşullarını belirler. Bu komut dosyası standartlarında, UTXO'nın (çıktı) `scriptPubKey`i `witnessScript`in bir Hash'ünü içerir. Bu UTXO`yı yeni bir işlemde girdi olarak kullanmak için, sahibinin `scriptPubKey`deki parmak izi ile eşleştiğini kanıtlamak amacıyla orijinal `tanıklıkScript`ini ortaya çıkarması gerekir. Daha sonra `tanıklıkScript` işlemin `scriptWitness` dosyasına dahil edilmelidir, bu dosya aynı zamanda imza gibi komut dosyasını doğrulamak için gerekli Elements'i de içerir. Bu nedenle, `witnessScript` bir P2SH işlemindeki `redeemscript`ın SegWit için eşdeğeridir, tek farkı `scriptSig`e değil işlemin tanığına yerleştirilmiş olmasıdır.


> ► *Dikkat, `witnessScript` `scriptWitness` ile karıştırılmamalıdır. TanıkScript` bir P2WSH veya P2SH-P2WSH UTXO'un harcama koşullarını tanımlar ve kendi başına bir komut dosyası oluştururken, `scriptWitness` herhangi bir SegWit girdisinin tanık verilerini içerir.*