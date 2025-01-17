---
term: OP_CHECKSIGADD (0XBA)

---
Extracts the top three values from the stack: a `public key`, a `CScriptNum` `n`, and a `signature`. If the signature is not the empty vector and is not valid, the script terminates with an error. If the signature is valid or is the empty vector (`OP_0`), two scenarios are presented:


- If the signature is the empty vector: a `CScriptNum` with the value of `n` is pushed onto the stack, and execution continues;
- If the signature is not the empty vector and remains valid: a `CScriptNum` with the value of `n + 1` is pushed onto the stack, and execution continues.

To simplify, `OP_CHECKSIGADD` performs an operation similar to `OP_CHECKSIG`, but instead of pushing true or false onto the stack, it adds `1` to the second value at the top of the stack if the signature is valid, or leaves this value unchanged if the signature represents the empty vector. `OP_CHECKSIGADD` allows for the creation of the same multisignature policies in Tapscript as with `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` but in a batch verifiable manner, meaning it removes the lookup process in the verification of a traditional multisig and thus speeds up verification while reducing the operational load on the nodes' CPUs. This opcode was added in Tapscript solely for the needs of Taproot.