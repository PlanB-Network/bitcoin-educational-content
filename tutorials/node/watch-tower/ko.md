---
name: Lightning Watchtower
description: 라이트닝 노드에서 Watchtower 이해하기 및 사용하기
---
![cover](assets/cover.webp)



## 워치타워는 어떻게 작동하나요?



Lightning Network 생태계의 필수적인 부분인 _워치타워_는 사용자의 라이트닝 채널을 추가적으로 보호하는 역할을 합니다. 감시탑의 주요 역할은 채널 상태를 모니터링하고 채널의 한 쪽이 다른 쪽을 속이려고 할 때 개입하는 것입니다.



Watchtower는 채널이 침해되었는지 어떻게 확인할 수 있나요? 고객(채널의 당사자 중 한 명)으로부터 위반을 정확하게 식별하고 처리하는 데 필요한 정보를 받습니다. 이 정보에는 가장 최근 거래의 세부 정보, 채널의 현재 상태, 페널티 거래를 생성하는 데 필요한 Elements가 포함됩니다. 이 데이터를 Watchtower으로 전송하기 전에 고객은 기밀을 유지하기 위해 데이터를 암호화할 수 있습니다. 따라서 Watchtower이 데이터를 수신하더라도 실제로 침해가 발생하기 전까지는 데이터를 해독할 수 없습니다. 이 암호화 메커니즘은 고객의 개인정보를 보호하고 Watchtower가 민감한 정보에 무단으로 액세스하는 것을 방지합니다.



이 튜토리얼에서는 **Watchtower**를 사용하는 3가지 방법을 살펴보겠습니다:




- 첫째, LND을 통한 고전적인 원시 방식입니다,
- 그런 다음 Satoshi의 눈으로 다른 접근 방식을 사용합니다,
- 마지막으로 Umbrel로 호스팅되는 Lightning 노드에서 Watchtower을 간단하게 구성할 수 있습니다.



## 1 - Watchtower 또는 LND을 통해 클라이언트 구성하기



