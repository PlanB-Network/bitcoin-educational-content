---
term: BLK*.DAT
---

Nazwa plików w Bitcoin Core, które przechowują nieprzetworzone dane blokowe Blockchain. Każdy plik jest identyfikowany przez unikalny numer w nazwie. Bloki są zapisywane w porządku chronologicznym, począwszy od pliku blk00000.dat. Gdy plik ten osiągnie maksymalną pojemność, kolejne bloki są zapisywane w pliku blk00001.dat, a następnie blk00002.dat itd. Każdy plik blk ma maksymalną pojemność 128 mebibajtów (MiB), co odpowiada nieco ponad 134 megabajtom (MB). Pliki te zostały przeniesione do folderu `/blocks` od wersji 0.8.0.