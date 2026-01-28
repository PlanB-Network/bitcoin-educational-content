---
term: Yol bulma
definition: Lightning Network üzerinde bir ödemeyi yönlendirmek için en uygun yolun belirlenmesi süreci.
---

Lightning kanal ağı üzerinden bir ödemeyi yönlendirmek için en uygun yolu belirlemek üzere bir düğüm tarafından kullanılan süreç. Yol bulma, alıcıya ulaşmak için en uygun ara düğümleri seçmesi gereken ödeme düğümü tarafından gerçekleştirilir. Bu seçim, ücretler, kanal kapasitesi ve zaman kilitleri gibi bir dizi kritere dayanır.


Yol bulma algoritmaları, dedikodu verilerinden ağ topolojisinin bir grafiğini oluşturur ve ödeyen ile alıcı düğüm arasındaki çeşitli olası rotaları değerlendirir. Bu rotalar çeşitli kriterlere göre en iyiden en kötüye doğru sıralanır. Düğüm daha sonra ödemeyi bunlardan biri üzerinde yapmayı başarana kadar bu rotaları test eder.