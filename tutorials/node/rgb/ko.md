---
name: RGB
description: RGB 소개 및 자산 생성
---

![cover](assets/cover.webp)


## 소개


2009년 1월 3일 Satoshi 나카모토는 첫 번째 Bitcoin 노드를 출시했으며, 그 순간부터 새로운 노드가 합류하고 Bitcoin는 마치 새로운 형태의 생명체처럼 행동하기 시작했으며, 진화를 멈추지 않고 조금씩 조금씩 네트워크 보안에 기여하는 에너지와 컴퓨팅 파워에 투자하도록 일반적으로 채굴자라고 불리는 사용자들을 끌어들이는 독특한 설계의 결과로 세계에서 가장 안전한 네트워크가 되었습니다.


Bitcoin가 계속 성장하고 채택됨에 따라 확장성 문제에 직면했습니다. Bitcoin 네트워크는 대략 10분 안에 거래가 포함된 새 블록을 채굴할 수 있으며, 하루에 144개의 블록이 있고 블록당 최대 거래가 2700개라고 가정하면 Bitcoin는 초당 4.5개의 거래만 허용했습니다. Satoshi는 이 한계를 알고 있었습니다. 2011년 3월 마이크 헌에게 보낸 이메일1에서 오늘날 우리가 결제 채널로 알고 있는 소액결제의 작동 방식을 설명합니다. 승인을 기다리지 않고 빠르고 안전하게 소액결제. 바로 이 부분에서 off-chain 프로토콜이 등장합니다.


크리스찬 데커에 따르면2 off-chain 프로토콜은 일반적으로 사용자가 Blockchain의 데이터를 사용하고 마지막 순간까지 Blockchain 자체에 손을 대지 않고 관리하는 시스템입니다. 이 개념을 기반으로 Lightning Network이 탄생했는데, off-chain 프로토콜을 사용하여 거의 즉각적으로 Bitcoin 결제가 이루어질 수 있는 네트워크이며, 이러한 모든 작업이 블록체인에 기록되지 않기 때문에 초당 수천 건의 트랜잭션이 가능하고 Bitcoin을 확장할 수 있습니다.


Bitcoin의 off-chain 프로토콜 분야의 연구 개발은 판도라의 상자를 열었으며, 오늘날 우리는 탈중앙화된 방식으로 가치 이전 이상의 것을 달성할 수 있다는 것을 알고 있으며, 비영리 LNP/BP 표준 협회는 Bitcoin 및 Lightning Network의 Layer 2 및 3 프로토콜 개발에 주력하고 있으며, 이러한 프로젝트 중 RGB가 눈에 띕니다.


## RGB이란 무엇인가요?


RGB은 피터 토드3의 일회용 씰과 클라이언트 측 검증에 대한 연구로부터 등장했으며, 2016년부터 2019년까지 Giacomo Zucco와 커뮤니티에서 Bitcoin와 Lightning Network을 위한 더 나은 자산 프로토콜로 만들어냈습니다. 이러한 아이디어를 더욱 발전시켜 2019년부터 커뮤니티의 참여로 RGB의 구현을 이끌고 있는 Maxim Orlovsky에 의해 본격적인 Smart contract 시스템으로 발전시켰습니다.


RGB은 확장 가능하고 기밀이 유지되는 방식으로 복잡한 스마트 컨트랙트를 실행할 수 있는 일련의 오픈 소스 프로토콜로 정의할 수 있습니다. 이는 특정 네트워크(예: Bitcoin 또는 라이트닝)가 아니며, 각 Smart contract는 서로 다른 통신 채널(기본값은 Lightning Network)을 사용하여 상호 작용할 수 있는 Contract 참여자의 집합일 뿐입니다. RGB은 Bitcoin Blockchain을 상태 Layer로 사용하고 Smart contract의 코드와 데이터 off-chain를 유지하여 확장 가능하며, 스마트 컨트랙트를 위한 Ownership 제어 시스템으로 Bitcoin 트랜잭션(및 스크립트)을 활용하고, Smart contract의 진화는 off-chain 체계로 정의되지만 최종적으로는 모든 것이 클라이언트 측에서 검증된다는 점에 유의해야 합니다.


간단히 말해서, RGB은 "전통적인" 시스템처럼 Blockchain를 사용하지 않기 때문에 사용자가 추가 비용 없이 언제든지 Smart contract을 감사하고 실행하고 개별적으로 확인할 수 있는 시스템으로, 이더리움이 개척한 복잡한 스마트 컨트랙트 시스템은 각 작업마다 상당한 양의 가스를 소비해야 하기 때문에 약속한 확장성을 달성하지 못해 결과적으로 기존 금융 시스템에서 제외된 사용자들을 위한 옵션이 되지 못했습니다.


