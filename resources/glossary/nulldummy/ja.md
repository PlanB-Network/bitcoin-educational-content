---
term: NULLDUMMY
---

BIP147によってSegWitソフトフォークで導入された合意ルールで、`OP_CHECKMULTISIG`および`OP_CHECKMULTISIGVERIFY`オペコードで使用されるダミー要素が空のバイト配列(`OP_0`)であることを要求します。この措置は、この要素に`OP_0`以外の値を禁止することで、変更可能性のベクトルを排除するために実施されました。