*이 튜토리얼은 [LND 공식 문서](https://github.com/lightningnetwork/LND/blob/master/docs/Watchtower.md)에서 발췌한 것입니다. 원본 버전과 일부 내용이 변경되었을 수 있습니다



V0.7.0부터 `LND`는 `LND`의 완전히 통합된 하위 시스템으로 프라이빗 이타적 Watchtower의 실행을 지원합니다. 워치타워는 고객 노드가 오프라인 상태이거나 침해 시점에 대응할 수 없는 경우 악의적이거나 우발적인 침해 시나리오에 대한 2차 방어선을 제공하여 채널 자금에 대한 보안 수준을 높입니다.



서비스 대가로 채널 자금의 일부를 요구하는 _보상 감시탑_과 달리, _알트루스트 감시탑_은 수수료를 부과하지 않고 피해자의 모든 자금(On-Chain 수수료 제외)을 돌려줍니다. 보상 망루는 이후 버전에서 활성화될 예정이며, 아직 테스트 및 개선 단계에 있습니다.



또한, 이제 'LND'을 _감시 타워 클라이언트_로 작동하도록 구성하여 다른 이타적 감시 타워로부터 암호화된 침해 해결 트랜잭션(소위 "정의 트랜잭션")을 저장할 수 있습니다. Watchtower은 고정된 크기의 암호화된 블롭을 저장하며, 위반 당사자가 취소된 Commitment 상태를 브로드캐스트한 후에만 정의 트랜잭션을 해독하고 게시할 수 있습니다. 고객 ↔ Watchtower 통신은 임시 키 쌍을 사용하여 암호화되고 인증되므로 Watchtower이 장기 자격 증명을 통해 고객을 추적할 수 있는 기능이 제한됩니다.



이번 릴리스에서는 이미 'LND' 사용자에게 상당한 보안을 제공하는 일부 기능만 제한적으로 배포하기로 결정했습니다. 다른 많은 Watchtower 관련 기능들은 거의 완성 단계에 있거나 상당히 진전된 상태이며, 테스트를 거쳐 안전하다고 판단되는 대로 계속 제공될 예정입니다.



참고: 당분간 워치타워는 해지된 커밋의 `to_local` 및 `to_remote` 출력만 저장합니다. 프로토콜이 암호화된 블롭에 추가 서명 데이터를 포함하도록 확장될 수 있으므로 HTLC 출력 저장 기능은 향후 버전에 배포될 예정입니다._



### Watchtower 구성



Watchtower을 설정하려면 명령줄 사용자는 gRPC 또는 `lncli`를 통해 Watchtower과 상호 작용할 수 있는 선택적 `watchtowerrpc` 서브서버를 컴파일해야 합니다. 게시된 바이너리에는 기본적으로 `watchtowerrpc` 서브서버가 포함되어 있습니다.



Watchtower를 활성화하기 위한 최소 구성은 `Watchtower.active=1`입니다.



Lncli 타워 정보`로 Watchtower 구성 정보를 검색할 수 있습니다:



```shell
$  lncli tower info
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"listeners": [
"[::]:9911"
],
"uris": [
],
}
```



Watchtower 구성 옵션의 전체 세트는 `LND -h` 를 통해 사용할 수 있습니다:



```shell
$  lnd -h
...
watchtower:
--watchtower.active                                     If the watchtower should be active or not
--watchtower.towerdir=                                  Directory of the watchtower.db (default: $HOME/.lnd/data/watchtower)
--watchtower.listen=                                    Add interfaces/ports to listen for peer connections
--watchtower.externalip=                                Add interfaces/ports where the watchtower can accept peer connections
--watchtower.readtimeout=                               Duration the watchtower server will wait for messages to be received before hanging up on client connections
--watchtower.writetimeout=                              Duration the watchtower server will wait for messages to be written before hanging up on client connections
...
```



#### 청취 인터페이스



기본적으로 Watchtower은 사용 가능한 모든 인터페이스에서 포트 `9911`에 해당하는 `:9911`에서 수신 대기합니다. 사용자는 `--Watchtower.listen=` 옵션을 통해 수신 인터페이스를 직접 정의할 수 있습니다. 설정은 `lncli 타워 정보`의 `"리스너"` 필드에서 확인할 수 있습니다. Watchtower에 연결하는 데 문제가 있는 경우 `<포트>`가 열려 있는지 또는 프록시가 활성 Interface에 올바르게 구성되어 있는지 확인하세요.



#### 외부 IP 주소



또한 사용자는 `Watchtower.externalip=`로 Address의 외부 IP를 지정할 수 있으며, 이는 RPC 또는 `lncli 타워 정보`를 통해 Watchtower의 전체 URI(pubkey@host:port)를 노출합니다:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911"
]
```



다음 명령어로 연결하여 사용할 수 있도록 고객에게 Watchtower URI를 전달할 수 있습니다:



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



Watchtower 고객이 원격으로 액세스해야 하는 경우 반드시 :




- 포트 9911(또는 `Watchtower.listen`를 통해 정의된 포트)을 엽니다.
- 프록시를 사용하여 오픈 포트에서 Watchtower의 수신 중인 Address로 트래픽을 리디렉션합니다.



#### 토르 숨겨진 서비스



워치타워는 토르 숨김 서비스를 지원하며, 시작 시 다음 옵션을 사용하여 자동으로 generate을 설정할 수 있습니다:



```shell
$  lnd --tor.active --tor.v3 --watchtower.active
```



그러면 `lncli 타워 정보` 쿼리 중에 `"uris"` 필드에 .onion Address가 나타납니다:



```shell
$  lncli tower info
...
"uris": [
"03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@bn2kxggzjysvsd5o3uqe4h7655u7v2ydhxzy7ea2fx26duaixlwuguad.onion:9911"
]
```



