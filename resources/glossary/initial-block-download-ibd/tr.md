---
term: İLK BLOK İNDİRME (IBD)
---

Bir düğümün Blockchain'ı Genesis bloğundan indirip doğruladığı ve Bitcoin ağındaki diğer düğümlerle senkronize ettiği süreci ifade eder. Yeni bir Full node başlatılırken IBD gerçekleştirilmelidir. Bu ilk senkronizasyonun başlangıcında, düğüm önceki işlemler hakkında hiçbir bilgiye sahip değildir. Bu nedenle her bloğu ağdaki diğer düğümlerden indirir, geçerliliğini doğrular ve ardından Blockchain'ın yerel sürümüne ekler. Blockchain ve UTXO setinin büyüyen boyutu nedeniyle IBD'nin uzun ve yoğun kaynak gerektirebileceğini belirtmek gerekir. Yürütme hızı, düğümü barındıran bilgisayarın hesaplama yeteneklerine, RAM kapasitesine, depolama cihazının hızına ve bant genişliğine bağlıdır. Size bir fikir vermek için, güçlü bir internet bağlantınız varsa ve düğüm bol miktarda RAM'e sahip en yeni MacBook'ta barındırılıyorsa, IBD yalnızca birkaç saat sürecektir. Tersine, Raspberry Pi gibi bir mikrobilgisayar kullanıyorsanız, IBD bir hafta veya daha uzun sürebilir.


> ► *Fransızcada genellikle doğrudan bir IBD'ye atıfta bulunulduğu kabul edilir. Bazen kullanılan çeviri "synchronisation initiale" veya "téléchargement initial des blocs" şeklindedir.*