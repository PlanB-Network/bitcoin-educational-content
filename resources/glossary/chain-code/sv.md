---
term: Kedjekod
definition: 256-bitars kryptografiskt saltvärde som används vid HD-härledning av plånboksnycklar.
---

I samband med hierarkisk deterministisk (HD) härledning av Bitcoin plånböcker är chain code ett 256-bitars kryptografiskt saltvärde som används för att generate barnnycklar från en överordnad nyckel, enligt BIP32-standarden. chain code används i kombination med den överordnade nyckeln och barnets index för att på ett deterministiskt sätt skapa generate för ett nytt nyckelpar (privat nyckel och publik nyckel) utan att avslöja den överordnade nyckeln eller andra härledda barnnycklar.


Därför finns det en unik chain code för varje nyckelpar. chain code erhålls antingen genom att hasha Wallet:s seed och ta den högra halvan av bitarna. I det här fallet kallas den för en master-chain code, som är associerad med den privata masternyckeln. Alternativt kan den erhållas genom att hasha en överordnad nyckel med dess överordnade chain code och ett index, och sedan behålla de högra bitarna. Detta kallas då en underordnad chain code.


Det är omöjligt att härleda nycklar utan att känna till den chain code som är associerad med varje föräldrapar. Den introducerar pseudoslumpmässiga data i härledningsprocessen för att säkerställa att genereringen av kryptografiska nycklar förblir oförutsägbar för angripare samtidigt som den är deterministisk för Wallet-innehavaren.


