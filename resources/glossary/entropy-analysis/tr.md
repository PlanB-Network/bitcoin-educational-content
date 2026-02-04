---
term: Entropi analizi
definition: Analistlerin bir Bitcoin işlemi yapılandırması hakkındaki bilgi eksikliğini ölçen gösterge.
---

Zincir analizi bağlamında entropi aynı zamanda LaurentMT tarafından icat edilen ve Shannon entropisinden türetilen bir göstergenin adıdır. Bu gösterge, analistlerin bir Bitcoin işleminin tam konfigürasyonu hakkında sahip oldukları bilgi eksikliğinin ölçülmesini sağlar. Başka bir deyişle, bir işlemin entropisi ne kadar yüksekse, analistlerin girdiler ve çıktılar arasındaki bitcoin hareketlerini tespit etmesi o kadar zorlaşır.


Uygulamada entropi, harici bir gözlemcinin bakış açısından, bir işlemin diğer harici veya dahili kalıpları ve sezgisel yöntemleri dikkate almaksızın yalnızca girdi ve çıktı miktarlarına dayalı olarak birden fazla olası yorum sunup sunmadığını ortaya koyar. Yüksek entropi daha sonra işlem için daha iyi gizlilik ile eş anlamlıdır.


Entropi, olası kombinasyonların sayısının ikili logaritması olarak tanımlanır. Burada $E$ işlemin entropisini ve $C$ olası yorumların sayısını temsil etmek üzere kullanılan formül yer almaktadır:


$$
E = \log_2(C)
$$


İşlemde yer alan UTXO'ların değerleri dikkate alındığında, $C$ yorum sayısı, girdilerin çıktılarla ilişkilendirilebileceği yolların sayısını temsil eder. Başka bir deyişle, bir işlemi analiz eden harici bir gözlemcinin bakış açısından ortaya çıkabilecek yorumların sayısını belirler.