현재 Blockchain 업계에서는 스마트 컨트랙트 코드와 데이터를 모두 Blockchain에 저장하고 네트워크의 각 노드에서 실행해야 한다고 주장하는데, 이는 과도한 크기 증가나 계산 자원의 오용에 대한 우려 때문입니다. RGB이 제안하는 방식은 스마트 컨트랙트와 데이터를 Blockchain에서 분리하여 다른 플랫폼에서 볼 수 있는 네트워크의 포화 상태를 피하고, 각 노드가 각 Contract를 실행하도록 강제하지 않고 관련 당사자가 실행하도록 하여 이전에는 볼 수 없었던 수준의 기밀성을 추가하기 때문에 훨씬 더 지능적이고 효율적입니다.


![RGB vs Ethereum](assets/1.webp)


## RGB의 스마트 컨트랙트


RGB에서 Smart contract 개발자는 시간이 지남에 따라 Contract가 어떻게 진화하는지에 대한 규칙을 지정하는 체계를 정의합니다. 이 체계는 RGB에서 스마트 컨트랙트 구축을 위한 표준이며, 발행을 위해 Contract를 정의하는 발행자와 Wallet 또는 Exchange 모두 Contract를 검증해야 하는 특정 체계를 준수해야 합니다. 유효성 검사가 올바른 경우에만 각 당사자가 요청을 수락하고 자산을 사용할 수 있습니다.


RGB의 Smart contract는 그래프의 일부만 항상 알려져 있고 나머지 부분에는 접근할 수 없는 상태 변화의 Directed Acyclic Graph(DAG)입니다. RGB 체계는 Smart contract가 시작하는 이 그래프의 진화를 위한 핵심 규칙 집합입니다. 각 Contract Participant는 이러한 규칙을 추가할 수 있으며(Schema에서 허용하는 경우), 결과 그래프는 이러한 규칙의 반복적인 적용을 통해 구축됩니다.


## 대체 가능한 자산


RGB의 대체 가능한 자산은 LNPBP RGB-20 사양4을 따르며, RGB-20이 정의되면 자산을 사용하는 데 필요한 내용이 포함된 "Genesis 데이터"로 알려진 자산 데이터가 Lightning Network을 통해 배포됩니다. 가장 기본적인 형태의 자산은 2차 발행, token 소각, 리노미네이션 또는 교체가 허용되지 않습니다.


때때로 발행자는 향후 더 많은 토큰, 즉 USDT와 같은 스테이블 코인을 발행해야 하는데, 이는 각 token의 가치를 USD와 같은 인플레이션 통화 가치에 묶어두는 것입니다. 이를 위해 더 복잡한 RGB-20 스키마가 존재하며, 발행자는 Genesis 데이터 외에도 위탁을 생성해야 하며, 이 정보로 자산의 총 유통 Supply를 알 수 있습니다. 자산을 소각하거나 이름을 변경하는 경우에도 마찬가지입니다.


자산과 관련된 정보는 공개 또는 비공개가 될 수 있습니다. 발행자가 기밀 유지가 필요한 경우 token에 대한 정보를 공유하지 않고 절대적으로 비공개로 운영할 수 있지만, 발행자와 보유자가 전체 과정을 투명하게 공개해야 하는 반대의 경우도 있습니다. 이는 token 데이터를 공유함으로써 달성할 수 있습니다.


## RGB-20 절차


소각 절차는 토큰을 비활성화하며, 소각된 토큰은 더 이상 사용할 수 없습니다.


교체 절차는 토큰이 소각되고 동일한 양의 token가 새로 생성될 때 발생합니다. 이렇게 하면 자산의 기록 데이터 크기를 줄이는 데 도움이 되며, 이는 자산 속도를 유지하는 데 중요합니다.


자산을 교체하지 않고도 자산을 소각할 수 있는 사용 사례를 지원하기 위해 자산 소각만 허용하는 RGB-20의 하위 체계가 사용됩니다.


## 대체 불가능한 자산


RGB의 대체 불가능한 자산은 LNPBP RGB-21 사양5을 따르며, NFT로 작업할 때는 기본 체계와 하위 체계도 있습니다. 이러한 체계에는 각인 절차가 있어 token 소유자의 일부가 사용자 지정 데이터를 첨부할 수 있으며, 오늘날 NFT에서 가장 흔히 볼 수 있는 예는 token에 연결된 디지털 아트입니다. token 발행자는 RGB-21 하위 체계를 사용하여 이러한 데이터 각인을 금지할 수 있습니다. 다른 NFT Blockchain 시스템과 달리 RGB는 다른 많은 형태의 RGB 전용 Smart contract 기능을 구축하는 데에도 사용되는 Bifrost라는 라이트닝 P2P 네트워크 확장을 활용하여 완전히 탈중앙화되고 검열에 저항하는 방식으로 대용량 미디어 token 데이터를 배포할 수 있습니다.


