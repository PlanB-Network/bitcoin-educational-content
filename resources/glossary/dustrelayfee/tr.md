---
term: Dustrelayfee
definition: Toz sınırını hesaplamak için kullanılan ücret oranını tanımlayan düğüm parametresi.
---

Ağ düğümleri tarafından "Dust sınırını" belirlemek için kullanılan bir standardizasyon kuralı Bu parametre sanal kilobayt başına Sats (Sats/kvB) cinsinden bir ücret oranı belirler ve bir UTXO'ün değerinin bir işleme dahil edilmesi için gerekli ücretlerden daha az olup olmadığını hesaplamak için bir referans görevi görür. Gerçekten de, bir UTXO, transfer edilmesi için temsil ettiği değerden daha fazla ücret gerektiriyorsa, Bitcoin üzerinde "Dust" olarak kabul edilir. Bu limitin hesaplanması aşağıdaki gibidir:


```text
limit = (input size + output size) * fee rate
```


Bir işlemin Bitcoin bloğuna dahil edilmesi için gerekli ücret oranı sürekli değiştiğinden, `DustRelayFee` parametresi her düğümün bu hesaplamada kullanılan ücret oranını tanımlamasına olanak tanır. Varsayılan olarak, Bitcoin core'te bu değer 3.000 Sats/kvB olarak ayarlanmıştır. Örneğin, sırasıyla 148 ve 34 bayt ölçen bir P2PKH girişi ve çıkışı için Dust limitini hesaplamak için hesaplama şöyle olacaktır:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


Bu, söz konusu düğümün değeri 546 Sats'den küçük olan P2PKH güvenli UTXO içeren işlemleri iletmeyeceği anlamına gelir.