---
term: REDEEMSCRIPT

---
A script that defines the specific conditions that inputs must meet to unlock the funds associated with a P2SH output. In a P2SH UTXO, the `scriptPubKey` contains the hash of the `redeemScript`. When a transaction wishes to spend this UTXO as an input, it must provide the clear `redeemScript` that matches the hash contained in the `scriptPubKey`. The `redeemScript` is thus given in the `scriptSig` of the input, along with other elements necessary to satisfy the script's conditions, such as signatures or public keys. This encapsulated structure ensures that the details of the spending conditions remain hidden until the bitcoins are actually spent. It is notably used for Legacy P2SH multisignature wallets.