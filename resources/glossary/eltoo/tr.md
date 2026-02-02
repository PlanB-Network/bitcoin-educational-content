---
term: Eltoo
definition: Lineer bir güncelleme yaklaşımıyla Lightning kanal durumlarının yönetimini basitleştiren protokol.
---

Bitcoin'in ikinci katmanları için bir UTXO'nin Ownership'ının ortaklaşa nasıl yönetileceğini tanımlayan genel bir protokol. Eltoo, Christian Decker, Rusty Russell ve Olaoluwa Osuntokun tarafından, özellikle Lightning kanal durumlarının, yani açılış ve kapanış arasındaki müzakere mekanizmalarıyla ilgili sorunları çözmek için tasarlanmıştır. Eltoo mimarisi, doğrusal bir durum yönetim sistemi getirerek müzakere sürecini basitleştirir ve yerleşik cezaya dayalı yaklaşımı daha esnek ve daha az cezalandırıcı bir güncelleme yöntemiyle değiştirir. Bu protokol, bir işlemin imzasındaki tüm girdilerin göz ardı edilmesine izin veren yeni bir SigHash türünün kullanılmasını gerektirir. Bu SigHash başlangıçta `SIGHASH_NOINPUT`, daha sonra `SIGHASH_ANYPREVOUT` (*A Any Previous Output*) olarak adlandırılmıştır. Uygulanması BIP118'de planlanmıştır.


> ► *Eltoo bazen "LN-Symmetry" olarak da anılır.*