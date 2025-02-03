---
term: OP_EVAL

---
Opcode diusulkan oleh Gavin Andresen pada tahun 2011. Opcode ini mengambil skrip yang terletak di bagian atas stack, mengeksekusinya seolah-olah itu adalah bagian dari `scriptPubKey`, dan menempatkan hasilnya pada stack. `OP_EVAL` ditinggalkan karena kekhawatiran terkait kompleksitas opcode ini, yang pada akhirnya akan digantikan oleh P2SH.