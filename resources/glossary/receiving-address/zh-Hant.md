---
term: 接收 Address
---

用來接收比特幣的資訊。一個 Address 通常是通過對一個公開密鑰進行散列，使用 `SHA256` 和 `RIMPEMD160` 並在這個摘要中加入元資料來構建的。用於建構接收 Address 的公開金鑰是使用者 Wallet 的一部分，因此是從他們的 seed 衍生出來的。例如，SegWit 位址由以下資訊組成：


- 指定 "Bitcoin "的人力資源計劃：`bc`；
- 分隔符： `1`；
- 使用的 SegWit 版本：`q` 或 `p`；
- 有效載荷： 公開金鑰的摘要（或在 Taproot 的情況下直接使用公開金鑰）；
- 校驗和：BCH 碼。


但是，接收的 Address 也可以代表其他東西，這取決於所使用的腳本模型。例如，P2SH 位址是使用腳本的 Hash 來構建的。另一方面，Taproot 位址則直接包含經調整過的公開金鑰，而不需要散列。


接收的 Address 可以字母數字字串或 QR 代碼的形式表示。每個 Address 可以使用多次，但非常不鼓勵這種做法。事實上，為了維持一定程度的隱私權，建議每個 Bitcoin Address 只使用一次。每次向自己的 Wallet 付款時，都應該產生一個新的 Address。對於 SegWit V0 位址，Address 以 `Bech32` 編碼；對於 SegWit V1 位址，Address 以 `Bech32m` 編碼；對於 Legacy 位址，Address 以 `Base58check` 編碼。從技術角度來看，收到 Bitcoin 就等於擁有與公開金鑰相關的私密金鑰 (也就是 Address)。當有人收到比特幣時，寄件者會更新現有的支出限制，因此現在只有收件者才能擁有這項權力。


![](../../dictionnaire/assets/23.webp)