---
name: RGB Lightning Node
description: RLN으로 RGB 호환 라이트닝 노드를 시작하려면 어떻게 해야 하나요?
---
![cover](assets/cover.webp)


이 단계별 튜토리얼에서는 레그테스트 환경에서 라이트닝 RGB 노드를 설정하는 방법을 배우게 됩니다. RGB 토큰을 생성하고 채널에서 토큰을 유통하는 방법을 살펴봅니다.


## RLN 프로젝트


비트파이넥스의 RGB 팀은 2022년부터 완전한 기술 스택을 개발하여 RGB 생태계를 강화하기 위해 노력해 왔습니다. 하나의 상용 제품을 목표로 하기보다는 오픈소스 소프트웨어 브릭을 제공하고, RGB 프로토콜 사양에 기여하고, 구현 레퍼런스를 만드는 데 주력하고 있습니다.


RGB 생태계에 대한 비트파이넥스의 주목할 만한 기여 중에는 [*RGBlib* 라이브러리](https://github.com/RGB-Tools/RGB-lib)가 있는데, 이는 Rust로 작성되고 코틀린과 파이썬의 바인딩을 통해 액세스 가능하며 복잡한 검증 및 참여 메커니즘을 캡슐화하여 RGB 애플리케이션 개발을 크게 간소화합니다.


비트파이넥스 팀은 또한 안드로이드에서 사용할 수 있는 "[*아이리스 Wallet*](https://iriswallet.com/)"이라는 RGB 모바일 Wallet을 설계했습니다. 이 Wallet은 RGB 프록시 서버의 사용을 통합하여 RGB에서 *Client-side Validation*에 대한 off-chain 데이터 교환(*위탁*)을 쉽게 관리할 수 있습니다.


비트파이넥스는 'RGB-lightning-node'(RLN) 프로젝트도 개발했습니다. 이는 `Rust-lightning`(LDK)의 Fork를 기반으로 한 daemon로, 채널 내 RGB 자산의 존재를 고려하도록 수정되었습니다. 채널이 열리면 RGB 토큰의 존재를 지정할 수 있으며, 채널 상태가 업데이트될 때마다 라이트닝 출력에 토큰의 분포를 반영하는 State Transition이 생성됩니다. 이를 통해 :




- 예를 들어 USDT로 라이트닝 채널을 엽니다;
- 라우팅 경로에 충분한 유동성이 있는 경우 네트워크를 통해 이러한 토큰을 라우팅합니다;
- 라이트닝의 처벌 및 타임록 로직을 수정하지 않고 활용하세요: Commitment Transaction의 추가 출력에서 RGB 전환을 Anchor으로 변경하기만 하면 됩니다.


RLN 코드는 아직 알파 단계이므로 **regtest** 또는 **Testnet**에서만 사용하는 것을 권장합니다.


## RGB 프로토콜 알림


RGB은 Bitcoin 위에서 실행되는 프로토콜로, 기반이 되는 Blockchain에 과부하를 주지 않으면서 Smart contract 기능과 디지털 자산 관리를 에뮬레이트합니다. 예를 들어 이더리움에서와 같은 기존의 On-Chain 스마트 컨트랙트와 달리, RGB은 "*Client-side Validation*" 시스템에 의존합니다. 대부분의 데이터와 상태 기록은 관련된 참여자들에 의해서만 교환되고 저장되는 반면, Bitcoin는 *Tapret* 또는 *Opret* 같은 메커니즘을 통해 소규모 암호화 약정만 호스팅합니다. 따라서 RGB 프로토콜에서 Bitcoin Blockchain은 타임스탬프 서버와 Double-spending 보호 시스템으로만 사용됩니다.


RGB Contract은 진화적 상태 머신처럼 구조화되어 있습니다. 엄격하게 유형화되고 컴파일된 Schema에 따라 초기 상태(예: Supply, 티커 또는 기타 메타데이터 설명)를 정의하는 Genesis으로 시작합니다. 그런 다음 상태 전환과 필요한 경우 상태 확장을 적용하여 이 상태를 수정하거나 확장합니다. 대체 가능한 자산(RGB20)을 전송하든 고유 자산(RGB21)을 생성하든 각 작업에는 *일회용 씰*이 포함됩니다. 이는 Bitcoin UTXO를 off-chain 스테이트에 연결하고 이중 지출을 방지하는 동시에 기밀성과 확장성을 보장합니다.


RGB 프로토콜의 작동 방식에 대해 자세히 알아보려면 이 종합 교육 과정을 수강하는 것이 좋습니다:


https://planb.network/courses/3ce1d37c-05ba-4f54-aa15-7586d37b2bb7

## RGB 호환 라이트닝 노드 설치


RGB-lightning-node` 바이너리를 컴파일하고 설치하려면 먼저 리포지토리와 해당 하위 모듈을 복제한 다음 :


```bash
git clone https://github.com/RGB-Tools/rgb-lightning-node --recurse-submodules --shallow-submodules
```


![RLN](assets/fr/01.webp)




- Recurse-submodules` 옵션은 필요한 하위 장치(`Rust-lightning`의 수정된 버전 포함)도 복제합니다;
- Shallow-submodules` 옵션은 복제 깊이를 제한하여 다운로드 속도를 높이는 동시에 필수 커밋에 대한 액세스를 계속 제공합니다.


프로젝트 루트에서 다음 명령을 실행하여 바이너리를 컴파일하고 설치합니다:


```bash
cargo install --locked --debug --path .
```


![RLN](assets/fr/02.webp)




- '--잠겨 있음'은 종속성 버전이 존중되도록 합니다;
- 디버그`는 필수는 아니지만 집중하는 데 도움이 될 수 있습니다(원하는 경우 `--해제`를 사용할 수 있습니다);
- 경로 .`는 현재 디렉터리에서 설치하도록 '화물 설치'에 지시합니다.


이 명령이 끝나면 `$CARGO_HOME/bin/`에서 `RGB-lightning-node` 실행 파일을 사용할 수 있습니다. 이 경로가 `$PATH`에 있는지 확인하여 어느 디렉토리에서나 명령을 호출할 수 있도록 하세요.


## 전제 조건


작동하려면 `RGB-lightning-node` daemon의 존재와 구성이 필요합니다:




- bitcoind`** 노드


각 RLN 인스턴스는 On-Chain 트랜잭션을 브로드캐스트하고 모니터링하기 위해 `bitcoind`과 통신해야 합니다. 인증(로그인/비밀번호) 및 URL(호스트/포트)을 daemon에 제공해야 합니다.




- 인덱서**(일렉트럼 또는 에스플로라)


특히 자산이 앵커링된 UTXO을 찾으려면 daemon이 On-Chain 트랜잭션을 나열하고 탐색할 수 있어야 합니다. 일렉트럼 서버 또는 Esplora의 URL을 지정해야 합니다.




- RGB** 프록시


프록시 서버는 Lightning 피어 간 Exchange의 RGB *위탁*을 간소화하기 위한 구성 요소(선택 사항이지만 적극 권장)입니다. 다시 한 번 URL을 지정해야 합니다.


API를 통해 daemon을 *잠금 해제*할 때 ID와 URL을 입력합니다.


## 다시 테스트 시작


간단한 사용을 위해, Docker를 통해 일련의 서비스를 자동으로 시작하는 `regtest.sh` 스크립트가 있습니다: gW-52`, `electrs`(인덱서), `RGB-proxy-server`.


![RLN](assets/fr/03.webp)


이를 통해 미리 구성된 격리된 로컬 환경을 시작할 수 있습니다. 재부팅할 때마다 컨테이너와 데이터 디렉터리를 생성하고 삭제합니다. 먼저 :


```bash
./regtest.sh start
```


이 스크립트는 :




- 저장할 `docker/` 디렉터리를 만듭니다;
- Regtest에서 `bitcoind`와 인덱서 `electrs` 및 `RGB-proxy-server`를 실행합니다;
- 모든 것이 사용할 준비가 될 때까지 기다리세요.


![RLN](assets/fr/04.webp)


다음으로 여러 개의 RLN 노드를 실행해 보겠습니다. 예를 들어, 별도의 셸에서 (3개의 RLN 노드를 시작하려면) 를 실행합니다:


```bash
# 1st shell
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network regtest
# 2nd shell
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network regtest
# 3rd shell
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network regtest
```


![RLN](assets/fr/05.webp)




- 네트워크 regtest` 매개변수는 regtest 구성의 사용을 나타냅니다;
- '--daemon-listening-port'는 Lightning 노드가 API 호출(JSON)을 수신 대기할 REST 포트를 나타냅니다;
- `--ldk-peer-listening-port`는 수신할 Lightning P2P 포트를 지정합니다;
- 데이터알드케이0/`, `데이터알드케이1/`은 스토리지 디렉터리 경로입니다(각 노드는 정보를 개별적으로 저장합니다).


이제 API를 통해 브라우저에서 RLN 노드에 명령을 실행할 수 있습니다. 특히 여기에서 데몬을 *잠금 해제*할 수 있습니다. 노드와 동일한 컴퓨터에서 브라우저를 열고 URL 을 입력하기만 하면 됩니다:


```url
https://rgb-tools.github.io/rgb-lightning-node/
```


노드가 채널을 열려면 먼저 다음 명령으로 생성된 Address에 비트코인이 있어야 합니다(예: 노드 n°1의 경우):


```bash
curl -X POST http://localhost:3001/address
```


답변은 Address를 제공합니다.


![RLN](assets/fr/06.webp)


bitcoind` 레그테스트에서 몇 개의 비트코인을 채굴해 보겠습니다. Run :


```bash
./regtest.sh mine 101
```


![RLN](assets/fr/07.webp)


위에서 생성한 노드 Address로 자금을 전송합니다:


```bash
./regtest.sh sendtoaddress <address> <amount>
```


![RLN](assets/fr/08.webp)


그런 다음 블록을 채굴하여 거래를 확인합니다:


```bash
./regtest.sh mine 1
```


![RLN](assets/fr/09.webp)


## Testnet 출시(도커 제외)


보다 현실적인 시나리오를 테스트하려면 Regtest가 아닌 Testnet에서 퍼블릭 서비스 또는 사용자가 제어하는 서비스를 가리키는 RLN 노드를 실행할 수 있습니다:


```bash
rgb-lightning-node dataldk0/ --daemon-listening-port 3001 \
--ldk-peer-listening-port 9735 --network testnet
rgb-lightning-node dataldk1/ --daemon-listening-port 3002 \
--ldk-peer-listening-port 9736 --network testnet
rgb-lightning-node dataldk2/ --daemon-listening-port 3003 \
--ldk-peer-listening-port 9737 --network testnet
```


기본적으로 구성을 찾을 수 없는 경우 daemon는 :




- 비트코인드_rpc_호스트`: `electrum.iriswallet.com`
- 비트코인드_rpc_port`: `18332`
- 인덱서_URL`: `ssl://electrum.iriswallet.com:50013`
- 프록시 엔드포인트`: `rpcs://proxy.iriswallet.com/0.2/json-RPC`


로그인 사용 :




- `bitcoind_rpc_username`: `사용자`
- 비트코인드_rpc_사용자명`: `비밀번호`


'초기화`/`잠금해제` API를 통해 Elements을 사용자 지정할 수도 있습니다.


## RGB token 발행


token를 발급하려면 먼저 '컬러링 가능한' UTXO를 생성합니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"up_to": false,
"num": 4,
"size": 2000000,
"fee_rate": 4.2,
"skip_sync": false
}' \
http://localhost:3001/createutxos
```


![RLN](assets/fr/10.webp)


물론 순서를 조정할 수도 있습니다. 트랜잭션을 확인하기 위해 :


```bash
./regtest.sh mine 1
```


이제 RGB 에셋을 만들 수 있습니다. 명령은 생성하려는 에셋의 유형과 매개변수에 따라 달라집니다. 여기서는 "PBN"이라는 이름의 NIA(*비팽창형 에셋*) token을 1000 단위의 Supply으로 생성하겠습니다. '정밀도'를 사용하면 단위의 분할 가능성을 정의할 수 있습니다.


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amounts": [
1000
],
"ticker": "PBN",
"name": "Plan B Network",
"precision": 0
}' \
http://localhost:3001/issueassetnia
```


