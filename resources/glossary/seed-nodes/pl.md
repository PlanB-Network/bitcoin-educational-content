---
term: seed NODES
---

Statyczna lista publicznych węzłów Bitcoin, zintegrowana bezpośrednio z kodem źródłowym Bitcoin Core (`Bitcoin/src/chainparamsseeds.h`). Lista ta służy jako punkty połączenia dla nowych węzłów Bitcoin dołączających do sieci, ale jest używana tylko wtedy, gdy nasiona DNS nie dostarczą odpowiedzi w ciągu 60 sekund od ich żądania. W takim przypadku nowy węzeł Bitcoin połączy się z tymi węzłami seed, aby ustanowić pierwsze połączenie z siecią i zażądać adresów IP innych węzłów. Ostatecznym celem jest uzyskanie niezbędnych informacji do wykonania początkowego pobierania bloków (IBD) i synchronizacji z łańcuchem, który zgromadził najwięcej pracy. Lista węzłów seed obejmuje prawie 1000 węzłów, zidentyfikowanych zgodnie ze standardem ustanowionym przez BIP155. Węzły seed stanowią zatem trzecią metodę połączenia z siecią dla węzła Bitcoin, po możliwym wykorzystaniu pliku `peers.dat`, utworzonego przez sam węzeł, oraz pozyskiwaniu nasion DNS.


> uwaga: węzłów seed nie należy mylić z "nasionami DNS", które są drugą metodą nawiązywania połączeń