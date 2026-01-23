---
term: BIP0111
definition: Düğümlerin Bloom Filtreleri (BIP37) için desteğini bildirmesini sağlayan NODE_BLOOM servis bitinin eklenmesi.
---

Düğümlerin BIP37'de açıklandığı gibi Bloom Filtrelerini desteklediklerini açıkça belirtmelerine izin vermek için `NODE_BLOOM` adlı bir hizmet bitinin eklenmesini önerir. NODE_BLOOM`un tanıtılması, düğüm operatörlerinin DoS risklerini azaltmak için bu hizmeti devre dışı bırakmalarını sağlar. BIP37 seçeneği Bitcoin core'da varsayılan olarak devre dışıdır. Etkinleştirmek için yapılandırma dosyasına `peerbloomfilters=1` parametresi girilmelidir.