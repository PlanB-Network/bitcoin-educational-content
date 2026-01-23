---
term: Tài khoản

definition: Trong ví HD, một cấp độ dẫn xuất (chiều sâu 3) cho phép tổ chức các khóa và địa chỉ theo cấu trúc phân cấp.
---
In HD (Hierarchical Deterministic) wallets, an account represents a derivation layer at depth 3 according to BIP32. Each account is sequentially numbered starting from `/0'/` (hardened derivation, so in reality `/2^31/` or `/2 147 483 648/`). It is at this derivation depth that the well-known `xpubs` are located. Nowadays, typically only one account is used within an HD wallet. However, originally, they were conceived to segregate various categories of use within the same wallet. For example, if we take a standard derivation path for an external Taproot (P2TR) reception address: `m/86'/0'/0'/0/0`, the account index is the second `/0'/`.