대체 가능한 자산과 대체 불가능한 토큰 외에도 RGB과 바이프로스트는 향후 기사에서 다룰 DEX, 유동성 풀, 알고리즘 스테이블 코인 등 다른 형태의 스마트 콘트랙트를 생성하는 데 사용할 수 있습니다.


## RGB의 NFT와 다른 플랫폼의 NFT 비교



- 고가의 Blockchain 스토리지 필요 없음
- IPFS가 필요 없는 대신 Lightning Network 확장(Bifrost라고 함)이 사용되며 완전히 엔드투엔드 암호화됩니다
- 특별한 데이터 관리 솔루션이 필요 없습니다. Bifrost가 그 역할을 대신합니다
- NFT 토큰 또는 발행 자산/Contract ABI에 대한 데이터를 유지하기 위해 웹사이트를 신뢰할 필요가 없습니다
- 기본 제공 DRM 암호화 및 Ownership 관리
- Lightning Network(Bifrost)를 사용한 백업 인프라스트럭처
- 콘텐츠 수익화 방법(NFT 자체 판매뿐만 아니라 콘텐츠에 대한 여러 차례의 액세스 권한)


## 결론


거의 13년 전 Bitcoin이 출시된 이후 이 분야에 대한 많은 연구와 실험이 있었고, 성공과 실수를 통해 탈중앙화 시스템이 실제로 어떻게 작동하는지, 무엇이 실제로 탈중앙화되고 어떤 행동이 중앙화로 이끄는 경향이 있는지 조금 더 이해할 수 있었으며,이 모든 것을 통해 진정한 탈중앙화는 달성하기 어렵고 드문 현상이라는 결론을 내렸으며 진정한 탈중앙화는 Bitcoin에서만 달성되었으며 이러한 이유로 우리는 그 위에 구축하려는 노력에 집중하고 있습니다.


RGB는 Bitcoin 토끼굴 안에 자체 토끼굴이 있는데, 제가 그 토끼굴을 빠져나오는 동안 제가 배운 것을 게시하고 다음 글에서는 LNP 및 RGB 노드와 사용 방법에 대해 소개할 것입니다.



- 1 https://plan99.net/~mike/Satoshi-emails/thread4.html
- 2 https://btctranscripts.com/chaincode-labs/chaincode-residency/2018-10-22-christian-decker-history-of-lightning/
- 3 https://lists.linuxfoundation.org/pipermail/Bitcoin-dev/2016-June/012773.html
- 4 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0020.md
- 5 https://github.com/LNP-BP/LNPBPs/blob/master/lnpbp-0021.md


## RGB 노드 튜토리얼


### 소개


이 튜토리얼에서는 RGB 노드를 사용하여 대체 가능한 token을 생성하는 방법과 이를 전송하는 방법을 설명합니다. 이 문서는 RGB 노드 데모를 기반으로 하며 실제 Testnet 데이터를 사용한다는 점에서 다르며, 이를 위해서는 지금부터 자체 Partially Signed Bitcoin Transaction, PSBT를 구축해야 한다는 점이 다릅니다.


### 요구 사항


이 튜토리얼은 우분투를 기반으로 하는 Pop!OS를 사용하여 작성되었으므로 Linux 배포판을 사용하는 것이 좋습니다:



- 화물
- Bitcoin core
- git


참고: 이 튜토리얼에서는 Linux 터미널에서 명령을 실행하는 방법을 보여드리며, 사용자가 작성한 내용과 터미널에서 받는 응답을 구분하기 위해 bash 프롬프트를 상징하는 $를 포함시켰습니다.


몇 가지 종속성을 설치해야 합니다:


```
$ sudo apt install -y build-essential pkg-config libzmq3-dev libssl-dev libpq-dev libsqlite3-dev cmake
```


빌드 및 실행


RGB 노드는 WIP(작업 진행 중)이므로 올바르게 컴파일하고 사용할 수 있도록 특정 커밋(3f3c520c19d84c66d430e76f0fc68c5a66d79c84)에서 자신을 찾아야 하며, 이를 위해 다음 명령을 실행합니다.