참고: Watchtower 공개 키는 `LND` 노드의 공개 키와 구별됩니다. 당분간은 'Soft 화이트리스트' 역할을 하며, 고객이 Watchtower의 공개키를 백업으로 사용하려면 고급 화이트리스트 메커니즘이 마련될 때까지는 이 공개키를 알아야 합니다. Watchtower을 전체 인터넷에 노출할 준비가 되어 있지 않다면 이 공개 키를 공개적으로 공개하지 않는 것이 좋습니다



#### Watchtower 데이터베이스 디렉토리



Watchtower 데이터베이스는 `Watchtower.towerdir=` 옵션을 사용하여 이동할 수 있습니다. 데이터베이스를 문자열로 구분하기 위해 선택한 경로에 `/Bitcoin/Mainnet/Watchtower.db` 접미사가 추가됩니다. 따라서 `Watchtower.towerdir=/path/to/towerdir`을 설정하면 `/path/to/towerdir/Bitcoin/Mainnet/Watchtower.db`에 데이터베이스가 생성됩니다.



예를 들어 Linux에서 Watchtower의 기본 데이터베이스는 :


`/home/$USER/.LND/data/Watchtower/Bitcoin/Mainnet/Watchtower.db`



### Watchtower 클라이언트 구성



Watchtower 클라이언트를 구성하려면 두 가지 항목이 필요합니다:





- Wtclient.active` 옵션으로 Watchtower 클라이언트를 활성화합니다.



```shell
$  lnd --wtclient.active
```





- 활성 Watchtower의 URI입니다.



```shell
$  lncli wtclient add 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63@1.2.3.4:9911
```



이러한 방식으로 여러 개의 워치타워를 구성할 수 있습니다.



#### 법적 거래에 대한 수수료율



사용자는 `wtclient.sweep-fee-rate` 옵션을 통해 정의 트랜잭션의 수수료율을 선택적으로 설정할 수 있으며, 이 옵션은 sat/바이트 단위의 값을 허용합니다. 기본값은 10 sat/바이트이지만, 피크 요금이 발생하는 동안 더 높은 우선순위를 달성하기 위해 더 높은 요율을 설정할 수 있습니다. Sweep-fee-rate`를 변경하면 daemon 재시작 후 모든 신규 업데이트에 적용됩니다.



#### 감독



이제 `lncli wtclient` 명령어를 사용하여 Watchtower 클라이언트와 직접 상호 작용하여 등록된 모든 감시탑의 정보를 얻거나 수정할 수 있습니다.



예를 들어, `lncli wtclient tower`를 사용하면 위에 추가된 Watchtower과 현재 협상 중인 세션 수를 확인할 수 있고 `active_session_candidate` 필드 덕분에 백업에 사용 중인지 여부를 확인할 수 있습니다.



```shell
$  lncli wtclient tower 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": []
}
```



Watchtower 세션에 대한 정보를 얻으려면 `--include_sessions` 옵션을 사용하세요.



```shell
$  lncli wtclient tower --include_sessions 03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63
{
"pubkey": "03281d603b2c5e19b8893a484eb938d7377179a9ef1a6bca4c0bcbbfc291657b63",
"addresses": [
"1.2.3.4:9911"
],
"active_session_candidate": true,
"num_sessions": 1,
"sessions": [
{
"num_backups": 0,
"num_pending_backups": 0,
"max_backups": 1024,
"sweep_sat_per_vbyte": 10
}
]
}
```



모든 Watchtower 클라이언트 구성 옵션은 `lncli wtclient -h` 를 통해 사용할 수 있습니다:



```shell
$  lncli wtclient -h
NAME:
lncli wtclient - Interact with the watchtower client.

USAGE:
lncli wtclient command [command options] [arguments...]

COMMANDS:
add     Register a watchtower to use for future sessions/backups.
remove  Remove a watchtower to prevent its use for future sessions/backups.
towers  Display information about all registered watchtowers.
tower   Display information about a specific registered watchtower.
stats   Display the session stats of the watchtower client.
policy  Display the active watchtower client policy configuration.

OPTIONS:
--help, -h  show help
```




## 2 - 나만의 Satoshi의 눈 설치하기



