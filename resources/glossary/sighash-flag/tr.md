---
term: Sighash bayrağı
definition: Bir işlemin hangi bileşenlerinin imza tarafından kapsandığını belirleyen parametre.
---

Bir Bitcoin işleminde, bir işlemin hangi bileşenlerinin (girdiler ve çıktılar) ilgili imza tarafından kapsanacağını ve böylece değişmez hale geleceğini belirleyen bir parametre. SigHash Bayrağı her bir girdinin dijital imzasına eklenen bir bayttır. Bu nedenle SigHash Bayrağı seçimi, işlemin hangi kısımlarının imza tarafından dondurulduğunu ve hangilerinin daha sonra değiştirilebileceğini doğrudan etkiler. Bu mekanizma, imzaların işlem verilerini imzalayanın niyetine göre kesin ve güvenli bir şekilde işlemesini sağlar. Üç ana SigHash Bayrağı vardır:



- `SIGHASH_ALL` (`0x01`): İmza, işlemin tüm girdileri ve çıktıları için geçerlidir, böylece onları tamamen kilitler;



- `SIGHASH_NONE` (`0x02`): İmza tüm girdilere uygulanır ancak çıktıların hiçbirine uygulanmaz ve çıktıların imzadan sonra değiştirilmesine izin verir;



- `SIGHASH_SINGLE` (`0x03`): İmza tüm girdileri ve imzalı girdinin indeksine karşılık gelen yalnızca bir çıktıyı kapsar.


Bu üç SigHash Bayrağına ek olarak, `SIGHASH_ANYONECANPAY` (`0x80`) değiştiricisi önceki türlerin her biriyle birleştirilebilir. Bu değiştirici kullanıldığında, girdilerin yalnızca bir kısmı imzalanır ve diğerleri değiştirilmeye açık bırakılır. İşte değiştirici ile mevcut kombinasyonlar:



- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): İmza, işlemin tüm çıktılarını kapsarken tek bir girdi için geçerlidir;



- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): İmza, herhangi bir çıktı taahhüt etmeden tek bir girdiyi kapsar;



- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): İmza tek bir girdi için ve yalnızca bu girdiyle aynı indekse sahip çıktı için geçerlidir.


> ► *Bazen "SigHash" için kullanılan eşanlamlı bir ifade "Signature Hash Types "dir.*