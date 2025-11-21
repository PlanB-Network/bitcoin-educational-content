---
term: BIP0137
---

提出使用 Bitcoin 私密金鑰及其相關地址簽署訊息的標準格式，以證明 Address 的 Ownership。本 BIP 旨在解決簽署訊息時與不同類型 Bitcoin 位址 (P2PKH、P2SH、P2WPKH...) 相關的歧義。它引進了一種透過簽章明確區分這些 Address 格式的方法。這些簽章對於各種應用都很有用，例如資金證明、審計，以及其他需要透過 Address 私密金鑰驗證 Address 的用途。BIP322 之後又推出了新的簽章格式，可擴展此標準並將其通用於任何類型的腳本。