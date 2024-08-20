---
term: CHÍNH SÁCH (MINISCRIPT)
---

Một ngôn ngữ cấp cao, hướng người dùng cho phép việc chỉ định đơn giản các điều kiện dưới đó một UTXO có thể được mở khóa trong khuôn khổ của Miniscript. Chính sách là một mô tả trừu tượng về các quy tắc chi tiêu. Nó sau đó có thể được biên dịch thành miniscript, là một tương đương một-một với các thao tác từ ngôn ngữ script bản địa của Bitcoin.

![](../../dictionnaire/assets/30.png)

Ngôn ngữ chính sách hơi khác biệt so với ngôn ngữ miniscript. Ví dụ, hãy tưởng tượng một hệ thống bảo mật với một lộ trình chính là khóa A, và một lộ trình phục hồi là khóa B, nhưng dưới một thời gian chờ là một năm (khoảng 52,560 khối). Trong chính sách, điều này sẽ được:

```plaintext
or(pk(A),and(pk(B),older(52560)))
```

Một khi được biên dịch thành miniscript, nó sẽ là:

```plaintext
andor(pk(B),older(52560),pk(A))
```

Và một khi được chuyển đổi thành script bản địa, nó sẽ là:

```plaintext
<B>
OP_CHECKSIG
OP_NOTIF
<A>
OP_CHECKSIG
OP_ELSE
<50cd00>
OP_CHECKSEQUENCEVERIFY
OP_ENDIF
```