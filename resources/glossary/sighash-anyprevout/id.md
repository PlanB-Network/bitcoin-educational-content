---
term: SIGHASH_ANYPREVOUT

---
Proposal untuk implementasi pengubah _SigHash Flag_ baru di Bitcoin, yang diperkenalkan dengan BIP118. `SIGHASH_ANYPREVOUT` memungkinkan fleksibilitas yang lebih besar dalam manajemen transaksi, terutama untuk aplikasi tingkat lanjut seperti saluran pembayaran di Jaringan Lightning dan pembaruan Eltoo. `SIGHASH_ANYPREVOUT` memungkinkan tanda tangan untuk tidak terikat pada UTXO tertentu sebelumnya (*Any Previous Output*). Jika digunakan bersama dengan `SIGHASH_ALL`, hal ini akan memungkinkan penandatanganan semua output dari sebuah transaksi, tetapi tidak untuk inputnya. Ini akan memungkinkan penggunaan kembali tanda tangan untuk transaksi yang berbeda, selama kondisi tertentu yang ditentukan terpenuhi.

> ► *Pengubah SigHash SIGHASH_ANYPREVOUT ini berasal dari ide SIGHASH_NOINPUT yang awalnya diusulkan oleh Joseph Poon pada tahun 2016 untuk menyempurnakan konsepnya tentang Jaringan Lightning*
