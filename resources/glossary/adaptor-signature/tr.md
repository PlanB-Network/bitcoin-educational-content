---
term: ADAPTÖR IMZASI
---

Gizli bir veri parçasını ortaya çıkarmak için gerçek bir imzanın ek bir imza ("uyarlayıcı imza" olarak adlandırılır) ile birleştirilmesini sağlayan kriptografik yöntem. Bu yöntem, geçerli imza, uyarlayıcı imza ve sır arasında iki Elements'ın bilinmesinin eksik üçüncü unsurun çıkarılmasına izin vereceği şekilde çalışır. Bu yöntemin ilginç özelliklerinden biri, muhatabımızın uyarlayıcı imzasını ve bu uyarlayıcı imzayı hesaplamak için kullanılan sırla bağlantılı eliptik eğri üzerindeki belirli noktayı biliyorsak, sırrın kendisine doğrudan erişimimiz olmadan aynı sırla eşleşecek kendi uyarlayıcı imzamızı türetebilmemizdir. Birbirine güvenmeyen iki paydaş arasındaki bir Exchange'de, bu teknik katılımcılar arasında iki hassas bilginin eş zamanlı olarak açığa çıkmasını sağlar. Bu süreç, Coin Takası veya Atomik Takas gibi anlık işlemlerde güven ihtiyacını ortadan kaldırır. Daha iyi anlamak için bir örnek verelim. Alice ve Bob birbirlerine 1 BTC göndermek istiyor, ancak birbirlerine güvenmiyorlar. Bu nedenle, bu Exchange'de diğer tarafa güvenme ihtiyacını ortadan kaldırmak için adaptör imzaları kullanacaklardır (böylece bunu "atomik" bir Exchange haline getireceklerdir). Aşağıdaki şekilde ilerlerler:


- Alice bu atomik Exchange'i başlatır. Bob'e 1 BTC gönderen bir $m_A$ işlemi yaratır. Bu işlemi kendi özel anahtarı $p_A$ ($P_A = p_A \cdot G$) ve bir Nonce $n_A$ ve bir gizli $t$ ($N_A = n_A \cdot G$ ve $T = t \cdot G$) kullanarak doğrulayan bir imza $s_A$ oluşturur:

$$s_A = n_A + t + H(N_A + T \paralel P_A \paralel m_A) \cdot p_A$$



- Alice, gizli $t$ ve gerçek imzası $s_A$'dan uyarlayıcı imzasını $s_A'$ hesaplar:

$$s_A' = s_A - t$$



- Alice, Bob'ye adaptör imzası $s_A'$, imzasız işlemi $m_A$, gizli $T$'ye karşılık gelen nokta ve Nonce $N_A$'ya karşılık gelen noktayı gönderir. Bu bilgi parçalarını "adaptör" olarak adlandırıyoruz. Sadece bu bilgilerle Bob'nin Alice'un BTC'sini kurtaramayacağını unutmayın.
- Ancak Bob, Alice'ün kendisini kandırmadığını doğrulayabilir. Bunu yapmak için, Alice'ün adaptör imzasının $s_A'$ vaat edilen işlem $m_A$ ile eşleşip eşleşmediğini kontrol eder. Eğer aşağıdaki denklem doğruysa, Alice'ün adaptör imzasının geçerli olduğuna ikna olur:

$$s_A' \cdot G = N_A + H(N_A + T \paralel P_A \paralel m_A) \cdot P_A$$



- Bu doğrulama Bob'ya Alice'ten güvence sağlar, böylece atomik takas sürecine gönül rahatlığıyla devam edebilir. Daha sonra Alice'e 1 BTC gönderen kendi $m_B$ işlemini ve şimdilik yalnızca Alice'in bildiği aynı gizli $t$ ile bağlantılı olacak kendi adaptör imzası $s_B'$'yi yaratacaktır (Bob bu $t$ değerini değil, yalnızca Alice'in kendisine sağladığı karşılık gelen $T$ noktasını bilmektedir): $$s_B' = n_B + H(N_B + T \paralel P_B \paralel m_B) \cdot p_B$$



- Bob, Alice'ye uyarlayıcı imzası $s_B'$, imzasız işlemi $m_B$, gizli $T$'ye karşılık gelen nokta ve Nonce $N_B$'ye karşılık gelen noktayı gönderir. Alice artık Bob'un adaptör imzası $s_B'$ ile yalnızca kendisinin bildiği gizli $t$'yi birleştirerek Bob'un BTC'sini kendisine gönderen $m_B$ işlemi için geçerli bir imza $s_B$ hesaplayabilir:

$$s_B = s_B' + t$$


$$(s_B' + t) \cdot G = N_B + T + H(N_B + T \paralel P_B \paralel m_B) \cdot P_B$$



- Alice, Bob'ün kendisine söz verdiği BTC'yi geri almak için bu imzalı $m_B$ işlemini Bitcoin Blockchain'de yayınlar. Bob bu işlemi Blockchain'de öğrenir. Böylece $s_B = s_B' + t$ imzasını çıkarabilir. Bu bilgiden, Bob ihtiyaç duyduğu ünlü sır $t$'yi izole edebilir:

$$t = (s_B' + t) - s_B' = s_B - s_B'$$



- Bununla birlikte, bu gizli $t$ Bob'in Alice'ün adaptör imzası $s_A'$'dan geçerli imza $s_A$'yı üretmesi için tek eksik bilgiydi, bu da Alice'ten Bob'e bir BTC gönderen $m_A$ işlemini doğrulamasını sağlayacaktı. Daha sonra $s_A$'yı hesaplar ve sırayla $m_A$ işlemini yayınlar: $$s_A = s_A' + t$$


$$(s_A' + t) \cdot G = N_A + T + H(N_A + T \paralel P_A \paralel m_A) \cdot P_A$$