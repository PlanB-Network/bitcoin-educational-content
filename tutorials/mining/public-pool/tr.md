---
name: Halka Açık Havuz
description: Halka Açık Havuza Giriş
---

![signup](assets/cover.webp)


**Halka Açık Havuz** herhangi bir havuz değildir; **Solo Havuz** olarak da bilinir. Miner'niz bir bloğu Mining yapmayı başarırsa, havuzun diğer katılımcılarıyla veya havuzun kendisiyle paylaşılmayan tüm Block reward'ı toplarsınız.


**Halka Açık Havuz** yalnızca Miner'iniz için bir **blok şablonu** sağlar, böylece bir **Bitcoin düğümüne** ve Miner'inizle iletişim kuran yazılıma sahip olmanıza gerek kalmadan görevini yerine getirebilir. Bilgi işlem gücünüzü diğer katılımcılarınkiyle bir araya getirmediğiniz için, bir bloğu başarılı bir şekilde Mining yapma şansınız açıkça çok düşüktür, bu da bazen şanslı bir bireyin büyük ikramiyeyi kazandığı bir piyango sistemini andırır.


![signup](assets/1.webp)


Halka Açık Havuzun** **Gösterge Tablosunda**, havuzun **Toplam Hashrate** gibi bazı istatistiklerinin yanı sıra havuza bağlı farklı madenci türlerinin bir dağılımına da sahipsiniz.


![signup](assets/2.webp)


İlk birkaç satırda, toplam 649TH/s için bağlı 1323 **Bitaxe** ile **Bitaxe** görebiliriz. **Bitaxe**, **Antminer S19** gibi bir **ASIC** çipinin, 15W için 0,5TH/s'lik küçük bir Miner yapmak için bir **opensource** elektronik kart üzerinde basit bir şekilde yeniden kullanılmasına izin veren bir **Açık kaynak** projesidir. Bu ders için örnek olarak kullanacağımız Miner budur.


## Bir **İşçi** Ekleme 👷‍♂️


![signup](assets/cover.webp)


Sayfanın üst kısmında, Address **stratum+tcp://public-pool.io:21496** havuzunu kopyalayabilirsiniz.


Ardından, **kullanıcı** alanı için, sahip olduğunuz bir **Bitcoin** Address girin.


Birden fazla madenciniz varsa, hepsi için aynı Address'yi girebilirsiniz, böylece **hashrate'leri** birleştirilir ve tek bir Miner olarak görünür. Ayrıca her birine ayrı bir isim ekleyerek onları ayırt edebilirsiniz. Bunu yapmak için **Bitcoin** Address'den sonra **.workername** eklemeniz yeterlidir.


Son olarak, **parola** alanı için **'x'** kullanın.


Örnek: Eğer **Bitcoin** Address'nız **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'** ise ve Miner'inize **"Brrrr "** adını vermek istiyorsanız, Miner'inizin Interface'ine aşağıdaki bilgileri girersiniz:



- URL**: stratum+tcp://public-pool.io:21496
- KULLANICI**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- Şifre**: **'x'**

Miner'unuz bir **Bitaxe** ise, alanlar biraz farklıdır, ancak bilgiler aynı kalır:


- URL**: public-pool.io (burada, baştaki **'stratum+tcp://'** kısmını ve sondaki **':21496'** kısmını kaldırmanız gerekir, bu kısım port alanında raporlanacaktır)
- Port**: 21496
- Kullanıcı**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- Şifre**: **'x'**


![signup](assets/3.webp)


Mining'i başlattıktan birkaç dakika sonra, **Public Pool** web sitesinde Address'nizi arayarak verilerinizi görebileceksiniz.


## Gösterge Tablosu


![signup](assets/4.webp)


Public Pool'a** bağlandıktan sonra, **User** alanına girdiğiniz **Bitcoin** Address ile arama yaparak **Dashboard'unuza** erişebilirsiniz. Bizim durumumuzda bu **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'** şeklindedir.


Gösterge tablosunda** hem verileriniz hem de ağ hakkında farklı bilgiler görüntülenir.


![signup](assets/5.webp)


Bitcoin** ağının toplam çalışma gücüne karşılık gelen **Ağ Hash Oranına** sahipsiniz.


Ağ Zorluğu** bir bloğu doğrulamak için ulaşılması gereken zorluğu gösterir.


Ve **En İyi Zorluğunuz** ulaştığınız en yüksek zorluktur. Şans eseri 🍀 ağ zorluğuna ulaşırsanız, tüm Block reward'yı kazanırsınız... 100 bloktan sonra. Onları harcayabilmek için 100 blok beklemeniz gerekir.


Ayrıca, çıkarılan son bloğun numarası ve WU cinsinden ifade edilen ağırlığı olan **Blok Yüksekliğine** sahipsiniz, maksimum 4.000.000'dur.


Aşağıda, **Kullanıcı** alanında **Bitcoin** Address cihazınızın arkasına **.name** ekleyerek ayrı bir isim verdiyseniz, her bir cihazınızın tüm istatistiklerini ayrı ayrı görebilirsiniz.