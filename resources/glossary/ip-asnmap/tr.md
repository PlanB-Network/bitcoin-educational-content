---
term: IP_ASN.MAP
definition: Ağ bağlantılarını çeşitlendirmek için IP adreslerini ASN'lere eşleyen Bitcoin Core dosyası.
---

Bitcoin core'da Otonom Sistem Numaralarına (ASN) dayanarak IP adreslerinin kümelenmesini (yani gruplandırılmasını) geliştiren ASMAP'i saklamak için kullanılan dosya. Bu dosya, giden bağlantıları IP ağ öneklerine (/16) göre gruplandırmak yerine, İnternet'teki her ağ için benzersiz tanımlayıcılar olan ASN'lere bir IP adresleme haritası oluşturarak bağlantıları çeşitlendirmeye olanak tanır. Amaç, belirli saldırılara (özellikle Erebus saldırısı) karşı koruma sağlamak için bağlantıları çeşitlendirerek Bitcoin ağının güvenliğini ve topolojisini iyileştirmektir.