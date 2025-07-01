---
name: Pedoman Pengoreksian
description: Apa saja faktor penting yang perlu diingat sewaktu mengoreksi pada Plan ₿ Network?
---
![github](assets/cover.webp)


Selamat datang di tutorial tentang panduan yang harus diikuti saat mengoreksi konten di Plan ₿ Network. Kami senang Anda berbagi misi kami untuk menerjemahkan materi Bitcoin ke dalam sebanyak mungkin bahasa, untuk membantu orang mendapatkan kesadaran tentang cara kerjanya dan bagaimana hal ini dapat digunakan dalam kehidupan sehari-hari.


Pertama-tama, berkontribusi pada [repositori publik] Plan ₿ Network (https://github.com/PlanB-Network/Bitcoin-educational-content) memberi Anda kesempatan untuk menulis tutorial, mengoreksi konten yang sudah ada, atau bahkan mengusulkan penambahan bahasa baru pada platform ini. Untuk mengetahui lebih lanjut, bergabunglah dengan [Grup Telegram] (https://t.me/PlanBNetwork_ContentBuilder) kami terlebih dahulu, dan tulislah presentasi singkat tentang Anda dan bahasa yang Anda kuasai.


Tutorial ini didedikasikan untuk kontributor yang ingin mengoreksi konten. Kebanyakan dari mereka tidak tahu banyak tentang [Github](https://planb.network/en/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c) atau [Bahasa penurunan harga](https://www.markdownguide.org/basic-syntax/) yang kami gunakan di repositori, jadi penting untuk berbagi wawasan tentang hal-hal yang perlu mereka perhatikan saat menjalankan tugas ini.


Saya membuatnya setelah mengumpulkan masalah paling umum yang dihadapi oleh para korektor saat menyelesaikan tugas mereka. Jangan ragu untuk memberikan saran, karena hal ini dapat membantu orang lain untuk berkembang.


Sebelum membahas secara spesifik, hal pertama yang harus dilakukan adalah membaca tutorial ini tentang tindakan praktis yang dapat diterapkan di Github, dengan melakukan forking pada repositori Plan ₿ Network, melakukan perubahan, dan mengirim PR:


https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6

## Apa yang dimaksud dengan proofreading?


Proofreading adalah proses peninjauan akhir dari sebuah teks tertulis, untuk mengidentifikasi dan memperbaiki kesalahan dalam tata bahasa, ejaan, tanda baca, dan format. Proses ini memastikan bahwa teks tersebut jelas, koheren, dan bebas dari kesalahan sebelum dipublikasikan atau diserahkan.


Apabila Anda menjalani jenis tugas ini, penting untuk mengikuti makna bahasa aslinya (EN atau FR), tetapi pastikan bahwa teks dalam bahasa akhir selancar mungkin bagi penutur asli.


## Langkah pertama sebelum mengoreksi pada Plan ₿ Network


Sebelum memulai tugas pemeriksaan baru, umumkanlah di [grup Telegram](https://t.me/PlanBNetwork_ContentBuilder) atau beritahukan koordinator Plan ₿ Network Anda, yang akan membuka [isu] khusus(https://github.com/orgs/PlanB-Network/projects/3). Ketika Anda menerima tautan isu, cukup beri komentar bahwa Anda memulai tugas proofreading untuk konten tersebut.

Sistem ini memungkinkan koordinator untuk melacak kemajuan di dalam repo, dan memungkinkan konten untuk "diklaim" oleh korektor, mencegah upaya duplikasi oleh orang lain.

Pada isu itu sendiri, Anda akan menemukan tautan yang membawa Anda langsung ke konten untuk diperiksa. Anda bisa langsung mengkliknya, atau bahkan lebih baik lagi, Anda bisa kembali ke repositori bercabang Anda sendiri dan bekerja langsung dari sana.


Pertama-tama, SELALU ingat untuk MENYINKRONISASI repo Anda, pada cabang "dev". Dengan cara ini, konten akan selalu diperbarui sebelum Anda memulai jenis tugas apa pun, dan Anda tidak akan membuat konflik antara materi lama dan baru. Pastikan untuk mengklik "Sinkronisasi Fork" dan "Perbarui cabang".



![REVIEW](assets/en/1.webp)



Setelah berhasil menyinkronkan, Anda dapat langsung mengakses konten yang diinginkan dan melakukan komit di cabang baru, seperti yang ditunjukkan dalam [tutorial] ini (https://planb.network/tutorials/contribution/content/contribution-proofreading-review-tutorial-1ee068ca-ddaf-4bec-b44e-b41a9abfdef6). Jika tidak, Anda dapat membuka cabang baru tempat bekerja, dengan mengklik "Cabang", seperti yang ditunjukkan di bawah ini.



![REVIEW](assets/en/2.webp)



Di dalam halaman baru ini, Anda akan menemukan semua cabang yang telah Anda buka di bawah judul "Cabang Anda". Bagian ini sangat berguna karena memungkinkan Anda untuk dengan mudah menemukan tempat di mana Anda memodifikasi beberapa konten. Jika Anda ingin membuka cabang baru, Anda dapat mengklik "Cabang Baru" di sudut kanan atas halaman.


![REVIEW](assets/en/3.webp)



Kemudian, Anda akan mendapatkan pop-up di mana Anda perlu memasukkan nama cabang baru. Dalam kasus di bawah ini, saya memilih untuk menamainya "BTC101-FR". Dengan cara ini, saya akan selalu ingat bahwa cabang khusus ini perlu digunakan untuk mengoreksi kursus BTC101 dalam bahasa Prancis, dan **saya tidak akan menggunakannya untuk tugas lain**.


Saya sarankan Anda melakukan hal yang sama: pastikan untuk membuka cabang baru kapan pun Anda perlu memulai tugas baru.



![REVIEW](assets/en/4.webp)



Setelah membuat cabang baru ini, pastikan untuk mengkliknya dari "Cabang Anda" di halaman sebelumnya dan mulai mengerjakan file *.md* yang terkait dengan konten tertentu (dalam kasus saya, saya akan mengklik folder "courses", dan sub-folder BTC101, untuk mencari fr.md). Semua komit yang terkait dengan file tertentu harus dikomit (disimpan) di dalam cabang yang sama.


## Bahasa asli atau terjemahan?


Ketika melakukan pemeriksaan ulang konten, penting untuk selalu memeriksa versi asli bahasa Inggris (atau Prancis). Perlu diketahui bahwa kami menerjemahkan menggunakan alat bantu bahasa AI, sehingga hasil terjemahan dalam bahasa target mungkin tidak lancar atau tidak dapat dimengerti dengan baik oleh pembaca akhir.


Oleh karena itu, jangan ragu untuk melakukan penyesuaian pada teks dan memodifikasi kalimat, jika diperlukan. Tujuan kami adalah untuk meningkatkan kelancaran, tetapi selalu mengikuti makna aslinya. Jika ada keraguan tentang cara memperlakukan kata tertentu, pastikan untuk bertanya kepada koordinator penerjemahan.


Alat bantu LLM dapat menerjemahkan beberapa kata yang berhubungan dengan Bitcoin secara harfiah, seperti Lightning Network, yang akan menjadi "Rete Fulmine" dalam bahasa Italia, misalnya.


Hal ini terutama terjadi ketika berhubungan dengan kata-kata yang sangat teknis. Dalam kasus seperti ini, disarankan untuk mempertahankan kata asli bahasa Inggris pada bahasa target Anda untuk kejelasan yang lebih baik, kecuali jika peraturan bahasa Anda mengharuskan Anda untuk menerjemahkan setiap kata. Dalam kasus kedua ini, selalu lakukan penelitian untuk melihat apakah ada orang lain dalam komunitas Bitcoin Anda yang telah menerjemahkan kata tersebut dan kata tersebut sekarang digunakan secara luas.



- Salah satu solusinya adalah dengan memeriksa [BitcoinWiki] (https://en.Bitcoin.it/wiki/Main_Page) dalam bahasa target Anda untuk melihat apakah kata tersebut sudah diterjemahkan atau belum. Jika belum, Anda tetap menggunakan kata tersebut dalam bahasa Inggris.



- Bagaimanapun, saran saya adalah tetap memasukkan kata EN, dan kemudian arti yang sesuai dalam bahasa target di dalam tanda kurung, mengikuti skema EN (LANG), atau sebaliknya. Contoh. Address (indirizzo) atau indirizzo (Address).



- Solusi lain yang baik adalah dengan mempertahankan kata/frasa asli EN, kemudian membuat hyperlink yang mengarahkan ke [glosarium](https://planb.network/en/resources/glossary) di planb.network. Untuk melakukan ini, Anda perlu memasukkan kata/frasa di dalam tanda kurung siku, dan tautan di dalam tanda kurung bulat, seperti yang dapat Anda lihat pada contoh di bawah ini:


```
[UTXO](https://planb.network/resources/glossary/utxo)
```


Pada hasil akhir (gambar di bawah), Anda tidak akan memvisualisasikan seluruh tautan, dan kata tersebut akan dapat diklik.


![REVIEW](assets/en/5.webp)



Harap diperhatikan bahwa tautan glosarium yang akan Anda ambil dari situs web berisi kode bahasa setelah kata "network" (contoh: ``https://planb.network/en/resources/glossary/UTXO``-> di sini Anda dapat membaca kode bahasa "en"). Dalam kasus ini, hapus kode bahasa dari tautan tersebut, seperti yang Anda lihat pada kotak di atas. Dengan cara ini, sistem akan secara otomatis membawa pembaca ke bahasa yang ditentukan.


Konten pada repo penuh dengan hyperlink seperti di atas. Setelah Anda mengetahui apa maksudnya, pastikan untuk tidak menghapus tautan apa pun yang disisipkan oleh penulis.


Hal lain yang terkait dengan rendering kata adalah sebagai berikut. Jika Anda menemukan "Plan ₿ Network" dalam teks, biarkan dalam bentuk aslinya. Jangan menerjemahkan kata "rencana" atau kata "jaringan". Selain itu, JANGAN gunakan kata sandang "The" ketika memperkenalkan Plan ₿ Network, dan **anggaplah sebagai merek**.


Hal yang sama berlaku untuk "₿-CERT", "BIZ SCHOOL", "TECH SCHOOL", yang juga harus disimpan dalam bentuk aslinya.


Satu catatan terakhir untuk paragraf ini: seperti yang kami katakan di atas, kami menggunakan alat bantu AI untuk menerjemahkan konten, dan kemudian kami meminta campur tangan "manusia" untuk memastikan semuanya lancar dan terkoreksi dengan baik.


Ketika Anda mengoreksi menggunakan AI untuk sebagian besar teks, kami pasti akan menyadarinya, karena kami sudah terbiasa dengan struktur kalimat yang dihasilkan AI. Jika kami menemukan bahwa Anda hanya mengandalkan AI untuk mengoreksi, tanpa melakukan perubahan yang signifikan, hadiah akhir di Sats dapat dikurangi setengahnya!


## Struktur tajuk


Dalam bahasa markdown, tajuk (dan judul paragraf) semuanya dimulai dengan tanda Hash ``#``. Jumlah tanda Hash sesuai dengan tingkat judul. Sebagai contoh, tajuk level tiga memiliki tiga tanda angka sebelum teks (misalnya, `### Tajuk Saya`).


Dalam kursus, bagian yang paling penting diperkenalkan dengan satu tanda Hash tunggal, sedangkan sub-bagian dapat memiliki dua hingga empat tanda Hash. Dalam tutorial, kami biasanya hanya menggunakan header dengan dua tanda Hash.



![REVIEW](assets/en/6.webp)


Pastikan untuk **JANGAN PERNAH** menghapus tanda Hash sebelum judul, jika tidak, Anda akan menimbulkan masalah dengan struktur teks.


Pada saat yang sama, **jangan** mengubah bagian chapterID yang dapat Anda lihat pada gambar di atas, ``<chapterId>d668fdf6-fb4c-4bbf-82e1-afcb95c122e0</chapterId>`` atau referensi video seperti ``:::video id=ba99951f-81d2-418f-b5e7-4b8c9f8b8cc8:::``.


Ketika kita menyisipkan ``#`` sebelum sebuah judul, maka secara otomatis judul tersebut akan menjadi tebal di pratinjau kursus, jadi hindari membuat judul menjadi tebal selama koreksi.


Selain itu, dalam versi bahasa Inggris, judul yang memiliki satu atau dua ``#`` memiliki semua kata yang dimulai dengan huruf kapital, sedangkan judul yang dimulai dengan tiga atau empat, biasanya tidak mengikuti aturan ini. Jika memungkinkan, pastikan judul dalam bahasa target Anda mengikuti struktur ini.


## Bagian awal kursus


Pada awal konten apa pun, Anda akan menemukan kata-kata huruf kecil statis berikut ini: "nama", "deskripsi", "tujuan". Kata-kata ini digunakan oleh situs web untuk menerjemahkan konten itu sendiri dan **selalu dibiarkan dalam bahasa Inggris**. Oleh karena itu, JANGAN menerjemahkannya, jika tidak, konten akan menimbulkan masalah sinkronisasi. Pastikan Anda hanya mengoreksi bagian setelah titik dua, yang secara otomatis diterjemahkan oleh AI.



![REVIEW](assets/en/7.webp)



Pada bagian awal yang sama ini, pertahankan format seperti apa adanya. Jangan menambahkan apa pun di awal teks. Contoh: hindari menambahkan "tt" sebelum tanda hubung, seperti pada gambar di bawah ini!



![REVIEW](assets/en/8.webp)


## Rekomendasi format


Di bawah ini Anda dapat menemukan beberapa contoh masalah format yang perlu diperhatikan saat mengoreksi konten dalam bahasa target Anda.



- Perhatikan tanda baca yang aneh seperti `\*\*\`, atau ``**`` yang mungkin mewakili rendering yang buruk dari simbol tebal. Pada gambar di bawah ini, Anda dapat melihat bahwa tanda bintang hanya berada di sebelah kanan kata, yang terlihat aneh.


![REVIEW](assets/en/9.webp)



Selalu periksa teks bahasa Inggris asli untuk melihat apakah teks yang dicetak tebal memang seharusnya ada di sana. Dalam kasus ini, cukup dengan menambahkan dua tanda bintang di awal kata, untuk membuatnya ditampilkan dengan benar di situs web. Bahkan dalam bahasa markdown, untuk membuat huruf tebal, Anda harus menyisipkan dua tanda bintang ``**`` sebelum dan sesudah kata/kalimat (lihat contoh di bawah).



![REVIEW](assets/en/10.webp)




- Masalah yang sama dapat terjadi pada simbol seperti $ dan `` ``.

Pastikan untuk memeriksa file bahasa asli (biasanya EN atau FR) untuk melihat di mana simbol-simbol ini seharusnya berada. Anda selalu dapat meminta bantuan koordinator untuk masalah ini.



- Jika Anda menemukan tanda kutip, pastikan untuk melakukan riset online untuk menemukan terjemahan yang tepat dalam bahasa Anda. Kutipan biasanya disisipkan setelah simbol ``>``.



![REVIEW](assets/en/11.webp)


## Pengoreksian kuis


Tahukah Anda bahwa Anda juga bisa mengoreksi pertanyaan kuis di setiap mata kuliah? Misalnya, jika Anda ingin mengoreksi kuis untuk BTC101 di mata kuliah IT, Anda dapat membuka cabang khusus dan mengikuti cara ini: "kursus" -> "BTC101" -> "kuis" Di sana, Anda akan menemukan semua folder yang didedikasikan untuk setiap pertanyaan, bersama dengan file bahasa terkait dalam format _yml_.


Sekali lagi, pastikan Anda berada di cabang khusus yang Anda buka secara khusus untuk tujuan ini, dan selalu informasikan kepada koordinator.


Setelah meninjau pertanyaan, pastikan Anda mengubah status "ditinjau" dari "salah" menjadi "benar", seperti yang ditunjukkan pada gambar di bawah ini.


![REVIEW](assets/en/12.webp)


## Praktik terbaik lainnya


Jika Anda perlu mencari kata-kata tertentu di dalam teks, Anda bisa mengklik ``CTRL+F`` dan bagian find-replace (cari-ganti) akan muncul. Bagian ini sangat berguna apabila Anda perlu melompat ke bagian teks tertentu, atau Anda perlu mengganti kata/kalimat tertentu secara batch, tanpa menggulir seluruh konten.



![REVIEW](assets/en/13.webp)



Ketika menggunakan fungsi "ganti semua", penting untuk memeriksa ulang hasilnya untuk memastikan bahwa tautan juga belum diubah. Misalnya, jika Anda ingin mengubah kata "Bitcoin" menjadi "Bitcoin" (yang mungkin diperlukan dalam beberapa bahasa), menggunakan fungsi "ganti semua" dapat secara efisien memperbarui semua contoh di dalam teks. Namun, perlu diketahui bahwa alat ini juga akan memodifikasi setiap tautan yang mengandung kata tersebut, yang berpotensi menyebabkan masalah pengalihan.


Pada contoh di bawah ini, proofreader menggunakan fungsi di atas untuk mengganti "Satoshi" dengan "Satoshi (Sats)", dan juga mengubah tautan ke tutorial yang berisi kata itu sendiri. Akibatnya, tautan tersebut menjadi tidak valid.


![REVIEW](assets/en/14.webp)


Mengikuti topik tautan, jika penulis menyisipkan tautan yang merujuk ke kursus tutorial Plan ₿ Network, situs web akan secara otomatis membuat "kartu" yang menunjukkan thumbnail terkait. Sebagai konsekuensinya, selalu pastikan bahwa Anda memiliki spasi di antara teks dan tautan itu sendiri, jika tidak, Anda mungkin akan melihat kesalahan berikut ini pada situs web.


![REVIEW](assets/en/15.webp)




Terakhir, praktik terbaik lainnya yang dapat diterapkan ketika Anda menyelesaikan tugas proofreading dan mengirimkan PR adalah kembali ke edisi asli yang dibuka oleh koordinator, dan berkomentar dengan "Proofreading selesai". Pastikan juga untuk memasukkan tautan PR Anda di sana.


## Kesimpulan


Singkatnya, menyadari kesalahan umum yang dilakukan oleh proofreader dapat sangat membantu Anda meningkatkan keterampilan Anda saat memeriksa konten. Sangat mudah untuk mengabaikan hal-hal seperti konteks atau konsistensi, jadi, menangkap kesalahan ini dapat membuat perbedaan besar. Ingatlah selalu bahwa seorang pemula mungkin membaca kursus dan tutorial ini, jadi tanggung jawab kita untuk memastikan bahwa mereka memahami sepenuhnya.


Terima kasih telah membaca tutorial ini, dan selamat menikmati perjalanan proofreading Anda!