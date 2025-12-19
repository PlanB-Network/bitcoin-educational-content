---
term: DNS 시드
---

네트워크에 가입하는 새 Bitcoin 노드의 초기 연결 지점입니다. 실제로는 특정 DNS 서버인 이러한 시드에는 Address 코드에 영구적으로 Bitcoin core 코드가 포함되어 있습니다. 새 노드가 시작되면 이러한 서버에 연결하여 활성 상태일 것으로 추정되는 Bitcoin 노드의 임의의 IP 주소 목록을 얻습니다. 그런 다음 새 노드는 이 목록에 있는 노드들과 연결을 설정하여 초기 블록 다운로드(IBD)를 수행하는 데 필요한 정보를 얻고 가장 많은 작업이 누적된 체인과 동기화할 수 있습니다. 2024년 현재 Bitcoin core DNS 시드 목록과 유지 관리를 담당하는 개인은 다음과 같습니다(https://github.com/Bitcoin/Bitcoin/blob/master/src/kernel/chainparams.cpp):


- seed.Bitcoin.sipa.be: 피터 우일;
- dnsseed.bluematt.me: 매트 코랄로;
- dnsseed.Bitcoin.dashjr-list-of-P2P-nodes.us: Luke Dashjr;
- seed.bitcoinstats.com: 크리스찬 데커;
- seed.Bitcoin.jonasschnelli.ch: 요나스 슈넬리;
- seed.btc.petertodd.net: 피터 토드;
- seed.Bitcoin.sprovoost.nl: 스요르스 프로부스트;
- dnsseed.emzy.de: 스테판 오에스테;
- seed.Bitcoin.wiz.biz: 제이슨 모리스;
- seed.Mainnet.achownodes.xyz: Ava Chow.


DNS 시드는 Bitcoin 노드가 연결을 설정하는 데 우선순위에 따라 두 번째 방법입니다. 첫 번째 방법은 노드 자체에서 생성한 peers.dat 파일을 사용하는 것입니다. 이 파일은 사용자가 수동으로 수정하지 않는 한 새 노드의 경우 당연히 비어 있습니다.


> 참고: DNS 시드를 연결을 설정하는 세 번째 방법인 'seed 노드'와 혼동해서는 안 됩니다