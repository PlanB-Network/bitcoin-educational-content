---
term: OP_CHECKSIGADD (0XBA)
---

Mengekstrak tiga nilai teratas dari tumpukan: sebuah `public key`, sebuah `CScriptNum` `n`, dan sebuah `signature`. Jika tanda tangan tidak merupakan vektor kosong dan tidak valid, skrip akan berakhir dengan kesalahan. Jika tanda tangan valid atau merupakan vektor kosong (`OP_0`), dua skenario disajikan:
* Jika tanda tangan merupakan vektor kosong: sebuah `CScriptNum` dengan nilai `n` didorong ke tumpukan, dan eksekusi berlanjut;
* Jika tanda tangan bukan vektor kosong dan tetap valid: sebuah `CScriptNum` dengan nilai `n + 1` didorong ke tumpukan, dan eksekusi berlanjut.
Untuk menyederhanakan, `OP_CHECKSIGADD` melakukan operasi serupa dengan `OP_CHECKSIG`, tetapi alih-alih mendorong nilai benar atau salah ke tumpukan, ini menambahkan `1` ke nilai kedua di atas tumpukan jika tanda tangan valid, atau meninggalkan nilai ini tidak berubah jika tanda tangan mewakili vektor kosong. `OP_CHECKSIGADD` memungkinkan penciptaan kebijakan multisignature yang sama dalam Tapscript seperti dengan `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` tetapi dalam cara yang dapat diverifikasi secara batch, yang berarti menghilangkan proses pencarian dalam verifikasi multisig tradisional dan dengan demikian mempercepat verifikasi sambil mengurangi beban operasional pada CPU node. Opcode ini ditambahkan dalam Tapscript semata-mata untuk kebutuhan Taproot.