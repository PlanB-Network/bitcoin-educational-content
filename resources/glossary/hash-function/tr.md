---
term: Hash fonksiyonu
definition: Değişken boyutlu bir girdiden sabit boyutlu bir çıktı üreten matematiksel fonksiyon.
---

Değişken boyutlu bir girdi (mesaj olarak adlandırılır) alan ve sabit boyutlu bir çıktı (Hash, hashing, digest veya parmak izi olarak adlandırılır) üreten matematiksel bir işlev. Hash fonksiyonları kriptografide yaygın olarak kullanılan ilkel araçlardır. Kendilerini güvenli bağlamlarda kullanım için uygun kılan belirli özellikler sergilerler:


- Ön görüntü direnci: belirli bir Hash üreten bir mesaj bulmak, yani $h = H(m)$ olacak şekilde bir Hash $h$ için bir ön görüntü $m$ bulmak çok zor olmalıdır, burada $H$ Hash fonksiyonudur;
- İkinci ön görüntü direnci: Bir $m_1$ mesajı verildiğinde, $H(m_1) = H(m_2)$ olacak şekilde başka bir $m_2$ mesajı ($m_1$'den farklı) bulmak çok zor olmalıdır;
- Çarpışma direnci: $H(m_1) = H(m_2)$ olacak şekilde iki farklı $m_1$ ve $m_2$ mesajı bulmak çok zor olmalıdır;
- Kurcalama direnci: Girişteki küçük değişiklikler çıkışta önemli ve öngörülemeyen değişikliklere neden olmalıdır.


Bitcoin bağlamında, Hash fonksiyonları Proof-of-Work mekanizması (*Proof-of-Work*), işlem tanımlayıcıları, Address üretimi, sağlama toplamı hesaplamaları ve Merkle ağaçları gibi veri yapılarının oluşturulması dahil olmak üzere çeşitli amaçlar için kullanılır. Protokol tarafında, Bitcoin yalnızca çift `SHA256` Hash`den oluşan `HASH256` olarak da adlandırılan `SHA256d` işlevini kullanır. hASH256` ayrıca özellikle genişletilmiş anahtarlar (`xpub`, `xprv`...) için belirli sağlama toplamlarının hesaplanmasında da kullanılır. Wallet tarafında aşağıdakiler de kullanılır:


- Mnemonic cümlelerinin sağlama toplamları için basit `SHA256`;
- deterministik ve hiyerarşik cüzdanların türetilmesi sürecinde kullanılan `HMAC` ve `PBKDF2` algoritmaları içinde `SHA512`;
- bir `SHA256` ve bir `RIPEMD160`ın ardışık kullanımını tanımlayan `HASH160`. hASH160`, alıcı adresleri oluşturma sürecinde (P2PK ve P2TR hariç) ve genişletilmiş anahtarlar için üst anahtar parmak izlerinin hesaplanmasında kullanılır.