![RLN](assets/fr/11.webp)


응답에는 새로 생성된 에셋의 ID가 포함됩니다. 이 식별자를 기억하세요. 제 경우에는 입니다:


```txt
rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10
```


![RLN](assets/fr/12.webp)


그런 다음 On-Chain으로 전송하거나 라이트닝 채널에 할당할 수 있습니다. 다음 섹션에서 바로 이 작업을 수행하겠습니다.


## 채널 열기 및 RGB 자산 전송하기


먼저 `/connectpeer` 명령을 사용하여 노드를 Lightning Network의 피어에 연결해야 합니다. 제 예제에서는 두 노드를 모두 제어합니다. 따라서 이 명령으로 두 번째 라이트닝 노드의 공개 키를 검색하겠습니다:


```bash
curl -X 'GET' \
'http://localhost:3002/nodeinfo' \
-H 'accept: application/json'
```


이 명령은 내 노드 n°2 의 공개 키를 반환합니다:


```txt
031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94
```


![RLN](assets/fr/13.webp)


다음으로 관련 에셋(`PBN`)을 지정하여 채널을 열겠습니다. Openchannel` 명령을 사용하면 채널의 크기를 사토시 단위로 정의하고 RGB 에셋을 포함하도록 선택할 수 있습니다. 생성하려는 항목에 따라 다르지만 제 경우에는 명령이 :


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"peer_pubkey_and_opt_addr": "031e81e4c5c6b6a50cbf5d85b15dad720fec92c62e84bafb34088f0488e00a8e94@localhost:9736",
"capacity_sat": 1000000,
"push_msat": 10000000,
"asset_amount": 500,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"public": true,
"with_anchors": true,
"fee_base_msat": 1000,
"fee_proportional_millionths": 0,
"temporary_channel_id": "a8b60c8ce3067b5fc881d4831323e24751daec3b64353c8df3205ec5d838f1c5"
}' \
http://localhost:3001/openchannel
```


