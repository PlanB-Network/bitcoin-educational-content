---
term: ETIKET (SESSIZ ÖDEMELER)
---

Sessiz Ödemeler protokolünde etiketler, birçok başka statik adres oluşturmak amacıyla başlangıçtaki statik Address'ı değiştirmek için kullanılan tam sayılardır. Bu etiketlerin kullanımı, Sessiz Ödemeler yoluyla gönderilen ödemelerin, her kullanım için farklı statik adresler kullanılarak, bu ödemelerin tespit edilmesi (tarama) için operasyonel yükü aşırı derecede artırmadan ayrılmasına olanak tanır. Bob, iki açık anahtardan oluşan statik bir Address $B$ kullanır: tarama için $B_{\text{scan}}$ ve harcama için $B_{\text{spend}}$. Hash $b_{\text{scan}}$ ve $G$ üreteç noktası ile skaler olarak çarpılan bir $m$ tamsayısı, $B_{\text{spend}}$ harcama açık anahtarına eklenerek bir tür yeni harcama açık anahtarı $B_m$ oluşturulur:


$$ B_m = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } m) \cdot G $$


Örneğin, ilk anahtar $B_1$ bu şekilde elde edilir:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Bob tarafından yayınlanan statik Address artık $B_{\text{scan}}$ ve $B_m$'den oluşacaktır. Örneğin, $1$ etiketine sahip ilk statik Address şöyle olacaktır:


$$ B = B_{\text{scan}} \text{ ‖ } B_1 $$


Sadece $1$ etiketinden başlıyoruz, çünkü $0$ etiketi değişim için ayrılmıştır. Bob tarafından sağlanan etiketli statik Address'ye bitcoin göndermek isteyen Alice, $B_{\text{spend}}$ yerine yeni $B_1$ kullanarak benzersiz Address $P_0$ ödemesini türetecektir:


$$ P_0 = B_1 + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


Gerçekte, Alice, Bob'ün etiketli bir Address'e sahip olduğunu bile bilmeyebilir, çünkü sadece sağladığı statik Address'in ikinci kısmını kullanır, bu durumda $B_{\text{spend}}$ yerine $B_1$ değeridir. Ödemeleri taramak için Bob her zaman bu şekilde $B_{\text{spend}}$ ile ilk statik Address değerini kullanacaktır:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

Ardından, $P_0$ için bulduğu değeri her bir çıktıdan teker teker çıkaracaktır. Daha sonra bu çıkarma işlemlerinin sonuçlarından birinin Wallet'sında kullandığı etiketlerden birinin değeriyle eşleşip eşleşmediğini kontrol eder. Örneğin, $1$ etiketli #4 numaralı çıktı ile eşleşirse, bu çıktının $B_1$ etiketli statik Address ile ilişkili bir Sessiz Ödeme olduğu anlamına gelir:

$$ Out_4 - P_0 = \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Bu işe yarıyor çünkü:


$$ B_1 = B_{\text{spend}} + \text{Hash}(b_{\text{scan}} \text{ ‖ } 1) \cdot G $$


Bu yöntem sayesinde Bob, kullanımları uygun şekilde ayırmak için hepsi temel statik Address'dan ($B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}}$) türetilen çok sayıda statik adres ($B_1$, $B_2$, $B_3$... ile) kullanabilir.


Ancak, statik adreslerin bu şekilde ayrılması yalnızca kişisel Wallet yönetimi açısından geçerlidir, ancak kimliklerin ayrılmasına izin vermez. Hepsi aynı $B_{\text{scan}}$'a sahip olduğundan, tüm statik adresleri birlikte ilişkilendirmek ve tek bir varlığa ait oldukları sonucuna varmak çok kolaydır.