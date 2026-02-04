---
term: OP_NOP (0X61)
definition: Hiçbir etkisi olmayan, gelecekteki soft fork'lar için bir ekleme noktası olarak kullanılan opcode.
---

Yığın veya kodun durumu üzerinde hiçbir etki oluşturmaz. Hiçbir hareket, kontrol veya değişiklik gerçekleştirmez. Bir Soft Fork aracılığıyla aksi kararlaştırılmadıkça hiçbir şey yapmaz. Aslında, 2010 yılında Satoshi Nakamoto tarafından değiştirilmelerinden bu yana, `OP_NOP` komutları (`OP_NOP1` (`0XB0`) ila `OP_NOP10` (`0XB9`)) bir Soft Fork şeklinde yeni opcode'lar eklemek için kullanılır.


Böylece, `OP_NOP2` (`0XB1`) ve `OP_NOP3` (`0XB2`) sırasıyla `OP_CHECKLOCKTIMEVERIFY` ve `OP_CHECKSEQUENCEVERIFY` uygulamak için zaten kullanılmıştır. Bunlar, ilişkili zamansal değerleri yığından kaldırmak için `OP_DROP` ile birlikte kullanılır, böylece düğüm güncel olsun ya da olmasın kodun yürütülmesine devam edilmesine izin verilir. Bu nedenle `OP_NOP` komutları, zaten var olan veya gelecekteki Soft çatallarıyla eklenebilecek ek koşulları kontrol etmek için bir komut dosyasına bir kesinti noktası eklenmesine izin verir. Tapscript'ten bu yana, `OP_NOP` kullanımı daha verimli olan `OP_SUCCESS` ile değiştirilmiştir.