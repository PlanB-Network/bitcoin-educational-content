---
term: SIGOPS (SIGNATURE OPERATIONS)

---
Refers to the digital signature operations necessary to validate transactions. Each Bitcoin transaction can contain multiple inputs, each of which may require one or more signatures to be considered valid. The verification of these signatures is done through the use of specific opcodes called "sigops". Specifically, this includes `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG`, and `OP_CHECKMULTISIGVERIFY`. These operations impose a certain workload on the network nodes that must verify them. To prevent DoS attacks through the artificial inflation of the number of sigops, the protocol therefore imposes a limit on the number of sigops allowed per block, to ensure that the validation load remains manageable for the nodes. This limit is currently set at a maximum of 80,000 sigops per block. To count, nodes follow these rules:

In the `scriptPubKey`, `OP_CHECKSIG` and `OP_CHECKSIGVERIFY` count as 4 sigops. The opcodes `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` count for 80 sigops. Indeed, during counting, these operations are multiplied by 4 when they are not part of a SegWit input (for a P2WPKH, the number of sigops will therefore be 1);

In the `redeemScript`, the opcodes `OP_CHECKSIG` and `OP_CHECKSIGVERIFY` also count as 4 sigops, `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` are accounted for as `4n` if they precede `OP_n`, or 80 sigops otherwise;

For the `witnessScript`, `OP_CHECKSIG` and `OP_CHECKSIGVERIFY` are worth 1 sigop, `OP_CHECKMULTISIG` and `OP_CHECKMULTISIGVERIFY` are counted as `n` if they are introduced by `OP_n`, or 20 sigops otherwise;

In Taproot scripts, sigops are treated differently compared to traditional scripts. Instead of directly counting each signature operation, Taproot introduces a sigops budget for each transaction input, which is proportional to the size of that input. This budget is 50 sigops plus the byte size of the input's witness. Each signature operation reduces this budget by 50. If the execution of a signature operation drops the budget below zero, the script is invalid. This method allows for more flexibility in Taproot scripts, while maintaining protection against potential abuses related to sigops, by directly linking them to the weight of the input. Thus, Taproot scripts are not included in the 80,000 sigops per block limit.