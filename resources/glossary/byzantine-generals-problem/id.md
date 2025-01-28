---
term: MASALAH PARA JENDERAL BIZANTIUM

---
Masalah ini pertama kali dirumuskan oleh Leslie Lamport, Robert Shostak, dan Marshall Pease dalam majalah khusus *ACM Transactions on Programming Languages and Systems, vol 4, no. 3* ["The Byzantine Generals Problem"] (https://lamport.azurewebsites.net/pubs/byz.pdf) pada bulan Juli 1982. Hal ini digunakan saat ini untuk mengilustrasikan tantangan dalam hal pengambilan keputusan ketika sistem terdistribusi tidak dapat mempercayai aktor mana pun.

Dalam metafora ini, sekelompok jenderal Bizantium dan pasukannya masing-masing berkemah di sekitar kota yang ingin mereka serang atau kepung. Para jenderal secara geografis terpisah satu sama lain dan harus berkomunikasi melalui kurir untuk mengoordinasikan strategi mereka. Apakah mereka menyerang atau mundur tidak menjadi masalah, selama semua jenderal mencapai kesepakatan.

Oleh karena itu, kami dapat mempertimbangkan persyaratan berikut:


- Setiap jenderal harus membuat keputusan: menyerang atau mundur (ya atau tidak);
- Setelah keputusan dibuat, keputusan tersebut tidak dapat diubah;
- Semua jenderal harus menyetujui keputusan yang sama dan melaksanakannya secara serempak.

Selain itu, seorang jenderal hanya dapat berkomunikasi dengan jenderal lain melalui pesan yang dikirimkan oleh kurir, yang dapat ditunda, dihancurkan, diubah, atau hilang. Dan bahkan jika sebuah pesan berhasil disampaikan, satu atau beberapa jenderal dapat memilih (dengan alasan apa pun) untuk mengkhianati kepercayaan yang telah terjalin dan mengirimkan pesan palsu, sehingga menimbulkan kekacauan.

Menerapkan dilema ini ke dalam konteks blockchain Bitcoin, setiap jenderal mewakili sebuah node di dalam jaringan, yang perlu mencapai sebuah konsensus mengenai keadaan sistem. Dengan kata lain, mayoritas partisipan dalam jaringan terdistribusi harus setuju dan melakukan tindakan yang sama untuk menghindari kegagalan total. Satu-satunya cara untuk mencapai konsensus dalam sistem terdistribusi jenis ini adalah dengan memiliki setidaknya 2/3 node jaringan yang dapat diandalkan dan jujur. Oleh karena itu, jika mayoritas jaringan memutuskan untuk bertindak jahat, sistem akan rentan.

> ► *Dilema ini kadang-kadang juga disebut "Masalah Siaran yang Dapat Diandalkan. "*