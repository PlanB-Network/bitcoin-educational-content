---
term: BIP0032
---

BIP32 hiyerarşik deterministik Wallet (HD Wallet) kavramını tanıtmıştır. Bu öneri, tek yönlü türetme işlevleri kullanılarak ortak bir `ana seed`den bir anahtar çifti hiyerarşisi oluşturulmasına izin verir. Üretilen her bir anahtar çiftinin kendisi diğer alt anahtarların ebeveyni olabilir ve böylece ağaç benzeri (hiyerarşik) bir yapı oluşturur. BIP32'nin avantajı, birden fazla farklı anahtar çiftinin yönetimine olanak sağlaması ve bunları yeniden oluşturmak için yalnızca tek bir seed tutmaya ihtiyaç duymasıdır. Bu yenilik, kullanıcı gizliliği açısından ciddi bir sorun olan Address'ın yeniden kullanımı sorunuyla mücadeleye önemli ölçüde yardımcı olmuştur. BIP32 ayrıca yönetimini kolaylaştırmak için aynı Wallet içinde alt dalların oluşturulmasına da izin verir.