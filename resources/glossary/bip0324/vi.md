---
term: BIP0324

definition: Vận chuyển P2P V2 với mã hóa cơ hội cho các giao tiếp giữa các nút Bitcoin.
---
Introduces a new version of the Bitcoin P2P transport protocol incorporating opportunistic encryption to enhance the privacy and security of communications between nodes. The P2P V2 transport of BIP324 was included as an option (disabled by default) in version 26.0 of Bitcoin Core, deployed in December 2023. It can be activated with the `v2transport=1` option in the configuration file. This improvement is inspired by BIP150 and BIP151.