---
term: OP_CHECKSIGADD (0XBA)

---
Mengekstrak tiga nilai teratas dari tumpukan: `kunci publik`, `CScriptNum` `n`, dan `tanda tangan`. Jika tanda tangan bukan vektor kosong dan tidak valid, skrip akan diakhiri sebagai salah. Jika tanda tangan valid atau vektor kosong (`OP_0`), dua skenario akan ditampilkan:

- Jika tanda tangan adalah vektor kosong: sebuah `CScriptNum` dengan nilai `n` didorong ke dalam stack, dan eksekusi dilanjutkan;
- Jika tanda tangan bukan vektor kosong dan tetap valid: sebuah `CScriptNum` dengan nilai `n + 1` didorong ke _stack_, dan eksekusi dilanjutkan.

Untuk menyederhanakan, `OP_CHECKSIGADD` melakukan operasi yang mirip dengan `OP_CHECKSIG`, tetapi alih-alih mendorong nilai benar atau salah ke _stack_, ia menambahkan `1` ke nilai kedua di bagian atas tumpukan jika tanda tangan valid, atau membiarkan nilai ini tidak berubah jika tanda tangan merepresentasikan vektor kosong. `OP_CHECKMULTISIGADD` memungkinkan pembuatan kebijakan _multisignature_ yang sama di Tapscript seperti halnya `OP_CHECKMULTISIG` dan `OP_CHECKMULTISIGVERIFY` tetapi dengan cara yang dapat diverifikasi secara _batch_, yang berarti menghapus proses pencarian dalam verifikasi _multisig_ tradisional dan dengan demikian mempercepat verifikasi sekaligus mengurangi beban operasional pada CPU node. Opcode ini ditambahkan dalam Tapscript semata-mata untuk kebutuhan Taproot.
