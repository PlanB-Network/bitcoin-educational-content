---
term: BIP0385
definition: Deskriptörlerde çıktı betiklerini adrese göre veya onaltılık (hexadecimal) formatta tanımlamak için kullanılan addr() ve raw() fonksiyonları.
---

Descriptor fonksiyonları `addr(ADDR)` ve `raw(HEX)` tanıtılır. Addr(ADDR)` işlevi, bir alıcı Address kullanarak bir çıktı betiğini tanımlamaya izin verirken, `raw(HEX)` işlevi, bu betiğin ham onaltılık gösterimini kullanarak bir çıktı betiğini belirtmeyi sağlar. BIP385, Descriptor ile ilgili diğer tüm BIP'lerle birlikte (BIP386 hariç) Bitcoin core'ın 0.17 sürümünde uygulanmıştır.