*이 튜토리얼은 [Bitcoin의 여름 블로그](https://blog.summerofbitcoin.org/)에 있는 글의 일부를 발췌한 것입니다. 원본 버전*을 일부 수정했습니다



Satoshi의 눈([Rust-TEOS](https://github.com/talaia-labs/Rust-teos))은 [Bolt 13](https://github.com/sr-gi/bolt13/blob/master/13-watchtowers.md?ref=blog.summerofbitcoin.org)을 준수하는 비축형 Watchtower 라이트닝입니다. 두 가지 주요 구성 요소로 이루어져 있습니다:





- teos**: 명령줄 Interface(CLI)과 Watchtower의 필수 서버 기능을 포함합니다. 이 _crate_가 컴파일되면 **teosd**와 **teos-CLI**의 두 개의 바이너리가 생성됩니다.





- teos-common**: 공유 서버 측 및 클라이언트 측 기능을 포함합니다(클라이언트 생성에 유용).



Watchtower을 올바르게 실행하려면 **teosd** 명령으로 Watchtower을 실행하기 전에 **bitcoind**을 실행해야 합니다. 이 두 명령을 실행하기 전에 **Bitcoin.conf** 파일을 구성해야 합니다. 설정 방법은 다음과 같습니다:





- 소스에서 Bitcoin core을 설치하거나 다운로드합니다. 다운로드 후 **Bitcoin.conf** 파일을 Bitcoin core 사용자 디렉토리에 넣습니다. 사용 중인 운영 체제에 따라 파일 위치에 대한 자세한 내용은 이 링크를 참조하세요.





- 위치가 확인되면 다음 옵션을 추가합니다:



```shell
# RPC
server=1
rpcuser=<your-user>
rpcpassword=<your-password>

# chaîne
regtest=1
```





- server**: RPC 요청의 경우





- rpcuser** 및 **rpcpassword**: RPC 클라이언트를 서버에 인증합니다





- regtest**: 필수는 아니지만 개발을 계획하는 경우 유용합니다.



Rpcuser** 및 **rpcpassword**의 값은 사용자가 직접 선택해야 합니다. 따옴표 없이 입력해야 합니다. 예를 들어



```shell
rpcuser=aniketh
rpcpassword=strongpassword
```



이제 **bitcoind**을 실행하면 노드가 시작됩니다.





- Watchtower 부분의 경우 먼저 소스에서 **teos**를 설치해야 합니다. 이 링크의 지침을 따르세요.





- 시스템에 **teos**를 성공적으로 설치하고 테스트를 실행했다면, 마지막 단계인 **teos.toml** 파일을 teos 사용자 디렉터리에 설정할 수 있습니다. 이 파일은 홈 디렉터리 아래의 **.teos**(점 표시) 폴더에 위치해야 합니다. 예를 들어 Linux에서는 **/home//.teos**입니다. 위치를 찾았으면 **teos.toml** 파일을 만들고 **bitcoind**에서 변경한 내용에 따라 이 옵션을 설정합니다:



```shell
# bitcoind
btc_network = "regtest"
btc_rpc_user = <your-user>
btc_rpc_password = <your-password>
```



여기서 사용자 아이디와 비밀번호는 **따옴표 안에** 입력해야 한다는 점에 유의하세요. 이전 예제 사용 :



```shell
btc_rpc_user = "aniketh"
btc_rpc_password = "strongpassword"
```



이 작업이 완료되면 Watchtower을 시작할 준비가 된 것입니다. Regtest**에서 실행 중이므로, Watchtower이 처음 연결되었을 때 Bitcoin 테스트 네트워크에서 블록이 채굴되지 않았을 가능성이 높습니다(채굴되었다면 뭔가 잘못되었다는 뜻입니다). Watchtower은 **bitcoind**의 마지막 100개 블록의 내부 캐시를 구축하므로 처음 시작할 때 다음과 같은 오류가 발생할 수 있습니다:



```shell
ERROR [teosd] Not enough blocks to start the tower (required: 100). Mine at least 100 more
```



Regtest**를 사용하기 때문에 다른 네트워크(예: Mainnet 또는 Testnet)에서 볼 수 있는 평균 10분 지연을 기다릴 필요 없이 RPC 명령을 실행하여 Miner 블록을 수행할 수 있습니다. Miner 차단 방법에 대한 자세한 내용은 **bitcoin-cli** 도움말을 참조하세요.



![Image](assets/fr/01.webp)



이제 Watchtower을 성공적으로 실행했습니다. 축하합니다. 🎉




## 3 - 엄브렐에서 Watchtower 구성하기



엄브렐에서는 모든 것이 그래픽 Interface을 통해 이루어지기 때문에 Watchtower에 연결하여 라이트닝 노드를 보호하는 것은 매우 간단합니다. 노드에 원격으로 연결한 후 "**라이트닝 노드**" 애플리케이션을 엽니다.



![Image](assets/fr/02.webp)



Interface의 오른쪽 상단에 있는 작은 점 3개를 클릭한 다음 '**고급 설정**'을 선택합니다.



![Image](assets/fr/03.webp)



"**Watchtower**" 메뉴에서는 두 가지 옵션을 사용할 수 있습니다:





- Watchtower 서비스**: 이 옵션을 사용하면 다른 노드의 채널을 모니터링하여 사기 시도를 감지하는 서비스, 즉 Watchtower를 운영할 수 있습니다. 침해가 발생하면 Watchtower가 Blockchain에 트랜잭션을 게시하여 사용자가 잠긴 자금을 복구할 수 있도록 합니다. 활성화되면 Watchtower의 URI가 나타나고 다른 노드에 전달되어 다른 노드가 이를 Watchtower 클라이언트에 추가할 수 있습니다;





- Watchtower 클라이언트**: 이 옵션을 사용하면 외부 워치타워에 연결하여 자체 채널을 보호할 수 있습니다. 활성화하면 노드가 채널에 대한 필요한 정보를 전송할 Watchtower 서비스를 추가할 수 있습니다. 그러면 이러한 감시 타워가 노드의 상태를 모니터링하고 사기 시도가 있을 경우 개입합니다.



물론 노드를 보호하기 위해 *Watchtower 클라이언트*를 활성화하는 것이 우선이지만, 그 대가로 다른 사용자의 보안에 기여하기 위해 *Watchtower 서비스*를 활성화하는 것도 권장합니다.



![Image](assets/fr/04.webp)



그런 다음 Green "**노드 저장 후 재시작**" 버튼을 클릭합니다. LND가 재시작됩니다.



같은 메뉴에서 Watchtower 서비스를 활성화한 경우 해당 서비스의 URI도 확인할 수 있습니다. 채널을 보호하기 위해 외부 Watchtower의 URI를 추가할 수도 있습니다. "**추가**"를 클릭하여 확인합니다.



![Image](assets/fr/05.webp)



온라인에서 사용할 수 있는 여러 감시탑이 있습니다. 예를 들어, [LN+와 Voltage는 이타적인 Watchtower](https://lightningnetwork.plus/Watchtower)에 연결할 수 있는 망루를 제공합니다:



```
023bad37e5795654cecc69b43599da8bd5789ac633c098253f60494bde602b60bf@iiu4epqzm6cydqhezueenccjlyzrqeruntlzbx47mlmdgfwgtrll66qd.onion:9911
```



![Image](assets/fr/06.webp)



또 다른 옵션은 동료 비트코인과 함께 Watchtower URI를 Exchange화하여 서로가 서로의 노드를 보호하는 것입니다.



또한 망루 중 하나를 사용할 수 없게 될 경우의 위험을 줄이기 위해 여러 개의 망루를 설치하는 것이 좋습니다.



마지막으로 "**Watchtower 클라이언트 스윕 수수료율**" 매개변수를 조정할 수 있습니다. 이는 블록에 포함될 Watchtower 생방송 처벌 거래에 대해 지불할 수 있는 최대 수수료 요율을 정의합니다. 채널에 잠긴 금액에 맞게 충분히 높은 값을 설정해야 합니다.