---
term: OP_VER (0X62)

definition: Opcode deshabilitado que colocaba la versión del cliente, convertido en OP_SUCCESS.
---
Permitía introducir la versión del cliente en la pila. Este opcode estaba desactivado porque si se hubiera utilizado, cada actualización habría llevado a un hard fork. BIP342 modificó este opcode a `OP_SUCCESS`.