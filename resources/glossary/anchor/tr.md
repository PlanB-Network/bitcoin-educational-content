---
term: Anchor
definition: RGB protokolünde, bir Bitcoin işlemindeki taahhüdün dahil edilmesini kanıtlayan veri seti, içeriğini kamuya açıklamadan.
---

RGB protokolünde bir Anchor, bir işleme tek bir Commitment'in dahil edildiğini kanıtlamak için kullanılan bir dizi istemci tarafı verisini temsil eder. RGB protokolünde, bir Anchor aşağıdaki Elements'den oluşur:




- transaction ID Bitcoin (txid) Witness Transaction'ten ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Tapret Commitment mekanizması kullanılıyorsa Ekstra İşlem Kanıtı (ETP).


Bu nedenle bir Anchor, belirli bir Bitcoin işlemi ile RGB protokolü tarafından doğrulanan özel veriler arasında doğrulanabilir bir bağlantı kurmaya yarar. Bu verilerin, tam içerikleri kamuya açıklanmadan, gerçekten Blockchain'ye dahil edildiğini garanti eder.