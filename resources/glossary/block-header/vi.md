---
term: BLOCK HEADER
---

Block header là một cấu trúc dữ liệu đóng vai trò là thành phần chính trong việc xây dựng một khối Bitcoin. Mỗi khối bao gồm một header và một danh sách các giao dịch. Block header chứa thông tin quan trọng đảm bảo tính toàn vẹn và hợp lệ của một khối trong blockchain. Block header chứa 80 byte metadata và bao gồm các thành phần sau:
* Phiên bản khối;
* Hash của khối trước đó;
* Root của cây Merkle của các giao dịch;
* Dấu thời gian của khối;
* Mục tiêu khó khăn;
* Nonce.

Ví dụ, đây là header của khối số 785,530 ở định dạng hexadecimal, được khai thác bởi Foundry USA vào ngày 15 tháng 4 năm 2023:

```text
00e0ff3f5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000206b
de3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0bcb13a64b2e00517
43f09a40
```

Nếu chúng ta phân tích header này, chúng ta có thể nhận ra:
* Phiên bản:

```text
00e0ff3f
```

* Hash của khối trước:

```text
5ffe3b0d9247dc437e18edc19252e4517cee941752d501000000000000000000
```

* Root của Merkle:

```text
206bde3a10826e2acb2f28fba70463601c789293d0c9c4348d7a0d06711e97c0
```

* Dấu thời gian:

```text
bcb13a64
```

* Mục tiêu:

```text
b2e00517
```

* Nonce:

```text
43f09a40
```

Để được coi là hợp lệ, một khối phải có một header mà, sau khi được hash với `SHA256d`, tạo ra một hash nhỏ hơn hoặc bằng mục tiêu khó khăn.

> ► *Trong tiếng Anh, nó được gọi là "Block Header".*