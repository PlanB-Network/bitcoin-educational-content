---
term: BIP0044
definition: HD cüzdanlar için türetme yollarının tam yapısını tanımlayan standart purpose, coin_type, account, change ve address_index.
---

HD cüzdanları için standart bir hiyerarşik türetme yapısı sunan bir iyileştirme önerisi. BIP44, anahtar türetme için BIP32 ve "amaç" alanının kullanımı için BIP43 tarafından oluşturulan ilkeler üzerine inşa edilmiştir. Beş seviyeli bir türetme yapısı sunar: `m / purpose' / coin_type' / account' / change / address_index`. İşte her bir derinliğin ayrıntıları:


- m /` ana özel anahtarı gösterir. Bir Wallet için benzersizdir ve aynı derinlikte kardeşleri olamaz. Ana anahtar doğrudan Wallet'ın seed'inden türetilir;
- m/amaç' /` takip edilen standardın tanımlanmasına yardımcı olan türetme amacını belirtir. Bu alan BIP43'te açıklanmıştır. Örneğin, Wallet BIP84 (SegWit V0) standardını takip ediyorsa, indeks `84'` olacaktır;
- m / purpose' / Coin-type' /` kripto para biriminin türünü gösterir. Bu, çoklu Coin Wallet'te bir kripto para birimine ayrılmış dallar ile başka bir kripto para birimine ayrılmış dallar arasında net bir ayrım yapılmasını sağlar. Bitcoin'e adanmış dizin `0'`dır;
- m / purpose' / Coin-type' / account' /` hesap numarasını gösterir. Bu derinlik, bir Wallet'nin farklı hesaplar halinde kolayca ayırt edilmesini ve düzenlenmesini sağlar. Bu hesaplar `0'`dan başlayarak numaralandırılır. Genişletilmiş anahtarlar (`xpub`, `xprv`...) bu derinlikte bulunur;
- m / purpose' / Coin-type' / account' / change /` zinciri belirtir. Derinlik 3'te tanımlanan her hesabın derinlik 4'te iki zinciri vardır: bir dış zincir ve bir iç zincir ("değişiklik" olarak da adlandırılır). Harici zincir, kamuya açık olarak iletilmesi amaçlanan adresleri, yani Wallet yazılımımızda "al" seçeneğine tıkladığımızda bize sunulan adresleri türetir. İç zincir, kamuya açık olarak değiş tokuş edilmesi amaçlanmayan adresleri, yani öncelikle değişim adreslerini türetir. Dış zincir `0` indeksi ile, iç zincir ise `1` indeksi ile tanımlanır. Bu derinlikten itibaren artık sertleştirilmiş bir türetme değil, normal bir türetme gerçekleştirdiğimizi fark edeceksiniz (kesme işareti yoktur). Bu mekanizma sayesinde tüm alt açık anahtarları `xpub`larından türetebiliyoruz;
- m / purpose' / Coin-type' / account' / change / Address-index` basitçe alıcı Address'in numarasını ve aynı dalda aynı derinlikteki kardeşlerinden ayırt etmek için anahtar çiftini belirtir. Örneğin, ilk türetilen Address `0` indeksine sahiptir, ikinci Address `1` indeksine sahiptir ve bu böyle devam eder...

Örneğin, Address alıcım `m / 86' / 0' / 0' / 0 / 5` türetme yoluna sahipse, aşağıdaki bilgileri çıkarabiliriz:


- 86'`, BIP86 (Taproot veya SegWitV1) türetme standardını takip ettiğimizi gösterir;
- 0'` bunun bir Bitcoin Address olduğunu gösterir;
- 0'` Wallet'nin ilk hesabında olduğumuzu gösterir;
- 0` harici bir Address olduğunu gösterir;
- 5` bu hesabın altıncı harici Address olduğunu gösterir.