```
$ git clone https://github.com/rgb-org/rgb-node.git
$ cd rgb-node
$ git checkout 3f3c520c19d84c66d430e76f0fc68c5a66d79c84
```


이제 컴파일을 하는데, 박수 버전에 획기적인 변경 사항이 도입되었으므로 --locked 플래그를 사용하는 것을 잊지 마세요.


```
$ cargo install --path . --all-features --locked

....
....
Finished release [optimized] target(s) in 2m 14s
Installing /home/user/.cargo/bin/fungibled
Installing /home/user/.cargo/bin/rgb-cli
Installing /home/user/.cargo/bin/rgbd
Installing /home/user/.cargo/bin/stashd
Installed package `rgb_node v0.4.2 (/home/user/dev/rgb-node)` (executables `fungibled`, `rgb-cli`, `rgbd`, `stashd`)

```


Rust 컴파일러에 따르면 바이너리는 $HOME/.cargo/bin 디렉터리에 복사되었으므로 컴파일러가 다른 위치에 복사한 경우 해당 디렉터리가 $PATH에 포함되어 있는지 확인해야 합니다.


설치된 바이너리 중 3개의 데몬 또는 서비스(d로 끝나는 파일)와 CLI(명령줄 Interface)를 볼 수 있으며, CLI를 사용하면 기본 rgbd daemon과 상호 작용할 수 있습니다. 이 튜토리얼에서는 두 개의 노드를 실행할 예정이므로 두 개의 클라이언트가 필요하며, 각 클라이언트는 자체 노드에 연결해야 하므로 두 개의 별칭을 생성합니다.


```
alias rgb0-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data0 -n testnet"
alias rgb1-cli="$HOME/.cargo/bin/rgb-cli -d $HOME/rgbdata/data1 -n testnet"
```


별칭을 실행하거나 $HOME/.bashrc 파일 끝에 별칭을 추가하고 소스 $HOME/.bashrc를 실행하면 됩니다.

전제


RGB 노드는 Wallet 관련 기능을 처리하지 않으며, Bitcoin core과 같은 외부 Wallet에서 제공할 데이터에 대한 RGB 전용 작업만 수행합니다. 특히 발급 및 전송에 대한 기본적인 워크플로우를 시연하기 위해서는 다음과 같은 기능이 필요합니다:



- RGB-node-0이 새로 발행된 자산을 바인딩할 발행_utxo입니다
- RGB-node-1이 자산을 수신하는 receive_utxo
- RGB-node-0이 자산 변경 사항을 수신하는 change_utxo
- 출력 공개 키가 전송에 Commitment을 포함하도록 조정되는 Partially Signed Bitcoin Transaction(tx.PSBT)입니다.


Bitcoin core CLI을 사용하고, bitcoind daemon를 Testnet에서 실행해야 상호 운용성을 확보할 수 있으며, 마지막에는 이 튜토리얼을 따라 한 다른 RGB 사용자에게 자신의 에셋을 보낼 수 있게 됩니다.


간단하게 하기 위해 이 별칭을 ~/.bashrc 파일 끝에 추가하겠습니다.


```
alias bcli="bitcoin-cli -testnet"
```


미사용 출력 트랜잭션을 나열하고 두 개를 선택해 보겠습니다. 하나는 발급_utxo, 다른 하나는 변경_utxo가 될 것입니다. 중요한 것은 발행자가 이 두 UTXO를 제어할 수 있다는 것입니다.


```
$ bcli listunspent
[
{
"txid": "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893",
"vout": 1,
"address": "tb1qn4w9u5x0hxgm30hx6q2rhdwz58xr4ekqdq0vgm",
"label": "",
"scriptPubKey": "00149d5c5e50cfb991b8bee6d0143bb5c2a1cc3ae6c0",
"amount": 0.01703963,
"confirmations": 62432,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/0'/5']031e0fc9a03e69326c3deeabfd749a7f7b094e3151ada90cd13019efac663c5663)#dj7rhpdt",
"safe": true
},
{
"txid": "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f",
"vout": 1,
"address": "tb1qyd537gf0xmm9ehmhaf3nv0a230crg56mhp9ap3",
"scriptPubKey": "001423691f212f36f65cdf77ea63363faa8bf034535b",
"amount": 0.02877504,
"confirmations": 189184,
"spendable": true,
"solvable": true,
"desc": "wpkh([ec924f82/0'/1'/0']03ae333417e86840145e95ab2852c8f7ca8b8f82cd910883f7ce0c69649403cef2)#jlcj23vw",
"safe": true
}
]
```


