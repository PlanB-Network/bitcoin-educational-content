---
term: chain code
---

Bitcoin cüzdanlarının hiyerarşik deterministik (HD) türetilmesi bağlamında chain code, BIP32 standardına göre bir ana anahtardan generate alt anahtarlarını türetmek için kullanılan 256 bitlik bir kriptografik tuz değeridir. chain code, ana anahtar ve alt anahtar dizini ile birlikte, ana anahtarı veya türetilen diğer alt anahtarları açığa çıkarmadan yeni bir anahtar çiftini (özel anahtar ve açık anahtar) deterministik olarak generate yapmak için kullanılır.


Bu nedenle, her anahtar çifti için benzersiz bir chain code vardır. chain code ya Wallet'in seed'sının hashlenmesi ve bitlerin sağ yarısının alınmasıyla elde edilir. Bu durumda, ana özel anahtarla ilişkilendirilen ana chain code olarak adlandırılır. Alternatif olarak, bir ana anahtarın ana chain code ve bir dizin ile hash edilmesi ve ardından sağ bitlerin tutulmasıyla elde edilebilir. Bu daha sonra çocuk chain code olarak adlandırılır.


Her bir ebeveyn çifti ile ilişkili chain code bilinmeden anahtar türetmek mümkün değildir. Kriptografik anahtarların üretiminin saldırganlar için öngörülemez kalmasını ve Wallet sahibi için deterministik olmasını sağlamak için türetme sürecine sözde rastgele veriler ekler.


> ► *İngilizcede "code de chaîne" "chain code" olarak adlandırılır ve "code de chaîne maître" "master chain code" olarak adlandırılır.*