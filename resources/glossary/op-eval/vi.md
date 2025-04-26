---
term: OP_EVAL

---
Opcode proposed by Gavin Andresen in 2011. It takes the script located at the top of the stack, executes it as if it were part of the `scriptPubKey`, and places its result on the stack. `OP_EVAL` was abandoned due to concerns related to the complexity of this opcode, which would eventually be superseded by P2SH.