여기에서 자세히 알아보세요:




- 피어_공개키_및_옵트_주소`: 연결하려는 피어의 식별자(앞서 찾은 공개 키);
- `CAPACITY_SAT`: 사토시 단위의 총 채널 용량입니다;
- pUSH_MSAT`: 채널이 열릴 때 처음에 피어에게 전송되는 밀리사토시 단위의 금액 (여기서는 나중에 RGB 전송을 할 수 있도록 10,000 Sats을 즉시 전송합니다) ;
- `자산_금액`: 채널에 커밋할 RGB 에셋의 양입니다;
- `asset_id` : 채널에 참여한 RGB 에셋의 고유 식별자입니다;
- 공개`: 네트워크에서 라우팅을 위해 채널을 공개할지 여부를 나타냅니다.


![RLN](assets/fr/14.webp)


거래를 확인하기 위해 6개의 블록이 채굴됩니다:


```bash
./regtest.sh mine 6
```


![RLN](assets/fr/15.webp)


이제 라이트닝 채널이 열렸으며 노드 n°1 측에 500개의 `PBN` 토큰이 있습니다. 노드 n°2가 `PBN` 토큰을 받으려면 generate을 Invoice로 바꿔야 합니다. 방법은 다음과 같습니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"amt_msat": 3000000,
"expiry_sec": 420,
"asset_id": "rgb:fc7fMj5S-8yz!vIl-260BEhU-Hj1skvM-ZHcjfyz-RTcWc10",
"asset_amount": 100
}' \
http://localhost:3002/lninvoice
```


