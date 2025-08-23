---
term: TAHIL
---

Bir Bitcoin hiyerarşik deterministik portföyün özel bağlamında, bir seed rastgele bir olaydan türetilen 512 bitlik bir bilgi parçasıdır. Bir Bitcoin portföyü için deterministik ve hiyerarşik olarak generate bir dizi özel anahtarı ve bunlara karşılık gelen açık anahtarları belirlemek için kullanılır. seed genellikle kurtarma ifadesinin kendisi ile karıştırılır. Ancak bu aynı şey değildir. seed, `PBKDF2` işlevinin Mnemonic ifadesine ve herhangi bir passphrase'a uygulanmasıyla elde edilir.


seed, hiyerarşik deterministik portföyün temellerini tanımlayan BIP32 ile icat edilmiştir. Bu standartta seed 128 bit olarak ölçülmüştür. Bu, üretilen her anahtar için yeni yedeklemeler gerektiren JBOK (*Just a Bunch Of Keys*) portföylerinin aksine, bir portföydeki tüm anahtarların tek bir bilgi parçasından türetilmesine olanak tanır. BIP39 daha sonra bu seed'nın insanlar tarafından okunmasını kolaylaştırmak için bir kodlama önermiştir. Bu kodlama, genellikle Mnemonic cümlesi veya kurtarma cümlesi olarak adlandırılan bir cümle şeklini alır. Bu standart, özellikle sağlama toplamı kullanımı sayesinde seed'yı kaydederken hataları önler.


Bitcoin bağlamı dışında, genel olarak kriptografide seed, generate kriptografik anahtarlar için kullanılan bir başlangıç değeridir veya daha geniş anlamda, bir sözde rastgele sayı üreteci tarafından üretilen herhangi bir veri türüdür. Kriptografik sistemin güvenliğini garanti altına almak için bu başlangıç değerinin rastgele ve öngörülemez olması gerekir. Aslında, seed sisteme entropi katar, ancak bunu takip eden üretim süreci deterministiktir.


> ► *Genel tabirle, bitcoin kullanıcılarının çoğu "seed "den bahsederken Mnemonic ifadesine atıfta bulunur, Mnemonic ifadesi ile ana anahtar arasında yer alan ara türetme durumuna değil