아웃포인트에 대해 더 알아보기 전에 단일 트랜잭션에는 여러 개의 출력이 포함될 수 있으며, 아웃포인트에는 콜론으로 구분된 특정 출력을 참조하기 위해 32바이트 txid과 4바이트 출력 인덱스 번호(vout)가 모두 포함됩니다. Listunspent 출력에서 두 개의 UTXO를 볼 수 있는데, 각각 txid과 vout은 발급_utxo 및 변경_utxo 아웃포인트입니다.


receive_utxo는 수신기가 제어하는 UTXO이며, 이 경우 다른 Wallet의 아웃포인트인 e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0을 사용할 것입니다.



- iSSUANCE_UTXO: 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
- change_utxo: cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1
- receive_utxo: e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0


이제 부분적으로 서명된 트랜잭션(tx.PSBT)을 생성하여 전송 커밋을 포함하도록 출력을 조정할 것입니다. txid와 vout을 여러분의 것으로 바꾸는 것을 잊지 마세요. 대상 Address는 중요하지 않으며, 여러분의 것이 될 수도 있고 다른 사람의 것이 될 수도 있고 Sats이 어디로 가는지는 중요하지 않으며, 중요한 것은 발급_utxo를 사용한다는 점입니다.


```
$ bcli walletcreatefundedpsbt "[{/"txid/":/"4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893/",/"vout/":1}]" "[{/"tb1q9crtjp0y6rt00c4fcrmuamrylzkcalcxls80j9/":/"0.00050000/"}]"
{
"psbt": "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==",
"fee": 0.00000280,
"changepos": 0
}
```


출력은 base64 인코딩의 PSBT을 제공했으며, 이를 사용하여 tx.PSBT을 만들 것입니다.


```
$ echo "cHNidP8BAHECAAAAAZM4E58uD9auiZ7esJkFbmD5p/7PcgBTn5UwiQ0hhRdMAQAAAAD/////ArM7GQAAAAAAFgAU4xQr/g1lgG2P9+gZudpFD8mOGGRQwwAAAAAAABYAFC4GuQXk0Nb34qnA987sZPitjv8GAAAAAAABAHECAAAAAYiK0TdTiaEs4oDovRokqspfLZr5EHYH8Pnj/Tv5GFB5AQAAAAD+////Av8Bh80AAAAAFgAUsLjOd30aRkUna41LAT5c3CnAz5obABoAAAAAABYAFJ1cXlDPuZG4vubQFDu1wqHMOubAyw8gAAEBHxsAGgAAAAAAFgAUnVxeUM+5kbi+5tAUO7XCocw65sAiBgMeD8mgPmkybD3uq/10mn97CU4xUa2pDNEwGe+sZjxWYxDskk+CAAAAgAAAAIAFAACAACICA2J21wOqW6bj7/ePTVI7QGvU6e4Sk8DhN5pmd9hrwSd7EOyST4IAAACAAQAAgAcAAIAAAA==" | base64 -d > tx.psbt
```


각 노드의 데이터 디렉터리가 저장되는 rgbdata라는 새 디렉터리를 만들어 보겠습니다.


```
$ mkdir $HOME/rgbdata
$ cd $HOME/rgbdata
```


이미 $HOME/rgbdata에 위치한 각 노드를 다른 터미널에서 시작하는데, 여기서 ~/.cargo/bin은 RGB 노드 설치 후 카고가 모든 바이너리를 복사한 디렉터리입니다.


```
$ rgbd -vvvv -b ~/.cargo/bin -d ./data0 -n testnet
$ rgbd -vvvv -b ~/.cargo/bin -d ./data1 -n testnet
```


### 발급


자산을 발행하려면 대체 가능한 발행 하위 명령으로 rgb0-CLI를 실행한 다음 인수, 티커 USDT, 이름 "USD Tether", 할당에 아래에서 보는 것처럼 발행 금액과 발행_utxo를 사용합니다:


```
$ rgb0-cli fungible issue USDT "USD Tether" 1000@4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1
```


자산이 성공적으로 발행되었습니다. 이 정보를 사용하여 공유하세요:

자산 정보:


```
genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"


genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
```


에셋을 전송하려면 에셋아이디가 필요합니다.


```
$ rgb0-cli fungible list

- name: USD Tether
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
```


### generate blinded UTXO


새로운 USDT를 받기 위해 RGB-node-1은 자산을 보유하기 위해 receive_utxo에 해당하는 blinded UTXO을 generate해야 합니다.


```
$ rgb1-cli fungible blind e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0

Blinded outpoint: utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf
Outpoint blinding secret: 1679197189805229975
```


이 UTXO과 관련된 전송을 수락하려면 원본 receive_utxo와 blinding_factor가 필요합니다.


