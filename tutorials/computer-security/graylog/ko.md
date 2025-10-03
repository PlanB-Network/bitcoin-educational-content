---
name: Graylog
description: 간편한 로그 중앙 집중화 및 분석
---
![cover](assets/cover.webp)



___



*이 튜토리얼은 [IT-Connect](https://www.it-connect.fr/)에 게시된 플로리안 버넬의 오리지널 콘텐츠를 기반으로 합니다. 라이선스 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 원본 텍스트가 변경되었을 수 있습니다*



___



## 데비안 12에 그레이로그 배포



### I. 프레젠테이션



Graylog는 머신과 네트워크 장치의 로그를 실시간으로 중앙 집중화하여 저장하고 분석하도록 설계된 오픈 소스 "로그 싱크" 솔루션입니다. 이 튜토리얼에서는 무료 버전의 Graylog를 데비안 12 머신에 설치하는 방법을 알아보세요!



정보 시스템 내에서 **리눅스**나 **윈도우**를 실행하는 각 **서버**와 각 **네트워크 장치**(스위치, 라우터, 방화벽 등)는 **자체적인 로그**를 생성하여 로컬에 저장합니다. 로그가 각 머신에 로컬로 저장되면 이벤트 분석 및 상관관계 파악이 매우 어렵습니다... 이때 **Graylog**가 등장합니다. 그레이로그는 **로그 싱크** 역할을 하며, 이는 **모든 머신이 (예를 들어 syslog를 통해) 로그를 전송**한다는 것을 의미합니다. 그러면 Graylog는 이러한 로그를 **저장하고 색인을 생성**하는 동시에 글로벌 검색을 수행하고 알림을 생성할 수 있습니다.



그레이로그는 의심스러운 행동과 다양한 문제(안정성, 성능 등)를 쉽게 식별할 수 있는 분석 및 모니터링 도구입니다.




![Image](assets/fr/034.webp)



**참고: 무료 버전인 Graylog Open은 실제 침입 탐지 기능이 없기 때문에 Wazuh와 같은 SIEM이 아닙니다.**



### II. 전제 조건



스택 그레이로그**는 설치 및 구성해야 하는 **여러 구성 요소**를 기반으로 합니다. 여기서는 모든 구성 요소를 동일한 서버에 설치하지만 여러 노드를 기반으로 클러스터를 생성하고 여러 서버에 역할을 분산할 수 있습니다. 이 튜토리얼에서는 현재 가장 최신 버전인 **Graylog 6.1**을 설치하겠습니다.





- 현재 그레이로그에 권장되는 버전인 MongoDB 7**(최소 5.0.7, 최대 7.x)
- Amazon에서 만든 Elasticsearch의 오픈 소스 Fork인 OpenSearch**(최소 1.1.x, 최대 2.15.x)
- OpenJDK 17**



그레이로그 서버**는 **데비안 12**에서 실행되고 있지만, 도커를 포함한 다른 배포판에서도 설치가 가능합니다. 가상 머신에는 모든 구성 요소에 충분한 리소스를 제공하기 위해 **8GB RAM**과 **256GB 디스크 공간**이 장착되어 있습니다(그렇지 않으면 성능에 상당한 영향을 미칠 수 있음). 그러나 **그레이로그 아키텍처의 크기는 처리할 정보의 양에 따라 달라지기 때문에 대략적인 가이드로서 말씀드리는 것입니다. Graylog는 하루에 30MB 또는 300MB의 데이터를 처리할 수 있으며, 하루에 300GB의 데이터를 처리할 수도 있습니다. 테라바이트 단위의 로그**도 처리할 수 있는 **확장 가능한 솔루션**입니다([이 페이지](https://go2docs.graylog.org/current/planning_your_deployment/planning_your_deployment.html?tocpath=Plan%20Your%20Deployment%7C_____0) 참조).



![Image](assets/fr/032.webp)



출처: Graylog



구성을 시작하기 전에 그레이로그 머신에 고정 IP Address을 할당하고 최신 업데이트를 설치합니다. 로컬 컴퓨터의 표준 시간대를 설정하고 날짜 및 시간 동기화를 위한 NTP 서버를 정의해야 합니다. 실행할 명령은 다음과 같습니다:



```
sudo timedatectl set-timezone Europe/Paris
```



**참고: **그레이로그 데이터 노드**를 대신 사용하는 경우 OpenSearch 설치는 선택 사항입니다.



### III 그레이로그의 단계별 설치



패키지 캐시를 업데이트하고 앞으로의 작업에 필요한 도구를 설치하는 것부터 시작하겠습니다.



```
sudo apt-get update
sudo apt-get install curl lsb-release ca-certificates gnupg2 pwgen
```



![Image](assets/fr/030.webp)



#### A. 몽고DB 설치하기



이 작업이 완료되면 MongoDB 설치를 시작합니다. MongoDB 리포지토리에 해당하는 GPG 키를 다운로드합니다:



```
curl -fsSL https://www.mongodb.org/static/pgp/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
```



그런 다음 MongoDB 6 리포지토리를 Debian 12 머신에 추가합니다:



```
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg] http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
```



다음으로 패키지 캐시를 업데이트하고 MongoDB 설치를 시도해 보겠습니다:



```
sudo apt-get update
sudo apt-get install -y mongodb-org
```



종속성이 누락되어 MongoDB를 설치할 수 없습니다: **libssl1.1**. Debian 12에는 이 패키지가 리포지토리에 없기 때문에 계속 진행하려면 이 패키지를 수동으로 설치해야 합니다.



```
Les paquets suivants contiennent des dépendances non satisfaites :
mongodb-org-mongos: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
mongodb-org-server: Dépend: libssl1.1 (>= 1.1.1) mais il n'est pas installable
E: Impossible de corriger les problèmes, des paquets défectueux sont en mode « garder en l'état ».
```



Wget** 명령으로 "**libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb**"(최신 버전)라는 DEB 패키지를 다운로드한 다음 **dpkg** 명령으로 설치합니다. 그러면 다음 두 개의 명령이 생성됩니다:



```
wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2.23_amd64.deb
```



![Image](assets/fr/028.webp)



MongoDB 설치를 다시 시작합니다:



```
sudo apt-get install -y mongodb-org
```



그런 다음 MongoDB 서비스를 다시 시작하고 Debian 서버가 시작될 때 자동으로 시작되도록 설정합니다.



```
sudo systemctl daemon-reload
sudo systemctl enable mongod.service
sudo systemctl restart mongod.service
sudo systemctl --type=service --state=active | grep mongod
```



몽고DB가 설치되었으면 다음 구성 요소 설치로 넘어갈 수 있습니다.



#### B. OpenSearch 설치



서버에 OpenSearch를 설치하는 단계로 넘어가겠습니다. 다음 명령은 OpenSearch 패키지의 서명 키를 추가합니다:



```
curl -o- https://artifacts.opensearch.org/publickeys/opensearch.pgp | sudo gpg --dearmor --batch --yes -o /usr/share/keyrings/opensearch-keyring
```



그런 다음 OpenSearch 리포지토리를 추가하여 나중에 **apt**로 패키지를 다운로드할 수 있도록 합니다:



```
echo "deb [signed-by=/usr/share/keyrings/opensearch-keyring] https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main" | sudo tee /etc/apt/sources.list.d/opensearch-2.x.list
```



패키지 캐시를 업데이트하세요:



```
sudo apt-get update
```



그런 다음 인스턴스의 관리자** 계정의 기본 비밀번호를 **정의하는 데 주의하면서 OpenSearch를 **설치**합니다. 여기서 비밀번호는 "**IT-Connect2024!**"이지만, 이 값을 강력한 비밀번호로 바꾸세요. **"**P@ssword123**"과 같은 약한 비밀번호**는 피하고 각 유형(소문자, 대문자, 숫자, 특수 문자)을 하나 이상 포함한 **8자 이상**을 사용해야 하며, 그렇지 않으면 설치가 끝날 때 오류가 발생합니다. **오픈서치 2.12.**부터 필수 조건입니다



```
sudo env OPENSEARCH_INITIAL_ADMIN_PASSWORD=IT-Connect2024! apt-get install opensearch
```



설치하는 동안 잠시만 기다려주세요...



완료했으면 잠시 시간을 내어 최소한의 구성을 수행합니다. YAML 형식의 구성 파일을 엽니다:



```
sudo nano /etc/opensearch/opensearch.yml
```



파일이 열리면 다음 옵션을 설정합니다:



```
cluster.name: graylog
node.name: ${HOSTNAME}
path.data: /var/lib/opensearch
path.logs: /var/log/opensearch
discovery.type: single-node
network.host: 127.0.0.1
action.auto_create_index: false
plugins.security.disabled: true
```



이 OpenSearch 구성은 단일 노드를 설정하도록 설계되었습니다. 다음은 우리가 사용하는 다양한 매개변수에 대한 몇 가지 설명입니다:





- cluster.name: graylog: 이 매개변수는 OpenSearch 클러스터의 이름을 "**graylog**"로 지정합니다.
- node.name: **${HOSTNAME}**: 노드 이름은 로컬 Linux 머신의 이름과 일치하도록 동적으로 설정됩니다. 노드가 하나만 있더라도 이름을 올바르게 지정하는 것이 중요합니다.
- path.data: /var/lib/opensearch: 이 경로는 OpenSearch가 로컬 시스템에서 데이터를 저장하는 위치(이 경우 "**/var/lib/opensearch**"에)를 지정합니다.
- path.logs: /var/log/opensearch: 이 경로는 OpenSearch 로그 파일이 저장되는 위치(여기서는 "**/var/log/opensearch**"에)를 정의합니다.
- discovery.type: single-node: 이 매개변수는 단일 노드에서 작동하도록 OpenSearch를 구성하므로 "**단일 노드**" 옵션을 선택해야 합니다.
- network.host: 127.0.0.1: 이 구성은 OpenSearch가 Interface 로컬 루프에서만 수신 대기하도록 하며, 이는 Graylog와 동일한 서버에 있기 때문에 충분합니다.
- action.auto_create_index: false**: 자동 색인 생성을 비활성화하면 기존 색인 없이 문서를 전송할 때 OpenSearch가 자동으로 색인을 생성하지 않습니다.
- plugins.security.disabled: true**: 이 옵션은 OpenSearch 보안 플러그인을 비활성화하므로 인증, 액세스 관리 또는 통신 암호화를 사용하지 않습니다. 이 설정은 그레이로그를 설정할 때 시간을 절약할 수 있지만 프로덕션 환경에서는 사용하지 않는 것이 좋습니다([이 페이지](https://opensearch.org/docs/1.0/security-plugin/index/) 참조).



일부 옵션은 이미 존재하므로 '#'를 제거하여 활성화한 다음 값을 표시하기만 하면 됩니다. 옵션을 찾을 수 없는 경우 파일 끝에 직접 선언할 수 있습니다.



![Image](assets/fr/023.webp)



이 파일을 저장하고 닫습니다.



#### C. Java(JVM) 구성



이 서비스가 사용할 수 있는 메모리 양을 조정하려면 OpenSearch에서 사용하는 Java 가상 머신을 구성해야 합니다. 다음 구성 파일을 편집합니다:



```
sudo nano /etc/opensearch/jvm.options
```



여기에 배포된 구성을 사용하면 **OpenSearch는 4GB의 할당된 메모리로 시작하여 최대 4GB**까지 늘릴 수 있으므로 작동 중에 메모리 변동이 없습니다. 여기서 구성은 가상 머신에 총 **8GB RAM**이 있다는 사실을 고려합니다. 두 매개변수의 값은 모두 같아야 합니다. 즉, 회선을 교체해야 합니다:



```
-Xms1g
-Xmx1g
```



이 라인으로:



```
-Xms4g
-Xmx4g
```



다음은 수정할 이미지입니다:



![Image](assets/fr/022.webp)



이 파일을 저장한 후 닫습니다.



또한 Linux 커널에서 "**max_map_count**" 매개변수의 구성을 확인해야 합니다. 이 매개변수는 애플리케이션의 요구 사항을 충족하기 위해 프로세스당 매핑되는 메모리 영역의 한도를 정의합니다. **OpenSearch**는 **Elasticsearch**와 마찬가지로 메모리 관리 오류를 방지하기 위해 이 값을 "262144"로 설정할 것을 권장합니다.



원칙적으로 새로 설치한 Debian 12 머신에서는 이 값이 이미 올바릅니다. 하지만 확인해 봅시다. 다음 명령을 실행해 보세요:



```
cat /proc/sys/vm/max_map_count
```



"**262144**" 이외의 값이 나오면 다음 명령을 실행하고, 그렇지 않으면 실행할 필요가 없습니다.



```
sudo sysctl -w vm.max_map_count=262144
```



마지막으로 OpenSearch 자동 시작을 활성화하고 관련 서비스를 시작합니다.



```
sudo systemctl daemon-reload
sudo systemctl enable opensearch
sudo systemctl restart opensearch
```



시스템 상태를 표시하면 4GB RAM이 있는 Java 프로세스가 표시되어야 합니다.



```
top
```



![Image](assets/fr/029.webp)



다음 단계: 대망의 그레이로그 설치!



#### D. 그레이로그 설치



그레이로그 6.1**을 최신 버전으로 **설치하려면 다음 4가지 명령어를 실행하여 그레이로그 서버를 **다운로드 및 설치**하세요:



```
wget https://packages.graylog2.org/repo/packages/graylog-6.1-repository_latest.deb
sudo dpkg -i graylog-6.1-repository_latest.deb
sudo apt-get update
sudo apt-get install graylog-server
```



이 작업이 완료되면 그레이로그의 구성을 몇 가지 변경한 후 실행을 시도해야 합니다.



이 두 가지 옵션을 구성하는 것부터 시작하겠습니다:





- password_secret**: 이 매개변수는 그레이로그가 사용자 비밀번호의 저장을 보호하기 위해 사용하는 키를 정의하는 데 사용됩니다(솔팅 키의 개념으로). 이 키는 **유니크** 및 **랜덤**이어야 합니다.
- root_password_sha2**: 이 매개변수는 그레이로그의 기본 관리자 비밀번호에 해당합니다. Hash SHA-256으로 저장됩니다.



비밀번호_비밀** 매개변수에 대한 96자 키를 생성하는 것부터 시작하겠습니다:



```
pwgen -N 1 -s 96
wVSGYwOmwBIDmtQvGzSuBevWoXe0MWpNWCzhorBfvMMhia2zIjHguTbfl4uXZJdHOA0EEb1sOXJTZKINhIIBm3V57vwfQV59
```



반환된 값을 복사한 다음 그레이로그 구성 파일을 엽니다:



```
sudo nano /etc/graylog/server/server.conf
```



다음과 같이 **password_secret** 매개변수에 키를 붙여넣습니다:



![Image](assets/fr/027.webp)



파일을 저장하고 닫습니다.



다음으로 기본적으로 생성된 "**admin**" 계정의 비밀번호를 설정해야 합니다. 구성 파일에 비밀번호의 Hash를 저장해야 하며, 이는 비밀번호를 계산해야 함을 의미합니다. 아래 예시는 "**LogsWells@**" 비밀번호의 Hash를 보여줍니다. 이 값을 자신의 비밀번호에 맞게 조정하세요.



```
echo -n "PuitsDeLogs@" | shasum -a 256
6b297230efaa2905c9a746fb33a628f4d7aba4fa9d5c1b3daa6846c68e602d71
```



얻은 값을 출력으로 복사합니다(줄 끝에 하이픈을 생략).



그레이로그 구성 파일을 다시 엽니다:



```
sudo nano /etc/graylog/server/server.conf
```



Root_password_sha2** 옵션에 다음과 같이 값을 붙여넣습니다:



![Image](assets/fr/026.webp)



구성 파일에서 "**http_bind_address**" 옵션을 설정합니다. "**0.0.0.0:9000**"을 지정하여 모든 서버 IP Address을 통해 **9000** 포트에서 그레이로그의 Interface 웹에 액세스할 수 있도록 합니다.



![Image](assets/fr/024.webp)



그런 다음 "**elasticsearch_hosts**" 옵션을 `http://127.0.0.1:9200`로 설정하여 로컬 OpenSearch 인스턴스를 선언합니다. 그레이로그 데이터 노드**를 사용하지 않기 때문에 이 옵션은 필수입니다. 이 옵션이 없으면 더 이상 진행할 수 없습니다...



![Image](assets/fr/025.webp)



파일을 저장하고 닫습니다.



이 명령은 다음 부팅 시 자동으로 시작되도록 그레이로그를 활성화하고 그레이로그 서버를 즉시 실행합니다.



```
sudo systemctl enable --now graylog-server
```



이 작업이 완료되면 브라우저에서 그레이로그에 연결을 시도합니다. 서버의 IP Address(또는 이름)과 포트 9000을 입력합니다.



**참고로:**



얼마 전까지만 해도 그레이로그에 처음 로그인할 때 아래와 유사한 인증 창이 나타났습니다. 로그인 "**admin**"과 비밀번호를 입력해야 했습니다. 그리고 나서 연결이 되지 않는다는 사실에 불쾌하게 놀랐을 것입니다.



![Image](assets/fr/031.webp)



그레이로그 서버의 명령줄로 돌아가서 로그를 확인해야 했습니다. 그런 다음 **첫 번째 연결의 경우** 로그에 명시된 **임시 비밀번호를 사용해야 한다는 것을 확인할 수 있었습니다.



```
tail -f /var/log/graylog-server/server.log
```



![Image](assets/fr/021.webp)



그런 다음 "**admin**" 사용자 및 임시 비밀번호로 연결을 다시 시도해야 로그인이 가능했습니다!



**더 이상 그렇지 않습니다. 관리자 계정과 명령줄에 설정된 비밀번호로 로그인하기만 하면 됩니다**



![Image](assets/fr/033.webp)



**그레이로그의 Interface에 오신 것을 환영합니다!



![Image](assets/fr/019.webp)



#### E. 그레이로그: 새 관리자 계정 만들기



그레이로그에서 기본적으로 생성한 관리자 계정을 사용하는 대신 개인 관리자 계정을 직접 만들 수 있습니다. "**시스템**" 메뉴를 클릭한 다음 "**사용자 및 팀**"에서 "**사용자 만들기**" 버튼을 클릭합니다. 그런 다음 양식을 작성하고 계정에 관리자 역할을 할당합니다.



![Image](assets/fr/020.webp)



개인화된 계정에는 기본 관리자 계정과 달리 이름과 성, 이메일 Address 등의 추가 정보가 포함될 수 있습니다. 또한 각 사용자가 명명된 계정으로 작업할 때 더 나은 추적성을 보장합니다.



## Rsyslog를 사용하여 그레이로그로 로그 보내기



### I. 프레젠테이션



이 두 번째 파트에서는 로그를 그레이로그 서버로 전송하도록 Linux 시스템을 구성하는 방법을 알아보겠습니다. 이를 위해 시스템에 Rsyslog를 설치하고 구성합니다.



### II. Linux 로그를 수신하도록 그레이로그 구성하기



먼저 그레이로그를 구성하는 것부터 시작하겠습니다. 세 단계로 구성할 수 있습니다:





- 입력**을 생성하여 Linux 시스템이 UDP**를 통해 Syslog 로그를 **전송**할 수 있는 진입점을 만듭니다.
- 모든 Linux 로그를 저장하고 **색인**하기 위해 새 **색인**을 생성합니다.
- 그레이로그가 수신한 로그를 새 Linux 인덱스로 **라우팅**하기 위해 **스트림**을 생성합니다.



#### A. Syslog용 입력 만들기



그레이로그 Interface에 로그온하고 메뉴에서 "**시스템**"을 클릭한 다음 "**입력**"을 클릭합니다. 드롭다운 목록에서 "**Syslog UDP**"를 선택한 다음 "**새 입력 시작**"이라고 표시된 버튼을 클릭합니다. TCP 시스로그 입력을 만들 수도 있지만, 이 경우 보안을 위해 TLS 인증서를 사용해야 하지만 이 문서에서는 다루지 않습니다.



![Image](assets/fr/001.webp)



화면에 마법사가 나타납니다. 먼저 이 입력란에 이름을 지정하고(예: "**Graylog_UDP_Rsyslog_Linux**") 포트를 선택합니다. 기본적으로 포트는 "**514**"이지만 사용자 지정할 수 있습니다. 여기서는 "**12514**" 포트를 선택했습니다.



![Image](assets/fr/016.webp)



"**전체 메시지 저장**" 옵션을 체크하여 전체 로그 메시지를 그레이로그에 저장할 수도 있습니다. "**입력 시작**"을 클릭합니다.



![Image](assets/fr/017.webp)



새 입력이 생성되어 이제 활성화되었습니다. 이제 Graylog가 12514/UDP 포트에서 Syslog 로그를 수신할 수 있지만 아직 애플리케이션 구성을 완료하지 못했습니다.



![Image](assets/fr/018.webp)


**참고: ** 하나의 입력으로 여러 Linux 머신의 로그를 저장할 수 있습니다.



#### B. 새 Linux 인덱스 만들기



Linux 머신의 로그를 저장하기 위해 그레이로그에 인덱스를 만들어야 합니다. 그레이로그의 **인덱스**는 수신된 로그, 즉 수신된 메시지를 포함하는 저장 구조입니다. Graylog는 OpenSearch를 저장 엔진으로 사용하며, 빠르고 효율적인 검색을 위해 메시지가 색인화됩니다.



그레이로그의 메뉴에서 "**시스템**"을 클릭한 다음 "**인덱스**"를 클릭합니다. 새 페이지가 나타나면 "**색인 세트 만들기**"를 클릭합니다.



![Image](assets/fr/005.webp)



이 인덱스의 이름을 "**Linux 인덱스**"와 같이 지정하고 설명과 접두사를 추가한 다음 확인합니다. 여기서는 이 인덱스에 모든 Linux 로그를 **저장**합니다. 특정 로그만 저장하도록 특정 인덱스를 만들 수도 있습니다(예: [SSH] 로그만(https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/ "SSH"), 웹 서비스 로그 등).



![Image](assets/fr/006.webp)



이제 이 인덱스로 메시지를 라우팅하기 위해 새 스트림을 만들어야 합니다.



#### C. 스트림 만들기



새 스트림을 만들려면 그레이로그의 메인 메뉴에서 "**스트림**"을 클릭합니다. 그런 다음 오른쪽의 "**스트림 만들기**" 버튼을 클릭합니다. 표시되는 창에서 스트림의 이름을 "**리눅스 스트림**"으로 지정하고 "**인덱스 세트**"라는 필드에 "**리눅스 인덱스**"라는 인덱스를 선택합니다. 선택을 확인합니다.



**참고: "'기본 스트림'에서 일치하는 항목 제거" 옵션을 선택하지 않으면 이 스트림에 해당하는 메시지도 '기본 스트림'에 포함됩니다.**



![Image](assets/fr/002.webp)



그런 다음 Steam 설정에서 "**스트림 규칙 추가**" 버튼을 클릭하여 새 메시지 라우팅 규칙을 추가합니다. 이 창이 보이지 않으면 메뉴에서 "**스트림**"을 클릭한 다음 스트림에 해당하는 줄에서 "**더보기**"를 클릭한 다음 "**규칙 관리**"를 클릭합니다.



"**입력 일치**" 유형을 선택하고 이전에 생성한 **Rsyslog 입력을 UDP**에서 선택합니다. "**규칙 만들기**" 버튼으로 확인합니다. 이제 새 입력에 대한 모든 메시지가 Linux용 인덱스로 전송됩니다.



![Image](assets/fr/003.webp)



새 스트림이 목록에 표시되어야 하며 "**실행 중**" 상태여야 합니다. 메시지 대역폭은 "**0 msg/s**"로 표시되는데, 이는 현재 Rsyslog UDP 입력으로 로그를 전송하고 있지 않기 때문입니다. 스트림의 로그를 보려면 해당 스트림의 이름을 클릭하기만 하면 됩니다.



![Image](assets/fr/004.webp)



**그레이로그 측에서는 모든 것이 준비되었습니다**. 다음 단계는 Linux 머신을 구성하는 것입니다.



### III. Linux에 Rsyslog 설치 및 구성하기



로컬 또는 원격으로 Linux 시스템에 로그온하고 권한 상승 권한이 있는 사용자 계정을 사용합니다(sudo를 통해). 그렇지 않으면 'root' 계정을 직접 사용하세요.



#### A. Rsyslog 패키지 설치하기



먼저 패키지 캐시를 업데이트하고 "**rsyslog**"라는 이름의 패키지를 설치합니다.



```
sudo apt-get update
sudo apt-get install rsyslog
```



그런 다음 서비스 상태를 확인합니다. 대부분의 경우 이미 실행 중입니다.



```
sudo systemctl status rsyslog
```



#### B. Rsyslog 구성



Rsyslog의 기본 구성 파일은 여기에 있습니다:



```
/etc/rsyslog.conf
```



또한 "**/etc/rsyslog.d/**" 디렉토리는 Rsyslog에 대한 추가 구성 파일을 저장하는 데 사용됩니다. 기본 구성 파일에는 이 디렉터리에 있는 모든 "**.conf**" 파일을 가져오기 위한 Include 지시어가 있습니다. 이렇게 하면 기본 파일을 수정하지 않고도 Rsyslog를 구성하기 위한 추가 파일을 가질 수 있습니다.



이 디렉터리에서는 파일이 알파벳 순서로 로드되므로 숫자를 사용하여 로드 순서를 정의해야 합니다. 숫자 접두사를 추가하면 여러 구성 파일 간의 우선순위를 관리할 수 있습니다. 여기에는 추가 파일이 하나뿐이므로 문제가 되지 않습니다.



이 디렉토리에 "**10-graylog.conf**"라는 파일을 생성합니다:



```
sudo nano /etc/rsyslog.d/10-graylog.conf
```



이 파일에 이 줄을 삽입합니다:



```
*.* @192.168.10.220:12514;RSYSLOG_SyslogProtocol23Format
```



이 대사를 해석하는 방법은 다음과 같습니다:





- .*`: Linux 시스템에서 모든 Syslog 로그를 Graylog로 전송한다는 의미입니다.
- `@`: 전송이 UDP로 수행됨을 나타냅니다. TCP로 전환하려면 "**@@**"를 지정해야 합니다.
- 192.168.10.220:12514`: 그레이로그 서버의 Address과 로그가 전송되는 포트(입력에 해당)를 나타냅니다.
- rSYSLOG_SyslogProtocol23Format`: 그레이로그로 전송할 메시지의 형식에 해당합니다.



완료되면 파일을 저장하고 Rsyslog를 다시 시작합니다.



```
sudo systemctl restart rsyslog.service
```



이 작업을 수행하면 첫 번째 메시지가 그레이로그 서버에 도착해야 합니다!



### IV. 그레이로그에서 Linux 로그 표시



그레이로그에서 "**스트림**"을 클릭하고 새 스트림을 선택하면 관련 메시지를 볼 수 있습니다. 또는 "**검색**"을 클릭하고 Steam을 선택한 후 검색을 시작하세요.



다음은 Interface의 몇 가지 주요 기능입니다:



**1** - 메시지를 표시할 기간을 선택합니다. 기본적으로 최근 5분 동안의 메시지가 표시됩니다.



**2** - 표시할 스트림을 선택합니다.



**3** - 메시지 목록의 자동 새로고침(예: 5초마다)을 사용 설정합니다. 그렇지 않으면 정적이므로 수동으로 새로 고쳐야 합니다.



**4** - 기간, 스트림 또는 필터를 수정한 후 돋보기를 클릭하면 검색이 시작됩니다.



**5** - 검색 필터를 지정하는 입력창입니다. 여기서는 방금 Rsyslog를 설정한 새 머신의 로그만 표시하도록 "**source:srv\-docker**"를 지정합니다.



로그는 Linux 시스템에서 전송됩니다:



![Image](assets/fr/015.webp)



### V. SSH 연결 실패 확인



그레이로그의 강점은 로그를 색인하고 소스 머신, Timestamp, 메시지 콘텐츠 등 다양한 기준에 따라 검색을 수행할 수 있는 기능에 있습니다. 우리는 실패한 SSH 연결을 식별하고자 할 수 있습니다.



원격 컴퓨터(예: 그레이로그 서버)에서 방금 Rsyslog를 구성한 Linux 서버에 연결을 시도합니다. 예를 들어



```
ssh [email protected]
```



그런 다음 일부러 잘못된 **사용자 이름**과 **비밀번호**를 입력하여 **generate 연결 오류**를 발생시킵니다. "**/var/log/auth.log**" 파일에 다음과 유사한 메시지를 generate로 기록합니다:



```
Failed password for invalid user it-connect from 192.168.10.199 port 50352 ssh2
```



이러한 메시지는 그레이로그에서 찾을 수 있습니다.



그레이로그에서 다음 검색 필터를 사용하여 일치하는 메시지만 표시합니다:



```
message:Failed password AND application_name:sshd
```



서버가 여러 대이고 특정 서버의 로그를 분석하려는 경우 해당 서버의 이름을 추가로 지정하세요:



```
message:Failed password AND application_name:sshd AND source:srv\-docker
```



다음은 하루 중 여러 시간대에 걸쳐 여러 연결 오류가 발생한 컴퓨터의 결과 개요입니다:



![Image](assets/fr/009.webp)



IP Address "**192.168.10.199**"의 컴퓨터에서 연결 시도가 실패했습니다. 이 호스트의 활동에 대해 더 자세히 알고 싶으시면 **이 IP Address**를 검색하세요. 그레이로그는 로그 전송이 구성된 모든 호스트에서 이 IP Address가 참조된 모든 로그를 출력합니다(로그 전송이 구성된 경우).



이 경우 사용할 필터는 다음과 같을 수 있습니다:



```
message:"192.168.10.199"
```



추가 결과를 얻을 수 있습니다(SSH 애플리케이션에서 필터링하지 않으므로 당연한 결과입니다):



![Image](assets/fr/008.webp)



### VI. 결론



이 튜토리얼을 따라하면 로그를 그레이로그 서버로 보내도록 Linux 시스템을 구성할 수 있습니다. 이렇게 하면 로그 싱크에서 Linux 호스트의 로그를 중앙 집중화할 수 있습니다!



더 나아가 이상 징후가 감지되면 알림을 받을 수 있는 대시보드와 알림을 만드는 것도 고려해 보세요.



![Image](assets/fr/007.webp)