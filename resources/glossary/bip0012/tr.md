---
term: BIP0012
definition: İç içe geçmiş betikler için OP_EVAL işlem kodunu (opcode) tanıtan, güvenlik nedeniyle yerini BIP16'ya (P2SH) bırakan teklif.
---

Gavin Andresen tarafından Bitcoin işlem komut dosyalarının esnekliğini ve gizliliğini artırmak için öneri. Bu BIP, işlem doğrulama işlemi sırasında bir `scriptSig` verisi içinde bulunan bir komut dosyasının değerlendirilmesine olanak tanıyan `OP_EVAL` adlı yeni bir komut dosyası işlem kodunun uygulanmasını önermektedir. BIP12'nin ana değişikliği, bir komut dosyasının başka bir komut dosyasının içine dahil edilmesine izin vermektir. Bu teknik, kullanılan Address'a bitcoin gönderen kullanıcılara açıklamak zorunda kalmadan, harcama sırasında doğrulanabilen daha karmaşık koşulların oluşturulmasını sağlar. BIP12 daha sonra yerini daha güvenli önerilere, özellikle de `OP_EVAL` ile aynı hedeflere ulaşmak için farklı bir yöntem sunan BIP16'ya (P2SH) bırakmıştır.