---
term: PSBT
definition: Kısmen imzalanmış Bitcoin işlemlerini oluşturmak ve paylaşmak için standartlaştırılmış format.
---

"Partially Signed Bitcoin Transaction" için kısaltma. Wallet yazılımı gibi Bitcoin ile ilgili yazılımlarda tamamlanmamış işlemlerin oluşturulma şeklini standartlaştırmak için BIP174 ile tanıtılan bir spesifikasyondur. Bir PSBT, girdilerin tam olarak imzalanmamış olabileceği bir işlemi kapsüller. Bir katılımcının ek veri gerektirmeden işlemi imzalaması için gerekli tüm bilgileri içerir. Böylece, bir PSBT 3 farklı şekilde olabilir:


- Tamamen inşa edilmiş ancak henüz imzalanmamış bir işlem;
- Bazı girdilerin imzalandığı ancak diğerlerinin henüz imzalanmadığı kısmi imzalı bir işlem;
- Ya da tamamen imzalanmış bir Bitcoin işlemi, ağ üzerinde yayına hazır hale dönüştürülebilir.


PSBT formatı farklı Wallet yazılımları ve imza cihazları (Hardware Wallet) arasında birlikte çalışabilirliği kolaylaştırır. Şu anda, BIP174'te tanımlandığı gibi PSBT'in 0 sürümü kullanılmaktadır, ancak sürüm 2 BIP370 aracılığıyla önerilmektedir.


> ► *PSBT'un 1. versiyonu mevcut değildir. Sürüm 0 ilk sürüm olduğu için ikinci sürüm gayri resmi olarak sürüm 2 olarak adlandırılmıştır. BIP370'i yazan Ava Chow, herhangi bir karışıklığı önlemek için bu yeni sürüme 2 numarasını vermeye karar verdi.*