와 함께 :




- `amt_msat`: 밀리사토시 단위의 Invoice 양(최소 3000 Sats) ;
- `expiry_sec` : Invoice 만료 시간(초) ;
- `asset_id` : Invoice과 연결된 RGB 에셋의 식별자;
- `자산_금액`: 이 Invoice로 전송할 RGB 자산의 양입니다.


이에 대한 응답으로 RGB Invoice을 받게 됩니다:


```txt
lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj
```


![RLN](assets/fr/16.webp)


이제 필요한 현금을 보유하고 있는 첫 번째 노드에서 'PBN' token으로 이 Invoice를 지불합니다:


```bash
curl -X POST -H "Content-Type: application/json" \
-d '{
"invoice": "lnbcrt30u1pncgd4rdqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qv0grex9c6m22r9ltkzmzhddwg87eykx96zt47e5pz8sfz8qp28fgpp5jksvqtleryhvwr299qdz96qxzm24augy5agkdhltudk463lt9dassp5d6n0sqgl0c4gx52fdmutrdtqamt0y4xuz2rcgel4hpjwne08gmls9qyysgqcqpcxqzdylz5wfnkywnxvvmkvnt2x4fj6wre0gshvjtv95ervvzzg4592t2gdgchx6mkf5k45jrrdfn8j73d2f2xx4mrxycq7qzry4v4jan6uxhhacyqa4gn6plggwpq9j74tu74f2zsamtz6ymt600p8su4c4ap9g9d8ku2x3wdh6fuc8fd8pff2yzpjrf24ys3cltca9fgqut6gzj"
}' \
http://localhost:3001/sendpayment
```


![RLN](assets/fr/17.webp)


결제가 완료되었습니다. 명령을 실행하여 확인할 수 있습니다:


```bash
curl -X 'GET' \
'http://localhost:3001/listpayments' \
-H 'accept: application/json'
```


![RLN](assets/fr/18.webp)


RGB 에셋을 전송하도록 수정된 라이트닝 노드를 배포하는 방법은 다음과 같습니다. 이 데모는 를 기반으로 합니다:




- Regtest 환경(`./regtest.sh`를 통해) 또는 Testnet ;
- bitcoind`, 인덱서 및 `RGB-proxy-server`를 기반으로 하는 라이트닝 노드(`RGB-lightning-node`);
- 채널 열기/닫기, 토큰 발행, 라이트닝을 통한 자산 전송 등을 위한 일련의 JSON REST API입니다.


이 프로세스 덕분에 :




- 라이트닝 참여 거래에는 RGB 전환의 앵커링과 함께 추가 출력(OP_RETURN 또는 Taproot)이 포함됩니다;
- 송금은 기존 라이트닝 결제와 똑같은 방식으로 이루어지지만, RGB token이 추가됩니다;
- 경로에 비트코인과 자산 RGB의 유동성이 충분하다면 여러 RLN 노드를 연결하여 여러 노드에서 결제를 라우팅하고 실험해볼 수 있습니다.


이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 올려주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


또한 LNP/BP 협회에서 개발한 RGB CLI 도구를 사용하여 RGB Contract를 만드는 방법을 설명하는 이 다른 튜토리얼을 추천합니다:


https://planb.network/tutorials/node/others/rgb-cli-1f8a28d4-fa99-4261-9d80-48275b496fd4