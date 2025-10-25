---
name: Lightning Network Daemon (Linux)
description: Linux에서 Lightning Network Daemon 설치 및 실행
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network는 Bitcoin의 두 번째 Layer로, 특히 거래의 속도와 저렴한 비용 덕분에 번개처럼 빠르게 처리할 수 있습니다.



이 튜토리얼에서는 Linux 시스템(Ubuntu 24.04 배포판)에 Lightning Network Daemon 구현을 설치합니다.



## Lightning Network Daemon이란 무엇인가요?



Lightning Network Daemon은 Lightning Network의 완전한 Go 구현입니다. Lightning Labs에서 만든 것으로, 컴퓨터에서 라이트닝 노드의 전체 인스턴스를 실행할 수 있습니다.


즉, 이 구현을 사용하면 :





- Lightning Network**와 상호작용하세요: 명령줄을 사용해 컴퓨터 단말기에서 직접 라이트닝 지갑을 만들고, 결제 채널과 경로를 관리하는 등 다양한 작업을 수행할 수 있습니다.
- 원격 Bitcoin 노드 또는 자체 Bitcoin core 인스턴스 연결**: LND를 사용하면 Bitcoin 인스턴스를 연결하여 백엔드로 사용할 수 있습니다. 이 구현을 사용하려면 컴퓨터에서 Bitcoin core 인스턴스를 실행할 필요가 없습니다.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## 나만의 라이트닝 노드를 보유해야 하는 이유는 무엇인가요?


라이트닝은 전송 프로세스를 최적화하고 거래 비용을 절감하는 Bitcoin 오버레이입니다.



라이트닝 노드를 회전시키면 주권과 자율성을 얻게 됩니다. 자금에 대한 통제권은 여러분에게 있다는 점을 명심하세요:



"열쇠가 아니라 비트코인이 아닙니다."



이러한 의미에서 라이트닝 노드를 실행하면 다음과 같은 방식으로 데이터의 보안과 무결성이 향상됩니다:





- 완전한 제어**: 나만의 결제 채널을 관리하고, 나만의 은행이 되어 자산의 주인이 되세요.
- 기밀 유지**: 개인정보 보호를 위해 제3자에 의존하지 않고 거래하세요.
- 학습과 자율성**: Lncli` 명령어 덕분에 터미널에서 직접 적용해 봄으로써 Lightning의 기본 프로세스를 더 잘 이해할 수 있습니다.
- 탈중앙화**: Bitcoin/Lightning Network를 강화하고 탈중앙화하는 데 적극적으로 참여하세요.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


머신에서 LND 구현 인스턴스를 실행하는 데는 두 가지 옵션이 있습니다. 로컬에서 실행하도록 자체 머신에서 환경을 설정하거나 Docker 컨테이너에서 LND을 설치할 수 있습니다. 여기서는 첫 번째 옵션에 집중하고 이후 튜토리얼에서 Docker를 진행하는 방법을 살펴보겠습니다.


## 소스 코드에서 LND 설치



### 전제 조건


LND은 Go로 작성되었으므로 Linux 시스템에 GoLang 환경과 필요한 종속성이 있는지 확인해야 합니다.





- 하드웨어 요구 사항:**


원활하고 원활한 경험을 위해서는 컴퓨터가 LND 라이트닝 노드를 실행하는 데 필요한 용량을 갖추고 있어야 합니다.



다음이 필요합니다:


1. *최적의 유동성을 위한 *8GB RAM**,


2. **멀티코어 프로세서(쿼드코어 이상)**를 통해 노드의 작업을 효율적으로 관리할 수 있습니다,


3. **pruned 노드 모드의 경우 최소 5GB의 디스크 공간**, Bitcoin core을 실행하려면 1TB(원격 노드를 사용하는 경우 선택 사항)





- 유용한 종속성을 설치합니다:


아래 명령어를 통해 LND를 실행하는 데 필요한 도구를 머신에 설치할 수 있습니다. 무엇보다도 버전 관리 도구인 `Git`과 소스 코드에서 LND 구현을 실행하고 빌드할 수 있는 `make`를 설치해야 합니다.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Linux 머신에 GoLang 설치**



이 튜토리얼 날짜 기준으로 LND을 설치하려면 **Go** 버전 1.23.6이 필요합니다.



이전 버전이 이미 설치되어 있는 경우 새 Go 설치를 위해 해당 버전을 제거하세요.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Go** 환경 구성


.bashrc` 파일에서 다음 환경 변수를 초기화하여 Linux 시스템에 Go를 추가합니다.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- 설치** 확인 (프랑스어)


