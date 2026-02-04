---
term: Türetme yolu
definition: Bir HD cüzdanda, çocuk anahtarların ana anahtardan itibaren türetme yolunu tanımlayan endeks dizisi.
---

Hiyerarşik Deterministik (HD) cüzdanlar bağlamında, türetme yolu, bir ana anahtardan alt anahtarları türetmek için kullanılan indeks dizisini ifade eder. BIP32'de açıklanan bu yol, alt anahtarların türetilmesi için ağaç yapısını tanımlar. Türetme yolu eğik çizgilerle ayrılmış bir dizi indisle temsil edilir ve her zaman ana anahtarla başlar (`m/` olarak gösterilir). Örneğin, tipik bir yol `m/84'/0'/0'/0/0` şeklinde olabilir. Her türetme seviyesi belirli bir derinlikle ilişkilendirilir:


- m /` ana özel anahtarı gösterir. Bir Wallet için benzersizdir ve aynı derinlikte kardeşleri olamaz. Ana anahtar doğrudan seed'den türetilir;
- m/amaç' /` takip edilen standardın tanımlanmasına yardımcı olan türetme amacını belirtir. Bu alan BIP43'te açıklanmıştır. Örneğin, Wallet BIP84 standardına (SegWit V0) bağlıysa, indeks `84'` olacaktır;
- m / purpose' / Coin-type' /` kripto para biriminin türünü gösterir. Bu, çoklu Coin Wallet'te bir kripto para birimine ayrılmış şubeler ile diğerine ayrılmış şubeler arasında net bir ayrım yapılmasını sağlar. Bitcoin'e adanmış dizin `0'`dır;
- m/amaç' /Coin-tipi' /hesap' /` hesap numarasını gösterir. Bu derinlik, bir Wallet'yi farklı hesaplara ayırmayı ve düzenlemeyi kolaylaştırır. Bu hesaplar `0'`dan başlayarak numaralandırılır. Genişletilmiş anahtarlar (`xpub`, `xprv`...) bu derinlik seviyesinde bulunur;
- m / purpose' / Coin-type' / account' / change /` yolu gösterir. Derinlik 3'te tanımlanan her hesabın derinlik 4'te iki yolu vardır: bir dış zincir ve bir iç zincir ("değişim" olarak da adlandırılır). Harici zincir, herkese açık olarak paylaşılması amaçlanan adresleri, yani Wallet yazılımımızda "al" seçeneğine tıkladığımızda bize sunulan adresleri türetir. İç zincir, kamuya açık olarak paylaşılması amaçlanmayan adresleri, özellikle de değişim adreslerini türetir. Harici zincir `0` indeksi ile, dahili zincir ise `1` indeksi ile tanımlanır. Bu derinlikten itibaren artık sertleştirilmiş bir türetme değil, normal bir türetme gerçekleştirdiğimizi fark edeceksiniz (kesme işareti yoktur). Bu mekanizma sayesinde tüm alt açık anahtarları `xpub`larından türetebiliyoruz;



- m / purpose' / Coin-type' / account' / change / Address-index` basitçe alıcı Address'in numarasını ve aynı dalda aynı derinlikteki kardeşlerinden ayırt etmek için anahtar çiftini belirtir. Örneğin, ilk türetilen Address `0` indeksine sahiptir, ikinci Address `1` indeksine sahiptir ve bu böyle devam eder...


Örneğin, Address alıcım `m / 86' / 0' / 0' / 0 / 5` türetme yoluna sahipse, aşağıdaki bilgileri çıkarabiliriz:


- 86'`, BIP86 (Taproot / SegWit V1) türetme standardını takip ettiğimizi gösterir;
- 0'` bunun bir Bitcoin Address olduğunu gösterir;
- 0'` Wallet'in ilk hesabında olduğumuzu gösterir;
- 0` harici bir Address olduğunu gösterir;
- 5` bu hesabın altıncı harici Address olduğunu gösterir.


