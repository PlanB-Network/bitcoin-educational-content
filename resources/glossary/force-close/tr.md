---
term: Zorla kapatma
definition: İmzalanmış son taahhüt işlemini yayınlayarak bir Lightning kanalının tek taraflı kapatılması.
---

İşbirlikçi olmayan Lightning kanal kapatma mekanizması. İki kullanıcı Multisig 2/2 ile bir kanal açtığında, her biri zincirdeki bitcoinlerini geri almak için imzalanmış olan son Commitment Transaction'ı yayınlayarak kanalı tek taraflı olarak kapatabilir. Bu "zorla kapatma" olarak bilinir.


Bu yöntem genellikle katılımcılardan biri artık yanıt vermiyorsa veya kanalın işbirliği içinde kapatılması mümkün değilse kullanılır. Zorla kapatmadan kaçınılabiliyorsa, en iyisi budur, çünkü zincir içi fonları kurtarmak daha uzun sürer ve ücretler açısından çok daha pahalı olabilir.


Zorla kapatmada, iki kullanıcıdan biri Lightning kanalının bilinen son durumunu yansıtan Commitment Transaction'yi yayınlar. Ardından, bitcoinlerin zincir üzerinde geri alınabilmesi için bir zaman kilidi vardır ve diğer tarafa işlemin en son kanal durumuna karşılık geldiğini doğrulaması için zaman tanınır. Bir kullanıcı güncel olmayan bir Commitment Transaction yayınlayarak hile yapmaya çalışırsa, diğer taraf hilekarı cezalandırmak ve kanaldaki tüm fonları geri almak için iptal sırrını kullanabilir.