---
term: Adres yeniden kullanımı
definition: Aynı Bitcoin adresini birden fazla kez ödeme almak için kullanmanın önerilmeyen bir uygulaması, bu da fonların izlenmesine izin vererek gizliliğe zarar veriyor.
---

Address'ün yeniden kullanımı, bazen birkaç farklı işlemde birden fazla UTXO'yu engellemek için aynı alıcı Address'ü kullanma uygulamasını ifade eder. Bitcoinler tipik olarak benzersiz bir Address'e karşılık gelen bir kriptografik anahtar çifti kullanılarak kilitlenir. Blockchain herkese açık olduğundan, hangi adreslerin kaç bitcoin ile ilişkili olduğunu görmek kolaydır. Aynı Address'ün birden fazla ödeme için yeniden kullanılması durumunda, ilişkili tüm UTXO'ların aynı varlığa ait olduğunu düşünmek mantıklıdır. Bu nedenle, Address'ün yeniden kullanımı kullanıcının gizliliği için bir sorun teşkil eder. Birden fazla işlem ve UTXO arasında deterministik bağlantıların yanı sıra On-Chain fon takibinin sürdürülmesine olanak tanır. KİS-4 Nakamoto Beyaz Kitap'ında bu sorundan zaten bahsetmiştir:


> *Ek bir güvenlik duvarı olarak, her işlem için yeni bir anahtar çifti kullanılmalı ve bunların ortak bir sahibine bağlanması engellenmelidir.*


Nakamoto, S. (2008). "*Bitcoin: A Peer-to-Peer Electronic Cash System*". https://bitcoin.org/bitcoin.pdf.

Gizliliği en az düzeyde korumak için, her alıcı Address'nin yalnızca bir kez kullanılması şiddetle tavsiye edilir. Her yeni ödeme için yeni bir generate Address kullanılması uygundur. Değişiklik çıktıları için de yeni bir Address kullanılmalıdır. Neyse ki, deterministik ve hiyerarşik cüzdanlar sayesinde çok sayıda adres kullanmak çok kolay hale gelmiştir. Bir Wallet ile ilişkili tüm anahtar çiftleri seed'dan kolayca yeniden oluşturulabilir. Wallet yazılımının "Al" düğmesine tıkladığınızda her zaman yeni ve farklı bir Address üretmesinin nedeni de budur.

