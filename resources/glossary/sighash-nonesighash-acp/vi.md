---
term: SIGHASH_NONE/SIGHASH_ACP

---
Type of SigHash Flag (`0x82`) combined with the `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) used in Bitcoin transaction signatures. This combination indicates that the signature applies only to a specific input, without committing to any output. This allows other participants to freely add additional inputs and modify all the transaction's outputs.