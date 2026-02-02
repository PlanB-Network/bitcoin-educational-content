---
term: SIGHASH_NONE/SIGHASH_ACP

definition: Sự kết hợp SigHash ký một đầu vào cụ thể duy nhất mà không cam kết với bất kỳ đầu ra nào.
---
Type of SigHash Flag (`0x82`) combined with the `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) used in Bitcoin transaction signatures. This combination indicates that the signature applies only to a specific input, without committing to any output. This allows other participants to freely add additional inputs and modify all the transaction's outputs.