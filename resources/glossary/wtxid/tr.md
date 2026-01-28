---
term: WTXID
definition: SegWit ile sunulan TXID'nin bir uzantısı olan ve witness verilerini içeren işlem tanımlayıcı.
---

SegWit ile tanıtılan tanık verilerini içeren geleneksel txid'ün bir uzantısı. txid, tanık hariç işlem verilerinin bir Hash'ü iken, WTXID, tanık dahil tüm işlem verilerinin `SHA256d'sidir. WTXID'ler, kökü Coinbase Transaction'a yerleştirilen ayrı bir Merkle Tree'de saklanır. Bu ayrım, txid'ün işlem değiştirilebilirliğinin ortadan kaldırılmasını sağlar.