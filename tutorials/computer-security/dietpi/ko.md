---
name: DietPi
description: 저성능 머신에 최적화된 경량 운영 체제. 셀프 호스팅을 선호하는 경우
---

![cover](assets/cover.webp)



기술 분야가 아닌 사람들에게는 '오드로이드', '라즈베리 파이', '오렌지 파이' 또는 '라드사'와 같은 브랜드는 거의 알려져 있지 않습니다. 하지만 기술 업계만 살펴봐도 일반적으로 사용되는 컴퓨터에 비해 크기가 매우 작은 단일 마더보드에 구축된 **SBC** 컴퓨터가 개인 프로젝트를 지원하는 데 없어서는 안 될 필수품이라는 것을 알 수 있습니다.



이러한 컴퓨터는 다양한 모델로 생산됩니다. 이러한 저성능 컴퓨터에서 원활하게 실행되도록 조정된 Linux 배포판을 호스팅하는 것이 좋습니다.



**다이어트파이도 예외는 아닙니다**: 데비안 기반 운영체제로, 가능한 한 가볍고 성능이 가장 낮은 'SBC'도 매우 빠르게 만들도록 최적화되어 있습니다. 이 튜토리얼이 작성되는 시점에 데비안12 북웜에서 데비안13 트릭시로 전환되었으며, 이제 오픈 소스 `RISC-V` 프로세서 기반 SBC도 지원합니다. DietPi는 더 연구할 가치가 있는 즐거운 발견입니다.



## 강점



이것은 소형 라즈베리형 보드용 데비안의 "일반적인 복제본"이 아닙니다. 다이어트파이가 그렇습니다:




- 속도와 가벼움에 최적화**: [다른 SBC용 데비안 배포판과 비교](https://dietpi.com/blog/?p=888), DietPi는 모든 면에서 더 가볍습니다. DietPi ISO 이미지의 무게는 1GB 미만으로, 구형 Raspberry 또는 Orange PI 전용 이미지 중 가장 작습니다(예를 들어). RAM 및 CPU 리소스에 대한 요구가 매우 낮기 때문에 구형 보드에서도 항상 최상의 성능을 발휘합니다.
- 기본 제공 자동화 및 설치 프로그램**: 전용 명령 모음은 사용자가 시스템 리소스를 모니터링하고 프로그램 설치 및 실행, 버전 업데이트, 백업, 모든 로그 확인 등의 작업을 자동화하는 데 도움이 됩니다.
- 강력한 실험 지향 커뮤니티**: 다이어트파이 커뮤니티의 [튜토리얼](https://dietpi.com/forum/c/community-tutorials/8) 및 프로젝트는 클릭 한 번으로 설치할 수 있는 소프트웨어에서 영감을 얻기에 이상적입니다.



**SBC를 최대한 활용하기가 그 어느 때보다 쉬워졌습니다**.



## 셀프 호스팅을 위한 자동화


고급 네트워킹 솔루션을 실행하기 위해 자체 서버를 실험하거나 Bitcoin 전문성을 발전시키기 위한 도구를 사용하고 싶으신가요? DietPi가 바로 여러분이 찾던 솔루션일 수 있습니다. 많은 사람들이 자체 인프라를 관리하고 완벽하게 구성되고 보호된 서버를 실행하는 방법을 알고 있지만, DietPi는 처음부터 시작하려는 사람들에게 적합한 단계입니다.



이러한 작업에 필요한 모든 복잡한 작업을 수동으로 수행하는 대신 DietPi를 사용하면 '마법사'와 자체 명령줄을 사용하여 구축할 수 있습니다. 여기에서 개인 클라우드, _스마트 홈_ 장치 관리, 자동 백업 및 크론탭은 물론 고급 솔루션을 실험해 볼 수 있습니다.



![img](assets/en/01.webp)



## 설치



### 다운로드



DietPi는 운영 체제를 다양한 장치에 구울 수 있도록 수많은 ISO 이미지 세트를 제공합니다. 예를 들어 라즈베리 파이5용 ISO는 아직 테스트 중이지만, 여러분의 보드에 적합한 ISO를 찾을 수 있습니다.



이 가이드에서는 씬 클라이언트에 설치하기로 했기 때문에 _PC/VM_을 선택한 다음 _Native PC_를 선택했습니다. 이러한 장치에는 부트 로더의 생성이 다른 두 개의 ISO 이미지가 있습니다. 튜토리얼에 사용된 머신은 상당히 오래된 머신이므로 _BIOS/CSM_ 버전을 선택했습니다. 최신 머신을 사용하는 경우 올바른 버전은 `UEFI`일 수 있습니다.



![img](assets/en/02.webp)



설치 프로그램 이미지`, `sha256` 및 `서명`이 포함된 페이지로 이동합니다.



![img](assets/en/03.webp)



매일 사용하는 컴퓨터의 '홈'에 디렉토리를 준비하여 필요한 파일을 'wget'으로 다운로드할 수 있도록 합니다.



![img](assets/en/04.webp)



개발자의 공개 키는 최소한의 조사가 필요하지만 이 링크(https://github.com/MichaIng.gpg)에서 찾을 수 있습니다.



![img](assets/en/05.webp)



Ls -la`로 디렉터리의 내용을 확인하고 `gpg --import`로 MichaIng 키를 키링으로 가져옵니다.



### 인증 및 플래시



마지막으로, 제가 가장 추천하는 부분은 다운로드한 운영 체제의 진위 여부를 확인하여 SBC에 설치하는 것입니다.



![img](assets/en/06.webp)



Sha256sum 명령으로 '양호한 서명' 결과와 동일한 Hash 제어를 얻은 경우, ISO를 USB 스틱에 플래시할 수 있습니다. 이를 위해 Whale Etcher와 같은 앱을 사용하세요.



![img](assets/en/07.webp)



## 다이어트파이 설치



![img](assets/en/09.webp)



플래시 드라이브를 다이어트파이를 호스팅할 장치로 옮기고 라임 Green 운영 체제 설치를 시작합니다. 이 연습에서는 16GB RAM, 운영 체제용 128GB SSD 및 두 번째 1TB 데이터 디스크가 장착된 씬 클라이언트를 사용합니다. 설치에는 30분도 채 걸리지 않았지만, 예를 들어 라즈베리를 사용하는 경우에는 리소스가 더 적고 시간이 더 오래 걸릴 수 있습니다. 설치하는 동안 진행 상황이 표시됩니다.



![img](assets/en/08.webp)



라즈베리 등을 위해 설계된 DietPi의 진정한 본질은 그래픽 환경이 없고 기본 'shsh' 액세스가 가능한 소위 '헤드리스' 설치입니다. 대신 이 가이드에서는 그래픽 환경, 정확히 말하면 LXDE를 볼 수 있습니다.



이 단계에서는 기본적으로 사용할 웹 브라우저를 크롬과 파이어폭스 중 어느 것을 선택할지 묻는 메시지가 표시됩니다. 둘 다 잘 작동하며 개인적인 선호도 외에는 특별히 금기 사항이 없습니다.



마지막에 설치 프로그램에서 이미 프로그램을 설치할 것인지 묻는 메시지가 표시될 수 있지만, 여기서 **아무것도 미리 로드하지 않는 것이 좋습니다**. 이 단계가 끝나면 보안상의 이유로 두 사용자의 기본 비밀번호를 변경하라는 메시지가 표시됩니다. 가장 중요한 것은 **`글로벌 소프트웨어 비밀번호(GSP)`**를 설정해야 하며, 이를 통해 다양한 소프트웨어에 대한 액세스를 통제된 방식으로 보장할 수 있습니다. **OS 설치 중에 소프트웨어를 다운로드할 때 'GSP'를 설정하지 않으면 사실상 액세스할 수 없게 됩니다**. '글로벌 소프트웨어 비밀번호'를 설정한 후 삭제했다가 다시 설치해야 하므로 **이중 작업을 피하기 위해 아무것도 넣지 마세요**. (불편함이 있을 가능성이 있지만 100% 확실하지는 않습니다).



설치는 운영 체제 개발을 지원하는 데 사용되는 자동화된 데이터 수집 서비스인 DietPi-Survey를 활성화하라는 요청으로 끝납니다. 웹사이트에 따르면, 데이터 수집은 DietPi에서 제공하는 자동화를 통해 소프트웨어를 다운로드하거나 다음 릴리즈로 업그레이드할 때 활성화됩니다. 누구나 옵트인(_옵트인_) 또는 옵트아웃(_옵트아웃_) 옵션을 선택할 수 있습니다.



![img](assets/en/23.webp)



설치가 완료된 후 재부팅하면 설정한 대로 DietPi가 화면에 나타납니다. 튜토리얼에서는 앞서 언급했듯이 `LXDE` 그래픽 환경을 선택했습니다. 바탕 화면에서 `htop`을 시작하는 바로 가기와 열린 터미널을 찾았습니다.



![img](assets/en/10.webp)



### "운영 체제의 '도구'



Linux 배포판에서 사용하는 대부분의 프로그램은 잊어버리세요 - DietPi는 매우 최적화되어 있기 때문에 상당수의 프로그램이 제외되어 있습니다. 기본적으로 많은 명령을 수동으로 설치해야 하지만, 이제 막 사용해보려는 경우 유혹을 뿌리치고 DietPi의 자동화를 테스트해 보세요.



새 운영 체제를 시작하는 데 가장 먼저 유용한 도구인 터미널로, 전원을 켤 때마다 자동으로 열립니다.



![img](assets/en/11.webp)



터미널 화면에서 이 운영 체제의 [도구](https://dietpi.com/docs/dietpi_tools/)를 나타내는 'dietpi-'가 앞에 오는 일련의 명령이 나열되어 있습니다:




- '다이어트파이 런처': 운영 체제, 파일 관리자 등에 액세스합니다
- '다이어트파이 소프트웨어': 제품군에서 이미 사용 가능한 모든 소프트웨어를 설치할 수 있는 도구를 나타냅니다
- 다이어트피-config`: 시스템 구성, 심지어 가장 고급 구성에 액세스합니다.



![img](assets/en/14.webp)



### 백업



서버 백업은 시스템 관리자가 처음 시작할 때부터 예상해야 하는 일상적인 작업입니다.



다이어트파이에는 '다이어트파이-백업' 명령이 있는데, 이 명령은 이상적인 솔루션을 찾기 위해 살펴볼 것을 권장합니다: 사용하는 애플리케이션에 따라 증분 백업 또는 정기 백업을 설정할 수 있으며, 루틴을 사용자 정의하는 모든 옵션을 설정할 수 있습니다.



![img](assets/en/22.webp)



다이어트피-드라이브_관리자`를 시작하여 백업 대상(예: 다른 디스크)을 선택하여 대상 드라이브를 마운트하고 이 기능에 사용합니다.



## 구성



셀프 호스팅은 호기심이 많든 단순히 열정이 있든 누구에게나 권장할 만한 경험입니다. 하지만 서버를 가동하고 구성하는 데에는 적지 않은 기술적 어려움이 따릅니다. 바로 이 부분에서 **다이어트파이**의 단순성이 빛을 발하며, 몇 가지 간단한 단계로 필요에 맞는 시스템을 구성할 수 있습니다.



![img](assets/en/24.webp)



기본 설정과 고급 설정을 명령어 하나만 있으면 Interface에서 간편하게 이용할 수 있습니다:



'''dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo 다이어트파이 소프트웨어


```