---
name: Electrum OP_RETURN
description: 使用 Electrum 註冊 Blockchain Bitcoin 的訊息
---

![cover](assets/cover.webp)




本教學逐步說明如何使用 Wallet 電子琴在 Blockchain Bitcoin 上寫入訊息。此操作使用 OP_RETURN 指令在交易中插入文字，在 Blockchain 上公開可見。按照這些簡單的步驟即可成功註冊。



---
## 先決條件





- 一台電腦 (Windows、macOS 或 Linux)。
- 網際網路連線。
- 在您的 Wallet 中放入幾個 Satoshis (Sats) 或 bitcoins (BTC)，以支付交易金額和費用。
- 文字到十六進位轉換器 (例如線上網站) 或專用工具，例如 [this OP_RETURN script generator](https://resources.davidcoen.it/opreturnelectrum/)。



---

## 步驟 1：下載並安裝 Electrum



![image](assets/fr/01.webp)



1.請造訪 Electrum 官方網站：[electrum.org](https://electrum.org/).


2.下載與您的作業系統（Windows、macOS、Linux）相對應的版本。


3.依照安裝人員的指示安裝 Electrum。


4.透過比較檔案的簽章或 Hash，檢查下載檔案的完整性（可選，但基於安全理由建議使用）。



→更多詳細資訊請參閱 Electrum 教學 ：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 步驟 2：建立或匯入 Wallet



1.啟動 Electrum。


2.如果您已有 seed 詞組 (恢復詞組)，請選擇 Create a new Wallet（建立新的 Wallet）或 Restore an existing Wallet（恢復現有的 Wallet）。


3.請依照指示設定您的 Wallet ：




 - 對於新的 Wallet，請記下您的 seed 句子，並將其保存在安全的地方（紙張、保險箱等）。
 - 對於現有的 Wallet，請輸入您的 seed 短語來還原它。


4.設定密碼以保護您的 Wallet。



→更多詳細資訊請參閱 Electrum 教學 ：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 步驟 3：檢查可用資金



確保您的 Wallet 包含足夠的 bitcoins (BTC) 或 satoshis (Sats) 來 ：




- 交易金額（例如 0.00001 BTC 或 1000 Sats）。
- 交易費用，依網路大小而異（一般為幾千 Sats）。



諮詢 Electrum 中的 Balance 以檢查您的資金。



![image](assets/fr/02.webp)



如有必要，請轉移 BTC 或 Sats 來為您的 Wallet 供電。要做到這一點，請前往 「接收 」標籤，然後點擊 「創建請求」：



![image](assets/fr/03.webp)



這會顯示接收 Address：



![image](assets/fr/04.webp)



→更多詳細資訊請參閱 Electrum 教學 ：



https://planb.network/tutorials/wallet/desktop/electrum-efec9166-46b5-4937-8cee-6bc310975177


---

## 步驟 4：準備要銘刻的訊息



選擇您要輸入的訊息 (例如 `Thanks Satoshi`)。注意：OP_RETURN 訊息限制為 80 位元組，即約 80 個 ASCII 字元。



*花點時間想一想：您在 Blockchain Bitcoin 上寫下的東西是永恆的，所有人都可以存取，所以 :*




- 留下我們人性的美麗表現，
- 避免輸入您可能會後悔的內容



*Blockchain 空間和您的比特幣都很寶貴，請善加利用*。



將您的訊息轉換為十六進位 ：




- 您可以使用 [線上工具](https://www.rapidtables.com/convert/number/ascii-to-hex.html)，但請注意不要在那裡處理敏感資料（雖然原則上，打算透過 OP_RETURN 在 Blockchain Bitcoin 上公佈的資訊不會有任何保密問題）；
- 為了提高機密性，請使用小型 Python .NET Framework 在本機執行轉換：



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



例如：ASCII `Thanks Satoshi` 的十六進位值為 `5468616e6b73205361746f736869`。



準備交易腳本。以下是預期格式的範例：



```script
bc1q879cv4p5q6s9537orange3zss33d3turzad8, 0.00001
script(OP_RETURN 5468616e6b73205361746f736869), 0
```



它是由 ：





- 目的地 **Address**：有效的 Bitcoin Address。Ici, `bc1q879cv4p5q6s9537orange3zss33d3turzad8`。這可以是您自己的 Address，如果您希望將轉帳的資金退回給自己；
- **Amount transferred**: 交易金額，這裡是 `0.00001` BTC。**請注意**：由於 Electrum 使用的單位是 BTC，交易腳本中顯示的金額也必須以 BTC 表示，而不是 Sats；
- 腳本 **OP_RETURN**：訊息轉換為十六進位，前面加上 script(`OP_RETURN <messsage>), 0`。這裡的 `5468616e6b73205361746f736869` 代表訊息的十六進位。



⚠️ **注意**：在 OP_RETURN 之後顯示`0`是非常重要的，因為這個操作碼會標示腳本無效，使輸出永久無法使用。網路節點會從其 UTXO 套件中刪除此輸出。如果您輸入`0`以外的值，它將不可挽回地丟失：您的比特幣將被視為燒毀。因此，您應該總是用 OP_RETURN 輸入 `0`，以記錄所需的資料，但不將資金與之相關聯，因為資金會遺失。



提示：使用 [OP_RETURN Generator] 工具 (https://resources.davidcoen.it/opreturnelectrum/) 自動 generate 腳本。即使此工具建議以 BTC 輸入金額，請保持單位設定為 Electrum。



![image](assets/fr/05.webp)



要更改 Electrum 使用的單位，請在菜單欄中找到「偏好設定」，然後在「單位」標籤中選擇 BTC / mBTC / bits 或 Sats ：



![image](assets/fr/06.webp)




---

## 步驟 5：傳送交易



在 Electrum 中，移至「傳送」標籤。



![image](assets/fr/07.webp)



在「Pay to」欄位中，貼上準備好的腳本 (例如上面的腳本)。



![image](assets/fr/08.webp)



付款至」欄位應顯示在 Green 中，交易金額應顯示在下面一行。



檢查金額欄位中的金額及其單位。



按一下「付款...」，然後根據您願意支付的金額，以及您希望 Miner 處理交易並整合為區塊的速度，調整您的交易費用。



![image](assets/fr/09.webp)



按一下確定，然後用密碼確認交易。將會出現確認視窗。




---

## 步驟 6：驗證註冊



交易確認後 (可能需要幾分鐘)，請移至「歷史」標籤。



![image](assets/fr/10.webp)



在交易上按一下滑鼠右鍵，然後選擇「在資料總覽器上檢視」以查看詳細資料。



或者，複製目標 Address（例如，`bc1q879cv4p5q6s9537orange3zss33d3turzad8`），並在 Blockchain 探索器上檢視，例如 [Mempool.space](https://Mempool.space/) 或 [blockstream.info](https://blockstream.info/) 。



在交易詳細資料中尋找 OP_RETURN 欄位，查看您的訊息。



![image](assets/fr/11.webp)




![image](assets/fr/12.webp)




---

## 提示和最佳實踐





- 以少量進行測試：從小量交易開始 (例如 Sats 1000) 以避免代價高昂的錯誤。
- 確保包含 OP_RETURN 的輸出等於零，否則您的 bitcoins 將永久遺失。
- 檢查單位：確定輸入的金額與 Electrum 中顯示的單位相符（BTC、mBTC 或 Sats）。
- 交易費用：如果網路擁塞，請增加費用以加快確認速度。
- 簡訊：OP_RETURN 詞條限制為 80 位元組。請依此規劃您的訊息。



---

## 有用資源





- 下載 Electrum: [electrum.org](https://electrum.org/)
- OP_RETURN 腳本產生器：[resources.davidcoen.it/opreturnelectrum/](https://resources.davidcoen.it/opreturnelectrum/)
- Blockchain 探索者：[Mempool.space](https://Mempool.space/), [blockstream.info](https://blockstream.info/)