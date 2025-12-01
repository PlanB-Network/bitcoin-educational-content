---
name: Timestamp의 Plan ₿ Academy 디플로마
description: Plan ₿ Network가 인증서 및 졸업장에 대한 검증 가능한 증명을 발급하는 방법 이해하기
---

![cover](assets/cover.webp)


이 글을 읽고 계신다면 planb.network에서 수강한 과정 중 하나에 대해 ₿-CERT 시험 인증서 또는 수료증을 받으셨을 가능성이 높으므로 이 성과를 축하드립니다!


이 튜토리얼에서는 Plan ₿ Network에서 ₿-CERT 시험 인증서 또는 과정 완료에 관한 졸업장에 대한 검증 가능한 증명을 발급하는 방법을 알아보세요. 그런 다음 두 번째 부분에서는 이러한 증명의 진위 여부를 확인하는 방법을 설명합니다.


# Plan ₿ Academy 증명 메커니즘


Plan ₿ Network에서는 두 가지 암호화 연산에 의존하는 증명 메커니즘을 통해 타임체인(즉, Bitcoin Blockchain)을 사용하여 인증서와 졸업장에 암호화 서명하고 타임스탬프를 찍습니다:


1. 업적을 합성하는 텍스트 파일의 GPG 서명

2. 오픈타임스탬프](https://opentimestamps.org/)를 통해 동일한 서명된 파일의 타임스탬핑.


첫 번째 작업을 통해 인증서(또는 졸업장)의 발급자를 확인할 수 있으며, 두 번째 작업을 통해 발급 날짜를 확인할 수 있습니다.

이러한 간단한 증명 메커니즘을 통해 누구나 독립적으로 검증할 수 있는 부인할 수 없는 증거가 있는 인증서와 졸업장을 발급할 수 있다고 믿습니다.


![image](./assets/proof-mechanism.webp)


이 증명 메커니즘 덕분에 인증서 또는 졸업장의 아주 작은 세부 사항이라도 변경하려고 시도하면 서명된 파일의 SHA-256 Hash이 완전히 달라지고 서명과 Timestamp 모두 더 이상 유효하지 않으므로 변조가 즉시 드러나게 됩니다. 또한 누군가 Plan ₿ Network을 대신하여 인증서 또는 졸업장을 악의적으로 위조하려고 시도하는 경우 서명을 간단히 확인하는 것만으로도 사기가 드러날 수 있습니다.


## GPG 서명은 어떻게 작동하나요?


GPG 서명은 GNU Privacy Guard라는 오픈 소스 소프트웨어를 사용하여 생성됩니다. 이 소프트웨어를 사용하면 개인 키를 쉽게 생성하고, 서명을 서명 및 확인하고, 파일을 암호화 및 해독할 수 있습니다. 이 튜토리얼의 목적상, Plan ₿ Network은 개인/공개 키를 만들고 모든 ₿-CERT 인증서 및 과정 수료증에 서명하는 데 GPG를 사용한다는 점에 유의하는 것이 중요합니다.


반면에 서명된 파일의 진위 여부를 확인하려는 사람은 GPG를 사용하여 발급자의 공개키를 가져와서 확인할 수 있습니다.


이 멋진 소프트웨어에 대해 더 자세히 알고 싶으시다면 ["GNU 개인정보 보호 핸드북"](https://www.gnupg.org/gph/en/manual/x135.html)을 참조하세요


## 타임스탬프는 어떻게 작동하나요?


오픈타임스탬프를 사용하면 누구나 파일을 Timestamp로 생성하고 파일의 존재에 대한 검증 가능한 증거를 얻을 수 있습니다. 즉, 파일이 언제 생성되었는지에 대한 증거를 제공하는 것이 아니라 파일이 특정 시점 이전에 존재했다는 증거를 제공합니다.

오픈타임스탬프는 Bitcoin Blockchain에 증명을 저장하는 매우 효율적인 방법을 활용하여 이 서비스를 무료로 제공합니다. 이 서비스는 SHA-256 Hash 알고리즘을 사용하여 파일의 고유 식별자를 생성하고 다른 사용자가 제출한 파일의 해시를 사용하여 Merkle Tree을 구성합니다. Merkle Tree 구조의 Hash만 OP_RETURN 트랜잭션에 고정되어 파일 존재를 확인하는 안전하고 간결한 방법을 보장합니다.

이 트랜잭션이 블록에 들어가면, 초기 파일과 연결된 '.ots' 파일을 가진 사람은 누구나 타임스탬프의 진위 여부를 확인할 수 있습니다. 튜토리얼의 두 번째 부분에서는 임시 파일과 OpenTimestamps 웹사이트의 그래픽 Interface을 통해 Bitcoin 인증서 또는 과정 수료증을 확인하는 방법을 살펴보겠습니다.


# Plan ₿ Academy ₿-CERT 인증서 또는 디플로마 확인 방법


## 1단계. 인증서 또는 졸업장 다운로드


Planb.network에서 개인/학생 대시보드에 로그인합니다.


![image](./assets/login.webp)


왼쪽 메뉴를 클릭하여 '자격 증명'으로 이동하고 시험 세션 또는 디플로마를 선택합니다.


![image](./assets/credential.webp)


Zip 파일을 다운로드합니다.


![image](./assets/download.webp)


.zip` 파일을 마우스 오른쪽 버튼으로 클릭하고 "압축 풀기"를 선택하여 내용을 압축 해제합니다. 세 개의 다른 파일이 표시됩니다:



- 서명된 텍스트 파일(예: 인증서.txt)
- 개방형 Timestamp(OTS) 파일(예: certificate.txt.ots)
- PDF 인증서(예: certificate.pdf)


## 2단계: 텍스트 파일의 서명을 어떻게 확인할 수 있나요?


먼저 파일을 추출한 폴더로 이동하여 터미널을 엽니다(폴더 창을 마우스 오른쪽 버튼으로 클릭하고 '터미널에서 열기'를 클릭합니다). 그런 다음 아래 지침을 따르세요.


1. 다음 명령을 사용하여 Plan ₿ Academy 공개 PGP 키를 가져옵니다:


```bash
curl -s https://raw.githubusercontent.com/Asi0Flammeus/pgp-public-keys/master/Plan ₿ Academy-pk.asc | gpg --import
```


PGP 키를 성공적으로 가져왔다면 다음과 같은 메시지가 표시되어야 합니다


```
gpg: key 8F12D0C63B1A606E: public key "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```


참고: 1개의 키가 처리되고 0개의 키를 가져온 것으로 표시되면 이전에 이미 동일한 키를 가져온 것일 수 있으며, 이는 완전히 정상입니다.


2. 다음 명령을 사용하여 인증서 또는 졸업장의 서명을 확인합니다:


```bash
gpg --verify certificate.txt
```


이 명령은 다음을 포함하여 서명에 대한 세부 정보를 표시합니다:



- 서명자(Plan ₿ Academy)
- 서명된 시기
- 서명이 유효한지 여부


다음은 결과의 예입니다:


```
gpg: Signature made lun 11 nov 2024, 00:39:04 CET
gpg:                using RSA key 5720CD577E7894C98DBD580E8F12D0C63B1A606E
gpg:                issuer "admin@planb.network"
gpg: Good signature from "Plan ₿ Academy (used for Plan ₿ Academy platform) <admin@planb.network>" [unknown]
```


'잘못된 서명'과 같은 메시지가 표시되면 파일이 변조되었다는 뜻입니다.


## 3단계: 개방형 Timestamp 확인


### 그래픽 Interface를 통한 확인


1. 오픈타임스탬프 웹사이트 방문: https://opentimestamps.org/

2. '스탬프 및 확인' 탭을 클릭합니다.

3. OTS 파일(예: `certificate.txt.ots`)을 지정된 영역으로 끌어다 놓습니다.

4. 타임스탬프가 있는 파일(예: `인증서.txt`)을 지정된 영역으로 끌어다 놓습니다.

5. 웹사이트가 자동으로 열려 있는 Timestamp을 확인하고 결과를 표시합니다.


다음과 같은 메시지가 표시되면 Timestamp이 유효한 것입니다:


![cover](assets/opentimestamp_wegui_verified.webp)


### CLI 방법


참고: 이 절차를 수행하려면 **실행 중인 로컬 Bitcoin 노드가 필요합니다**


1. 다음 명령을 실행하여 공식 [저장소](https://github.com/opentimestamps/opentimestamps-client)에서 OpenTimestamps 클라이언트를 설치합니다:


```
pip install opentimestamps-client
```


2. 추출한 인증서 파일이 들어 있는 디렉토리로 이동합니다.


3. 다음 명령을 실행하여 열린 Timestamp을 확인합니다:


```
ots verify certificate.txt.ots
```


이 명령은



- Timestamp를 Bitcoin의 Blockchain과 비교하여 확인하십시오
- 파일에 타임스탬프가 찍힌 정확한 시간 표시
- Timestamp의 진품 여부 확인


### 최종 결과


다음 메시지가 **둘 다** 표시되면 인증이 성공한 것입니다:


1. GPG 서명은 **"Plan ₿ Network의 양호한 서명"**으로 보고됩니다

2. 오픈타임스탬프 검증은 특정 Bitcoin 블록 Timestamp을 표시하고 **"성공!"을 보고합니다 Bitcoin 블록 [블록 높이]는 [Timestamp] 기준으로 데이터가 존재했음을 증명합니다."** **


이제 Plan ₿ Network이 모든 ₿-CERT 인증서 및 디플로마에 대해 검증 가능한 증명을 발급하는 방법을 알았으니, 그 무결성을 쉽게 확인할 수 있습니다.