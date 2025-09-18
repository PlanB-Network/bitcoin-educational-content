---
name: Electrum OP_RETURN
description: 일렉트럼으로 Blockchain Bitcoin에 메시지 등록하기
---

![cover](assets/cover.webp)




이 단계별 튜토리얼에서는 Wallet 일렉트럼을 사용하여 Blockchain Bitcoin에 메시지를 작성하는 방법을 보여드립니다. 이 작업은 OP_RETURN 인스트럭션을 사용하여 트랜잭션에 텍스트를 삽입하여 Blockchain에서 공개적으로 볼 수 있도록 합니다. 성공적인 등록을 위해 다음의 간단한 단계를 따르세요.



---
## 전제 조건





- 컴퓨터(Windows, macOS 또는 Linux).
- 인터넷 연결.
- 거래 금액과 수수료를 충당하기 위해 Wallet에 사토시(Sats) 또는 비트코인(BTC) 몇 개를 넣으세요.
- 텍스트-헥스 변환기(예: 온라인 사이트) 또는 [이 OP_RETURN 스크립트 생성기](https://resources.davidcoen.it/opreturnelectrum/)와 같은 전용 도구.



---

## 1단계: Electrum 다운로드 및 설치



![image](assets/fr/01.webp)



1. 일렉트럼 공식 웹사이트를 방문하세요: [electrum.org](https://electrum.org/).


2. 사용 중인 운영 체제(Windows, macOS, Linux)에 해당하는 버전을 다운로드하세요.


3. 설치 관리자의 지침에 따라 Electrum을 설치합니다.


4. 파일의 서명 또는 Hash을 비교하여 다운로드한 파일의 무결성을 확인합니다(선택 사항이지만 보안상의 이유로 권장됨).



→ 일렉트럼 튜토리얼에 대한 자세한 내용 :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 2단계: Wallet 생성 또는 가져오기



1. 일렉트럼을 시작합니다.


2. 새 Wallet 만들기를 선택하거나 이미 seed 문구(복구 문구)가 있는 경우 기존 Wallet 복원을 선택합니다.


3. 지침에 따라 Wallet를 구성하세요:




 - 새 Wallet의 경우 seed 문장을 메모하여 안전한 장소(종이, 금고 등)에 보관하세요.
 - 기존 Wallet의 경우 seed 문구를 입력하여 복원합니다.


4. Wallet의 보안을 위해 비밀번호를 설정하세요.



→ 일렉트럼 튜토리얼에 대한 자세한 내용 :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 3단계: 사용 가능한 자금 확인



Wallet에 충분한 비트코인(BTC) 또는 사토시(Sats)가 포함되어 있는지 확인하십시오:




- 거래 금액(예: 0.00001 BTC 또는 1000 Sats).
- 거래 수수료는 네트워크 규모에 따라 달라집니다(일반적으로 수천 Sats).



잔액을 확인하려면 일렉트럼의 잔액을 참조하세요.



![image](assets/fr/02.webp)



필요한 경우 BTC 또는 Sats를 전송하여 Wallet에 공급합니다. 이렇게 하려면 '수신' 탭으로 이동하여 '요청 생성'을 클릭합니다:



![image](assets/fr/03.webp)



그러면 수신 Address이 표시됩니다:



![image](assets/fr/04.webp)



→ 일렉트럼 튜토리얼에 대한 자세한 내용 :



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 4단계: 새길 메시지 준비하기



입력할 메시지를 선택합니다(예: `Thanks Satoshi`). 참고: OP_RETURN 메시지는 80바이트, 즉 약 80개의 ASCII 문자로 제한됩니다.



*잠시 생각해 보세요: Blockchain Bitcoin에 쓴 글은 누구나 영구적으로 액세스할 수 있으므로 :*




- 우리 인간성의 아름다운 표현을 남깁니다,
- 후회할 만한 콘텐츠를 입력하지 마세요



*Blockchain 공간과 비트코인은 소중합니다, 현명하고 계획적으로 사용하세요*



메시지를 16진수로 변환합니다:




- 온라인 도구](https://www.rapidtables.com/convert/number/ascii-to-hex.html)를 사용할 수 있지만, 여기서 민감한 데이터를 처리하지 않도록 주의하세요(원칙적으로 Blockchain Bitcoin를 통해 OP_RETURN에 게시하려는 정보는 기밀성 문제가 발생하지 않습니다);
- 기밀성을 높이려면 작은 Python 을 사용하여 로컬에서 변환을 수행하세요:



```py
#!/usr/bin/env python3

def main():
ascii_text = input("Enter ASCII text: ")
try:
hex_output = ascii_text.encode('ascii').hex()
print(hex_output)
except UnicodeEncodeError:
print("Error: Input contains non-ASCII characters.", file=sys.stderr)

if __name__ == "__main__":
import sys
main()
```



예: `Thanks Satoshi`는 16진수로 `5468616e6b73205361746f736869`가 됩니다.



트랜잭션 스크립트를 준비합니다. 다음은 예상 형식의 예시입니다:



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



로 구성되어 있습니다:





- 목적지 Address**: 유효한 Bitcoin Address. Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`. 이체된 자금을 본인에게 돌려받고자 하는 경우 본인의 Address일 수 있습니다;
- 전송된 금액**: 트랜잭션 금액, 여기서는 `0.00001` BTC입니다. **참고**: 일렉트럼에서 사용하는 단위는 BTC이므로 트랜잭션 스크립트에 표시되는 금액도 Sats이 아닌 BTC로 표시해야 합니다;
- 스크립트 **OP_RETURN**: 스크립트(`OP_RETURN <메시지>), 0`이 앞에 오는 16진수로 변환된 메시지입니다. 여기서는 16진수 메시지의 경우 `5468616e6b73205361746f736869`입니다.



⚠️ **주의**: 이 옵코드는 스크립트를 유효하지 않은 것으로 표시하여 출력을 영구적으로 사용할 수 없게 만들므로 OP_RETURN 뒤에 '0'을 표시하는 것이 매우 중요합니다. 네트워크 노드는 UTXO 세트에서 이 출력을 삭제합니다. 0`이 아닌 다른 값을 입력하면 복구할 수 없게 손실되며, 비트코인은 소각된 것으로 간주됩니다. 따라서 원하는 데이터를 기록하려면 항상 OP_RETURN에 `0`을 입력해야 하지만, 자금을 연결하지 않으면 손실될 수 있습니다.



팁: [OP_RETURN 생성기] 도구(https://resources.davidcoen.it/opreturnelectrum/)를 사용하여 스크립트를 자동으로 generate으로 생성하세요. 이 도구에서 BTC로 금액을 입력하라는 메시지가 표시되더라도 단위는 Electrum에서 구성한 것을 유지하세요.



![image](assets/fr/05.webp)



Electrum에서 사용하는 단위를 변경하려면 메뉴 표시줄에서 "기본 설정"을 찾은 다음 "단위" 탭에서 BTC / mBTC / 비트 또는 Sats 를 선택합니다:



![image](assets/fr/06.webp)




---

## 5단계: 트랜잭션 보내기



Electrum에서 보내기 탭으로 이동합니다.



![image](assets/fr/07.webp)



'지급 대상' 필드에 준비된 스크립트(예: 위 스크립트)를 붙여넣습니다.



![image](assets/fr/08.webp)



'수취인' 필드는 Green에 표시되어야 하며, 거래 금액은 아래 줄에 표시되어야 합니다.



금액 필드에서 금액과 단위를 확인합니다.



"결제..."를 클릭하고 지불하고자 하는 금액과 Miner이 거래를 처리하고 블록에 통합할 속도에 따라 거래 수수료를 조정하세요.



![image](assets/fr/09.webp)



확인을 클릭하고 비밀번호로 거래를 확인합니다. 확인 창이 나타납니다.




---

## 6단계: 등록 확인



거래가 확인되면(몇 분 정도 소요될 수 있음) '내역' 탭으로 이동합니다.



![image](assets/fr/10.webp)



거래를 마우스 오른쪽 버튼으로 클릭하고 '탐색기에서 보기'를 선택하면 세부 정보를 확인할 수 있습니다.



또는 대상 Address(예: `bc1q879cv4p5q6s9537orange3zss33d3turzad8`)을 복사하여 [Mempool.space](https://Mempool.space/) 또는 [blockstream.info](https://blockstream.info/) 등의 Blockchain 탐색기에서 확인합니다.



거래 세부 정보에서 OP_RETURN 필드를 찾아 메시지를 확인합니다.



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## 팁 및 모범 사례





- 소량으로 테스트합니다: 비용이 많이 드는 오류를 피하려면 소액의 거래(예: Sats 1000)로 시작하세요.
- OP_RETURN가 포함된 출력이 0과 같아야 하며, 그렇지 않으면 비트코인이 영구적으로 손실됩니다.
- 단위를 확인합니다: 입력한 금액이 일렉트럼에 표시된 단위(BTC, mBTC 또는 Sats)와 일치하는지 확인합니다.
- 거래 수수료: 네트워크가 혼잡한 경우 더 빠른 확인을 위해 수수료를 인상합니다.
- 짧은 메시지: OP_RETURN 항목은 80바이트로 제한됩니다. 이에 맞게 메시지를 계획하세요.



---

## 유용한 리소스





- 일렉트럼 다운로드: [electrum.org](https://electrum.org/)
- OP_RETURN 스크립트 생성기: [resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain 탐험가: [Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)