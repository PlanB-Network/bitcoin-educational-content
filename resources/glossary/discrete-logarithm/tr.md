---
term: Ayrık logaritma
definition: Bitcoin'in kriptografik güvenliğinin temelini oluşturan, çözülmesi zor matematiksel problem.
---

Ayrık logaritma, bazı açık anahtar şifreleme algoritmalarında kullanılan matematiksel bir problemdir. Üreteci $g$ olan $q$ mertebesinde bir döngüsel grupta, $g^x = h$ şeklinde bir denklem varsa, $x$, $g$ tabanına göre $h$'nin $q$ modulo'suna göre ayrık logaritması olarak adlandırılır. Basit bir ifadeyle, $g$, $h$ ve $q$ bilindiğinde $x$ üssünün belirlenmesini içerir. Bu nedenle ayrık logaritma, sonlu bir döngüsel gruptaki üstelin tersidir. Bununla birlikte, $q$ 'nun büyük değerleri için, ayrık logaritma problemini çözmenin algoritmik olarak zor olduğu düşünülmektedir. Bu özellik, anahtar Exchange için Diffie-Hellman protokolü gibi birçok kriptografik protokolün güvenliğini sağlamak için kullanılır.


Ayrık logaritma, ECDSA (*Eliptik Eğri Dijital İmza Algoritması*) da dahil olmak üzere eliptik eğri kriptografisinde (ECC) de kullanılır. Eliptik eğriler bağlamında, ayrık logaritma problemi, $k \cdot G = K$ olacak şekilde bir $k$ skalerini bulmaya kadar uzanır; burada $G$ ve $K$ eğri üzerindeki noktalardır ve $\cdot$ nokta çarpma işlemini temsil eder. Bitcoin bağlamında, komut dosyaları UTXO'ları kilitlemek için ECDSA ya da Schnorr protokolünü kullanabilir. Her ikisi de ayrık logaritmanın hesaplanmasının olanaksızlığına dayanır.