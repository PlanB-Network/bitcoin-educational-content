---
term: OP_SUCCESS
definition: Tapscript'te otomatik başarıyı gösteren ayrılmış opcode'lar; gelecekteki soft fork'lar için kullanılır.
---

OP_SUCCESS` geçmişte devre dışı bırakılmış ve şimdi Tapscript'te gelecekte kullanılmak üzere ayrılmış bir dizi işlem kodunu temsil eder. Nihai amaçları, Soft çatalları aracılığıyla yeni işlevlerin eklenmesine izin vererek komut dosyası dilinin güncellemelerini ve uzantılarını kolaylaştırmaktır. Bir komut dosyasında bu işlem kodlarından birine rastlandığında, mevcut veri veya koşullardan bağımsız olarak komut dosyasının o bölümünün otomatik olarak başarılı olduğunu gösterir. Bu, komut dosyasının önceki işlemlerden bağımsız olarak hatasız bir şekilde yürütülmeye devam ettiği anlamına gelir.


Bu nedenle, bir `OP_SUCCESS` üzerine yeni bir işlem kodu eklendiğinde, bu mutlaka bir öncekinden daha kısıtlayıcı bir kuralın eklendiğini temsil eder. Güncellenen düğümler daha sonra bu kurala uygunluğu doğrulayabilir ve güncellenmeyen düğümler ilişkili işlemleri ve bunları içeren blokları reddetmeyecektir, çünkü `OP_SUCCESS` komut dosyasının bu bölümünü doğrular. Bu nedenle, Hard Fork yoktur.


Buna karşılık, `OP_NOP` (*İşlem Yok*) da kod içinde yer tutucu görevi görür, ancak kodun yürütülmesi üzerinde hiçbir etkisi yoktur. Bir `OP_NOP` ile karşılaşıldığında, kod, yığının durumunu veya kodun ilerleyişini değiştirmeden devam eder. Bu nedenle, temel fark yürütme üzerindeki etkileridir: `OP_SUCCESS` kodun o bölümünden başarılı bir geçişi garanti ederken, `OP_NOP` nötrdür ve ne yığını ne de kodun akışını etkilemez. Bu işlem kodları `OP_SUCCESSN` ile belirtilir, burada `N` `OP_SUCCESS`i ayırt etmek için kullanılan bir sayıdır.