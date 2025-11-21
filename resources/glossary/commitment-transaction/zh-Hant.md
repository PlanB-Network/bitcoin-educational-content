---
term: Commitment Transaction
---

在 Lightning 內的雙向通道中，Commitment Transaction 是雙方建立並簽署的交易，不會在主鏈上發布。它代表通道雙方之間資金分配的當前狀態，每次 Lightning 付款都會產生一個新的 Commitment Transaction。這些交易是有效的，但只有在通道單方面關閉時才會被廣播。它們包含每一方的輸出，反映了自通道打開以來根據 Lightning 付款進行的資金分配。相關的懲罰機制可阻止各方廣播過時的通道狀態，即反映錯誤資金分配的舊 Commitment 交易。