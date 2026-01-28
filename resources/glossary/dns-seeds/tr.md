---
term: Dns seeds
definition: Bitcoin ağına yeni katılan düğümlere aktif düğümlerin IP adreslerini sağlayan DNS sunucuları.
---

Ağa katılan yeni Bitcoin düğümleri için ilk bağlantı noktaları. Aslında belirli DNS sunucuları olan bu tohumların Address'leri kalıcı olarak Bitcoin core koduna gömülüdür. Yeni bir düğüm başladığında, muhtemelen aktif Bitcoin düğümlerinin IP adreslerinin rastgele bir listesini elde etmek için bu sunucularla iletişime geçer. Yeni düğüm daha sonra bu listedeki düğümlerle bağlantı kurarak İlk Blok İndirme (IBD) işlemini gerçekleştirmek ve en fazla birikmiş işe sahip olan zincirle senkronize olmak için gereken bilgileri elde edebilir. 2024 itibariyle Bitcoin core DNS tohumlarının ve bunların bakımından sorumlu kişilerin listesi aşağıdadır (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.Bitcoin.sipa.be: Pieter Wuille;
- dnsseed.bluematt.me: Matt Corallo;
- dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: Christian Decker;
- seed.Bitcoin.jonasschnelli.ch: Jonas Schnelli;
- seed.btc.petertodd.net: Peter Todd;
- seed.Bitcoin.sprovoost.nl: Sjors Provoost;
- dnsseed.emzy.de: Stephan Oeste;
- seed.Bitcoin.wiz.biz: Jason Maurice;
- seed.Mainnet.achownodes.xyz: Ava Chow.


DNS tohumları, bir Bitcoin düğümünün bağlantı kurması için öncelik sırasına göre ikinci yöntemdir. İlk yöntem, düğümün kendisinin oluşturduğu peers.dat dosyasını kullanmayı içerir. Bu dosya, kullanıcı elle değiştirmediği sürece, yeni bir düğüm durumunda doğal olarak boştur.


> ► *Not, DNS tohumları bağlantı kurmanın üçüncü yolu olan "seed düğümleri" ile karıştırılmamalıdır.*