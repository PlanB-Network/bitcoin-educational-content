---
term: SIGHASH_SINGLE/SIGHASH_ACP

definition: Sự kết hợp ký một đầu vào duy nhất và chỉ đầu ra có cùng chỉ mục.
---
Type of SigHash Flag (`0x83`) combined with the `SIGHASH_ANYONECANPAY` modifier (`SIGHASH_ACP`) used in Bitcoin transaction signatures. This combination specifies that the signature applies to only a specific single input and only to the output having the same index as this input. Other inputs and outputs can be added or modified by other parties. This configuration is useful for collaborative transactions where participants can add their own inputs to fund a specific output.