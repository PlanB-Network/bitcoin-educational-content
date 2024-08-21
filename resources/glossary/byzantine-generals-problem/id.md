---
term: MASALAH JENDERAL BIZANTIUM
---

Masalah ini pertama kali dirumuskan oleh Leslie Lamport, Robert Shostak, dan Marshall Pease dalam majalah spesialis *ACM Transactions on Programming Languages and Systems, vol 4, n° 3* ["The Byzantine Generals Problem"](https://lamport.azurewebsites.net/pubs/byz.pdf) pada Juli 1982. Masalah ini digunakan hari ini untuk mengilustrasikan tantangan dalam hal pengambilan keputusan ketika sebuah sistem terdistribusi tidak dapat mempercayai aktor mana pun.

Dalam metafora ini, sekelompok jenderal Bizantium dan pasukan masing-masing berkemah di sekitar kota yang ingin mereka serang atau kepung. Para jenderal terpisah secara geografis satu sama lain dan harus berkomunikasi melalui utusan untuk mengoordinasikan strategi mereka. Apakah mereka menyerang atau mundur tidak masalah, selama semua jenderal mencapai konsensus.

Oleh karena itu, kita dapat mempertimbangkan persyaratan berikut:
* Setiap jenderal harus membuat keputusan: menyerang atau mundur (ya atau tidak);
* Setelah keputusan dibuat, itu tidak dapat diubah;
* Semua jenderal harus setuju pada keputusan yang sama dan melaksanakannya secara sinkron.

Lebih lanjut, seorang jenderal hanya dapat berkomunikasi dengan jenderal lain melalui pesan yang disampaikan oleh kurir, yang bisa terlambat, dihancurkan, diubah, atau hilang. Dan bahkan jika sebuah pesan berhasil dikirim, satu atau lebih jenderal mungkin memilih (untuk alasan apa pun) untuk mengkhianati kepercayaan yang telah ditetapkan dan mengirim pesan palsu, menabur kekacauan.

Menerapkan dilema ini ke konteks blockchain Bitcoin, setiap jenderal mewakili sebuah node dalam jaringan, yang perlu mencapai konsensus tentang keadaan sistem. Dengan kata lain, mayoritas peserta dalam jaringan terdistribusi harus setuju dan melaksanakan tindakan yang sama untuk menghindari kegagalan total. Satu-satunya cara untuk mencapai konsensus dalam jenis sistem terdistribusi ini adalah dengan memiliki setidaknya 2/3 dari node jaringan yang dapat diandalkan dan jujur. Oleh karena itu, jika mayoritas jaringan memutuskan untuk bertindak secara jahat, sistem tersebut rentan.

> ► *Dilema ini terkadang juga disebut "Masalah Siaran yang Dapat Diandalkan."*