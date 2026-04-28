---
term: OP_CHECKMULTISIG (0XAE)
definition: N adet genel anahtardan M adet imzanın geçerli olduğunu doğrulayan işlem kodu.
---

Birden fazla imzayı birden fazla açık anahtara karşı kontrol eder. Girdi olarak bir dizi `N` açık anahtar ve `M` imza alır; burada `M`, `N`'den küçük veya eşit olabilir. oP_CHECKMULTISIG` en az `M` imzanın `N` açık anahtarın `M`'si ile eşleşip eşleşmediğini doğrular. Tarihsel bir hata nedeniyle, `OP_CHECKMULTISIG` tarafından yığından ek bir öğenin kaldırıldığını unutmayın. Bu öğe "*kukla öğe*" olarak adlandırılır. Bu nedenle, `scriptSig`de bir hatadan kaçınmak için, işe yaramaz bir eleman olan bir `OP_0`, kaldırmayı karşılamak ve hatayı atlamak için dahil edilir. BIP147'den bu yana (2017'de SegWit ile tanıtıldı), hata nedeniyle tüketilen işe yaramaz öğe, bir işlenebilirlik vektörü olduğu için kodun geçerli olması için `OP_0` olmalıdır. Bu işlem kodu Tapscript'te kaldırılmıştır.