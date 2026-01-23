---
term: BIP0093
definition: Bir tohumun (seed) Shamir'in gizli paylaşımı yoluyla birkaç parçaya bölünerek yedeklenmesini sağlayan Codex32 standardı.
---

Shamir'in Gizli Anahtar Paylaşımını kullanarak hiyerarşik deterministik bir portföyün (BIP32'ye göre) seed'ını kaydetmek ve geri yüklemek için bir standart öneren bilgilendirici BIP. Bu protokol, bir önek, bir eşik parametresi, bir tanımlayıcı, bir paylaşım indeksi, bir yük ve bir sağlama toplamından (BCH) oluşan yapılandırılmış bir dize sunarak bech32 formatından esinlenen "codex32" formatını tanımlar. Yöntem, seed'ın 31 adede kadar paylaşıma bölünmesine olanak tanır ve tam seed kurtarması için tanımlanmış bir eşik (1 ile 9 arasında) gereklidir.