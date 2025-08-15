---
term: OP_EVAL

---
_Opcode_ diusulkan oleh Gavin Andresen pada tahun 2011. Opcode ini mengambil skrip yang terletak di bagian atas _stack_, mengeksekusinya seolah-olah itu adalah bagian dari `scriptPubKey`, dan menempatkan hasilnya pada _stack_. `OP_EVAL` ditinggalkan karena kekhawatiran terkait kompleksitas _opcode_ ini, yang pada akhirnya akan digantikan oleh P2SH.
