---
name: Máy Tính Boltzmann
description: Hiểu về khái niệm entropy và cách sử dụng Boltzmann
---
![cover](assets/cover.webp)

***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, trang web KYCP.org hiện không thể truy cập được. Gitlab chứa mã của Máy Tính Boltzmann cũng đã bị tịch thu. Tính đến thời điểm hiện tại, việc tải xuống công cụ này không còn khả thi. Tuy nhiên, có khả năng mã nguồn có thể được tái xuất bản bởi người khác trong những tuần tới. Trong thời gian chờ đợi, bạn vẫn có thể hưởng lợi từ hướng dẫn này để hiểu cách hoạt động của Máy Tính Boltzmann. Các chỉ số do công cụ này cung cấp áp dụng cho bất kỳ giao dịch Bitcoin nào và cũng có thể được tính toán thủ công. Tôi sẽ cung cấp tất cả các phép tính cần thiết trong hướng dẫn này. Nếu bạn đã tải công cụ Python về máy của mình hoặc nếu bạn đang sử dụng RoninDojo, bạn có thể tiếp tục sử dụng công cụ và theo dõi hướng dẫn này như bình thường, nó vẫn hoạt động.*

_Chúng tôi đang ch closely theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này chỉ mang tính chất giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích sử dụng các công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ các luật lệ trong phạm vi quyền hạn của họ._

---

Máy Tính Boltzmann là một công cụ để phân tích giao dịch Bitcoin bằng cách đo lường mức độ entropy cùng với các chỉ số tiên tiến khác. Nó cung cấp cái nhìn sâu sắc về mối liên kết giữa các đầu vào và đầu ra của một giao dịch. Những chỉ số này cung cấp một đánh giá định lượng về quyền riêng tư của giao dịch và giúp xác định các lỗi tiềm ẩn.

Công cụ Python này được phát triển bởi các đội ngũ tại Samourai Wallet và OXT, nhưng nó có thể được sử dụng trên bất kỳ giao dịch Bitcoin nào.