```bash
go version
```



![go-version](assets/fr/03.webp)


### LND GitHub 리포지토리 복제하기



LND 소스 코드의 복사본을 컴퓨터에 로컬로 가져오려면 git을 사용하세요


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### 빌드 및 설치



이전에 설치한 `make` 도구를 사용하면 LND 소스 코드에서 실행 파일을 빌드하고 설치를 진행할 수 있습니다.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



머신에 LND 설치



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- 설치 확인** (프랑스어)



모든 것이 원활하게 진행되었는지 확인하기 위해 이 명령을 실행하면 현재 실행 중인 LND의 버전이 표시됩니다.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- 유지 관리 및 업그레이드



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **중요**: LND 업데이트에는 최신 버전의 Go가 필요할 수 있으므로 설치 중 종속성 문제를 방지하기 위해 시스템을 업데이트해야 합니다.


### Lightning Network Daemon 구성



Lightning LND 노드의 구성은 Bitcoin의 구성과 유사하며 노드의 모든 파라미터가 포함된 구성 파일에서 수행됩니다. 이렇게 하려면 컴퓨터의 루트에서 '.LND'라는 숨겨진 폴더를 만든 다음 이 폴더에 구성 파일인 `LND.conf`를 생성하면 됩니다.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





구성 파일에서 LND 노드를 설정할 수 있습니다.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## 구성 이해



LND 노드를 올바르고 완벽하게 설치하는 데 필요한 최소 구성을 이해하는 것이 중요합니다.



