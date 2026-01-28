---
name: BitBox02

description: BitBox02 설정 및 사용
---

![cover](assets/cover.webp)


비트박스02(https://bitbox.swiss/)는 비트코인을 안전하게 보호하기 위해 특별히 설계된 스위스산 물리적 Wallet입니다. 주요 기능으로는 마이크로SD 카드를 사용한 간편한 백업 및 복원, 미니멀하고 눈에 잘 띄지 않는 디자인, Bitcoin에 대한 포괄적인 지원 등이 있습니다.


![device](assets/1.webp)


전문가들이 설계한 최첨단 보안 기능을 제공하며, 보안 칩이 포함된 듀얼 칩 설계가 특징입니다. 소스 코드는 보안 연구원의 철저한 감사를 거쳤으며 완전히 오픈 소스입니다. 비트박스02는 간단하면서도 강력한 비트박스앱과 함께 제공되어 비트코인을 안전하게 관리할 수 있습니다. 이 앱은 Bitcoin용 Full node를 지원하며 앱과 장치 간의 종단 간 암호화 통신을 보장합니다. 스위스에서 제조된 BitBox02는 사용자들 사이에서 긍정적인 평판을 얻고 있습니다.


![video](https://youtu.be/sB4b2PbYaj0)


Wallet 사양은 다음과 같습니다:



- 연결성: USB-C
- 호환성: 호환성: Windows 7 이상, macOS 10.13 이상, Linux, Android
- 입력: 정전식 터치 센서
- 마이크로컨트롤러: ATSAMD51J20A; 120Mhz 32비트 Cortex-M4F; 진정한 난수 생성기
- 보안 칩: ATECC608B; 진정한 난수 생성기(NIST SP 800-90A/B/C)
- 디스플레이: 128 x 64 픽셀 흰색 OLED
- 재질: 폴리카보네이트
- 크기: 54.5 x 25.4 x 9.6mm(USB-C 플러그 포함)
- 무게: 기기 12g, 포장 및 액세서리 포함 160g


웹 사이트 https://bitbox.swiss/bitbox02/ 에서 데이터 시트 다운로드


## BitBox02 Hardware Wallet 사용 방법


### BitBox02 설정


BitBox02는 쉘에 USB-C 연결부가 부착되어 있습니다. 컴퓨터가 일반 USB 포트를 사용하는 경우 장치와 함께 제공되는 어댑터를 사용해야 합니다.


컴퓨터에 연결하면 기기의 전원이 켜집니다(아직 켜지지 않은 상태).


위와 아래에 센서가 있어 위나 아래를 터치하면 화면 방향을 원하는 대로 조정할 수 있습니다.


![image](assets/2.webp)


### BitBox02 앱 다운로드


Https://shiftcrypto.ch/ 을 방문하여 상단의 '앱' 링크를 클릭하면 다운로드 페이지로 이동합니다:


![image](assets/3.webp)


파란색 다운로드 버튼을 클릭합니다:


![image](assets/4.webp)


다운로드를 확인하려면(복잡성이 추가되지만 특히 Bitcoin를 많이 저장하는 경우 권장됨) 부록 A를 참조하세요.


다운로드가 완료되면 파일의 압축을 풀 수 있습니다. Mac에서는 다운로드한 파일을 더블클릭하면 다운로드 디렉터리에 BitBox 앱 아이콘이 나타납니다. 데스크톱 또는 원하는 위치로 끌어다 놓으면 쉽게 액세스할 수 있습니다.


앱을 두 번 클릭하여 실행합니다('설치'가 되지 않음).


Mac에서는 컴퓨터 보모가 경고를 표시합니다. 그냥 무시하고 '열기'를 클릭하세요:


![image](assets/5.webp)


그러면 다음과 같은 내용이 표시됩니다:


![image](assets/6.webp)


계속해서 장치를 컴퓨터에 연결합니다.


페어링 코드가 표시됩니다. 일치하는지 확인한 다음 센서를 터치하여 확인 표시를 선택합니다. 그런 다음 화면으로 돌아오면 계속 버튼을 사용할 수 있습니다.


![image](assets/7.webp)


그런 다음 새 seed를 만들거나 seed를 복원할 수 있는 옵션이 제공됩니다. 새 seed를 만드는 방법을 보여드리겠습니다(Wallet에 Bitcoin을 로드하기 전에 백업 품질을 테스트하기 위해 생성한 seed도 복원하는 것이 중요합니다).


![image](assets/8.webp)


장치에 microSD 카드가 함께 제공됩니다. 아직 삽입하지 않았다면 삽입하세요.


![image](assets/9.webp)


디바이스 이름을 지정하고 계속을 클릭한 다음 디바이스에서 확인합니다.


![image](assets/10.webp)


그러면 디바이스의 비밀번호를 설정하라는 메시지가 표시됩니다. 이것은 seed의 일부가 아닙니다. passphrase도 seed의 일부가 아닙니다. 단순히 장치를 잠그기 위한 비밀번호입니다. 디바이스의 전원을 켜면 매번 이 비밀번호를 입력하라는 메시지가 표시됩니다. 10번 연속 실패하면 디바이스의 모든 메모리가 지워지므로 주의해야 합니다. 화면의 애니메이션이 디바이스 컨트롤을 사용하여 비밀번호를 설정하는 방법을 알려줍니다.


![image](assets/11.webp)


다음 화면을 읽고 각 상자를 선택한 다음 계속 진행합니다.


![image](assets/12.webp)

![image](assets/13.webp)

![image](assets/14.webp)


Wallet를 사용할 준비가 완료되면 이렇게 생겼습니다.


![image](assets/15.webp)


### 너무 빠르지 않아요!!


이상하게도 BitBox02는 장치를 사용할 준비가 되었다고 알려주지만 seed 단어를 적으라는 메시지는 표시되지 않습니다! 우리가 가진 유일한 백업은 마이크로SD 카드에 저장된 파일입니다. 이것은 부적절합니다. 이러한 저장 장치는 "비트 썩음"으로 인해 영원히 지속되지 않습니다. 종이 백업과 복사본을 금고에 보관해야 합니다(일반적인 하드웨어 지갑 사용 방법 가이드에 설명된 대로)


seed 문구를 가져와서 적어두려면 왼쪽의 '장치 관리' 탭으로 이동한 다음 '복구 단어 표시'를 클릭합니다


![image](assets/16.webp)


그런 다음 확인을 거치면 기기가 단어를 표시합니다. 깔끔하게 적고 다른 사람이 볼 수 없도록 하세요.


![image](assets/17.webp)


그런 다음 왼쪽의 Bitcoin 탭을 클릭하여 수신 주소를 가져올 수 있습니다.


![image](assets/18.webp)


한 번에 하나씩 표시되지만 적어도 처음 20개 중에서 사용할 Address을 선택할 수 있습니다:


![image](assets/19.webp)


파란색 버튼을 클릭하면 전체 Address이 표시되며, Address이 화면의 디스플레이와 일치하는지 확인하라는 메시지가 표시됩니다. 이렇게 하면 컴퓨터의 멀웨어가 사용자를 속여 Bitcoin을 공격자의 Address로 전송하지 않는지 확인하는 데 유용합니다.


![image](assets/20.webp)


Bitcoin을 이 Wallet로 보내려면 Address을 복사하여 코인이 있는 Exchange의 출금 페이지에 붙여넣으면 됩니다. 먼저 소량의 테스트 금액을 송금한 다음 Exchange로 다시 보내거나 Wallet의 두 번째 Address으로 보내는 연습을 하는 것이 좋습니다.


더 많은 양을 사용하려면 passphrase을 만드는 것이 좋습니다(아래 참조). 원래 Wallet(passphrase 없음)를 미끼 Wallet로 사용할 수 있습니다(믿을 만한 미끼가 되려면 적당한 양이 들어 있어야 합니다).


### 노드에 연결


BitBox02가 자동으로 노드에 연결됩니다. 어디에 연결되는지 살펴봅시다. 왼쪽의 설정 탭을 클릭한 다음 "나만의 Full node 연결"을 클릭합니다.


![image](assets/21.webp)


여기에서 shiftcrypto의 노드에 연결되는 것을 볼 수 있습니다. 좋지 않습니다. 저희는 Bitcoin 주소와 IP Address을 모두 그들에게 넘겼습니다(물론 seed은 아닙니다. 그들은 저희 주소/잔액을 볼 수 있지만 사용할 수는 없습니다). 이 페이지에서 직접 노드 세부 정보를 입력하거나(이 특정 가이드의 범위를 벗어남), Sparrow Bitcoin Wallet, Electrum Desktop Wallet 또는 Specter Desktop과 같은 더 나은 소프트웨어를 사용할 수 있습니다. 이 가이드의 뒷부분에서 Sparrow Bitcoin Wallet를 시연해 보겠습니다.


![image](assets/22.webp)


passphrase 추가


이제 BitBox02 앱으로 장치를 설정했으므로(그리고 이 특정 Hardware Wallet에서는 불가피하게 주소를 공개했으므로), seed 문구에 passphrase을 추가할 수 있습니다. 이렇게 하면 동일한 seed를 사용하여 새로운 Wallet를 생성할 수 있으며, 시프트크립토는 새 주소를 절대 볼 수 없습니다. 이 Wallet는 자체 소프트웨어에만 연결할 것입니다.


### passphrase 활성화


이제 passphrase 기능을 '활성화'하세요(아직 passphrase을 설정하지 않은 상태입니다). '장치 관리' 탭으로 이동하여 'passphrase 활성화'(아래 빨간색 원)를 클릭합니다.


![image](assets/23.webp)


단계를 읽어보세요..


![image](assets/24.webp)

![image](assets/25.webp)

![image](assets/26.webp)


이제 장치 연결을 끊고 BitBox02 앱을 종료합니다


파먼의 비트박스02 섹션 끝.


이제 스펙터, Sparrow, 비트박스 Interface 등 모든 데스크톱 솔루션에서 사용할 수 있는 디바이스가 완벽하게 작동합니다.