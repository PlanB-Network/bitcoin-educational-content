---
term: 有用なロード
---

コンピューティングの一般的な文脈では、ペイロードとは、より大きなデータパケットに 含まれる重要なデータのことである。例えば、Bitcoin Address上のSegWit V0では、ペイロードは公開鍵のHashに相当し、様々なメタデータ(HRP、セパレータ、SegWitバージョン、チェックサム)は含まれない。たとえば、Addressの `bc1qc2eukw7reasfcmrafevp5dhv8635yuqays50gj` では、：




- bc`：人間が読める部分（HRP）；
- 1`: セパレーター；
- `q`:SegWit のバージョン。これはバージョン 0；
- c2eukw7reasfcmrafevp5dhv8635yuqa`: ペイロード、この場合は公開鍵のHash；
- ys50gj`：チェックサム。