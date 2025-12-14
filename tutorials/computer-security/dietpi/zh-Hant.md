---
name: DietPi
description: 輕量級作業系統，針對效能不佳的機器進行最佳化。偏重於自我託管
---

![cover](assets/cover.webp)



在非技術圈中，「Odroid」、「Raspberry Pi」、「Orange Pi」或「Radxa」等品牌鮮為人知。但只要放眼科技圈，您就會發現 **SBC** 電腦 - 建構在單一主機板上、尺寸通常比常用電腦還小 - 成為任何個人專案不可或缺的支援。



這些電腦的型號繁多。這些電腦最好搭載 Linux 發行版本，通常是為了在這些功率不足的機器上順暢運行而改裝的。



**DietPi 也不例外**：它是一個以 Debian 為基礎的作業系統，經過最佳化，盡可能輕巧，即使是性能最差的 `SBC` 也能非常快速。就在撰寫這篇教學時，它從 Debian12 Bookworm 轉換成 Debian13 Trixie，現在也支援開放原始碼的「RISC-V」處理器 SBC。DietPi 是一個令人愉快的發現，值得進一步研究。



## 優勢



這不是小型 Raspberry 類型板卡的 Debian「一般複製品」。DietPi 才是：




- 針對速度與輕量進行最佳化**：[與其他適用於 SBC 的 Debian 發行版比較](https://dietpi.com/blog/?p=888)，DietPi 在各方面都比較輕。DietPi ISO 映像檔的重量不到 1 GB，是目前專用於舊型 Raspberry 或 Orange PI (例如) 的發行版中最小的。DietPi 對 RAM 和 CPU 資源的需求非常低，因此即使是較舊的主機板也能發揮最佳效能。
- 內建自動化與安裝程式**：一套專用指令可協助使用者監控系統資源，以及自動執行安裝和啟動程式、更新版本、備份和檢查所有記錄的工作。
- 強大、以實驗為導向的社群**：來自 DietPi 社群的 [教學](https://dietpi.com/forum/c/community-tutorials/8) 和專案，是您從軟體中獲得靈感的理想選擇，有了 DietPi，您只要按一下就能安裝軟體。



**從 SBC 榨取每一滴水從未如此簡單**。



## 自動化自我託管


想要嘗試使用自己的伺服器來執行進階的網路解決方案，或使用工具來發展您的 Bitcoin 專業知識？DietPi 可能就是您一直在尋找的解決方案。雖然許多人都知道如何管理自己的基礎架構，並執行完美設定與保護的伺服器，但 DietPi 對於想要從零開始的人來說，是一個合適的步驟。



DietPi 不需要手動執行這種任務所需的所有複雜工作，而是允許您使用「精靈」和自己的命令列來建立它們。在這裡，您可以嘗試自己的個人雲端、_smart home_ 裝置管理、自動備份和 crontab，以及更進階的解決方案。



![img](assets/en/01.webp)



## 安裝



### 下載



DietPi 提供了無數的 ISO 映像集，可以將作業系統燒錄到許多不同的裝置上。有些僅支援：例如 Raspberry PI5 的 ISO 仍在測試中，但您絕對可以找到適合您的主機板的 ISO。



在本指南中，我選擇將其安裝在精簡型用戶端上，因此選擇到 _PC/VM_，然後再選擇到 _Native PC_。這些裝置有兩種 ISO 映像，它們在開機載入程式的世代上有所不同。教學中使用的機器相當老舊，所以選擇了 _BIOS/CSM_ 版本。如果您有較新的機器，正確的版本可能是 `UEFI`。



![img](assets/en/02.webp)



您將會進入包含「安裝程式影像」、「sha256」和「簽名」的頁面。



![img](assets/en/03.webp)



在您日常使用的電腦的 `home` 中準備一個目錄，以便使用 `wget` 下載必要的檔案。



![img](assets/en/04.webp)



開發人員的公開金鑰需要進行最低限度的研究，但您可以在以下連結找到：https://github.com/MichaIng.gpg。



![img](assets/en/05.webp)



使用 `ls -la` 檢查目錄內容，並使用 `gpg --import` 將 MichaIng 金鑰匯入您的金鑰鎖。



### 驗證與快閃



最後，也是我最推薦的部分：確認您已下載並即將安裝在 SBC 上的作業系統的真實性。



![img](assets/en/06.webp)



如果您使用 sha256sum 指令也得到 `Good signature` 結果和相同的 Hash 控制，您就可以繼續將 ISO 快閃到 USB 隨身碟。請使用 Whale Etcher 等應用程式來執行。



![img](assets/en/07.webp)



## DietPi 安裝



![img](assets/en/09.webp)



將快閃磁碟機轉移至 DietPi 的主機裝置，並開始安裝 lime Green 作業系統。在這個練習中，我們使用的瘦客戶機有 16 GB 記憶體、128 GB 作業系統固態硬碟，以及第二個 1 TB 資料磁碟。安裝過程不到 30 分鐘，但如果您要使用 Raspberry 等，資源可能會較少，所需時間也會較長。安裝過程中會顯示進度。



![img](assets/en/08.webp)



DietPi 是為 Raspberries 之類的產品所設計，其真正的本質是所謂的「無頭」安裝，沒有圖形環境，只有原生的「shsh」存取。在本指南中，您會看到圖形化環境，準確來說是 LXDE。



在這個步驟中，您也會被要求決定預設要使用哪個網頁瀏覽器，可以選擇 Chromium 或 Firefox。這兩種瀏覽器都很好用；除了您的個人偏好之外，兩者都沒有特別的禁忌。



在接近尾聲時，安裝程式可能會詢問您是否要安裝任何程式，但在此***我建議您不要預先載入任何***。您應該知道，在此步驟之後，基於安全理由，您會被要求變更兩個使用者的預設密碼。最重要的是，您需要**設定「全局軟體密碼 (GSP)」**，以確保以受控制的方式存取各種軟體。 **如果您在安裝作業系統時下載任何軟體，而沒有設定「GSP」，這些軟體幾乎無法存取**。設定「全局軟體密碼」後，您必須卸載並重複安裝這些軟體：因此，**請勿放入任何東西，以免造成雙重工作**。(不便是可能的，並非 100% 確定）。



安裝結束時會要求啟動 DietPi-Survey，這是用來支援作業系統開發的自動化資料收集服務。根據網站的說明，當您從 DietPi 提供的自動化中下載任何軟體，或是升級到下一個版本時，資料收集就會啟動。每個人都可以選擇加入 (_Opt IN_) 或退出 (_Opt OUT_)。



![img](assets/en/23.webp)



完成安裝及隨後的重新開機後，DietPi 就會出現在您設定的螢幕上。在教學中，如前所述，我選擇了「LXDE」圖形化環境。在桌面上，我找到了啟動 `htop` 和開啟終端機的捷徑。



![img](assets/en/10.webp)



### 「作業系統中的 」工具



忘掉大部分你在 Linux 發行版上使用的程式吧-DietPi 已經做了最佳化，你已經遺漏了不少。基本上你必須手動安裝許多指令，但如果你只是試用，請抵擋誘惑，試著把 DietPi 的自動化功能測試一下。



它絕對是您開始使用新作業系統的第一個有用工具，而且每次開啟時都會自動打開。



![img](assets/en/11.webp)



在終端機螢幕上，您會發現列出一系列以 `dietpi-` 為前的指令，代表此作業系統的 [工具](https://dietpi.com/docs/dietpi_tools/)：




- `dietpi-launcher`：用於存取作業系統、檔案管理員等
- dietpi-Software"：代表您可以安裝套件中所有軟體的工具。
- `dietpi-config`: 存取系統設定，即使是最進階的設定。



![img](assets/en/14.webp)



### 備份



備份伺服器是系統管理員從第一次啟動時就應該預期到的例行工作。



DietPi 有 `dietpi-Backup` 指令，我建議您探索該指令以找出理想的解決方案：它允許您設定定期備份，增量與否取決於所使用的應用程式，以及自訂例行程序的所有選項。



![img](assets/en/22.webp)



選擇備份的目的地，例如另一個磁碟，方法是啟動 `dietpi-Drive_Manager` 以掛載目的地磁碟機，並將其用於此功能。



## 組態



對每個人來說，無論是好奇還是熱衷，自我託管都是一種可取的體驗。然而，架設和配置伺服器涉及一些不小的技術挑戰。這就是 DietPi**的簡易性所在，讓您只需幾個簡單步驟，就能設定出符合您需求的系統。



![img](assets/en/24.webp)



基本和進階設定，全都在您指尖上的一個 Interface 指令中提供：



```dietpi-config


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


sudo dietpi-software


```