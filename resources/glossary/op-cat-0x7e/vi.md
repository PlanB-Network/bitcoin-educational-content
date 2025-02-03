---
term: OP_CAT (0X7E)

---
Allows for the concatenation of the two topmost elements on the stack (i.e., joining them end-to-end). This opcode has been disabled, making it currently impossible to use. However, it has recently come back into the spotlight. Some wish to add it to Tapscript to enable the combination of objects on the stack, thereby enhancing the expressiveness of this language. This simple additional tool could allow for:


- The use of Lamport signatures, which are presumably resistant to quantum attacks;
- The implementation of Vaults;
- The use of covenants;
- Or even, the use of non-equivocation contracts.