## Làm thế nào để sử dụng Máy Tính Boltzmann?
Để sử dụng Máy Tính Boltzmann, bạn có hai lựa chọn. Lựa chọn đầu tiên là cài đặt công cụ Python trực tiếp trên máy của bạn. Lựa chọn khác, bạn có thể sử dụng trang web KYCP.org (_Biết Quyền Riêng Tư Đồng Tiền Của Bạn_) với một nền tảng sử dụng đơn giản hơn. Đối với người dùng [RoninDojo](https://planb.network/tutorials/node/ronin-dojo-v2), lưu ý rằng công cụ này đã được tích hợp sẵn vào node của bạn.

Sử dụng trang web KYCP khá dễ dàng: chỉ cần nhập mã định danh giao dịch (TXID) bạn muốn phân tích vào thanh tìm kiếm và nhấn `ENTER`.
![KYCP](assets/1.webp)
Sau đó, bạn sẽ tìm thấy các thông tin khác nhau về giao dịch, bao gồm các liên kết giữa các đầu vào và đầu ra. Nhấp vào `liên kết xác định`.
![KYCP](assets/2.webp)
Bạn sẽ đến trang dành riêng cho các chỉ số của Máy Tính Boltzmann.
![KYCP](assets/3.webp)
Đối với những người muốn sử dụng công cụ trực tiếp từ node RoninDojo của họ, nó có thể được truy cập qua `RoninCLI > Bộ Công Cụ Samourai > Máy Tính Boltzmann`.

Giống như trang web KYCP.org, một khi công cụ Python đã được cài đặt, bạn chỉ cần dán TXID của giao dịch bạn muốn phân tích.

![KYCP](assets/7.webp)

Sau đó, nhấn phím `ENTER` để nhận kết quả.

![KYCP](assets/8.webp)

## Các chỉ số của Máy Tính Boltzmann là gì?
### Các Kết Hợp / Giải Thích:
Chỉ số đầu tiên mà phần mềm tính toán là tổng số các kết hợp có thể, được chỉ dưới dạng `nb combinations` hoặc `interpretations` trong công cụ.
Xét đến giá trị của các UTXO tham gia vào giao dịch, chỉ số này tính toán số cách mà các input có thể được kết hợp với các output. Nói cách khác, nó xác định số lượng giải thích hợp lý mà một giao dịch có thể gây ra từ góc độ của một người quan sát bên ngoài phân tích nó. Ví dụ, một giao dịch coinjoin được cấu trúc theo mô hình Whirlpool 5x5 trình bày `1,496` khả năng kết hợp: ![KYCP](assets/4.webp)
Một giao dịch coinjoin Whirlpool Surge Cycle 8x8, mặt khác, trình bày `9,934,563` giải thích có thể: ![KYCP](assets/5.webp)
Ngược lại, một giao dịch truyền thống hơn với 1 input và 2 output chỉ trình bày một giải thích duy nhất: ![KYCP](assets/6.webp)

### Entropy:
Chỉ số thứ hai được tính toán là entropy của một giao dịch, được chỉ định bởi `Entropy`.

Trong bối cảnh chung của mật mã học và thông tin, entropy là một thước đo định lượng về sự không chắc chắn hoặc khó dự đoán liên quan đến một nguồn dữ liệu hoặc một quá trình ngẫu nhiên. Nói cách khác, entropy là cách đo lường mức độ khó dự đoán hoặc đoán thông tin.

Trong bối cảnh cụ thể của phân tích chuỗi, entropy cũng là tên của một chỉ số, được suy ra từ entropy Shannon và [được phát minh bởi LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), được tính toán với công cụ Boltzmann.

Khi một giao dịch trình bày một số lượng lớn các kết hợp có thể, thường thì việc tham khảo đến entropy của nó là phù hợp hơn. Chỉ số này cho phép đo lường sự thiếu hiểu biết của các nhà phân tích về cấu hình chính xác của giao dịch. Nói cách khác, entropy càng cao, nhiệm vụ xác định các chuyển động bitcoin giữa các input và output trở nên khó khăn hơn đối với các nhà phân tích.

Trên thực tế, entropy tiết lộ liệu, từ góc độ của một người quan sát bên ngoài, một giao dịch có trình bày nhiều giải thích có thể dựa trên số lượng các input và output mà không cần xem xét các mô hình và quy tắc ngoại vi hoặc nội bộ khác hay không. Entropy cao sau đó đồng nghĩa với việc bảo mật tốt hơn cho giao dịch.

Entropy được định nghĩa là logarit nhị phân của số lượng các kết hợp có thể. Dưới đây là công thức được sử dụng:
```bash
E: entropy của giao dịch
C: số lượng các kết hợp có thể cho giao dịch

E = log2(C)
```

Trong toán học, logarit nhị phân (logarit cơ số 2) tương ứng với phép toán ngược của việc lũy thừa 2. Nói cách khác, logarit nhị phân của `x` là số mũ mà `2` phải được nâng lên để thu được `x`. Chỉ số này do đó được biểu thị bằng bit.

Hãy lấy ví dụ về việc tính entropy cho một giao dịch coinjoin được cấu trúc theo mô hình Whirlpool 5x5, mà như đã đề cập trước đó, cung cấp một số lượng các kết hợp có thể là `1,496`:
```bash
C = 1,496
E = log2(1,496)
E = 10.5469 bit
```
Như vậy, giao dịch coinjoin này hiển thị một entropy là `10.5469 bit`, được coi là rất thỏa đáng. Giá trị này càng cao, giao dịch chấp nhận càng nhiều giải thích khác nhau, do đó tăng cường mức độ riêng tư của nó.
Đối với một giao dịch coinjoin 8x8 trình bày `9,934,563` giải thích, entropy sẽ là:
```bash
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bit
```
Hãy xem xét một ví dụ khác với một giao dịch truyền thống hơn, bao gồm một đầu vào và hai đầu ra: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) Trong trường hợp của giao dịch này, chỉ có một cách giải thích có thể: `(In.0) > (Out.0 ; Out.1)`. Do đó, entropy của nó được xác định là `0`:```bash
C = 1
E = log2(1)
E = 0 bit
```

### Hiệu Suất:
Chỉ số thứ ba được cung cấp bởi Máy Tính Boltzmann được gọi là `Hiệu Suất Ví`. Chỉ số này đánh giá hiệu suất của giao dịch bằng cách so sánh nó với giao dịch lý tưởng nhất có thể trong một cấu hình giống hệt.

Điều này dẫn chúng ta đến khái niệm entropy tối đa, tương ứng với entropy cao nhất mà một cấu trúc giao dịch cụ thể có thể lý thuyết đạt được. Hiệu suất của giao dịch sau đó được tính toán bằng cách so sánh entropy tối đa này với entropy thực tế của giao dịch được phân tích.

Công thức sử dụng như sau:
```bash
ER: entropy thực tế của giao dịch được biểu thị bằng bit
EM: entropy tối đa có thể có cho một cấu trúc giao dịch nhất định được biểu thị bằng bit
Ef: hiệu suất của giao dịch được biểu thị bằng bit

Ef = ER - EM
```

Ví dụ, đối với cấu trúc coinjoin loại Whirlpool 5x5, entropy tối đa được thiết lập là `10.5469`:
```bash
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bit
```

Chỉ số này cũng được biểu thị dưới dạng phần trăm, công thức của nó sau đó là:
```bash
CR: số lượng tổ hợp có thể thực tế
CM: số lượng tổ hợp tối đa có thể với cùng một cấu trúc
Ef: hiệu suất được biểu thị dưới dạng phần trăm

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```

Một hiệu suất `100%` do đó chỉ ra rằng giao dịch tối đa hóa tiềm năng về quyền riêng tư theo cấu trúc của nó.