.LND/LND.conf` 파일의 내용을 바탕으로 필드에 대한 자세한 내용은 다음과 같습니다:





- 노즈백업**: LND이 지갑의 자동 백업을 수행할지 여부를 선택할 수 있습니다. 이 속성을 '0'으로 설정하면 개인적으로 선택한 안전한 위치에 복원 정보를 수동으로 저장할 수 있습니다.





- 디버그 레벨**: 작업 중 오류가 발생할 경우 오류 및 로그의 세부 수준을 정의할 수 있습니다.





- Bitcoin.active**: LND이 Bitcoin 노드로 작동하고 Bitcoin 네트워크와 상호 작용하도록 지시합니다.





- Bitcoin.Mainnet**: Bitcoin의 메인 네트워크(Mainnet)에 연결하기 위해 LND를 지정하며, Bitcoin Signet 및 Bitcoin Regtest 네트워크에 각각 `bitcoind.signet` 및 `bitcoind.regtest` 값을 설정할 수 있습니다





- Bitcoin.node**: LND가 연결할 Bitcoin 노드의 유형을 지정합니다.





- Bitcoin.rpcuser** 및 **Bitcoin.rpcpassword** : 대표.


각각 Bitcoin 노드에 연결하기 위한 로그인(사용자, 비밀번호)을 입력합니다





- bitcoind.zmqpubrawblock** 및 **bitcoind.zmqpubrawtx**: 각각 Bitcoin 네트워크에서 새로운 블록 및 트랜잭션에 대한 알림을 수신하는 제로엠큐 엔드포인트를 정의합니다.




## LND로 설치 확인



프로세스가 성공적으로 완료되었는지, 노드 정보를 최신 상태로 유지하기 위해 Lightning Network과 동기화하고 있는지 확인하고 싶을 것입니다.



LND 구현을 시작하고 노드에 대한 정보를 얻으려면 명령어를 입력하기만 하면 됩니다:


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## LND에서 작업 수행



설치가 완료되고 확인이 완료되면 사용을 시작할 수 있습니다.


다음은 시작하기 위한 필수 명령어입니다.



### Wallet 생성


자금 관리를 위한 모든 작업의 첫 번째 단계는 Lightning Wallet입니다.



⚠️ **중요**: 24단어 **seed 문구**를 주의 깊게 기록해 두세요. 문제 발생 시 자금을 회수하는 데 필요합니다.



또한 Wallet 노드를 재시작할 때 `lncli unlock` 명령으로 잠금을 해제할 수 있도록 LND 비밀번호를 저장해 두세요.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### 잔액 확인



단말기에서 직접 계정을 확인하세요:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### 노드에 대한 정보



아래 명령을 사용하여 노드에서 어떤 채널이 활성화되어 있는지 확인하세요.



```bash
lncli listchannels
```



연결된 노드 목록도 확인할 수 있습니다.



```bash
lncli listpeers
```



### 채널 관리



라이트닝 채널을 사용하면 Lightning Network의 다른 노드와 **쌍 단위로 직접 연결**할 수 있습니다. 이 채널에서는 채널의 용량까지 자유롭게 Exchange 사토시를 사용할 수 있습니다.



### 노드에 연결



다른 라이트닝 노드에 연결하는 것은 라이트닝의 힘을 적극적으로 활용하고 혜택을 누리기 위한 기본적인 조치입니다.



피어(라이트닝 노드)에 연결하려면 세 가지 정보가 필요합니다:




- 노드의 공개 키**: Bitcoin 네트워크에서 노드의 고유 식별자입니다;
- IP**: 노드가 설치된 컴퓨터의 IP입니다;
- PORT**: 이 노드와 통신할 수 있는 컴퓨터에서 열려 있는 포트입니다.



라이트닝 노드에 대한 정보를 나열하는 플랫폼인 [amboss](https://amboss.space/)에서 연결할 노드를 찾을 수 있습니다.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




내 시스템의 무결성을 유지하기 위해 **신뢰할 수 있는 노드**에 연결해야 합니다. 다음은 올바른 연결을 선택하기 위한 몇 가지 권장 사항입니다.





- 지리적 다각화**: 다른 지역의 노드에 연결하세요.





- 평판**: 가용성이 좋은 노드를 선택하세요.





- 용량**: 유동성이 좋은 매듭을 선택하세요.





- 요금**: 라우팅 요금을 확인합니다.


### 결제 채널 열기


결제 채널을 열려면 피어 노드에 **연결**되어 있는지 확인한 다음, 이 채널에서 차단하려는 **용량**(사토시의 양)을 정의하세요.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### 라이트닝 Invoice 생성



라이트닝 Invoice는 라이트닝 Wallet에서 사토시를 받고 싶다는 의사를 표현하는 문자열을 나타냅니다.


자체 노드로 Lightning 인보이스를 생성하면 데이터(지리적 및 개인 정보)를 보호하고 자금 관리에 대한 100% 자율성을 확보할 수 있습니다.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### 라이트닝 Invoice 지불하기



```bash
lncli payinvoice <FACTURE>
```


### 채널 닫기



현재 노드에서 활성 채널을 닫는 방법에는 두 가지가 있습니다.





- 협력 폐쇄**: 이는 노드가 결제 채널에서 탈퇴하겠다는 신호를 보내 진행 중인 작업을 완료하고 자금 손실을 방지하기 위해 데이터를 백업한다는 뜻입니다.


```
lncli closechannel <ID_CANAL>
```




- 강제 폐쇄**: ⚠️ 이 조치는 결제 채널에서 진행 중인 프로세스를 중단시키고 자금 손실 위험을 증가시키므로 가급적 피해야 합니다.


```
lncli closechannel --force <ID_CANAL>
```


## LND 노드를 위한 모범 사례 및 안전.


Bitcoin/라이트닝 노드를 사용할 때는 안전이 가장 중요합니다. 다음은 설치의 안전성을 강화하기 위한 몇 가지 사항입니다:





- 'seed 문구'를 안전한 오프라인 위치에 보관하세요.





- '~/.LND/channel.backup' 파일을 정기적으로 백업하세요: 이 파일은 노드에서 새 채널이 열릴 때마다(또는 이전 채널이 닫힐 때마다) 채널 상태를 저장합니다.


⚠️ 데이터 손실 또는 노드 장애 발생 시 채널을 복원하고 결제 채널에서 차단된 자금을 복구할 수 있습니다



이 파일의 백업 경로를 지정하여 아래 명령어로 자금을 복원할 수 있습니다:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Lightning Wallet의 복원 단어와 비밀번호를 저장했는지 확인하세요.
- 시스템을 최신 상태로 유지하세요.



## 현재 문제 해결


### 자주 발생하는 문제




- bitcoind 연결 오류**: RPC 로그인 정보 확인
- 동기화가 차단됨**: 인터넷 연결 확인
- 권한 오류**: 폴더 `~/.LND`의 권한을 확인하세요




이제 이 튜토리얼의 마지막 단계에 도달했습니다. Lightning에 대해 더 자세히 알고 싶으시다면 이 입문 과정을 통해 Lightning Network의 개념과 사례를 더 잘 이해하실 수 있습니다.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb