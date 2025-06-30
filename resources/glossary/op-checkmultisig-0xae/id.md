---
term: OP_CHECKMULTISIG (0XAE)

---
Memeriksa beberapa tanda tangan terhadap beberapa kunci publik. Dibutuhkan sebagai masukan serangkaian kunci publik `N` dan tanda tangan `M`, di mana  nilai `M` dapat kurang dari atau sama dengan `N`. `OP_CHECKMULTISIG` memverifikasi apakah setidaknya tanda tangan `M` cocok dengan `M` dari kunci publik `N`. Perhatikan bahwa karena adanya _bug off-by-one_ historis, sebuah elemen tambahan dihapus oleh `OP_CHECKMULTISIG` dari tumpukan. Elemen ini disebut "*elemen tiruan*". Untuk menghindari kesalahan pada `scriptSig`, sebuah `OP_0`, yang merupakan elemen yang tidak berguna, oleh karena itu disertakan untuk memenuhi penghapusan dan melewati _bug_. Sejak BIP147 (diperkenalkan dengan SegWit pada tahun 2017), elemen yang tidak berguna yang dikonsumsi karena _bug_ haruslah `OP_0` agar skrip menjadi valid, karena ini termasuk suatu vektor maleabilitas. _Opcode_ ini telah dihapus di Tapscript.
