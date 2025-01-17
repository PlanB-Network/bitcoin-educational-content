---
term: OP_CHECKSIG (0XAC)

---
Verifies the validity of a signature against a given public key. It takes the top two elements from the stack: the signature and the public key, and evaluates whether the signature is correct for the transaction hash and the specified public key. If the verification is successful, it pushes the value `1` (true) onto the stack, otherwise `0` (false). This opcode was modified in Tapscript to verify Schnorr signatures.