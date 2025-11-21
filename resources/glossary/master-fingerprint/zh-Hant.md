---
term: 主指紋
---

分層確定 (HD) Wallet 中主私人密碼匙的 4 位元組 (32 位元) 指紋。它是透過計算主私人密碼匙的「SHA256」 Hash，然後再計算「RIPEMD160」 Hash，這個過程在 Bitcoin 上被稱為「HASH160」。主指紋用於識別 HD Wallet，獨立於衍生路徑，但會考慮到 passphrase 的存在與否。主指紋是簡潔的資訊，可參考一組金鑰的來源，而不會透露 Wallet 的敏感資訊。