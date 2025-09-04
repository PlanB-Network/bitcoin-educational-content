---
term: BIP0111
---

Düğümlerin BIP37'de açıklandığı gibi Bloom Filtrelerini desteklediklerini açıkça belirtmelerine izin vermek için `NODE_BLOOM` adlı bir hizmet bitinin eklenmesini önerir. NODE_BLOOM`un tanıtılması, düğüm operatörlerinin DoS risklerini azaltmak için bu hizmeti devre dışı bırakmalarını sağlar. BIP37 seçeneği Bitcoin core'da varsayılan olarak devre dışıdır. Etkinleştirmek için yapılandırma dosyasına `peerbloomfilters=1` parametresi girilmelidir.