---
term: BIP0021
definition: Bağlantılar veya QR kodları aracılığıyla ödemeleri kolaylaştırmak için Bitcoin URI'lerinin (bitcoin ile başlayan bağlantılar) biçimini tanımlayan standart.
---

Nils Schneider ve Matt Corallo tarafından yazılan öneri, Luke Dashjr tarafından yazılan BIP20'ye dayanmaktadır ve bu da Nils Schneider tarafından yazılan başka bir belgeden alınmıştır. BIP21, ödemeleri kolaylaştırmak için alıcı adreslerinin URI'lerde (*Uniform Resource Identifier*) nasıl kodlanması gerektiğini tanımlar. Örneğin, "*Pandul*" etiketi altında bana 0.1 BTC gönderilmesini talep edeceğim BIP21'i takip eden bir Bitcoin URI şöyle görünecektir:


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


Bu standardizasyon, parametrelerini başlatmak için bir bağlantıya tıklamaya veya bir QR kodunu taramaya izin vererek Bitcoin işlemlerinin kullanıcı deneyimini geliştirir. BIP21 standardı artık Bitcoin Wallet yazılımında yaygın olarak benimsenmiştir.