### 전송


자산의 일정량을 RGB-node-1로 전송하려면 blinded UTXO로 전송해야 하고, RGB-node-0은 Consignment와 공개를 생성하고 이를 Bitcoin 트랜잭션에 커밋해야 합니다. 그런 다음 커밋을 포함하도록 수정할 PSBT이 필요합니다. 또한 -i 및 -a 옵션을 사용하면 자산의 원본이 될 입력 아웃포인트와 변경 사항을 받을 할당을 제공할 수 있으며, @<change_utxo>와 같은 방식으로 이를 표시해야 합니다.


```
$ rgb0-cli fungible transfer utxob16az597vp5nkr66nfzsykf8ngdnvzep5050rm00l7vv8wm7vew4jqj7jhhf 100 rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6 tx.psbt consignment.rgb disclosure.rgb witness.psbt -i 4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1 -a 900@cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1

Transfer succeeded, consignments and disclosure are written to "consignment.rgb" and "disclosure.rgb", partially signed witness transaction to "witness.psbt"
Consignment data to share:consignment1qxz4g7ec6da33llaxe97u9hx8p9wcgp2yv46ycudwy7ytjf4gdh88x6upcdmjfy3mp4y0n669j5ar5y6e04zfr7255kynff6eymx9tdfc7jux5jk6tgn4xm6lttlh3lh08070ltuh60l07mamlns2qyy984mg4m5dz0x6s5sy5edls2zjlmnvw708sh7fy2vuph745jcpgp92qrw27s73vm4ghrx57vammyf8wautwu5euujd8w3dupdtgp4px36gz8z0ywnuty45uqdwk672qqzjp3j77yl7urft6gewqksqgppczezn5c7gyux6gzgpye0wgyjp85ufdqlzy5cd8zwfg3q9550xq2hyf24qqz92wqskpgq8qsr8kp5p9dt49evmqlze9ylrx2sqpwpvpqp45lpvgjkgk542pks9850w5jquq3qqsj4xsqn9nu6w30lgpmrhdqs6jj0ez3myhj74kp223f0wg2y7vupczdq5pa23mzhzc6l647nl6ftrru0mjrh739yhgztsdhl2cdmhf0qm7du9n20up4rnnsp0tlp8665xldkq9z9u85tgh6nxmkfg3pc6wzk2t90pekj2d6l0km09vyt4vut24vhzg9qhrdsgr7dws828p6ejk7ddy0zkz3a2fq5648664w3se2egwvh904lzmpnc7a7wy4fayznunt6j4ndmm68y24tjje4qxnxs70w4lr9vz9q9qca903edtjd6c5f37jagafsqnhnlsuwvnqwc7uly4dw2rnlyxp4zcfqrfpkpez54c0lc3tmvppmv06ge97heevgt0acrq0ezgjr6ck9waqpanypl8dzrqdzjd05h735tdgv2wjjjucheur40h4wjw4pcdpc8pqlh7ef95rj2al8v3eexkgty8j2ne7kk2zxpe0wypq8ra0x76rt6cu00cw4w05v0u3ng6zhfrttz2c3m5nx64s8w98wa26dx79jwhne44gp9lmg6vkhxq98meslyr4zqtxjsg27xzj80m0csd77lr047vwycvdw0z8mwudm3uvlry9p9da4su72k9q84pphw4n0fyeet0ujzrdgacm6p777jun0y0v397mp4drafr6q7994kdl96m388xp6ggf5arn4d4ed53rv9tlkerckqvkng92uhdvngwcl3m6yqhxdjjnkca62tckxfnrae4cx4e6wx6ww5649v4hvuwkkajanllc38wavqy83xhn555l708354nt2quscchexsxjgezdxfnmxgue0cn4ktghd6xd2le76k5cw3t0p0nurs4h5rjz0j7twj9ulwkp7cmhhgl23r7g677gk36r5jw8panh2sq5966m08sa5632egd5ms6h0e504dtwskct3x6a93uutaumtc8aam8yyt66lrmrhcssw9ga2yg0496s6sdmaexa49064g3syc888egnwa8racrwwwwemknqamarpqlmqa5mg8zgt0dts8ehuwmgz4j3cjltr8gv78e7p84zm8pylann7dmss5suf4htqc04qx5trnk59m305ah2qp4mvkxwy6ts84sa30d80jzk9s6n40e4j8dcvq79ncg5e3z5g4esxyawmxk7lvm5efc30vtw8qqhe9xx3773djez6hjjx0x962z2radnvdmazkrmlqw7guxz29qvahcx79h33ncqhzhvekwaqqnrz3wxnp2qy3u83zdgdcgq27n5n22h7jjedrh28m8c6mn42xhfjasm5njsxtufqjxefnhc2n5zr0um0xlqk62cu25cjwuwwrcv3e4vhh2tdzn8rnlaefj98fvslg7sun95wpt2a4vcg4ua62v97aeqstvjegmlem5crnsamrhm3a2pcma2s22atr43lgx9vh7kn9lzymfe83a4vhe9rc6xl5pmy5hjw4t88k0fwh6lzmjtjvqtczq47ny7hv8ytdqdy2c7ce3gegnufkzwphkwtz6xqzklyw7e7f76fwfewfuyqal7dl8r9476jerrl40mav38sun2u8jvftw33x3r20dmeka34znmkgaz29ppk5hz3ldttw8zyz4k6q0gts8utqh53tuc7vtajl26rq2fnxr0vxcwlx9rfvn6v8ar8c73qkc3zca4mlgl7qu36sk7e
```


