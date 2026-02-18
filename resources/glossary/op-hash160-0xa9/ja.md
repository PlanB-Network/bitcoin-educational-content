---
term: OP_HASH160 (0XA9)

definition: 最上部の要素をSHA256、次にRIPEMD160でハッシュ化するOpcode。
---
SHA256` と `RIPEMD160` の両方の関数を同時に使用する。この2段階の処理により160ビットのフィンガープリントが生成される。