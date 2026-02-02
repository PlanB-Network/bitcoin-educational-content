---
term: Sigops (imza işlemleri)
definition: Bitcoin işlemlerini doğrulamak için gerekli olan dijital imza işlemleri.
---

İşlemleri doğrulamak için gerekli dijital imza işlemlerini ifade eder. Her bir Bitcoin işlemi birden fazla girdi içerebilir ve bunların her birinin geçerli sayılması için bir veya daha fazla imza gerekebilir. Bu imzaların doğrulanması, "sigops" adı verilen belirli işlem kodlarının kullanılmasıyla yapılır. Bunlar özellikle `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` ve `OP_CHECKMULTISIGVERIFY` işlemlerini içerir. Bu işlemler, bunları doğrulaması gereken ağ düğümlerine belirli bir iş yükü getirmektedir. Bu nedenle protokol, sigop sayısının yapay olarak şişirilmesi yoluyla DoS saldırılarını önlemek için, doğrulama yükünün düğümler için yönetilebilir kalmasını sağlamak amacıyla blok başına izin verilen sigop sayısına bir sınır getirir. Bu sınır şu anda blok başına maksimum 80.000 sigop olarak belirlenmiştir. Saymak için düğümler şu kuralları takip eder:


ScriptPubKey`de, `OP_CHECKSIG` ve `OP_CHECKSIGVERIFY` 4 sigop olarak sayılır. OP_CHECKMULTISIG` ve `OP_CHECKMULTISIGVERIFY` işlem kodları 80 sigop olarak sayılır. Aslında, sayım sırasında, bu işlemler bir SegWit girişinin parçası olmadıklarında 4 ile çarpılır (bir P2WPKH için sigop sayısı bu nedenle 1 olacaktır);


redeemscript`te, `OP_CHECKSIG` ve `OP_CHECKSIGVERIFY` işlem kodları da 4 sigop olarak sayılır, `OP_CHECKMULTISIG` ve `OP_CHECKMULTISIGVERIFY`, `OP_n`den önce gelirse `4n`, aksi takdirde 80 sigop olarak hesaplanır;


TanıkScript` için, `OP_CHECKSIG` ve `OP_CHECKSIGVERIFY` 1 sigop değerindedir, `OP_CHECKMULTISIG` ve `OP_CHECKMULTISIGVERIFY` `OP_n` tarafından tanıtılmışsa `n`, aksi takdirde 20 sigop olarak sayılır;


Taproot komut dosyalarında sigops, geleneksel komut dosyalarına kıyasla farklı şekilde ele alınır. Her imza işlemini doğrudan saymak yerine, Taproot her işlem girdisi için bu girdinin boyutuyla orantılı bir sigops bütçesi sunar. Bu bütçe 50 sigops artı girdinin tanığının bayt boyutudur. Her imza işlemi bu bütçeyi 50 azaltır. Bir imza işleminin yürütülmesi bütçeyi sıfırın altına düşürürse, kod geçersiz olur. Bu yöntem, Taproot komut dosyalarında daha fazla esneklik sağlarken, sigop'ları doğrudan girdinin ağırlığına bağlayarak sigop'larla ilgili olası kötüye kullanımlara karşı koruma sağlar. Bu nedenle, Taproot komut dosyaları blok başına 80.000 sigop sınırına dahil değildir.