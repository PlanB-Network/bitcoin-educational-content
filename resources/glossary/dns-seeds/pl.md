---
term: DNS SEEDS
---

Początkowe punkty połączenia dla nowych węzłów Bitcoin dołączających do sieci. Ziarna te, które są w rzeczywistości określonymi serwerami DNS, mają swoje Address na stałe osadzone w kodzie Bitcoin Core. Po uruchomieniu nowy węzeł kontaktuje się z tymi serwerami, aby uzyskać losową listę adresów IP przypuszczalnie aktywnych węzłów Bitcoin. Nowy węzeł może następnie nawiązać połączenia z węzłami na tej liście, aby uzyskać informacje potrzebne do wykonania początkowego pobrania bloku (IBD) i synchronizacji z łańcuchem, który ma najwięcej zgromadzonej pracy. Od 2024 r. znajduje się tutaj lista seedów Bitcoin Core DNS i osób odpowiedzialnych za ich utrzymanie (https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp):


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


Nasiona DNS są drugą w kolejności metodą nawiązywania połączeń przez węzeł Bitcoin. Pierwsza metoda polega na użyciu pliku peers.dat utworzonego przez sam węzeł. Ten plik jest naturalnie pusty w przypadku nowego węzła, chyba że użytkownik ręcznie go zmodyfikował.


> uwaga: ziaren DNS nie należy mylić z "węzłami seed", które są trzecim sposobem nawiązywania połączeń