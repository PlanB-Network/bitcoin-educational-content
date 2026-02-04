---
term: Genişletilmiş anahtar
definition: HD cüzdanlarda türetme için bir anahtar, zincir kodu ve meta verileri birleştiren dize.
---

Bir anahtarı (genel veya özel), ilişkili chain code'ı ve bir dizi meta veriyi birleştiren bir karakter dizisi. Genişletilmiş bir anahtar, alt anahtarları türetmek için gerekli tüm Elements'i tek bir tanımlayıcıda derler. Deterministik ve hiyerarşik cüzdanlarda kullanılırlar ve iki türde olabilirler: genişletilmiş bir açık anahtar (alt açık anahtarları türetmek için kullanılır) veya genişletilmiş bir özel anahtar (hem alt özel hem de açık anahtarları türetmek için kullanılır). Bu nedenle genişletilmiş bir anahtar, BIP32'de açıklanan birkaç farklı veri parçasını sırayla içerir:


- Önek: `prv` ve `pub` HRP (İnsan Tarafından Okunabilir Kısım) olup genişletilmiş özel anahtar (`prv`) veya genişletilmiş açık anahtar (`pub`) olduğunu belirtir. Ön ekin ilk harfi genişletilmiş anahtarın sürümünü belirtir: Bitcoin üzerinde Eski veya SegWit V1 için `x`, Bitcoin Testnet üzerinde Eski veya SegWit V1 için `t`, Bitcoin Testnet üzerinde Yuvalanmış SegWit için `y`, Bitcoin Testnet üzerinde Yuvalanmış SegWit için `u`, Bitcoin Testnet üzerinde SegWit V0 için `z`, Bitcoin Testnet üzerinde SegWit V0 için `v`.
- Genişletilmiş anahtara ulaşmak için ana anahtardan türetme sayısını gösteren derinlik;
- Üst parmak izi. Bu, ana ortak anahtarın `HASH160` değerinin ilk 4 baytını temsil eder;
- Dizin. Bu, genişletilmiş anahtarın türetildiği kardeşleri arasındaki çiftin numarasıdır;
- chain code;
- Özel anahtar `0x00` ise bir dolgu baytı;
- Özel veya genel anahtar;
- Bir sağlama toplamı. Genişletilmiş anahtarın geri kalanının `HASH256` kısmının ilk 4 baytını temsil eder.


Uygulamada, genişletilmiş açık anahtar generate alıcı adresleri için ve ilişkili özel anahtarları ifşa etmeden bir hesabın işlemlerini gözlemlemek için kullanılır. Bu, örneğin, "sadece izle" olarak adlandırılan bir Wallet oluşturulmasına izin verebilir. Ancak, açıklanması üçüncü tarafların işlemleri izlemesine ve ilişkili hesabın bakiyesini görmesine izin verebileceğinden, genişletilmiş açık anahtarın kullanıcının gizliliği için hassas bilgiler olduğuna dikkat etmek önemlidir.