### Mật Độ Entropy:
Chỉ số thứ tư là mật độ entropy, được ghi chú trên công cụ là `Mật Độ Entropy`. Nó cung cấp một cái nhìn về entropy tương đối cho mỗi đầu vào hoặc đầu ra của giao dịch. Chỉ số này hữu ích để đánh giá và so sánh hiệu suất của các giao dịch có kích thước khác nhau. Để tính toán nó, chỉ cần chia tổng entropy của giao dịch cho tổng số đầu vào và đầu ra tham gia:
```bash
ED: mật độ entropy được biểu thị bằng bit
E: entropy của giao dịch được biểu thị bằng bit
T: tổng số đầu vào và đầu ra trong giao dịch

ED = E / T
```

Hãy lấy ví dụ về một coinjoin Whirlpool 5x5:
```bash
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bit
```

Hãy cũng tính mật độ entropy cho một coinjoin Whirlpool 8x8:
```bash
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bit
```
Thông tin thứ năm được cung cấp bởi Máy tính Boltzmann là bảng xác suất tương ứng giữa các đầu vào và đầu ra. Bảng này chỉ ra, thông qua điểm Boltzmann, xác suất có điều kiện rằng một đầu vào cụ thể liên quan đến một đầu ra nhất định.
Do đó, đây là một phép đo định lượng về xác suất có điều kiện rằng một sự kết hợp giữa một đầu vào và một đầu ra trong một giao dịch xảy ra, dựa trên tỷ lệ số lượng sự kiện thuận lợi so với tổng số lượng sự kiện có thể xảy ra, trong một tập hợp các giải thích.

Lấy ví dụ về một Whirlpool coinjoin một lần nữa, bảng xác suất có điều kiện sẽ làm nổi bật cơ hội liên kết giữa mỗi đầu vào và đầu ra, cung cấp một phép đo định lượng về sự mơ hồ của các liên kết trong giao dịch:

| %       | Đầu ra 0 | Đầu ra 1 | Đầu ra 2 | Đầu ra 3 | Đầu ra 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Đầu vào 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Ở đây, chúng ta có thể thấy rõ ràng rằng mỗi đầu vào có cơ hội ngang nhau được liên kết với bất kỳ đầu ra nào, điều này tăng cường tính bảo mật của giao dịch.
Tính điểm Boltzmann bao gồm việc chia số lượng giải thích mà một sự kiện nhất định xảy ra cho tổng số lượng giải thích có sẵn. Do đó, để xác định điểm liên kết đầu vào số 0 với đầu ra số 3 (`512` giải thích), quy trình sau được sử dụng:
```bash
Giải thích (IN.0 > OUT.3) = 512
Tổng số Giải thích = 1496
Điểm = 512 / 1496 = 34%
```

Lấy ví dụ về một Whirlpool 8x8 coinjoin (chu kỳ tăng cường), bảng Boltzmann sẽ trông như thế này:

|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

Tuy nhiên, trong trường hợp của một giao dịch đơn giản với một đầu vào và hai đầu ra, tình hình là khác:

| %       | Đầu ra 0 | Đầu ra 1 |
|---------|----------|----------|
| Đầu vào 0 | 100%     | 100%     |

Ở đây, ta thấy rằng xác suất cho mỗi đầu ra xuất phát từ đầu vào số 0 là `100%`. Một xác suất thấp hơn do đó dẫn đến sự riêng tư cao hơn bằng cách làm loãng các liên kết trực tiếp giữa đầu vào và đầu ra.

### Liên Kết Định Rõ:
Thông tin thứ sáu được cung cấp là số lượng liên kết định rõ, bổ sung bởi tỷ lệ của những liên kết này. Chỉ số này tiết lộ bao nhiêu kết nối giữa các đầu vào và đầu ra trong giao dịch được phân tích là không thể chối cãi, với xác suất là `100%`. Mặt khác, tỷ lệ cung cấp một cái nhìn về trọng lượng của những liên kết định rõ này trong toàn bộ tập hợp các liên kết giao dịch.
Ví dụ, một giao dịch coinjoin kiểu Whirlpool không có liên kết định rõ nào, và do đó hiển thị chỉ số và tỷ lệ là `0%`. Ngược lại, trong giao dịch đơn giản thứ hai của chúng tôi được xem xét (với một đầu vào và hai đầu ra), chỉ số được thiết lập ở `2` và tỷ lệ đạt `100%`. Do đó, một chỉ số bằng không báo hiệu sự bảo mật xuất sắc do không có liên kết trực tiếp và không thể chối cãi giữa đầu vào và đầu ra.

**Nguồn Tài Nguyên Bên Ngoài:**

- Mã Boltzmann trên Samourai
- [Giao Dịch Bitcoin & Quyền Riêng Tư (Phần I) bởi Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Giao Dịch Bitcoin & Quyền Riêng Tư (Phần II) bởi Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Giao Dịch Bitcoin & Quyền Riêng Tư (Phần III) bởi Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- Trang Web KYCP
- [Bài Viết trên Medium về Giới Thiệu Kịch Bản Boltzmann bởi Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)