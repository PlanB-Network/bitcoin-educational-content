---
term: SIGHASH_ALL/SIGHASH_ACP

definition: Sự kết hợp SigHash cho phép thêm các đầu vào sau chữ ký ban đầu.
---
Type of SigHash Flag (`0x81`) combined with the `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) used in Bitcoin transaction signatures. This combination specifies that the signature applies to all the outputs and only to a specific input of the transaction. `SIGHASH_ALL | SIGHASH_ANYONECANPAY` allows other participants to add additional inputs to the transaction after its initial signature. It is particularly useful in collaborative scenarios, such as crowdfunding transactions, where different contributors can add their own inputs while preserving the integrity of the outputs committed by the initial signer.