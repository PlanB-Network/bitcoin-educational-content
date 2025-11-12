---
term: FİBER
---

"*Fast Internet Bitcoin Relay Engine*" kısaltmasıdır. Matt Corallo tarafından 2016 yılında Bitcoin bloklarının dünya genelinde dağıtımını hızlandırmak için tasarlanmış bir protokoldür. Amacı, yayılma gecikmelerini mümkün olduğunca fiziksel sınırlara yaklaştırmaktı. FIBRE, bir katılımcı tarafından çıkarılan blokların oranının, ağdaki konumlarından bağımsız olarak, bilgi işlem gücü açısından katkılarını doğru bir şekilde yansıtmasını sağlayarak Mining fırsatlarının daha adil bir şekilde dağıtılmasını sağlamayı amaçlamıştır.


Gerçekten de, blok iletimindeki gecikme, genellikle birbirine yakın konumlanmış büyük, iyi bağlantılı Mining gruplarını daha küçük olanların aleyhine olacak şekilde destekleyebilir. Bu olgu zamanla Mining'ün merkezileşmesini artırabilir ve sistemin genel güvenliğini azaltabilir. FIBRE bu sorunu çözmek için hata düzeltme kodları ve paket kaybını dengelemek için ek veri iletiminin yanı sıra BIP152'de açıklananlara benzer kompakt blokların kullanımını getirmiş ve bunların hepsi belirli TCP sınırlamalarını aşmak için UDP üzerinden çalışmıştır. Bununla birlikte, FIBRE, esas olarak tek bir bakıcıya bağımlı olması ve BIP152'nin benimsenmesinin böyle bir sistemi daha az gerekli hale getirmesi nedeniyle 2020'de terk edildi.