이렇게 하면 Consignment, 공개 및 조정 내용을 포함한 PSBT라는 세 개의 새 파일이 작성되고, 이 PSBT는 Witness Transaction이라고 하며, Consignment은 RGB-node-1로 전송됩니다.


### 증인


Witness Transaction를 서명하고 브로드캐스트해야 하므로 이를 다시 Base64로 인코딩해야 합니다.


```
$ base64 -w0 witness.psbt

cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA==
```


Walletprocesspsbt 하위 명령으로 서명합니다.


```
$ bcli walletprocesspsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8iBgKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cxDskk+CAAAAgAEAAIADAACAACICAsnwAXsMVlPXi/2ExgqtLoIN4TncWVW0EImSo9YwyhNmEOyST4IAAACAAQAAgAUAAIAG/ANSR0IBIQLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZgb8A1JHQgIgMD8j8bQGB8NgEobv3NUJr7aERA/FkGgQ5w2KwF+daDgAAA=="
{
"psbt": "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA=",
"complete": true
}
```


이제 마무리하고 암호를 받으세요.


```
$ bcli finalizepsbt "cHNidP8BAHECAAAAAe2pydT0BqfK5nBCdBSbm3W/vNKE/QxTr4eJcjwjDLDjAQAAAAD/////AiWbAAAAAAAAFgAUO1Bi4v2VHUJPmq5iyYhDv1tyTCcQJwAAAAAAABYAFPwfm3skdSeMnOfcDqBpgVjwuwESAAAAAAABAHECAAAAAeSwUiZ+p3/NM7yt3BAoDkm/afi//lplsffwwpTqjd+CAQAAAAD/////AlDDAAAAAAAAFgAULga5BeTQ1vfiqcD3zuxk+K2O/wbDwgAAAAAAABYAFLsvLLowx0NR5NyFKj9wl3IFvNcPAAAAAAEBH8PCAAAAAAAAFgAUuy8sujDHQ1Hk3IUqP3CXcgW81w8BCGsCRzBEAiAZud+YVf1FyZq0IDQ+/oAE34TKypedrJGUcYx0QIpaygIgZJO7xvN0dOQXbXTRYE0QxGIWsfo85Dhwne0/whoO06kBIQKIYFEbYKvRj25inaA0/c0PMIZD/BFAgFbjrBJe8cZ+cwAiAgLJ8AF7DFZT14v9hMYKrS6CDeE53FlVtBCJkqPWMMoTZhDskk+CAAAAgAEAAIAFAACABvwDUkdCASECyfABewxWU9eL/YTGCq0ugg3hOdxZVbQQiZKj1jDKE2YG/ANSR0ICIDA/I/G0BgfDYBKG79zVCa+2hEQPxZBoEOcNisBfnWg4AAA="
{
"hex": "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000",
"complete": true
}
```


### 방송


Sendrawtransaction 하위 명령을 사용하여 브로드캐스트하여 Blockchain로 확인을 받습니다.


```
$ bcli sendrawtransaction "02000000000101eda9c9d4f406a7cae6704274149b9b75bfbcd284fd0c53af8789723c230cb0e30100000000ffffffff02259b0000000000001600143b5062e2fd951d424f9aae62c98843bf5b724c271027000000000000160014fc1f9b7b2475278c9ce7dc0ea0698158f0bb011202473044022019b9df9855fd45c99ab420343efe8004df84caca979dac9194718c74408a5aca02206493bbc6f37474e4176d74d1604d10c46216b1fa3ce438709ded3fc21a0ed3a90121028860511b60abd18f6e629da034fdcd0f308643fc11408056e3ac125ef1c67e7300000000"
8e3787fe40b5feb3044f892e739bdb4043e10de384255a915a37725811abc3fe
```


