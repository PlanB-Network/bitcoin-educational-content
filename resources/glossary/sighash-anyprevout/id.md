---
istilah: SIGHASH_ANYPREVOUT
---

Proposal untuk implementasi modifikasi Flag SigHash baru dalam Bitcoin, diperkenalkan dengan BIP118. `SIGHASH_ANYPREVOUT` memungkinkan fleksibilitas yang lebih besar dalam pengelolaan transaksi, terutama untuk aplikasi lanjutan seperti saluran pembayaran di Lightning Network dan pembaruan Eltoo. `SIGHASH_ANYPREVOUT` memungkinkan tanda tangan tidak terikat pada UTXO sebelumnya yang spesifik (*Any Previous Output*). Digunakan bersama dengan `SIGHASH_ALL`, hal ini akan memungkinkan penandatanganan semua output dari sebuah transaksi, tetapi tidak satu pun dari inputnya. Ini akan memungkinkan penggunaan kembali tanda tangan untuk transaksi yang berbeda, selama kondisi tertentu yang ditentukan terpenuhi.

> ► *Modifikasi SigHash ini SIGHASH_ANYPREVOUT berasal dari ide SIGHASH_NOINPUT yang awalnya diajukan oleh Joseph Poon pada tahun 2016 untuk meningkatkan konsepnya tentang Lightning Network.*