### 수락


들어오는 전송을 수락하려면 RGB-node-1이 RGB-node-0으로부터 Consignment 파일을 수신해야 하며, 블라인드 UTXO 생성 중에 receive_utxo와 해당 블라인드_팩터가 생성되어 있어야 합니다.


```
$ rgb1-cli fungible accept consignment.rgb e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0 1679197189805229975

Asset transfer successfully accepted.
```


이제 <receive_utxo>를 실행하면 알려진 할당 필드에서 100개의 자산 유닛에 대한 새로운 할당을 확인할 수 있습니다:


```
$ rgb1-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 1
outpoint: "e40d9037e31d3f440552b30af16e764cf25ffda3899b4851cc4e38fd64718b09:0"
revealedAmount:
value: 100
blinding: 224561f10229eb9ebbdf05f497132d2b8344d70971c80510eddc607d615ee2a0
```


송금 당시 receive_utxo가 blinded였기 때문에, 지급인 RGB-node-0은 100 USDT가 전송된 위치에 대한 정보가 없으므로 알려진 할당에 위치가 표시되지 않습니다.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
```


그러나 보시다시피 RGB-node-0은 전송 명령에 -a 인수로 제공한 900개의 자산 변경을 볼 수 없습니다. 변경 사항을 등록하려면 RGB-node-0이 공개를 수락해야 합니다.


```
$ rgb0-cli fungible enclose disclosure.rgb

Disclosure data successfully enclosed.
```


RGB-node-0이 성공했다면 에셋을 나열하여 변경 사항을 확인할 수 있습니다.


```
$ rgb0-cli fungible list -l

- genesis: genesis1qyfe883hey6jrgj2xvk5g3dfmfqfzm7a4wez4pd2krf7ltsxffd6u6nrvjvvnc8vt9llmp7663pgututl9heuwaudet72ay9j6thc6cetuvhxvsqqya5xjt2w9y4u6sfkuszwwctnrpug5yjxnthmr3mydg05rdrpspcxysnqvvqpfvag2w8jxzzsz9pf8pjfwf0xvln5z7w93yjln3gcnyxsa04jsf2p8vu4sxgppfv0j9qerppqxhvztpqscnjsxvq5gdfy5v6j3wvpjxxqzcerxuglngnfvpxjkgqusct7cyx8zzezcfpqv3nxjxm2kjj4d0zu0ta6fjmpr8a0calk6h88h4ap5e4nucj0ch07aa73qsh3lj5sd89a32kwy0eq7tsa5zqqjpdqvqq5s46r0
id: rgb1tadqzve7vwfh39sl6gvqenp8wegsrzreekhhu0dhthx08ppzj9wq8p0je6
ticker: USDT
name: USD Tether
description: ~
knownCirculating: 1000
isIssuedKnown: ~
issueLimit: 0
chain: testnet
decimalPrecision: 0
date: "2022-02-23T20:53:26"
knownIssues:
- id: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
amount: 1000
origin: ~
knownInflation: {}
knownAllocations:
- nodeId: 5c912284f3cc5db73d7eafcd798801517627cc0c18d21f967893633e33015a5f
index: 0
outpoint: "4c1785210d8930959f530072cffea7f9606e0599b0de9e89aed60f2e9f133893:1"
revealedAmount:
value: 1000
blinding: "0000000000000000000000000000000000000000000000000000000000000001"
- nodeId: 28f82e2dcfa91282c28a8805ff0c7fde4bd4e0bdbd40c6ba55e191666e45327b
index: 0
outpoint: "cd66d3b77dfc1c2ecf958847c16a8a1311bba84ee7bf9dd55592a7b97b13028f:1"
revealedAmount:
value: 900
blinding: ddba9e0efdd614614420fa0b68ecd2d3376a05dd3d809b2ad1f5fe0f6ed75ea2
```


### 결론


우리는 대체 가능한 자산을 생성하고 비공개 방식으로 한 거래에서 다른 거래로 이동할 수있었습니다. Block explorer에서 확인 된 거래를 확인하면 일반 거래와 다른 점을 찾을 수 없으며, 이는 RGB가 일회용 씰을 사용하여 거래를 조정한다는 사실 덕분입니다. 이 게시물에서는 RGB가 어떻게 작동하는지 소개합니다.


이 게시물에 버그가 있을 수 있습니다. 이 가이드를 개선하기 위해 무언가를 발견하면 알려주세요, 제안 및 비판도 환영합니다, 행복한 해킹! 🖖