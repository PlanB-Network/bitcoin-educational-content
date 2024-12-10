---
name: Bí Mật Đằng Sau Ví Bitcoin
goal: Khám phá nguyên tắc mã hóa đằng sau ví Bitcoin.
objectives:
  - Định nghĩa các khái niệm lý thuyết cần thiết để hiểu các thuật toán mã hóa được sử dụng trong Bitcoin.
  - Hiểu rõ cấu trúc của một ví xác định và phân cấp.
  - Biết cách nhận diện và giảm thiểu rủi ro liên quan đến quản lý ví.
  - Hiểu nguyên tắc của hàm băm, khóa mã hóa, và chữ ký số.
---

# Hành Trình Vào Trái Tim Của Ví Bitcoin

Khám phá bí mật của ví Bitcoin xác định và phân cấp với khóa học CYP201 của chúng tôi! Dù bạn là người dùng thường xuyên hay một người hâm mộ muốn mở rộng kiến thức, khóa học này cung cấp một sự đắm chìm hoàn toàn vào cách thức hoạt động của những công cụ mà chúng ta hàng ngày sử dụng.

Học về cơ chế của hàm băm, chữ ký số (ECDSA và Schnorr), cụm từ ghi nhớ, khóa mã hóa, và việc tạo địa chỉ nhận, tất cả trong khi khám phá các chiến lược bảo mật tiên tiến.

Khóa học này không chỉ trang bị cho bạn kiến thức để hiểu cấu trúc của một ví Bitcoin mà còn chuẩn bị cho bạn sẵn sàng đắm mình vào thế giới mã hóa học thú vị.

Với phương pháp giảng dạy rõ ràng, hơn 60 sơ đồ giải thích, và ví dụ cụ thể, CYP201 sẽ giúp bạn hiểu từ A đến Z cách ví của bạn hoạt động, để bạn có thể tự tin điều hướng trong vũ trụ Bitcoin. Hãy kiểm soát UTXOs của bạn ngày hôm nay bằng cách hiểu cách ví HD hoạt động!

+++

# Giới Thiệu

<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Giới Thiệu Khóa Học

<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

Chào mừng bạn đến với khóa học CYP201, nơi chúng ta sẽ khám phá sâu về cách thức hoạt động của ví Bitcoin HD. Khóa học này được thiết kế cho bất kỳ ai muốn hiểu cơ bản kỹ thuật của việc sử dụng Bitcoin, dù họ là người dùng thông thường, người hâm mộ có hiểu biết, hay chuyên gia tương lai.

Mục tiêu của khóa học này là cung cấp cho bạn chìa khóa để nắm vững các công cụ bạn hàng ngày sử dụng. Ví Bitcoin HD, nằm ở trung tâm trải nghiệm người dùng của bạn, dựa trên một số khái niệm phức tạp, mà chúng tôi sẽ cố gắng làm cho dễ tiếp cận. Cùng nhau, chúng ta sẽ làm sáng tỏ chúng!

Trước khi đi sâu vào chi tiết cấu trúc và hoạt động của ví Bitcoin, chúng ta sẽ bắt đầu với một số chương về các nguyên tắc mã hóa cần biết cho phần sau.
Chúng ta sẽ bắt đầu với hàm băm mã hóa, cơ bản cho cả ví và chính giao thức Bitcoin. Bạn sẽ khám phá các đặc điểm chính, các hàm cụ thể được sử dụng trong Bitcoin, và trong một chương kỹ thuật hơn, bạn sẽ học chi tiết về cách thức hoạt động của hàm băm hàng đầu: SHA256.
![CYP201](assets/fr/010.webp)

Tiếp theo, chúng ta sẽ thảo luận về cách thức hoạt động của các thuật toán chữ ký số mà bạn sử dụng hàng ngày để bảo vệ UTXOs của mình. Bitcoin sử dụng hai loại: ECDSA và giao thức Schnorr. Bạn sẽ học về các nguyên tắc toán học đằng sau các thuật toán này và cách chúng đảm bảo an toàn cho giao dịch.

![CYP201](assets/fr/021.webp)

Một khi chúng ta đã hiểu rõ về những yếu tố này của mã hóa, chúng ta cuối cùng sẽ chuyển sang trọng tâm của khóa học: ví xác định và phân cấp! Đầu tiên, có một phần dành riêng cho cụm từ ghi nhớ, những chuỗi từ 12 hoặc 24 từ giúp bạn tạo và khôi phục ví của mình. Bạn sẽ khám phá cách những từ này được tạo ra từ một nguồn entropy và làm thế nào chúng giúp việc sử dụng Bitcoin trở nên dễ dàng.

![CYP201](assets/fr/040.webp)
Khóa học sẽ tiếp tục với việc nghiên cứu về cụm từ BIP39, hạt giống (không nên nhầm lẫn với cụm từ ghi nhớ), mã chuỗi chủ, và khóa chủ. Chúng ta sẽ xem chi tiết những yếu tố này là gì, vai trò tương ứng của chúng, và cách chúng được tính toán.

![CYP201](assets/fr/045.webp)

Cuối cùng, từ khóa chủ, chúng ta sẽ khám phá cách các cặp khóa mật mã được tạo ra một cách có hệ thống và phân cấp đến các địa chỉ nhận.

![CYP201](assets/fr/056.webp)

Khóa học này sẽ giúp bạn sử dụng phần mềm ví của mình một cách tự tin, đồng thời nâng cao kỹ năng của bạn trong việc nhận diện và giảm thiểu rủi ro. Chuẩn bị trở thành một chuyên gia thực thụ về ví Bitcoin!

# Hàm Băm

<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Giới thiệu về Hàm Băm

<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Loại thuật toán mật mã đầu tiên được sử dụng trên Bitcoin bao gồm các hàm băm. Chúng đóng một vai trò thiết yếu ở các cấp độ khác nhau của giao thức, nhưng cũng trong ví Bitcoin. Hãy cùng khám phá xem hàm băm là gì và nó được sử dụng như thế nào trong Bitcoin.

### Định nghĩa và Nguyên tắc của Băm

Băm là quá trình biến đổi thông tin có độ dài tùy ý thành một mảnh thông tin có độ dài cố định thông qua một hàm băm mật mã. Nói cách khác, một hàm băm nhận đầu vào bất kỳ và chuyển đổi nó thành một dấu vân tay cố định, gọi là "băm".
Băm cũng đôi khi được gọi là "digest", "condensate", "condensed", hoặc "hashed".

Ví dụ, hàm băm SHA256 tạo ra một băm có độ dài cố định 256 bit. Vì vậy, nếu chúng ta sử dụng đầu vào "_PlanB_", một thông điệp có độ dài tùy ý, băm được tạo ra sẽ là dấu vân tay 256-bit sau đây:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

![CYP201](assets/fr/001.webp)

### Đặc điểm của Hàm Băm

Những hàm băm mật mã này có một số đặc điểm thiết yếu làm cho chúng đặc biệt hữu ích trong bối cảnh của Bitcoin và các hệ thống máy tính khác:

1. Khả năng không thể đảo ngược (hoặc kháng ảnh trước)
2. Kháng thay đổi (hiệu ứng tuyết lở)
3. Kháng va chạm
4. Kháng ảnh trước thứ hai

#### 1. Khả năng không thể đảo ngược (kháng ảnh trước):

Khả năng không thể đảo ngược có nghĩa là việc tính toán băm từ thông tin đầu vào là dễ dàng, nhưng phép tính ngược lại, tức là tìm thông tin đầu vào từ băm, là gần như không thể. Tính chất này làm cho hàm băm hoàn hảo cho việc tạo ra các dấu vân tay số duy nhất mà không làm lộ thông tin gốc. Đặc điểm này thường được gọi là một hàm một chiều hoặc "_hàm cửa bẫy_".

Trong ví dụ đã cho, việc thu được băm `24f1b9…` bằng cách biết đầu vào "_PlanB_" là đơn giản và nhanh chóng. Tuy nhiên, việc tìm ra thông điệp "_PlanB_" chỉ bằng cách biết `24f1b9…` là không thể.

![CYP201](assets/fr/002.webp)

Do đó, không thể tìm ra một ảnh trước $m$ cho một băm $h$ sao cho $h = \text{HASH}(m)$, nơi $\text{HASH}$ là một hàm băm mật mã.

#### 2. Kháng thay đổi (hiệu ứng tuyết lở)

Đặc điểm thứ hai là khả năng chống thay đổi, còn được biết đến với cái tên **hiệu ứng tuyết lở**. Đặc điểm này được quan sát thấy trong một hàm băm nếu một thay đổi nhỏ trong thông điệp đầu vào dẫn đến một sự thay đổi lớn trong kết quả băm đầu ra.
Nếu quay lại ví dụ của chúng ta với đầu vào "_PlanB_" và hàm SHA256, chúng ta đã thấy rằng băm được tạo ra như sau:

```text
24f1b93b68026bfc24f5c8265f287b4c940fb1664b0d75053589d7a4f821b688
```

Nếu chúng ta thực hiện một thay đổi rất nhỏ đối với đầu vào bằng cách sử dụng "_Planb_" lần này, thì việc đơn giản thay đổi từ chữ "B" viết hoa thành chữ "b" viết thường đã hoàn toàn thay đổi băm đầu ra SHA256:

```text
bb038b4503ac5d90e1205788b00f8f314583c5e22f72bec84b8735ba5a36df3f
```

![CYP201](assets/fr/003.webp)

Tính chất này đảm bảo rằng ngay cả một sự thay đổi nhỏ của thông điệp gốc cũng có thể được phát hiện ngay lập tức, vì nó không chỉ thay đổi một phần nhỏ của băm, mà là toàn bộ băm. Điều này có thể quan trọng trong nhiều lĩnh vực để xác minh tính toàn vẹn của thông điệp, phần mềm, hoặc thậm chí là các giao dịch Bitcoin.

#### 3. Khả năng Chống Va Chạm

Đặc điểm thứ ba là khả năng chống va chạm. Một hàm băm có khả năng chống va chạm nếu việc tìm ra 2 thông điệp khác nhau tạo ra cùng một kết quả băm từ hàm là điều không thể tính toán được. Một cách chính thức, việc tìm ra hai thông điệp riêng biệt $m_1$ và $m_2$ sao cho:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

![CYP201](assets/fr/004.webp)

Trên thực tế, việc tồn tại va chạm cho các hàm băm là điều không thể tránh khỏi về mặt toán học, bởi vì kích thước của đầu vào có thể lớn hơn kích thước của đầu ra. Điều này được biết đến như nguyên lý ngăn kéo của Dirichlet: nếu $n$ đối tượng được phân phối vào $m$ ngăn kéo, với $m < n$, thì ít nhất một ngăn kéo sẽ chứa hai hoặc nhiều đối tượng. Đối với một hàm băm, nguyên lý này áp dụng bởi vì số lượng thông điệp có thể là (gần như) vô hạn, trong khi số lượng băm có thể là hữu hạn ($2^{256}$ trong trường hợp của SHA256).

Do đó, đặc điểm này không có nghĩa là không có va chạm cho các hàm băm, mà là một hàm băm tốt làm cho khả năng tìm thấy một va chạm trở nên không đáng kể. Ví dụ, đặc điểm này không còn được xác minh trên các thuật toán SHA-0 và SHA-1, tiền nhiệm của SHA-2, vì đã tìm thấy va chạm. Các hàm này do đó hiện nay thường được khuyến cáo chống lại và thường được coi là lỗi thời.
Đối với một hàm băm $n$ bit, khả năng chống va chạm là theo cấp độ của $2^{\frac{n}{2}}$, phù hợp với cuộc tấn công sinh nhật. Ví dụ, đối với SHA256 ($n = 256$), độ phức tạp của việc tìm kiếm một va chạm là theo cấp độ của $2^{128}$ lần thử. Trên thực tế, điều này có nghĩa là nếu ai đó truyền $2^{128}$ thông điệp khác nhau qua hàm, người đó có khả năng tìm thấy một va chạm.

#### 4. Khả năng Chống Preimage Thứ Hai

Khả năng chống preimage thứ hai là một đặc điểm quan trọng khác của các hàm băm. Nó khẳng định rằng, cho một thông điệp $m_1$ và băm của nó $h$, việc tìm ra một thông điệp khác $m_2 \neq m_1$ sao cho:

$$
\text{HASH}(m_1) = \text{HASH}(m_2)
$$

Do đó, khả năng chống preimage thứ hai tương tự như khả năng chống va chạm, ngoại trừ ở đây, cuộc tấn công khó hơn bởi vì kẻ tấn công không thể tự do chọn $m_1$.

### Ứng Dụng của Hàm Băm trong Bitcoin

Hàm băm được sử dụng nhiều nhất trong Bitcoin là **SHA256** ("_Secure Hash Algorithm 256 bits"_). Được thiết kế vào đầu những năm 2000 bởi NSA và được chuẩn hóa bởi NIST, nó tạo ra một đầu ra băm 256-bit.

Hàm này được sử dụng trong nhiều khía cạnh của Bitcoin. Ở cấp độ giao thức, nó được sử dụng trong cơ chế Chứng minh Công việc, nơi nó được áp dụng băm kép để tìm kiếm một va chạm một phần giữa tiêu đề của một khối ứng viên, được tạo bởi một thợ mỏ, và mục tiêu khó khăn. Nếu va chạm một phần này được tìm thấy, khối ứng viên trở nên hợp lệ và có thể được thêm vào blockchain.

SHA256 cũng được sử dụng trong việc xây dựng một cây Merkle, đây là bộ tích lũy được sử dụng để ghi lại các giao dịch trong các khối. Cấu trúc này cũng được tìm thấy trong giao thức Utreexo, cho phép giảm kích thước của Bộ UTXO. Ngoài ra, với sự giới thiệu của Taproot vào năm 2021, SHA256 được khai thác trong MAST (_Merkelised Alternative Script Tree_), cho phép chỉ tiết lộ các điều kiện chi tiêu thực sự được sử dụng trong một script, mà không tiết lộ các lựa chọn khác có thể. Nó cũng được sử dụng trong việc tính toán các định danh giao dịch, trong truyền dẫn các gói tin qua mạng P2P, trong chữ ký điện tử... Cuối cùng, và đây là điều đặc biệt quan tâm trong khóa học này, SHA256 được sử dụng ở cấp độ ứng dụng để xây dựng ví Bitcoin và phát sinh địa chỉ.

Hầu hết thời gian, khi bạn gặp việc sử dụng SHA256 trên Bitcoin, thực tế nó sẽ là một băm kép SHA256, được ghi chú là "**HASH256**", chỉ đơn giản là áp dụng SHA256 hai lần liên tiếp:
HASH256(m) = SHA256(SHA256(m))

Thực hành băm kép này thêm một lớp bảo mật chống lại một số cuộc tấn công tiềm năng, mặc dù một SHA256 đơn lẻ ngày nay được coi là an toàn về mặt mật mã.

Một hàm băm khác có sẵn trong ngôn ngữ Script và được sử dụng để phát sinh địa chỉ nhận là hàm RIPEMD160. Hàm này tạo ra một băm 160-bit (do đó ngắn hơn SHA256). Nó thường được kết hợp với SHA256 để tạo thành hàm HASH160:

$$
\text{HASH160}(m) = \text{RIPEMD160}(\text{SHA256}(m))
$$

Sự kết hợp này được sử dụng để tạo ra các băm ngắn hơn, đặc biệt trong việc tạo ra một số địa chỉ Bitcoin đại diện cho các băm của khóa hoặc băm của script, cũng như để sản xuất dấu vân tay khóa.

Cuối cùng, chỉ ở cấp độ ứng dụng, hàm SHA512 đôi khi cũng được sử dụng, đóng vai trò gián tiếp trong việc phát sinh khóa cho ví. Hàm này rất giống với SHA256 trong cách hoạt động; cả hai đều thuộc về cùng một gia đình SHA2, nhưng SHA512 tạo ra, như tên gọi của nó, một băm 512-bit, so với 256 bit của SHA256. Chúng tôi sẽ chi tiết về việc sử dụng nó trong các chương sau.

Bây giờ bạn đã biết những kiến thức cơ bản thiết yếu về hàm băm cho những gì tiếp theo. Trong chương tiếp theo, tôi đề xuất khám phá chi tiết hơn về cơ chế hoạt động của hàm nằm ở trung tâm của Bitcoin: SHA256. Chúng ta sẽ phân tích nó để hiểu cách nó đạt được các đặc tính mà chúng ta đã mô tả ở đây. Chương tiếp theo khá dài và kỹ thuật, nhưng không cần thiết để theo dõi phần còn lại của khóa học. Vì vậy, nếu bạn gặp khó khăn trong việc hiểu nó, đừng lo lắng và chuyển thẳng sang chương tiếp theo, sẽ dễ tiếp cận hơn nhiều.

## Cơ Chế Hoạt Động Bên Trong của SHA256

<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>
Chúng ta đã biết rằng các hàm băm có những đặc tính quan trọng giúp chúng được sử dụng trong Bitcoin. Bây giờ, chúng ta sẽ xem xét cơ chế bên trong của các hàm băm này, làm cho chúng có những đặc tính đó, và để làm điều này, tôi đề xuất phân tích hoạt động của SHA256.

Các hàm SHA256 và SHA512 thuộc về cùng một gia đình SHA2. Cơ chế của chúng dựa trên một cấu trúc đặc biệt được gọi là **Merkle-Damgård construction**. RIPEMD160 cũng sử dụng loại cấu trúc tương tự.

Nhắc lại, chúng ta có một thông điệp với kích thước tùy ý làm đầu vào cho SHA256, và chúng ta sẽ đưa nó qua hàm để nhận được một băm 256-bit làm đầu ra.

### Tiền xử lý đầu vào

Để bắt đầu, chúng ta cần chuẩn bị thông điệp đầu vào $m$ sao cho nó có một chiều dài tiêu chuẩn là bội số của 512 bits. Bước này rất quan trọng cho sự hoạt động đúng đắn của thuật toán sau này.
Để làm điều này, chúng ta bắt đầu với bước thêm bit đệm. Chúng ta trước tiên thêm một bit phân cách `1` vào thông điệp, tiếp theo là một số lượng bit `0` nhất định. Số lượng bit `0` được thêm vào được tính toán sao cho tổng chiều dài của thông điệp sau khi thêm vào này là tương đương với 448 modulo 512. Như vậy, chiều dài $L$ của thông điệp với các bit đệm là bằng:

$$
L \equiv 448 \mod 512
$$

$\text{mod}$, cho modulo, là một phép toán toán học mà, giữa hai số nguyên, trả về phần dư của phép chia Euclid của số thứ nhất cho số thứ hai. Ví dụ: $16 \mod 5 = 1$. Đây là một phép toán được sử dụng rộng rãi trong mật mã học.

Ở đây, bước thêm đệm đảm bảo rằng, sau khi thêm 64 bit ở bước tiếp theo, tổng chiều dài của thông điệp được cân bằng sẽ là một bội số của 512 bits. Nếu thông điệp ban đầu có chiều dài $M$ bits, số ($N$) bit `0` cần được thêm vào là:

$$
N = (448 - (M + 1) \mod 512) \mod 512
$$

Ví dụ, nếu thông điệp ban đầu là 950 bits, phép tính sẽ như sau:

$$
\begin{align*}
M & = 950 \\
M + 1 & = 951 \\
(M + 1) \mod 512 & = 951 \mod 512 \\
& = 951 - 512 \cdot \left\lfloor \frac{951}{512} \right\rfloor \\
& = 951 - 512 \cdot 1 \\
& = 951 - 512 \\
& = 439 \\
\\
448 - (M + 1) \mod 512 & = 448 - 439 \\
& = 9 \\
\\
N & = (448 - (M + 1) \mod 512) \mod 512 \\
N & = 9 \mod 512 \\
& = 9
\end{align*}
$$

Như vậy, chúng ta sẽ có thêm 9 bit `0` ngoài bit phân cách `1`. Các bit đệm của chúng ta được thêm vào ngay sau thông điệp $M$ của chúng ta sẽ như sau:

```text
1000 0000 00
```

Sau khi thêm các bit đệm vào thông điệp $M$ của chúng ta, chúng ta cũng thêm một biểu diễn 64-bit của chiều dài gốc của thông điệp $M$, được biểu diễn bằng nhị phân. Điều này cho phép hàm băm nhạy cảm với thứ tự của các bit và chiều dài của thông điệp.
Nếu quay lại ví dụ của chúng ta với thông điệp ban đầu là 950 bit, chúng ta chuyển đổi số thập phân `950` thành nhị phân, thu được `1110 1101 10`. Chúng ta hoàn thiện số này bằng cách thêm các số `0` vào phía dưới để tạo thành tổng cộng 64 bit. Trong ví dụ của chúng ta, điều này cho ra:

```text
0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011 1011 0110
```

Kích thước đệm này được thêm vào theo sau phần đệm bit. Do đó, thông điệp sau quá trình tiền xử lý của chúng ta bao gồm ba phần:

1. Thông điệp gốc $M$;
2. Một bit `1` theo sau bởi nhiều bit `0` để tạo thành phần đệm bit;
3. Một biểu diễn 64-bit của độ dài của $M$ để tạo thành phần đệm với kích thước.

![CYP201](assets/fr/006.webp)

### Khởi Tạo Biến

SHA256 sử dụng tám biến trạng thái ban đầu, được ký hiệu từ $A$ đến $H$, mỗi biến có 32 bit. Các biến này được khởi tạo với các hằng số cụ thể, là phần phân số của căn bậc hai của tám số nguyên tố đầu tiên. Chúng ta sẽ sử dụng các giá trị này trong quá trình băm:

- $A = 0x6a09e667$
- $B = 0xbb67ae85$
- $C = 0x3c6ef372$
- $D = 0xa54ff53a$
- $E = 0x510e527f$
- $F = 0x9b05688c$
- $G = 0x1f83d9ab$
- $H = 0x5be0cd19$

SHA256 cũng sử dụng 64 hằng số khác, được ký hiệu từ $K_0$ đến $K_{63}$, là phần phân số của căn bậc ba của 64 số nguyên tố đầu tiên:

$$
K[0 \ldots 63] = \begin{pmatrix}
0x428a2f98, & 0x71374491, & 0xb5c0fbcf, & 0xe9b5dba5, \\
0x3956c25b, & 0x59f111f1, & 0x923f82a4, & 0xab1c5ed5, \\
0xd807aa98, & 0x12835b01, & 0x243185be, & 0x550c7dc3, \\
0x72be5d74, & 0x80deb1fe, & 0x9bdc06a7, & 0xc19bf174, \\
0xe49b69c1, & 0xefbe4786, & 0x0fc19dc6, & 0x240ca1cc, \\
0x2de92c6f, & 0x4a7484aa, & 0x5cb0a9dc, & 0x76f988da, \\
0x983e5152, & 0xa831c66d, & 0xb00327c8, & 0xbf597fc7, \\
0xc6e00bf3, & 0xd5a79147, & 0x06ca6351, & 0x14292967, \\
0x27b70a85, & 0x2e1b2138, & 0x4d2c6dfc, & 0x53380d13, \\
0x650a7354, & 0x766a0abb, & 0x81c2c92e, & 0x92722c85, \\
0xa2bfe8a1, & 0xa81a664b, & 0xc24b8b70, & 0xc76c51a3, \\
0xd192e819, & 0xd6990624, & 0xf40e3585, & 0x106aa070, \\
0x19a4c116, & 0x1e376c08, & 0x2748774c, & 0x34b0bcb5, \\
0x391c0cb3, & 0x4ed8aa4a, & 0x5b9cca4f, & 0x682e6ff3, \\
0x748f82ee, & 0x78a5636f, & 0x84c87814, & 0x8cc70208, \\
0x90befffa, & 0xa4506ceb, & 0xbef9a3f7, & 0xc67178f2
\end{pmatrix}
$$

### Phân Chia Đầu Vào

Bây giờ, sau khi đã cân bằng đầu vào, chúng ta sẽ tiếp tục với giai đoạn xử lý chính của thuật toán SHA256: hàm nén. Bước này rất quan trọng, vì nó chủ yếu mang lại cho hàm băm những tính chất mật mã mà chúng ta đã nghiên cứu trong chương trước.

Đầu tiên, chúng ta bắt đầu bằng cách chia thông điệp đã được cân bằng (kết quả của các bước tiền xử lý) thành nhiều khối $P$ mỗi khối 512 bit. Nếu thông điệp đã cân bằng của chúng ta có tổng kích thước là $n \times 512$ bit, chúng ta sẽ có $n$ khối, mỗi khối 512 bit. Mỗi khối 512 bit sẽ được xử lý riêng lẻ bởi hàm nén, bao gồm 64 vòng của các hoạt động liên tiếp. Hãy đặt tên cho các khối này là $P_1$, $P_2$, $P_3$...

### Các Phép Toán Logic

Trước khi khám phá hàm nén chi tiết, điều quan trọng là phải hiểu các phép toán logic cơ bản được sử dụng trong đó. Các phép toán này, dựa trên đại số Boolean, hoạt động ở cấp độ bit. Các phép toán logic cơ bản được sử dụng là:

- **Phép giao (AND)**: ký hiệu $\land$, tương ứng với "VÀ" logic.
- **Phép hợp (OR)**: ký hiệu $\lor$, tương ứng với "HOẶC" logic.
- **Phép phủ định (NOT)**: ký hiệu $\lnot$, tương ứng với "PHỦ ĐỊNH" logic.

Từ những phép toán cơ bản này, chúng ta có thể định nghĩa các phép toán phức tạp hơn, như "HOẶC loại trừ" (XOR) ký hiệu $\oplus$, được sử dụng rộng rãi trong mật mã học.
Mỗi phép toán logic có thể được biểu diễn bằng một bảng chân lý, chỉ ra kết quả cho tất cả các tổ hợp giá trị đầu vào nhị phân có thể có (hai toán hạng $p$ và $q$).
Đối với XOR ($\oplus$):

| $p$ | $q$ | $p \oplus q$ |
| --- | --- | ------------ |
| 0   | 0   | 0            |
| 0   | 1   | 1            |
| 1   | 0   | 1            |
| 1   | 1   | 0            |

Đối với AND ($\land$):

| $p$ | $q$ | $p \land q$ |
| --- | --- | ----------- |
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |
NOT ($\lnot p$) :

| $p$ | $\lnot p$ |
| --- | --------- |
| 0   | 1         |
| 1   | 0         |

Để hiểu về hoạt động của XOR ở cấp độ bit, hãy lấy một ví dụ. Nếu chúng ta có hai số nhị phân 6 bit:

- $a = 101100$
- $b = 001000$

Khi đó:

$$
a \oplus b = 101100 \oplus 001000 = 100100
$$

Bằng cách áp dụng XOR từng bit một:

| Vị Trí Bit | $a$ | $b$ | $a \oplus b$ |
| ---------- | --- | --- | ------------ |
| 1          | 1   | 0   | 1            |
| 2          | 0   | 0   | 0            |
| 3          | 1   | 1   | 0            |
| 4          | 1   | 0   | 1            |
| 5          | 0   | 0   | 0            |
| 6          | 0   | 0   | 0            |

Kết quả là $100100$.

Ngoài các phép toán logic, hàm nén còn sử dụng các phép toán dịch bit, sẽ đóng vai trò quan trọng trong việc lan truyền bit trong thuật toán.

Đầu tiên, có phép dịch phải logic, ký hiệu là $ShR_n(x)$, dịch tất cả các bit của $x$ sang phải $n$ vị trí, điền các bit trống ở bên trái bằng số không.

Ví dụ, với $x = 101100001$ (trên 9 bit) và $n = 4$:

$$
ShR_4(101100001) = 000010110
$$

Một cách hình ảnh, phép dịch phải có thể được thấy như sau:

![CYP201](assets/fr/007.webp)
Một phép toán khác được sử dụng trong SHA256 cho việc thao tác bit là phép xoay phải vòng tròn, ký hiệu là $RotR_n(x)$, dịch các bit của $x$ sang phải $n$ vị trí, chèn lại các bit đã dịch vào đầu chuỗi.
Ví dụ, với $x = 101100001$ (trên 9 bit) và $n = 4$:

$$
RotR_4(101100001) = 000110110
$$

Một cách hình ảnh, phép xoay phải vòng tròn có thể được thấy như sau:

![CYP201](assets/fr/008.webp)

### Hàm Nén

Giờ đây, khi chúng ta đã hiểu về các phép toán cơ bản, hãy xem xét chi tiết hàm nén SHA256.

Trong bước trước, chúng ta đã chia đầu vào thành nhiều phần 512-bit $P$. Đối với mỗi khối 512-bit $P$, chúng ta có:

- **Các từ thông điệp $W_i$**: cho $i$ từ 0 đến 63.
- **Các hằng số $K_i$**: cho $i$ từ 0 đến 63, được định nghĩa trong bước trước.
- **Các biến trạng thái $A, B, C, D, E, F, G, H$**: được khởi tạo với các giá trị từ bước trước.
  16 từ đầu tiên, $W_0$ đến $W_{15}$, được trích xuất trực tiếp từ khối 512-bit đã được xử lý $P$. Mỗi từ $W_i$ bao gồm 32 bit liên tiếp từ khối. Ví dụ, chúng ta lấy mảnh dữ liệu đầu vào đầu tiên của mình $P_1$, và chúng ta tiếp tục chia nó thành các mảnh nhỏ hơn 32-bit mà chúng ta gọi là từ.

48 từ tiếp theo ($W_{16}$ đến $W_{63}$) được tạo ra sử dụng công thức sau:

$$
W_i = W_{i-16} + \sigma_0(W_{i-15}) + W_{i-7} + \sigma_1(W_{i-2}) \mod 2^{32}
$$

Với:

- $\sigma_0(x) = RotR_7(x) \oplus RotR_{18}(x) \oplus ShR_3(x)$
- $\sigma_1(x) = RotR_{17}(x) \oplus RotR_{19}(x) \oplus ShR_{10}(x)$

Trong trường hợp này, $x$ bằng $W_{i-15}$ cho $\sigma_0(x)$ và $W_{i-2}$ cho $\sigma_1(x)$.

Một khi chúng ta đã xác định tất cả các từ $W_i$ cho mảnh 512-bit của mình, chúng ta có thể chuyển sang hàm nén, bao gồm việc thực hiện 64 vòng.

![CYP201](assets/fr/009.webp)
Đối với mỗi vòng $i$ từ 0 đến 63, chúng ta có ba loại đầu vào khác nhau. Đầu tiên, $W_i$ mà chúng ta vừa xác định, một phần bao gồm mảnh thông điệp của chúng ta $P_n$. Tiếp theo, 64 hằng số $K_i$. Cuối cùng, chúng ta sử dụng các biến trạng thái $A$, $B$, $C$, $D$, $E$, $F$, $G$, và $H$, sẽ phát triển trong suốt quá trình băm và được sửa đổi với mỗi hàm nén. Tuy nhiên, đối với mảnh đầu tiên $P_1$, chúng ta sử dụng các hằng số ban đầu đã được cung cấp trước đó.
Sau đó, chúng ta thực hiện các thao tác sau đây trên các đầu vào của mình:

- **Hàm $\Sigma_0$:**

$$
\Sigma_0(A) = RotR_2(A) \oplus RotR_{13}(A) \oplus RotR_{22}(A)
$$

- **Hàm $\Sigma_1$:**

$$
\Sigma_1(E) = RotR_6(E) \oplus RotR_{11}(E) \oplus RotR_{25}(E)
$$

- **Hàm $Ch$ ("_Chọn_"):**

$$
Ch(E, F, G) = (E \land F) \oplus (\lnot E \land G)
$$

- **Hàm $Maj$ ("_Đa số_"):**

$$
Maj(A, B, C) = (A \land B) \oplus (A \land C) \oplus (B \land C)
$$

Sau đó, chúng ta tính toán 2 biến tạm thời:

- $temp1$:

$$
temp1 = H + \Sigma_1(E) + Ch(E, F, G) + K_i + W_i \mod 2^{32}
$$

- $temp2$:

$$
temp2 = \Sigma_0(A) + Maj(A, B, C) \mod 2^{32}
$$

Tiếp theo, chúng ta cập nhật các biến trạng thái như sau:

$$
\begin{cases}
H = G \\
G = F \\
F = E \\
E = D + temp1 \mod 2^{32} \\
D = C \\
C = B \\
B = A \\
A = temp1 + temp2 \mod 2^{32}
\end{cases}
$$

Sơ đồ sau đây đại diện cho một vòng của hàm nén SHA256 như chúng tôi vừa mô tả:

![CYP201](assets/fr/010.webp)

- Các mũi tên chỉ dòng chảy của dữ liệu;
- Các hộp biểu diễn các phép toán được thực hiện;
- Các ký hiệu $+$ xung quanh biểu diễn phép cộng modulo $2^{32}$.

Chúng ta có thể quan sát thấy rằng, sau vòng này, các biến trạng thái mới $A$, $B$, $C$, $D$, $E$, $F$, $G$, và $H$ được tạo ra. Những biến mới này sẽ được sử dụng làm đầu vào cho vòng tiếp theo, từ đó tạo ra các biến mới $A$, $B$, $C$, $D$, $E$, $F$, $G$, và $H$ để sử dụng cho vòng tiếp theo. Quá trình này tiếp tục cho đến vòng thứ 64.

Sau 64 vòng, chúng ta cập nhật các giá trị ban đầu của các biến trạng thái bằng cách cộng chúng với các giá trị cuối cùng ở cuối vòng 64:

$$

\begin{cases}
A = A_{\text{initial}} + A \mod 2^{32} \\
B = B_{\text{initial}} + B \mod 2^{32} \\
C = C_{\text{initial}} + C \mod 2^{32} \\
D = D_{\text{initial}} + D \mod 2^{32} \\
E = E_{\text{initial}} + E \mod 2^{32} \\
F = F_{\text{initial}} + F \mod 2^{32} \\
G = G_{\text{initial}} + G \mod 2^{32} \\
H = H_{\text{initial}} + H \mod 2^{32}
\end{cases}

$$

Những giá trị mới này của $A$, $B$, $C$, $D$, $E$, $F$, $G$, và $H$ sẽ được sử dụng làm giá trị ban đầu cho khối tiếp theo, $P_2$. Đối với khối này $P_2$, chúng ta lặp lại quá trình nén tương tự với 64 vòng, sau đó chúng ta cập nhật các biến cho khối $P_3$, và cứ thế cho đến khối cuối cùng của đầu vào đã được cân bằng.

Sau khi xử lý tất cả các khối thông điệp, chúng ta nối các giá trị cuối cùng của các biến $A$, $B$, $C$, $D$, $E$, $F$, $G$, và $H$ để tạo thành băm 256-bit cuối cùng của hàm băm của chúng ta:


$$

\text{Băm} = A \Vert B \Vert C \Vert D \Vert E \Vert F \Vert G \Vert H

$$

Mỗi biến là một số nguyên 32-bit, vì vậy việc nối chúng luôn tạo ra một kết quả 256-bit, bất kể kích thước của đầu vào thông điệp cho hàm băm.

### Lý do của Tính Chất Mật Mã Học

Vậy, làm thế nào mà hàm này không thể đảo ngược, chống va chạm, và chống can thiệp?

Đối với tính chống can thiệp, điều này khá dễ hiểu. Có rất nhiều phép tính được thực hiện liên tiếp, phụ thuộc cả vào đầu vào và các hằng số, nên sự thay đổi nhỏ nhất của thông điệp ban đầu hoàn toàn thay đổi lộ trình được thực hiện, và do đó hoàn toàn thay đổi băm đầu ra. Đây là hiệu ứng được gọi là hiệu ứng tuyết lở. Tính chất này một phần được đảm bảo bởi việc trộn lẫn các trạng thái trung gian với các trạng thái ban đầu cho mỗi phần.
Tiếp theo, khi thảo luận về hàm băm mật mã, thuật ngữ "khả năng không đảo ngược" không thường được sử dụng. Thay vào đó, chúng ta nói về "kháng ảnh nguyên," chỉ rõ rằng đối với bất kỳ $y$ nào, việc tìm một $x$ sao cho $h(x) = y$ là khó khăn. Khả năng kháng ảnh nguyên này được đảm bảo bởi độ phức tạp đại số và tính phi tuyến mạnh mẽ của các phép toán thực hiện trong hàm nén, cũng như do mất mát một số thông tin trong quá trình đó. Ví dụ, đối với một kết quả của phép cộng modulo, có nhiều toán hạng có thể:
$$

3+2 \mod 10 = 5 \\
7+8 \mod 10 = 5 \\
5+10 \mod 10 = 5

$$

Trong ví dụ này, chỉ biết modulo được sử dụng (10) và kết quả (5), người ta không thể xác định chắc chắn những toán hạng nào được sử dụng trong phép cộng. Người ta nói rằng có nhiều công thức đồng dư modulo 10.

Đối với phép toán XOR, chúng ta đối mặt với vấn đề tương tự. Hãy nhớ bảng chân lý cho phép toán này: bất kỳ đầu ra 1-bit nào cũng có thể được xác định bởi hai cấu hình đầu vào khác nhau có cùng xác suất chính xác. Do đó, không thể xác định chắc chắn các toán hạng của một phép XOR chỉ bằng cách biết kết quả của nó. Nếu chúng ta tăng kích thước của các toán hạng XOR, số lượng đầu vào có thể biết chỉ với kết quả tăng lên theo cấp số nhân. Hơn nữa, XOR thường được sử dụng cùng với các phép toán cấp bit khác, như phép $\text{RotR}$, làm tăng thêm nhiều giải thích có thể có cho kết quả.

Hàm nén cũng sử dụng phép toán $\text{ShR}$. Phép toán này loại bỏ một phần thông tin cơ bản, sau đó không thể truy xuất lại được. Một lần nữa, không có phương tiện đại số nào để đảo ngược phép toán này. Tất cả các phép toán một chiều và mất mát thông tin này được sử dụng rất thường xuyên trong các hàm nén. Số lượng đầu vào có thể cho một đầu ra nhất định do đó gần như vô hạn, và mỗi nỗ lực tính toán đảo ngược sẽ dẫn đến các phương trình với số lượng ẩn rất lớn, sẽ tăng lên theo cấp số nhân ở mỗi bước.

Cuối cùng, đối với đặc tính kháng va chạm, có nhiều yếu tố đóng vai trò. Quá trình tiền xử lý thông điệp gốc đóng một vai trò thiết yếu. Nếu không có quá trình tiền xử lý này, việc tìm ra va chạm trên hàm có thể dễ dàng hơn. Mặc dù, về lý thuyết, va chạm tồn tại (do nguyên lý nhốt chim), cấu trúc của hàm băm, kết hợp với các tính chất đã nêu, làm cho xác suất tìm thấy một va chạm cực kỳ thấp.
Đối với một hàm băm để có khả năng kháng va chạm, điều cần thiết là:
- Đầu ra không dự đoán được: Bất kỳ tính dự đoán nào cũng có thể được khai thác để tìm va chạm nhanh hơn so với tấn công bằng lực lượng mù. Hàm đảm bảo rằng mỗi bit của đầu ra phụ thuộc vào đầu vào một cách không tầm thường. Nói cách khác, hàm được thiết kế sao cho mỗi bit của kết quả cuối cùng có xác suất độc lập là 0 hoặc 1, ngay cả khi sự độc lập này không tuyệt đối trong thực tế.
- Phân phối của các băm là giả ngẫu nhiên: Điều này đảm bảo rằng các băm được phân phối đều.
- Kích thước của băm là đáng kể: không gian kết quả càng lớn, việc tìm ra va chạm càng khó khăn.

Các nhà mật mã học thiết kế các hàm này bằng cách đánh giá các cuộc tấn công tốt nhất có thể để tìm va chạm, sau đó điều chỉnh các tham số để làm cho những cuộc tấn công này trở nên không hiệu quả.

### Cấu Trúc Merkle-Damgård

Cấu trúc của SHA256 dựa trên cấu trúc Merkle-Damgård, cho phép biến đổi một hàm nén thành một hàm băm có thể xử lý các thông điệp với độ dài tùy ý. Đây chính xác là những gì chúng ta đã thấy trong chương này.
Tuy nhiên, một số hàm băm cũ như SHA1 hoặc MD5, sử dụng cấu trúc đặc biệt này, lại dễ bị tấn công mở rộng độ dài. Đây là một kỹ thuật cho phép kẻ tấn công biết được băm của một thông điệp $M$ và độ dài của $M$ (mà không cần biết nội dung thông điệp) để tính toán băm của một thông điệp $M'$ được tạo ra bằng cách nối $M$ với nội dung bổ sung.
SHA256, mặc dù sử dụng cùng một loại cấu trúc, lại có khả năng lý thuyết chống lại loại tấn công này, không giống như SHA1 và MD5. Điều này có thể giải thích bí ẩn của việc băm kép được thực hiện xuyên suốt Bitcoin bởi Satoshi Nakamoto. Để tránh loại tấn công này, Satoshi có thể đã ưu tiên sử dụng SHA256 kép:


$$

\text{HASH256}(m) = \text{SHA256}(\text{SHA256}(m))

$$

Điều này tăng cường an ninh chống lại các cuộc tấn công tiềm năng liên quan đến cấu trúc Merkle-Damgård, nhưng nó không tăng cường an ninh của quá trình băm về khả năng chống va chạm. Hơn nữa, ngay cả khi SHA256 đã dễ bị loại tấn công này, nó cũng không gây ra ảnh hưởng nghiêm trọng, vì tất cả các trường hợp sử dụng hàm băm trong Bitcoin đều liên quan đến dữ liệu công khai. Tuy nhiên, cuộc tấn công mở rộng độ dài chỉ có thể hữu ích cho kẻ tấn công nếu dữ liệu băm là riêng tư và người dùng đã sử dụng hàm băm như một cơ chế xác thực cho dữ liệu này, tương tự như một MAC. Do đó, việc thực hiện băm kép vẫn là một bí ẩn trong thiết kế của Bitcoin.
Bây giờ chúng ta đã xem xét chi tiết về cách hoạt động của các hàm băm, đặc biệt là SHA256, được sử dụng rộng rãi trong Bitcoin, chúng ta sẽ tập trung cụ thể hơn vào các thuật toán dẫn xuất mật mã được sử dụng ở cấp độ ứng dụng, đặc biệt là để dẫn xuất các khóa cho ví của bạn.

## Các thuật toán được sử dụng để dẫn xuất
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Trong Bitcoin ở cấp độ ứng dụng, ngoài các hàm băm, các thuật toán dẫn xuất mật mã cũng được sử dụng để tạo ra dữ liệu an toàn từ các đầu vào ban đầu. Mặc dù các thuật toán này dựa trên hàm băm, chúng phục vụ các mục đích khác nhau, đặc biệt là về xác thực và tạo khóa. Các thuật toán này giữ lại một số đặc điểm của hàm băm, như không thể đảo ngược, kháng thay đổi, và kháng va chạm.

Trên ví Bitcoin, chủ yếu có 2 thuật toán dẫn xuất được sử dụng:
1. **HMAC (*Hash-based Message Authentication Code*)**
2. **PBKDF2 (*Password-Based Key Derivation Function 2*)**

Chúng ta sẽ cùng khám phá cách hoạt động và vai trò của mỗi thuật toán.

### HMAC-SHA512

HMAC là một thuật toán mật mã tính toán một mã xác thực dựa trên sự kết hợp của một hàm băm và một khóa bí mật. Bitcoin sử dụng HMAC-SHA512, biến thể của HMAC sử dụng hàm băm SHA512. Chúng ta đã thấy trong chương trước rằng SHA512 thuộc cùng một gia đình hàm băm với SHA256, nhưng nó tạo ra một đầu ra 512-bit.

Dưới đây là sơ đồ hoạt động chung của nó với $m$ là thông điệp đầu vào và $K$ là khóa bí mật:

![CYP201](assets/fr/011.webp)

Hãy nghiên cứu chi tiết hơn về những gì xảy ra trong hộp đen HMAC-SHA512 này. Hàm HMAC-SHA512 với:
- $m$: thông điệp kích thước tùy ý do người dùng chọn (đầu vào đầu tiên);
- $K$: khóa bí mật tùy ý do người dùng chọn (đầu vào thứ hai);
- $K'$: khóa $K$ được điều chỉnh theo kích thước $B$ của các khối hàm băm (1024 bit cho SHA512, hoặc 128 byte);
- $\text{SHA512}$: hàm băm SHA512;
- $\oplus$: phép toán XOR (hoặc độc quyền);
- $\Vert$: toán tử nối, liên kết các chuỗi bit lại với nhau từ đầu đến cuối;
- $\text{opad}$: hằng số bao gồm byte $0x5c$ lặp lại 128 lần
- $\text{ipad}$: hằng số bao gồm byte $0x36$ lặp lại 128 lần
Trước khi tính toán HMAC, cần phải làm cho khóa và các hằng số cân đối theo kích thước khối $B$. Ví dụ, nếu khóa $K$ ngắn hơn 128 byte, nó sẽ được thêm vào các số không để đạt được kích thước $B$. Nếu $K$ dài hơn 128 byte, nó sẽ được nén sử dụng SHA512, sau đó thêm vào các số không cho đến khi đạt được 128 byte. Như vậy, một khóa cân đối được gọi là $K'$ được thu được.
Giá trị của $\text{opad}$ và $\text{ipad}$ được thu được bằng cách lặp lại byte cơ bản của chúng ($0x5c$ cho $\text{opad}$, $0x36$ cho $\text{ipad}$) cho đến khi đạt được kích thước $B$. Như vậy, với $B = 128$ byte, chúng ta có:


$$

\text{opad} = \underbrace{0x5c5c\ldots5c}\_{128 \, \text{byte}}

$$

Sau khi tiền xử lý hoàn tất, thuật toán HMAC-SHA512 được định nghĩa bởi phương trình sau:


$$

\text {HMAC-SHA512}\_K(m) = \text{SHA512} \left( (K' \oplus \text{opad}) \parallel \text{SHA512} \left( (K' \oplus \text{ipad}) \parallel m \right) \right)

$$

Phương trình này được chia thành các bước sau:
1. XOR khóa điều chỉnh $K'$ với $\text{ipad}$ để thu được $\text{iKpad}$;
2. XOR khóa điều chỉnh $K'$ với $\text{opad}$ để thu được $\text{oKpad}$;
3. Nối $\text{iKpad}$ với thông điệp $m$.
4. Băm kết quả này với SHA512 để thu được băm trung gian $H_1$.
5. Nối $\text{oKpad}$ với $H_1$.
6. Băm kết quả này với SHA512 để thu được kết quả cuối cùng $H_2$.

Các bước này có thể được tóm tắt một cách sơ đồ như sau:

![CYP201](assets/fr/012.webp)

HMAC được sử dụng trong Bitcoin đáng chú ý cho việc phát sinh khóa trong ví HD (Hierarchical Deterministic) (chúng ta sẽ nói về điều này chi tiết hơn trong các chương tiếp theo) và là một thành phần của PBKDF2.

### PBKDF2

PBKDF2 (*Password-Based Key Derivation Function 2*) là một thuật toán phát sinh khóa dựa trên mật khẩu được thiết kế để tăng cường bảo mật cho mật khẩu. Thuật toán áp dụng một hàm giả ngẫu nhiên (ở đây là HMAC-SHA512) trên một mật khẩu và một "salt" mã hóa, sau đó lặp lại thao tác này một số lần nhất định để sản xuất ra một khóa đầu ra.

Trong Bitcoin, PBKDF2 được sử dụng để tạo ra hạt giống của một ví HD từ một cụm từ ghi nhớ và một cụm từ bí mật (nhưng chúng ta sẽ nói về điều này chi tiết hơn trong các chương tiếp theo).

Quy trình PBKDF2 như sau, với:
- $m$: cụm từ ghi nhớ của người dùng;
- $s$: cụm từ bí mật tùy chọn để tăng cường bảo mật (trường trống nếu không có cụm từ bí mật);
- $n$: số lần lặp của hàm, trong trường hợp của chúng ta, là 2048.
Hàm PBKDF2 được định nghĩa theo cách lặp đi lặp lại. Mỗi lần lặp lấy kết quả của lần trước, đưa qua HMAC-SHA512, và kết hợp các kết quả liên tiếp để tạo ra khóa cuối cùng:
$$

\text{PBKDF2}(m, s) = \text{HMAC-SHA512}^{2048}(m, s)

$$

Một cách biểu đồ, PBKDF2 có thể được mô tả như sau:

![CYP201](assets/fr/013.webp)

Trong chương này, chúng ta đã khám phá các hàm HMAC-SHA512 và PBKDF2, sử dụng các hàm băm để đảm bảo tính toàn vẹn và an ninh của việc tạo khóa trong giao thức Bitcoin. Trong phần tiếp theo, chúng ta sẽ tìm hiểu về chữ ký số, một phương pháp mật mã khác được sử dụng rộng rãi trong Bitcoin.

# Chữ Ký Số
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Chữ Ký Số và Đường Cong Elliptic
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Phương pháp mật mã thứ hai được sử dụng trong Bitcoin liên quan đến các thuật toán chữ ký số. Hãy khám phá điều này bao gồm những gì và cách hoạt động của nó.

### Bitcoin, UTXOs và Điều Kiện Chi Tiêu

Thuật ngữ "*ví*" trong Bitcoin có thể gây nhầm lẫn cho người mới bắt đầu. Thực tế, cái được gọi là ví Bitcoin là phần mềm không trực tiếp giữ bitcoin của bạn, không giống như một ví vật lý có thể giữ tiền xu hoặc tiền giấy. Bitcoin chỉ đơn giản là đơn vị tài khoản. Đơn vị tài khoản này được biểu diễn bởi **UTXO** (*Unspent Transaction Outputs*), là các đầu ra giao dịch chưa được chi tiêu. Nếu những đầu ra này chưa được chi tiêu, điều đó có nghĩa là chúng thuộc về một người dùng. UTXOs, theo một cách nào đó, là các mảnh của bitcoin, có kích thước biến đổi, thuộc về một người dùng.

Giao thức Bitcoin là phân tán và hoạt động mà không cần một cơ quan trung ương. Do đó, nó không giống như hồ sơ ngân hàng truyền thống, nơi các euro thuộc về bạn chỉ đơn giản được liên kết với danh tính cá nhân của bạn. Trên Bitcoin, UTXOs của bạn thuộc về bạn vì chúng được bảo vệ bởi các điều kiện chi tiêu được chỉ định trong ngôn ngữ Script. Để đơn giản hóa, có hai loại script: script khóa (*scriptPubKey*), bảo vệ một UTXO, và script mở khóa (*scriptSig*), cho phép mở khóa một UTXO và do đó chi tiêu các đơn vị bitcoin mà nó đại diện.
Hoạt động ban đầu của Bitcoin với script P2PK liên quan đến việc sử dụng một khóa công khai để khóa quỹ, chỉ định trong một *scriptPubKey* rằng người muốn chi tiêu UTXO này phải cung cấp một chữ ký hợp lệ với khóa riêng tương ứng với khóa công khai này. Để mở khóa UTXO này, do đó, cần phải cung cấp một chữ ký hợp lệ trong *scriptSig*. Như tên của chúng, khóa công khai được biết đến bởi tất cả mọi người vì nó được phát sóng trên blockchain, trong khi khóa riêng chỉ được biết đến bởi chủ sở hữu hợp pháp của quỹ.
Đây là hoạt động cơ bản của Bitcoin, nhưng theo thời gian, hoạt động này trở nên phức tạp hơn. Đầu tiên, Satoshi cũng giới thiệu script P2PKH, sử dụng một địa chỉ nhận trong *scriptPubKey*, đại diện cho hash của khóa công khai. Sau đó, hệ thống trở nên phức tạp hơn nữa với sự xuất hiện của SegWit và sau đó là Taproot. Tuy nhiên, nguyên tắc chung vẫn cơ bản giống nhau: một khóa công khai hoặc một biểu diễn của khóa này được sử dụng để khóa UTXOs, và một khóa riêng tương ứng được yêu cầu để mở khóa chúng và do đó chi tiêu chúng.
Người dùng muốn thực hiện giao dịch Bitcoin do đó cần tạo một chữ ký số bằng khóa riêng của mình trên giao dịch đó. Chữ ký này có thể được các thành viên khác trong mạng xác minh. Nếu chữ ký hợp lệ, điều này có nghĩa là người khởi xướng giao dịch thực sự là chủ sở hữu của khóa riêng, và do đó là chủ sở hữu của số bitcoin mà họ muốn chi tiêu. Các người dùng khác sau đó có thể chấp nhận và lan truyền giao dịch.

Kết quả là, người dùng sở hữu bitcoin được khóa bằng khóa công khai phải tìm cách lưu trữ an toàn cái cho phép mở khóa quỹ của họ: khóa riêng. Một ví Bitcoin chính xác là một thiết bị sẽ cho phép bạn dễ dàng giữ tất cả các khóa của mình mà không cho người khác truy cập vào chúng. Do đó, nó giống như một móc khóa hơn là một ví.

Mối liên kết toán học giữa khóa công khai và khóa riêng, cũng như khả năng thực hiện chữ ký để chứng minh sở hữu khóa riêng mà không tiết lộ nó, được thực hiện bởi thuật toán chữ ký số. Trong giao thức Bitcoin, 2 thuật toán chữ ký được sử dụng: **ECDSA** (*Elliptic Curve Digital Signature Algorithm*) và **Schnorr signature scheme**. ECDSA là giao thức chữ ký số được sử dụng trong Bitcoin từ những ngày đầu. Schnorr là mới hơn trong Bitcoin, khi nó được giới thiệu vào tháng 11 năm 2021 với bản cập nhật Taproot.
Hai thuật toán này khá giống nhau về cơ chế của chúng. Cả hai đều dựa trên mật mã học đường cong elliptic. Sự khác biệt lớn giữa hai giao thức này nằm ở cấu trúc của chữ ký và một số tính chất toán học cụ thể. Chúng ta sẽ do đó nghiên cứu cách hoạt động của các thuật toán này, bắt đầu với cái cũ nhất: ECDSA.
### Mật mã học đường cong Elliptic

Mật mã học đường cong Elliptic (ECC) là một tập hợp các thuật toán sử dụng một đường cong elliptic với các tính chất toán học và hình học đa dạng của nó cho mục đích mật mã. Sự an toàn của các thuật toán này dựa trên sự khó khăn của bài toán logarit rời rạc trên đường cong elliptic. Đường cong elliptic đặc biệt được sử dụng cho trao đổi khóa, mã hóa không đối xứng, hoặc tạo chữ ký số.

Một tính chất quan trọng của các đường cong này là chúng đối xứng qua trục x. Do đó, bất kỳ đường thẳng không dọc nào cắt đường cong tại hai điểm riêng biệt sẽ luôn gặp đường cong tại một điểm thứ ba. Hơn nữa, bất kỳ tiếp tuyến nào của đường cong tại một điểm không đơn lẻ sẽ gặp đường cong tại một điểm khác. Những tính chất này sẽ hữu ích cho việc định nghĩa các phép toán trên đường cong.

Dưới đây là biểu diễn của một đường cong elliptic trên trường số thực:

![CYP201](assets/fr/014.webp)

Mỗi đường cong elliptic được xác định bởi một phương trình dạng:


$$

y^2 = x^3 + ax + b

$$

### secp256k1

Để sử dụng ECDSA hoặc Schnorr, người ta phải chọn các tham số của đường cong elliptic, tức là giá trị của $a$ và $b$ trong phương trình đường cong. Có các tiêu chuẩn khác nhau của đường cong elliptic được coi là an toàn về mặt mật mã. Tiêu chuẩn được biết đến nhiều nhất là đường cong *secp256r1*, được xác định và khuyến nghị bởi NIST (*Viện Tiêu chuẩn và Công nghệ Quốc gia*).

Tuy nhiên, Satoshi Nakamoto, người sáng lập Bitcoin, đã chọn không sử dụng đường cong này. Lý do cho sự lựa chọn này không rõ ràng, nhưng một số người tin rằng ông ấy đã muốn tìm một lựa chọn thay thế vì các tham số của đường cong này có thể chứa một cửa hậu. Thay vào đó, giao thức Bitcoin sử dụng tiêu chuẩn đường cong ***secp256k1***. Đường cong này được xác định bởi các tham số $a = 0$ và $b = 7$. Phương trình của nó do đó là:


$$

y^2 = x^3 + 7

$$

Biểu diễn đồ họa của nó trên trường số thực trông như thế này:
![CYP201](assets/fr/015.webp)
Tuy nhiên, trong mật mã học, chúng ta làm việc với các tập hợp số hữu hạn. Cụ thể hơn, chúng ta làm việc trên trường hữu hạn $\mathbb{F}_p$, đó là trường của các số nguyên modulo một số nguyên tố $p$.
**Định nghĩa**: Một số nguyên tố là một số nguyên tự nhiên lớn hơn hoặc bằng 2 chỉ có hai ước số nguyên dương phân biệt: 1 và chính nó. Ví dụ, số 7 là một số nguyên tố vì nó chỉ có thể chia hết cho 1 và 7. Ngược lại, số 8 không phải là số nguyên tố vì nó có thể chia hết cho 1, 2, 4 và 8.
Trong Bitcoin, số nguyên tố $p$ được sử dụng để định nghĩa trường hữu hạn là rất lớn. Nó được chọn theo cách mà thứ tự của trường (tức là số lượng phần tử trong $\mathbb{F}_p$) đủ lớn để đảm bảo an ninh mật mã.

Số nguyên tố $p$ được sử dụng là:

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

Trong ký hiệu thập phân, điều này tương ứng với:


$$

p = 2^{256} - 2^{32} - 977

$$

Do đó, phương trình của đường cong elliptic của chúng ta thực sự là:


$$

y^2 \equiv x^3 + 7 \mod p

$$

Xét đường cong này được định nghĩa trên trường hữu hạn $\mathbb{F}_p$, nó không còn giống một đường cong liên tục nữa mà giống như một tập hợp rời rạc các điểm. Ví dụ, đây là hình dạng của đường cong được sử dụng trong Bitcoin với $p = 17$ rất nhỏ:

![CYP201](assets/fr/016.webp)

Trong ví dụ này, tôi đã cố ý giới hạn trường hữu hạn là $p = 17$ vì mục đích giáo dục, nhưng người ta phải tưởng tượng rằng cái được sử dụng trong Bitcoin lớn hơn rất nhiều, gần như $2^{256}$.

Chúng ta sử dụng trường hữu hạn của các số nguyên modulo $p$ để đảm bảo độ chính xác của các phép toán trên đường cong. Thực tế, đường cong elliptic trên trường số thực phải chịu sự không chính xác do lỗi làm tròn trong các phép tính toán. Nếu thực hiện nhiều phép toán trên đường cong, những lỗi này tích tụ lại và kết quả cuối cùng có thể không chính xác hoặc khó tái tạo. Việc sử dụng độc quyền các số nguyên dương đảm bảo độ chính xác hoàn hảo của các phép tính và do đó khả năng tái tạo kết quả.

Toán học của đường cong elliptic trên trường hữu hạn tương đương với trường số thực, với sự điều chỉnh là tất cả các phép toán được thực hiện modulo $p$. Để giải thích đơn giản, chúng tôi sẽ tiếp tục trong các chương sau đây minh họa các khái niệm sử dụng một đường cong được định nghĩa trên số thực, trong khi nhớ rằng, trên thực tế, đường cong được định nghĩa trên một trường hữu hạn.

Nếu bạn muốn tìm hiểu thêm về nền tảng toán học của mật mã học hiện đại, tôi cũng khuyên bạn tham khảo khóa học khác trên Plan ₿ Network:

https://planb.network/courses/cyp302

## Tính Khóa Công Khai từ Khóa Riêng
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>
Như đã thấy trước đây, các thuật toán chữ ký số trên Bitcoin dựa trên một cặp khóa riêng và khóa công khai có liên kết toán học với nhau. Hãy cùng khám phá liên kết toán học này là gì và chúng được tạo ra như thế nào.

### Khóa Riêng

Khóa riêng đơn giản chỉ là một số ngẫu nhiên hoặc giả ngẫu nhiên. Trong trường hợp của Bitcoin, số này có kích thước 256 bit. Số lượng khả năng cho một khóa riêng Bitcoin do đó lý thuyết là $2^{256}$.
**Lưu ý**: Một "số ngẫu nhiên giả" là một số có các đặc tính gần giống với số ngẫu nhiên thực sự nhưng được tạo ra bởi một thuật toán xác định.
Tuy nhiên, trên thực tế, chỉ có $n$ điểm phân biệt trên đường cong elliptic secp256k1, nơi $n$ là bậc của điểm sinh $G$ của đường cong. Chúng ta sẽ thấy sau đây số này tương ứng với gì, nhưng chỉ cần nhớ rằng một khóa riêng hợp lệ là một số nguyên từ $1$ đến $n-1$, biết rằng $n$ là một số gần với nhưng hơi nhỏ hơn $2^{256}$. Do đó, có một số số 256-bit không hợp lệ để trở thành khóa riêng trong Bitcoin, cụ thể, tất cả các số từ $n$ đến $2^{256}$. Nếu việc tạo số ngẫu nhiên (khóa riêng) tạo ra một giá trị $k$ sao cho $k \geq n$, nó được coi là không hợp lệ, và một giá trị ngẫu nhiên mới phải được tạo ra.

Số lượng khả năng cho một khóa riêng Bitcoin do đó là khoảng $n$, là một số gần với $1.158 \times 10^{77}$. Số này lớn đến mức nếu bạn chọn một khóa riêng một cách ngẫu nhiên, thì gần như không thể thống kê chạm vào khóa riêng của người dùng khác. Để bạn có cái nhìn về quy mô, số lượng khóa riêng có thể có trên Bitcoin gần bằng với số lượng ước lượng các nguyên tử trong vũ trụ quan sát được.

Như chúng ta sẽ thấy trong các chương tiếp theo, ngày nay, đa số khóa riêng được sử dụng trên Bitcoin không được tạo ra một cách ngẫu nhiên mà là kết quả của sự phái sinh xác định từ một cụm từ ghi nhớ, bản thân nó cũng giả ngẫu nhiên (đây là cụm từ nổi tiếng gồm 12 hoặc 24 từ). Thông tin này không thay đổi gì cho việc sử dụng các thuật toán chữ ký như ECDSA, nhưng nó giúp tập trung lại việc phổ biến về Bitcoin.

Trong phần giải thích tiếp theo, khóa riêng sẽ được ký hiệu bằng chữ cái thường $k$.

### Khóa Công Khai
Khóa công khai là một điểm trên đường cong elliptic, được ký hiệu bằng chữ cái in hoa $K$, và được tính toán từ khóa riêng $k$. Điểm này $K$ được biểu diễn bởi một cặp tọa độ $(x, y)$ trên đường cong elliptic, mỗi tọa độ là một số nguyên modulo $p$, số nguyên tố xác định trường hữu hạn $\mathbb{F}_p$.
Trên thực tế, một khóa công khai không nén được biểu diễn bởi 512 bit (hoặc 64 byte), tương ứng với hai số 256-bit ($x$ và $y$) đặt liền kề nhau. Những số này là hoành độ ($x$) và tung độ ($y$) của điểm của chúng ta trên secp256k1. Nếu chúng ta thêm tiền tố, khóa công khai tổng cộng 520 bit.

Tuy nhiên, cũng có thể biểu diễn khóa công khai dưới dạng nén chỉ sử dụng 33 byte (264 bit) bằng cách chỉ giữ lại hoành độ $x$ của điểm của chúng ta trên đường cong và một byte chỉ ra tính chẵn lẻ của $y$. Đây là cái được gọi là khóa công khai nén. Tôi sẽ nói thêm về điều này trong những chương cuối của khóa học này. Nhưng điều bạn cần nhớ là khóa công khai $K$ là một điểm được mô tả bởi $x$ và $y$.

Để tính toán điểm $K$ tương ứng với khóa công khai của chúng ta, chúng ta sử dụng phép nhân vô hướng trên đường cong elliptic, được định nghĩa là phép cộng lặp lại ($k$ lần) của điểm sinh $G$:


$$

K = k \cdot G

$$

nơi:
- $k$ là khóa riêng (một số nguyên ngẫu nhiên từ $1$ đến $n-1$);
- $G$ là điểm sinh của đường cong elliptic được sử dụng bởi tất cả các thành viên của mạng lưới Bitcoin; - $\cdot$ đại diện cho phép nhân vô hướng trên đường cong elliptic, tương đương với việc cộng điểm $G$ vào chính nó $k$ lần.

Việc điểm $G$ này chung cho tất cả các khóa công khai trên Bitcoin cho phép chúng ta chắc chắn rằng cùng một khóa riêng $k$ sẽ luôn cho chúng ta cùng một khóa công khai $K$:

![CYP201](assets/fr/017.webp)

Đặc điểm chính của phép toán này là nó là một hàm một chiều. Việc tính toán khóa công khai $K$ khi biết khóa riêng $k$ và điểm sinh $G$ là dễ dàng, nhưng việc tính toán khóa riêng $k$ khi chỉ biết khóa công khai $K$ và điểm sinh $G$ là gần như không thể. Tìm $k$ từ $K$ và $G$ tương đương với việc giải quyết vấn đề logarit rời rạc trên đường cong elliptic, một vấn đề toán học khó mà không có thuật toán hiệu quả nào được biết đến. Ngay cả những máy tính mạnh mẽ nhất hiện nay cũng không thể giải quyết vấn đề này trong một khoảng thời gian hợp lý.
### Phép Cộng và Nhân Đôi Điểm trên Đường Cong Elliptic

Khái niệm về phép cộng trên đường cong elliptic được định nghĩa một cách hình học. Nếu chúng ta có hai điểm $P$ và $Q$ trên đường cong, phép toán $P + Q$ được tính bằng cách vẽ một đường thẳng đi qua $P$ và $Q$. Đường thẳng này sẽ nhất thiết cắt đường cong tại một điểm thứ ba $R'$. Sau đó, chúng ta lấy ảnh phản chiếu của điểm này qua trục x để thu được điểm $R$, là kết quả của phép cộng:


$$

P + Q = R

$$

Một cách hình ảnh, điều này có thể được biểu diễn như sau:

![CYP201](assets/fr/019.webp)

Đối với phép nhân đôi một điểm, tức là phép toán $P + P$, chúng ta vẽ tiếp tuyến của đường cong tại điểm $P$. Tiếp tuyến này cắt đường cong tại một điểm khác $S'$. Sau đó, chúng ta lấy ảnh phản chiếu của điểm này qua trục x để thu được điểm $S$, là kết quả của phép nhân đôi:


$$

2P = S

$$

Một cách hình ảnh, điều này được thể hiện như sau:

![CYP201](assets/fr/020.webp)

Bằng cách sử dụng các phép toán cộng và nhân đôi này, chúng ta có thể thực hiện phép nhân vô hướng của một điểm với một số nguyên $k$, ký hiệu là $kP$, bằng cách thực hiện lặp lại phép nhân đôi và cộng.

Ví dụ, giả sử chúng ta đã chọn một khóa riêng $k = 4$. Để tính toán khóa công khai tương ứng, chúng ta thực hiện:


$$

K = k \cdot G = 4G

$$

Một cách hình ảnh, điều này tương ứng với việc thực hiện một loạt các phép cộng và nhân đôi:
- Tính $2G$ bằng cách nhân đôi $G$.
- Tính $4G$ bằng cách nhân đôi $2G$.

![CYP201](assets/fr/021.webp)

Nếu chúng ta muốn, ví dụ, tính toán điểm $3G$, trước tiên chúng ta phải tính điểm $2G$ bằng cách nhân đôi điểm $G$, sau đó cộng $G$ và $2G$. Để cộng $G$ và $2G$, chỉ cần vẽ đường thẳng nối hai điểm này, lấy điểm duy nhất $-3G$ tại giao điểm giữa đường thẳng này và đường cong elliptic, và sau đó xác định $3G$ là điểm đối diện của $-3G$.

Chúng ta sẽ có:


$$

G + G = 2G

$$


$$

2G + G = 3G

$$

Một cách hình ảnh, điều này sẽ được biểu diễn như sau:
![CYP201](assets/fr/022.webp)
### Hàm Một Chiều

Nhờ những phép toán này, chúng ta có thể hiểu tại sao việc suy ra khóa công khai từ khóa riêng là dễ dàng, nhưng ngược lại thì gần như không thể.

Hãy quay lại với ví dụ đơn giản của chúng ta. Với khóa riêng $k = 4$. Để tính toán khóa công khai liên quan, chúng ta thực hiện:

$$
K = k \cdot G = 4G
$$

Chúng ta đã có thể dễ dàng tính toán được khóa công khai $K$ bằng cách biết $k$ và $G$.

Bây giờ, nếu ai đó chỉ biết khóa công khai $K$, họ sẽ đối mặt với vấn đề logarit rời rạc: tìm $k$ sao cho $K = k \cdot G$. Vấn đề này được coi là khó vì không có thuật toán hiệu quả nào để giải quyết nó trên các đường cong elliptic. Điều này đảm bảo an ninh cho các thuật toán ECDSA và Schnorr.

Tất nhiên, trong ví dụ đơn giản này với $k = 4$, sẽ có thể tìm ra $k$ thông qua thử và sai, vì số lượng khả năng là thấp. Tuy nhiên, trên thực tế đối với Bitcoin, $k$ là một số nguyên 256-bit, làm cho số lượng khả năng lớn đến mức không thể tưởng tượng được (khoảng $1.158 \times 10^{77}$). Do đó, việc tìm $k$ bằng cách sử dụng lực lượng brút-fô là không khả thi.

## Ký bằng Khóa Riêng

<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Bây giờ bạn đã biết cách suy ra khóa công khai từ khóa riêng, bạn đã có thể nhận bitcoin bằng cách sử dụng cặp khóa này như một điều kiện chi tiêu. Nhưng làm thế nào để chi tiêu chúng? Để chi tiêu bitcoin, bạn sẽ cần phải mở khóa _scriptPubKey_ gắn với UTXO của mình để chứng minh rằng bạn thực sự là chủ sở hữu hợp pháp của nó. Để làm điều này, bạn phải tạo ra một chữ ký $s$ phù hợp với khóa công khai $K$ hiện diện trong _scriptPubKey_ sử dụng khóa riêng $k$ đã được sử dụng ban đầu để tính toán $K$. Chữ ký số do đó là bằng chứng không thể chối cãi rằng bạn đang sở hữu khóa riêng liên kết với khóa công khai bạn tuyên bố.

### Các Tham Số Đường Cong Elliptic

Để thực hiện một chữ ký số, tất cả các bên tham gia đầu tiên phải đồng ý với các tham số của đường cong elliptic được sử dụng. Trong trường hợp của Bitcoin, các tham số của **secp256k1** như sau:

Trường hữu hạn $\mathbb{Z}_p$ được xác định bởi:

$$
p = 2^{256} - 2^{32} - 977
$$

```text
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
```

$p$ là một số nguyên tố rất lớn, nhỏ hơn một chút so với $2^{256}$.

Đường cong elliptic $y^2 = x^3 + ax + b$ trên $\mathbb{Z}_p$ được xác định bởi:

$$
a = 0, \quad b = 7
$$

Điểm sinh hoặc điểm gốc $G$:

```text
G = 0x0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
```

Con số này là dạng nén chỉ đưa ra hoành độ của điểm $G$. Tiền tố `02` ở đầu xác định giá trị nào trong hai giá trị có hoành độ $x$ này được sử dụng làm điểm sinh.
Số thứ tự $n$ của $G$ (số điểm tồn tại) và hệ số nhỏ $h$:

```text
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
```

$n$ là một số rất lớn, nhỏ hơn $p$ một chút.

$$
h=1
$$

$h$ là hệ số nhóm con. Tôi sẽ không giải thích chi tiết về điều này ở đây, vì nó khá phức tạp, và trong trường hợp của Bitcoin, chúng ta không cần phải xem xét đến nó vì nó bằng $1$.

Tất cả thông tin này đều công khai và được tất cả các bên tham gia biết đến. Nhờ vậy, người dùng có thể tạo chữ ký số và xác minh nó.

### Chữ ký với ECDSA

Thuật toán ECDSA cho phép người dùng ký một thông điệp bằng khóa riêng của họ, theo cách mà bất kỳ ai biết khóa công khai tương ứng có thể xác minh tính hợp lệ của chữ ký, mà không bao giờ tiết lộ khóa riêng. Trong bối cảnh của Bitcoin, thông điệp được ký phụ thuộc vào _sighash_ được người dùng chọn. Chính _sighash_ này sẽ quyết định những phần nào của giao dịch được bao phủ bởi chữ ký. Tôi sẽ nói thêm về điều này trong chương tiếp theo.

Dưới đây là các bước để tạo một chữ ký ECDSA:

Đầu tiên, chúng ta tính băm ($e$) của thông điệp cần được ký. Thông điệp $m$ do đó được đưa qua một hàm băm mật mã, thường là SHA256 hoặc double SHA256 trong trường hợp của Bitcoin:

$$
e = \text{HASH}(m)
$$

Tiếp theo, chúng ta tính một nonce. Trong mật mã, nonce đơn giản chỉ là một số được tạo ra một cách ngẫu nhiên hoặc giả ngẫu nhiên và chỉ được sử dụng một lần. Nói cách khác, mỗi lần một chữ ký số mới được tạo với cặp khóa này, sẽ rất quan trọng khi sử dụng một nonce khác nhau, nếu không, nó sẽ làm suy yếu bảo mật của khóa riêng. Do đó, chỉ cần xác định một số nguyên ngẫu nhiên và duy nhất $r$ sao cho $1 \leq r \leq n-1$, nơi $n$ là thứ tự của điểm sinh $G$ của đường cong elliptic.

Sau đó, chúng ta sẽ tính điểm $R$ trên đường cong elliptic với tọa độ $(x_R, y_R)$ sao cho:

$$
R = r \cdot G
$$

Chúng ta trích xuất giá trị của hoành độ của điểm $R$ ($x_R$). Giá trị này đại diện cho phần đầu tiên của chữ ký. Và cuối cùng, chúng ta tính phần thứ hai của chữ ký $s$ theo cách này:

$$
s = r^{-1} \left( e + k \cdot x_R \right) \mod n
$$

trong đó:

- $r^{-1}$ là nghịch đảo mô-đun của $r$ modulo $n$, tức là, một số nguyên sao cho $r \cdot r^{-1} \equiv 1 \mod n$;
- $k$ là khóa riêng của người dùng;
- $e$ là băm của thông điệp;
- $n$ là thứ tự của điểm sinh $G$ của đường cong elliptic.

Chữ ký sau đó đơn giản là sự nối tiếp của $x_R$ và $s$:

$$
\text{SIG} = x_R \Vert s
$$

### Xác minh Chữ ký ECDSA

Để xác minh một chữ ký $(x_R, s)$, bất kỳ ai biết khóa công khai $K$ và các tham số của đường cong elliptic có thể tiến hành theo cách này:
Đầu tiên, xác minh rằng $x_R$ và $s$ nằm trong khoảng $[1, n-1]$. Điều này đảm bảo rằng chữ ký tuân thủ các ràng buộc toán học của nhóm elliptic. Nếu không phải như vậy, người xác minh ngay lập tức từ chối chữ ký vì không hợp lệ.
Sau đó, tính băm của thông điệp:

$$
e = \text{HASH}(m)
$$

Tính nghịch đảo mô-đun của $s$ theo mô-đun $n$:

$$
s^{-1} \mod n
$$

Tính hai giá trị vô hướng $u_1$ và $u_2$ theo cách này:

$$
\begin{align*}
u_1 &= e \cdot s^{-1} \mod n \\
u_2 &= x_R \cdot s^{-1} \mod n
\end{align*}
$$

Và cuối cùng, tính điểm $V$ trên đường cong elliptic sao cho:

$$
V = u_1 \cdot G + u_2 \cdot K
$$

Chữ ký chỉ hợp lệ nếu $x_V \equiv x_R \mod n$, nơi $x_V$ là tọa độ $x$ của điểm $V$. Thực sự, bằng cách kết hợp $u_1 \cdot G$ và $u_2 \cdot K$, người ta thu được một điểm $V$ mà, nếu chữ ký hợp lệ, phải tương ứng với điểm $R$ được sử dụng trong quá trình ký (theo mô-đun $n$).

### Chữ ký với Giao thức Schnorr

Giao thức chữ ký Schnorr là một phương án thay thế cho ECDSA mang lại nhiều ưu điểm. Nó đã có thể được sử dụng trên Bitcoin từ năm 2021 và sự giới thiệu của Taproot, với các mẫu script P2TR. Giống như ECDSA, giao thức Schnorr cho phép ký một thông điệp bằng khóa riêng, theo cách mà chữ ký có thể được xác minh bởi bất kỳ ai biết khóa công khai tương ứng.
Trong trường hợp của Schnorr, cùng một đường cong như ECDSA được sử dụng với các tham số giống nhau. Tuy nhiên, khóa công khai được biểu diễn một cách khác biệt so với ECDSA. Thực sự, chúng chỉ được chỉ định bởi tọa độ $x$ của điểm trên đường cong elliptic. Không giống như ECDSA, nơi khóa công khai nén được biểu diễn bởi 33 byte (với byte tiền tố chỉ ra tính chẵn lẻ của $y$), Schnorr sử dụng khóa công khai 32 byte, chỉ tương ứng với tọa độ $x$ của điểm $K$, và giả định rằng $y$ là chẵn theo mặc định. Biểu diễn đơn giản này giảm kích thước của các chữ ký và tạo điều kiện thuận lợi cho một số tối ưu hóa trong các thuật toán xác minh.
Khóa công khai sau đó là tọa độ $x$ của điểm $K$:

$$
\text{pk} = K_x
$$

Bước đầu tiên để tạo ra một chữ ký là băm thông điệp. Nhưng không giống như ECDSA, nó được thực hiện với các giá trị khác và một hàm băm có nhãn được sử dụng để tránh xung đột trong các bối cảnh khác nhau. Một hàm băm có nhãn đơn giản chỉ bao gồm việc thêm một nhãn tùy ý vào đầu vào của hàm băm cùng với dữ liệu thông điệp.

![CYP201](assets/fr/023.webp)

Ngoài thông điệp, tọa độ $x$ của khóa công khai $K_x$, cũng như một điểm $R$ được tính từ nonce $r$ ($R=r \cdot G$) - đây là một số nguyên duy nhất cho mỗi chữ ký, được tính một cách xác định từ khóa riêng và thông điệp để tránh các lỗ hổng liên quan đến việc tái sử dụng nonce, cũng được truyền vào hàm có nhãn. Giống như đối với khóa công khai, chỉ tọa độ $x$ của điểm nonce $R_x$ được giữ lại để mô tả điểm.

Kết quả của việc băm này được ghi chú là $e$ và được gọi là "thách thức":

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Ở đây, $\text{HASH}$ là hàm băm SHA256, và $\text{``BIP0340/challenge''}$ là thẻ đặc biệt dành cho việc băm.

Cuối cùng, tham số $s$ được tính toán theo cách này từ khóa riêng $k$, nonce $r$, và thách thức $e$:

$$
s = (r + e \cdot k) \mod n
$$

Chữ ký sau đó đơn giản là cặp $Rx$ và $s$.

$$
\text{SIG} = R_x \Vert s
$$

### Xác minh Chữ ký Schnorr

Việc xác minh một chữ ký Schnorr đơn giản hơn so với chữ ký ECDSA. Dưới đây là các bước để xác minh chữ ký $(R_x, s)$ với khóa công khai $K_x$ và tin nhắn $m$:
Đầu tiên, chúng ta xác minh rằng $K_x$ là một số nguyên hợp lệ và nhỏ hơn $p$. Nếu điều này đúng, chúng ta lấy điểm tương ứng trên đường cong với $K_y$ là chẵn. Chúng ta cũng trích xuất $R_x$ và $s$ bằng cách tách chữ ký $\text{SIG}$. Sau đó, chúng ta kiểm tra rằng $R_x < p$ và $s < n$ (thứ tự của đường cong).
Tiếp theo, chúng ta tính toán thách thức $e$ theo cùng một cách như người phát hành chữ ký:

$$
e = \text{HASH}(\text{``BIP0340/challenge''}, R_x \Vert K_x \Vert m) \mod n
$$

Sau đó, chúng ta tính một điểm tham chiếu trên đường cong theo cách này:

$$
R' = s \cdot G - e \cdot K
$$

Cuối cùng, chúng ta xác minh rằng $R'_x = R_x$. Nếu hai tọa độ x khớp nhau, thì chữ ký $(R_x, s)$ thực sự hợp lệ với khóa công khai $K_x$.

### Tại sao điều này lại hoạt động?

Người ký đã tính $s = r + e \cdot k \mod n$, vì vậy $R' = s \cdot G - e \cdot K$ nên bằng với điểm gốc $R$, bởi vì:

$$
s \cdot G = (r + e \cdot k) \cdot G = r \cdot G + e \cdot k \cdot G
$$

Vì $K = k \cdot G$, chúng ta có $e \cdot k \cdot G = e \cdot K$. Do đó:

$$
R' = r \cdot G = R
$$

Vì vậy, chúng ta có:

$$
R'_x = R_x
$$

### Ưu điểm của chữ ký Schnorr

Chữ ký Schnorr mang lại một số ưu điểm cho Bitcoin so với thuật toán ECDSA ban đầu. Đầu tiên, Schnorr cho phép tổng hợp khóa và chữ ký. Điều này có nghĩa là nhiều khóa công khai có thể được kết hợp thành một khóa duy nhất.

![CYP201](assets/fr/024.webp)

Tương tự, nhiều chữ ký có thể được tổng hợp thành một chữ ký hợp lệ duy nhất. Do đó, trong trường hợp của một giao dịch đa chữ ký, một nhóm người tham gia có thể ký với một chữ ký duy nhất và một khóa công khai tổng hợp duy nhất. Điều này giảm đáng kể chi phí lưu trữ và tính toán cho mạng, vì mỗi nút chỉ cần xác minh một chữ ký duy nhất.

![CYP201](assets/fr/025.webp)

Hơn nữa, tổng hợp chữ ký cải thiện quyền riêng tư. Với Schnorr, việc phân biệt một giao dịch đa chữ ký với một giao dịch chữ ký đơn trở nên không thể. Sự đồng nhất này làm cho việc phân tích chuỗi khó khăn hơn, vì nó hạn chế khả năng xác định dấu vân tay ví.
Cuối cùng, Schnorr cũng mang lại khả năng xác minh hàng loạt. Bằng cách xác minh nhiều chữ ký cùng một lúc, các nút có thể tăng hiệu quả, đặc biệt là đối với các khối chứa nhiều giao dịch. Tối ưu hóa này giảm thời gian và nguồn lực cần thiết để xác thực một khối. Ngoài ra, chữ ký Schnorr không bị biến dạng, không giống như chữ ký được tạo ra bằng ECDSA. Điều này có nghĩa là một kẻ tấn công không thể chỉnh sửa một chữ ký hợp lệ để tạo ra một chữ ký hợp lệ khác cho cùng một thông điệp và cùng một khóa công khai. Lỗ hổng này trước đây có mặt trên Bitcoin và đặc biệt ngăn cản việc triển khai an toàn của Lightning Network. Nó đã được giải quyết cho ECDSA với bản cập nhật mềm SegWit vào năm 2017, bao gồm việc chuyển chữ ký sang một cơ sở dữ liệu riêng biệt từ các giao dịch để ngăn chặn sự biến dạng của chúng.

### Tại sao Satoshi lại chọn ECDSA?

Như chúng ta đã thấy, ban đầu Satoshi đã chọn triển khai ECDSA cho chữ ký số trên Bitcoin. Tuy nhiên, chúng ta cũng đã thấy rằng Schnorr vượt trội hơn ECDSA ở nhiều khía cạnh, và giao thức này được tạo ra bởi Claus-Peter Schnorr vào năm 1989, 20 năm trước khi Bitcoin được phát minh.

Thực sự, chúng ta không biết tại sao Satoshi không chọn nó, nhưng một giả thuyết có khả năng là giao thức này đã được cấp bằng sáng chế cho đến năm 2008. Mặc dù Bitcoin được tạo ra một năm sau, vào tháng 1 năm 2009, không có tiêu chuẩn hóa mã nguồn mở nào cho chữ ký Schnorr vào thời điểm đó. Có lẽ Satoshi coi việc sử dụng ECDSA, đã được sử dụng rộng rãi và kiểm tra trong phần mềm mã nguồn mở và có một số triển khai được công nhận (đặc biệt là thư viện OpenSSL được sử dụng cho đến năm 2015 trên Bitcoin Core, sau đó được thay thế bằng libsecp256k1 trong phiên bản 0.10.0) là an toàn hơn. Hoặc có thể anh ấy đơn giản không biết rằng bằng sáng chế này sẽ hết hạn vào năm 2008. Dù sao, giả thuyết có khả năng nhất dường như liên quan đến bằng sáng chế này và thực tế là ECDSA đã có lịch sử chứng minh và dễ triển khai hơn.

## Các cờ sighash

<chapterId>231c41a2-aff2-4655-9048-47b6d2d83d64</chapterId>

Như chúng ta đã thấy trong các chương trước, chữ ký số thường được sử dụng để mở khóa script của một đầu vào. Trong quá trình ký, cần phải bao gồm dữ liệu đã ký vào tính toán, được chỉ định trong các ví dụ của chúng tôi bằng thông điệp $m$. Dữ liệu này, một khi đã được ký, không thể được chỉnh sửa mà không làm cho chữ ký trở nên không hợp lệ. Thực sự, cho dù là ECDSA hay Schnorr, người xác minh chữ ký phải bao gồm trong tính toán của họ cùng một thông điệp $m$. Nếu nó khác với thông điệp $m$ ban đầu được sử dụng bởi người ký, kết quả sẽ không chính xác và chữ ký sẽ được coi là không hợp lệ. Khi đó, người ta nói rằng một chữ ký bao phủ một số dữ liệu nhất định và bảo vệ nó, theo một cách nào đó, khỏi sự chỉnh sửa không được phép.

### Cờ sighash là gì?

Trong trường hợp cụ thể của Bitcoin, chúng ta đã thấy rằng thông điệp $m$ tương ứng với giao dịch. Tuy nhiên, trên thực tế, nó phức tạp hơn một chút. Thực sự, nhờ có cờ sighash, có thể chọn dữ liệu cụ thể trong giao dịch sẽ được bao phủ hoặc không bởi chữ ký.
"Cờ sighash" do đó là một tham số được thêm vào mỗi đầu vào, cho phép xác định các thành phần của giao dịch được bao phủ bởi chữ ký liên quan. Những thành phần này là các đầu vào và các đầu ra. Sự lựa chọn của cờ sighash do đó xác định đầu vào và đầu ra nào của giao dịch được cố định bởi chữ ký và cái nào vẫn có thể được chỉnh sửa mà không làm mất hiệu lực của nó. Cơ chế này cho phép chữ ký cam kết dữ liệu giao dịch theo ý định của người ký.
Rõ ràng, một khi giao dịch được xác nhận trên blockchain, nó trở nên không thể thay đổi, bất kể các cờ sighash được sử dụng. Khả năng chỉnh sửa thông qua các cờ sighash chỉ giới hạn trong khoảng thời gian từ khi ký đến khi xác nhận.

Nói chung, phần mềm ví không cung cấp cho bạn tùy chọn để thủ công chỉnh sửa cờ sighash của các đầu vào khi bạn tạo một giao dịch. Theo mặc định, `SIGHASH_ALL` được thiết lập. Cá nhân tôi chỉ biết Sparrow Wallet cho phép chỉnh sửa này từ giao diện người dùng.

### Các cờ sighash hiện có trên Bitcoin là gì?

Trên Bitcoin, trước hết và quan trọng nhất là có 3 cờ sighash cơ bản:

- `SIGHASH_ALL` (`0x01`): Chữ ký áp dụng cho tất cả các đầu vào và tất cả các đầu ra của giao dịch. Giao dịch do đó hoàn toàn được bảo vệ bởi chữ ký và không thể được chỉnh sửa. `SIGHASH_ALL` là cờ sighash được sử dụng phổ biến nhất trong các giao dịch hàng ngày khi ai đó chỉ muốn thực hiện một giao dịch mà không muốn nó có thể bị chỉnh sửa.

![CYP201](assets/fr/026.webp)

Trong tất cả các sơ đồ của chương này, màu cam đại diện cho các yếu tố được bảo vệ bởi chữ ký, trong khi màu đen chỉ ra những yếu tố không được bảo vệ.

- `SIGHASH_NONE` (`0x02`): Chữ ký bao gồm tất cả các đầu vào nhưng không bao gồm bất kỳ đầu ra nào, do đó cho phép chỉnh sửa các đầu ra sau khi ký. Cụ thể, điều này giống như một chiếc séc trắng. Người ký mở khóa các UTXOs trong đầu vào nhưng để trường đầu ra hoàn toàn có thể chỉnh sửa. Bất kỳ ai biết giao dịch này có thể thêm đầu ra của họ chọn, ví dụ bằng cách chỉ định một địa chỉ nhận để thu thập các quỹ tiêu thụ bởi các đầu vào, và sau đó phát sóng giao dịch để thu hồi bitcoin. Chữ ký của chủ sở hữu các đầu vào sẽ không bị vô hiệu, vì nó chỉ bao gồm các đầu vào.

![CYP201](assets/fr/027.webp)

- `SIGHASH_SINGLE` (`0x03`): Chữ ký bao gồm tất cả các đầu vào cũng như một đầu ra duy nhất, tương ứng với chỉ số của đầu vào đã ký. Ví dụ, nếu chữ ký mở khóa _scriptPubKey_ của đầu vào #0, thì nó cũng bao gồm đầu ra #0. Chữ ký cũng bảo vệ tất cả các đầu vào khác, không thể được chỉnh sửa. Tuy nhiên, bất kỳ ai cũng có thể thêm một đầu ra bổ sung mà không làm mất hiệu lực chữ ký, miễn là đầu ra #0, là đầu ra duy nhất được bảo vệ bởi nó, không được chỉnh sửa.
  ![CYP201](assets/fr/028.webp)

Ngoài ba cờ sighash này, còn có bổ sung `SIGHASH_ANYONECANPAY` (`0x80`). Bổ sung này có thể kết hợp với một cờ sighash cơ bản để tạo ra ba cờ sighash mới:

- `SIGHASH_ALL | SIGHASH_ANYONECANPAY` (`0x81`): Chữ ký bao gồm một đầu vào duy nhất trong khi bao gồm tất cả các đầu ra của giao dịch. Cờ sighash kết hợp này cho phép, ví dụ, tạo một giao dịch gây quỹ. Người tổ chức chuẩn bị đầu ra với địa chỉ của họ và số tiền mục tiêu, và mỗi nhà đầu tư sau đó có thể thêm các đầu vào để tài trợ cho đầu ra này. Một khi đủ quỹ được tập hợp trong các đầu vào để đáp ứng đầu ra, giao dịch có thể được phát sóng.

![CYP201](assets/fr/029.webp)

- `SIGHASH_NONE | SIGHASH_ANYONECANPAY` (`0x82`): Chữ ký bao gồm một đầu vào, không cam kết với bất kỳ đầu ra nào;

![CYP201](assets/fr/030.webp)

- `SIGHASH_SINGLE | SIGHASH_ANYONECANPAY` (`0x83`): Chữ ký này chỉ bao gồm một đầu vào cũng như đầu ra có cùng chỉ số với đầu vào này. Ví dụ, nếu chữ ký mở khóa _scriptPubKey_ của đầu vào số 3, nó cũng sẽ bao gồm đầu ra số 3. Phần còn lại của giao dịch vẫn có thể được thay đổi, cả về các đầu vào khác và các đầu ra khác.
  ![CYP201](assets/fr/031.webp)

### Dự án Thêm Cờ Sighash Mới

Hiện tại (2024), chỉ có các cờ sighash được trình bày trong phần trước mới có thể sử dụng trên Bitcoin. Tuy nhiên, một số dự án đang xem xét việc thêm mới cờ sighash. Ví dụ, BIP118, được đề xuất bởi Christian Decker và Anthony Towns, giới thiệu hai cờ sighash mới: `SIGHASH_ANYPREVOUT` và `SIGHASH_ANYPREVOUTANYSCRIPT` (_AnyPrevOut = "Bất Kỳ Đầu Ra Trước Đó"_).

Hai cờ sighash này sẽ cung cấp một khả năng bổ sung trên Bitcoin: tạo chữ ký không bao gồm bất kỳ đầu vào cụ thể nào của giao dịch.

![CYP201](assets/fr/032.webp)

Ý tưởng này ban đầu được Joseph Poon và Thaddeus Dryja đề xuất trong Bản Trắng Lightning. Trước khi được đổi tên, cờ sighash này được gọi là `SIGHASH_NOINPUT`.
Nếu cờ sighash này được tích hợp vào Bitcoin, nó sẽ cho phép sử dụng các covenant, nhưng cũng là một tiền đề bắt buộc cho việc triển khai Eltoo, một giao thức chung cho các lớp thứ hai định nghĩa cách quản lý chung quyền sở hữu của một UTXO. Eltoo được thiết kế đặc biệt để giải quyết các vấn đề liên quan đến cơ chế thương lượng trạng thái của các kênh Lightning, tức là giữa việc mở và đóng.

Để mở rộng kiến thức về Mạng Lưới Lightning, sau khóa học CYP201, tôi rất khuyên bạn nên tham gia khóa học LNP201 của Fanis Michalakis, nơi đề cập đến chủ đề này một cách chi tiết:

https://planb.network/courses/lnp201

Trong phần tiếp theo, tôi đề xuất khám phá cách hoạt động của cụm từ ghi nhớ tạo nên ví Bitcoin của bạn.

# Cụm từ ghi nhớ

<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Sự phát triển của ví Bitcoin

<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Sau khi đã khám phá cách hoạt động của hàm băm và chữ ký số, chúng ta có thể nghiên cứu cách ví Bitcoin hoạt động. Mục tiêu sẽ là tưởng tượng cách một ví trên Bitcoin được xây dựng, cách nó được phân rã, và những thông tin khác nhau tạo nên nó được sử dụng như thế nào. Hiểu biết về cơ chế ví sẽ giúp bạn cải thiện việc sử dụng Bitcoin về mặt an ninh và riêng tư.

Trước khi đi sâu vào chi tiết kỹ thuật, điều cần thiết là làm rõ ý nghĩa của "ví Bitcoin" và hiểu được công dụng của nó.

### Ví Bitcoin là gì?

Khác với ví truyền thống, cho phép bạn lưu trữ tiền giấy và đồng xu vật lý, ví Bitcoin không "chứa" bitcoin theo nghĩa đen. Thực tế, bitcoin không tồn tại dưới dạng vật lý hay số hóa có thể được lưu trữ, nhưng được biểu diễn bởi các đơn vị tài khoản được mô tả trong hệ thống dưới dạng **UTXOs** (_Unspent Transaction Output_).
UTXOs vì thế đại diện cho các phân đoạn của bitcoin, với kích thước khác nhau, có thể được chi tiêu miễn là _scriptPubKey_ của chúng được thỏa mãn. Để chi tiêu bitcoin của mình, người dùng phải cung cấp một _scriptSig_ mở khóa _scriptPubKey_ liên kết với UTXO của họ. Bằng chứng này thường được thực hiện thông qua một chữ ký số, được tạo từ khóa riêng tương ứng với khóa công khai có trong _scriptPubKey_. Do đó, yếu tố quan trọng mà người dùng phải bảo mật là khóa riêng. Vai trò của một ví Bitcoin chính xác là quản lý các khóa riêng này một cách an toàn. Trên thực tế, vai trò của nó giống như một móc khóa hơn là một ví trong nghĩa truyền thống.

### Ví JBOK (_Just a Bunch Of Keys_)

Các ví đầu tiên được sử dụng trên Bitcoin là ví JBOK (_Just a Bunch Of Keys_), tổng hợp các khóa riêng được tạo ra một cách độc lập và không có liên kết nào giữa chúng. Các ví này hoạt động trên một mô hình đơn giản nơi mỗi khóa riêng có thể mở khóa một địa chỉ nhận Bitcoin duy nhất.

![CYP201](assets/fr/033.webp)

Nếu muốn sử dụng nhiều khóa riêng, sau đó cần phải tạo nhiều bản sao lưu để đảm bảo quyền truy cập vào quỹ trong trường hợp có vấn đề với thiết bị lưu trữ ví. Nếu sử dụng một khóa riêng duy nhất, cấu trúc ví này có thể đủ, vì một bản sao lưu duy nhất là đủ. Tuy nhiên, điều này gây ra một vấn đề: trên Bitcoin, việc luôn sử dụng cùng một khóa riêng được khuyến cáo mạnh mẽ là không nên. Thực tế, một khóa riêng được liên kết với một địa chỉ duy nhất, và địa chỉ nhận Bitcoin thường được thiết kế để sử dụng một lần. Mỗi lần bạn nhận quỹ, bạn nên tạo một địa chỉ trống mới.

Ràng buộc này xuất phát từ mô hình bảo mật của Bitcoin. Bằng cách tái sử dụng cùng một địa chỉ, nó làm cho việc truy vết tất cả giao dịch Bitcoin của tôi trở nên dễ dàng hơn cho các quan sát viên bên ngoài. Đó là lý do tại sao việc tái sử dụng một địa chỉ nhận được khuyến cáo mạnh mẽ là không nên. Tuy nhiên, để có nhiều địa chỉ và tách biệt công khai các giao dịch của chúng ta, cần phải quản lý nhiều khóa riêng. Trong trường hợp của ví JBOK, điều này đòi hỏi việc tạo ra nhiều bản sao lưu như có nhiều cặp khóa mới, một nhiệm vụ có thể nhanh chóng trở nên phức tạp và khó duy trì cho người dùng.

Để tìm hiểu thêm về mô hình bảo mật của Bitcoin và khám phá các phương pháp để bảo vệ sự riêng tư của bạn, tôi cũng khuyến nghị theo dõi khóa học BTC204 của tôi trên Plan ₿ Network:

https://planb.network/courses/btc204

### Ví HD (_Hierarchical Deterministic_)

Để giải quyết hạn chế của ví JBOK, một cấu trúc ví mới sau đó được sử dụng. Vào năm 2012, Pieter Wuille đã giới thiệu một cải tiến với BIP32, giới thiệu ví phân cấp xác định (HD wallets). Nguyên tắc của một ví HD là phái sinh tất cả các khóa riêng từ một nguồn thông tin duy nhất, được gọi là hạt giống, theo một cách xác định và phân cấp. Hạt giống này được tạo ngẫu nhiên khi ví được tạo và tạo thành một bản sao lưu duy nhất cho phép tái tạo tất cả các khóa riêng của ví. Do đó, người dùng có thể tạo ra một số lượng rất lớn các khóa riêng để tránh tái sử dụng địa chỉ và bảo vệ sự riêng tư của họ, trong khi chỉ cần thực hiện một bản sao lưu duy nhất của ví thông qua hạt giống.
![CYP201](assets/fr/034.webp)

Trong ví HD, việc phái sinh khóa được thực hiện theo một cấu trúc phân cấp cho phép các khóa được tổ chức vào các không gian phái sinh con, mỗi không gian con có thể được chia nhỏ hơn nữa, để tạo thuận lợi cho việc quản lý quỹ và tương thích giữa các phần mềm ví khác nhau. Ngày nay, tiêu chuẩn này được đa số người dùng Bitcoin chấp nhận. Vì lý do này, chúng ta sẽ xem xét nó chi tiết trong các chương tiếp theo.

### Tiêu Chuẩn BIP39: Cụm từ Ghi Nhớ

Ngoài BIP32, BIP39 chuẩn hóa định dạng hạt giống dưới dạng cụm từ ghi nhớ, nhằm mục đích hỗ trợ việc sao lưu và đọc hiểu dễ dàng cho người dùng. Cụm từ ghi nhớ, còn được gọi là cụm từ khôi phục hoặc cụm từ 24 từ, là một chuỗi các từ được rút ra từ một danh sách đã định trước, mã hóa an toàn hạt giống của ví.

Cụm từ ghi nhớ giúp việc sao lưu trở nên đơn giản hơn nhiều cho người dùng. Trong trường hợp mất, hỏng, hoặc bị đánh cắp thiết bị chứa ví, chỉ cần biết cụm từ ghi nhớ này là có thể tái tạo ví và khôi phục quyền truy cập vào tất cả các quỹ được bảo vệ bởi nó.

Trong các chương tiếp theo, chúng ta sẽ khám phá cơ chế hoạt động bên trong của ví HD, bao gồm cơ chế phát sinh khóa và các cấu trúc phân cấp khác nhau có thể có. Điều này sẽ giúp bạn hiểu rõ hơn về nền tảng mật mã mà an toàn tài sản trên Bitcoin dựa trên. Và để bắt đầu, trong chương tiếp theo, tôi đề xuất chúng ta khám phá vai trò của entropy tại cơ sở của ví của bạn.

## Entropy và Số Ngẫu Nhiên

<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>
Ví HD hiện đại (xác định và phân cấp) dựa vào một mảnh thông tin ban đầu gọi là "entropy" để tạo ra toàn bộ bộ khóa ví một cách xác định. Entropy này là một số ngẫu nhiên giả có mức độ hỗn loạn phần nào xác định mức độ an toàn của ví.

### Định Nghĩa của Entropy

Trong bối cảnh của mật mã học và thông tin, entropy là một thước đo định lượng về sự không chắc chắn hoặc không dự đoán được liên quan đến một nguồn dữ liệu hoặc một quá trình ngẫu nhiên. Nó đóng một vai trò quan trọng trong an toàn của các hệ thống mật mã, đặc biệt là trong việc tạo ra khóa và số ngẫu nhiên. Entropy cao đảm bảo rằng các khóa được tạo ra đủ không dự đoán được và kháng lại các cuộc tấn công bằng cách thử mọi tổ hợp có thể để đoán khóa.

Trong bối cảnh của Bitcoin, entropy được sử dụng để tạo ra hạt giống. Khi tạo một ví xác định và phân cấp, việc xây dựng cụm từ ghi nhớ được thực hiện từ một số ngẫu nhiên, chính nó được phát sinh từ một nguồn entropy. Cụm từ sau đó được sử dụng để tạo ra nhiều khóa riêng tư, một cách xác định và phân cấp, để tạo điều kiện chi tiêu trên UTXOs.

### Phương Pháp Tạo Ra Entropy

Entropy ban đầu được sử dụng cho một ví HD thường là 128 bit hoặc 256 bit, nơi:

- **128 bit entropy** tương ứng với một cụm từ ghi nhớ của **12 từ**;
- **256 bit entropy** tương ứng với một cụm từ ghi nhớ của **24 từ**.

Trong hầu hết các trường hợp, số ngẫu nhiên này được tạo ra tự động bởi phần mềm ví sử dụng một PRNG (_Pseudo-Random Number Generator_ - Máy Phát Số Ngẫu Nhiên Giả). PRNGs là một loại thuật toán được sử dụng để tạo ra các chuỗi số từ một trạng thái ban đầu, có các đặc tính tiếp cận với số ngẫu nhiên, mặc dù không thực sự là số ngẫu nhiên. Một PRNG tốt phải có các đặc tính như đồng nhất đầu ra, không dự đoán được, và kháng lại các cuộc tấn công dự đoán. Khác với máy phát số ngẫu nhiên thực sự (TRNG), PRNGs là xác định và có thể tái tạo.

![CYP201](assets/fr/035.webp)

Một phương án khác là tự tạo entropy, điều này mang lại quyền kiểm soát tốt hơn nhưng cũng rủi ro hơn nhiều. Tôi khuyên bạn mạnh mẽ không tự tạo entropy cho ví HD của mình.

Trong chương tiếp theo, chúng ta sẽ xem làm thế nào chúng ta đi từ một số ngẫu nhiên đến một cụm từ ghi nhớ của 12 hoặc 24 từ.

## Cụm Từ Ghi Nhớ

<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>
Cụm từ ghi nhớ, còn được gọi là "cụm từ khôi phục", "cụm từ bí mật", hoặc "cụm từ 24 từ", là một chuỗi thường gồm 12 hoặc 24 từ, được tạo ra từ entropy. Nó được sử dụng để suy ra một cách xác định tất cả các khóa của một ví HD. Điều này có nghĩa là từ cụm từ này, có thể tạo ra và tái tạo tất cả các khóa riêng tư và khóa công khai của ví Bitcoin một cách xác định, và do đó truy cập vào các quỹ được bảo vệ bằng nó. Mục đích của cụm từ ghi nhớ là cung cấp một phương tiện sao lưu và khôi phục bitcoin một cách an toàn và dễ sử dụng. Nó được giới thiệu vào các tiêu chuẩn vào năm 2013 với BIP39.
Hãy cùng khám phá cách chuyển từ entropy sang cụm từ ghi nhớ.

### Checksum

Để chuyển đổi entropy thành cụm từ ghi nhớ, trước tiên phải thêm một checksum (hoặc "tổng kiểm soát") vào cuối entropy. Checksum là một chuỗi bit ngắn đảm bảo tính toàn vẹn của dữ liệu bằng cách xác minh rằng không có sự thay đổi nào không mong muốn được giới thiệu.

Để tính toán checksum, hàm băm SHA256 được áp dụng cho entropy (chỉ một lần; đây là một trong những trường hợp hiếm hoi trong Bitcoin khi một hàm băm SHA256 đơn được sử dụng thay vì một hàm băm kép). Thao tác này tạo ra một băm 256-bit. Checksum bao gồm các bit đầu tiên của băm này, và độ dài của nó phụ thuộc vào độ dài của entropy, theo công thức sau:

$$
\text{CS} = \frac{\text{ENT}}{32}
$$

trong đó $\text{ENT}$ đại diện cho độ dài của entropy tính bằng bit, và $\text{CS}$ là độ dài của checksum tính bằng bit.

Ví dụ, đối với một entropy 256 bit, 8 bit đầu tiên của băm được lấy để tạo thành checksum:

$$
\text{CS} = \frac{256}{32} = 8 \text{ bit}
$$

Một khi checksum được tính toán, nó được nối với entropy để thu được một chuỗi bit mở rộng được ghi là $\text{ENT} \Vert \text{CS}$ ("nối" có nghĩa là đặt liền nhau).

![CYP201](assets/fr/036.webp)

### Sự Tương Ứng giữa Entropy và Cụm Từ Ghi Nhớ

Số lượng từ trong cụm từ ghi nhớ phụ thuộc vào kích thước entropy ban đầu, như được minh họa trong bảng sau với:

- $\text{ENT}$: kích thước tính bằng bit của entropy;
- $\text{CS}$: kích thước tính bằng bit của checksum;
- $w$: số lượng từ trong cụm từ ghi nhớ cuối cùng.

$$
\begin{array}{|c|c|c|c|}
\hline
\text{ENT} & \text{CS} & \text{ENT} \Vert \text{CS} & w \\
\hline
128 & 4 & 132 & 12 \\
160 & 5 & 165 & 15 \\
192 & 6 & 198 & 18 \\
224 & 7 & 231 & 21 \\
256 & 8 & 264 & 24 \\
\hline
\end{array}
$$

Ví dụ, đối với một entropy 256-bit, kết quả $\text{ENT} \Vert \text{CS}$ là 264 bit và tạo ra một cụm từ ghi nhớ gồm 24 từ.

### Chuyển Đổi Chuỗi Nhị Phân thành Cụm Từ Ghi Nhớ

Chuỗi bit $\text{ENT} \Vert \text{CS}$ sau đó được chia thành các phân đoạn 11 bit. Mỗi phân đoạn 11 bit, một khi được chuyển đổi sang thập phân, tương ứng với một số từ 0 đến 2047, chỉ vị trí của một từ [trong danh sách 2048 từ được chuẩn hóa bởi BIP39](https://github.com/Planb-Network/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf).

![CYP201](assets/fr/037.webp)
Ví dụ, đối với một entropy 128-bit, checksum là 4 bit, và do đó, chuỗi tổng cộng là 132 bit. Nó được chia thành 12 phân đoạn 11 bit (các bit màu cam chỉ checksum):

![CYP201](assets/fr/038.webp)

Mỗi phân đoạn sau đó được chuyển đổi thành một số thập phân đại diện cho một từ trong danh sách. Ví dụ, phân đoạn nhị phân `01011010001` tương đương trong hệ thập phân là `721`. Bằng cách cộng thêm 1 để căn chỉnh với chỉ mục của danh sách (bắt đầu từ 1 chứ không phải 0), điều này cho ra từ thứ hạng `722`, tức là "*focus*" trong danh sách.

![CYP201](assets/fr/039.webp)

Sự tương ứng này được lặp lại cho mỗi trong số 12 phân đoạn, nhằm thu được một cụm từ gồm 12 từ.

![CYP201](assets/fr/040.webp)

### Đặc điểm của Danh Sách Từ BIP39

Một đặc điểm của danh sách từ BIP39 là không có từ nào chia sẻ cùng bốn chữ cái đầu tiên theo cùng một thứ tự với một từ khác. Điều này có nghĩa là chỉ ghi lại bốn chữ cái đầu tiên của mỗi từ là đủ để lưu cụm từ ghi nhớ. Điều này có thể thú vị cho việc tiết kiệm không gian, đặc biệt là cho những người muốn khắc nó trên một hỗ trợ kim loại.

Danh sách này gồm 2048 từ tồn tại trong nhiều ngôn ngữ. Đây không phải là những bản dịch đơn giản, mà là những từ riêng biệt cho mỗi ngôn ngữ. Tuy nhiên, việc tuân thủ phiên bản tiếng Anh được khuyến nghị mạnh mẽ, vì các phiên bản bằng ngôn ngữ khác thường không được hỗ trợ bởi phần mềm ví.

### Chọn Độ Dài Nào cho Cụm Từ Ghi Nhớ của Bạn?
Để xác định độ dài tối ưu của cụm từ ghi nhớ của bạn, người ta phải xem xét đến mức độ bảo mật thực tế mà nó cung cấp. Một cụm từ 12 từ đảm bảo 128 bit bảo mật, trong khi một cụm từ 24 từ cung cấp 256 bit.

Tuy nhiên, sự khác biệt này về mức độ bảo mật của cụm từ không cải thiện tổng thể bảo mật của một ví Bitcoin, vì các khóa riêng tư được tạo ra từ cụm từ này chỉ hưởng lợi từ 128 bit bảo mật. Thực tế, như chúng ta đã thấy trước đó, các khóa riêng tư Bitcoin được tạo ra từ các số ngẫu nhiên (hoặc được suy ra từ một nguồn ngẫu nhiên) nằm trong khoảng từ $1$ đến $n-1$, nơi $n$ đại diện cho thứ tự của điểm sinh $G$ của đường cong secp256k1, một số nhỏ hơn một chút so với $2^{256}$. Người ta có thể nghĩ rằng các khóa riêng tư này cung cấp 256 bit bảo mật. Tuy nhiên, bảo mật của chúng nằm ở khó khăn trong việc tìm ra một khóa riêng tư từ khóa công khai tương ứng của nó, một khó khăn được thiết lập bởi vấn đề toán học của logarithm rời rạc trên đường cong elliptic (*ECDLP*). Đến nay, thuật toán được biết đến tốt nhất để giải quyết vấn đề này là thuật toán rho của Pollard, giảm số lượng phép toán cần thiết để phá một khóa xuống còn căn bậc hai của kích thước của nó.

Đối với các khóa 256-bit, như những khóa được sử dụng trên Bitcoin, thuật toán rho của Pollard do đó giảm độ phức tạp xuống còn $2^{128}$ phép toán:


$$

O(\sqrt{2^{256}}) = O(2^{128})

$$

Do đó, người ta coi rằng một khóa riêng tư được sử dụng trên Bitcoin cung cấp 128 bit bảo mật.

Kết quả là, việc chọn một cụm từ 24 từ không cung cấp thêm bảo vệ cho ví, vì 256 bit bảo mật trên cụm từ là vô ích nếu các khóa được suy ra chỉ cung cấp 128 bit bảo mật. Để minh họa nguyên tắc này, giống như có một ngôi nhà với hai cửa: một cửa gỗ cũ và một cửa cường lực. Trong trường hợp bị đột nhập, cửa cường lực sẽ không có ích, vì kẻ đột nhập sẽ đi qua cửa gỗ. Đây là một tình huống tương tự ở đây.
Một cụm từ gồm 12 từ, cũng cung cấp 128 bit bảo mật, vì vậy hiện tại là đủ để bảo vệ bitcoin của bạn khỏi bất kỳ nỗ lực trộm cắp nào. Miễn là thuật toán chữ ký số không thay đổi để sử dụng khóa lớn hơn hoặc dựa vào một vấn đề toán học khác ngoài ECDLP, một cụm từ 24 từ vẫn là thừa. Hơn nữa, một cụm từ dài hơn tăng nguy cơ mất mát trong quá trình sao lưu: một bản sao lưu ngắn gấp đôi luôn dễ quản lý hơn.
Để tìm hiểu thêm và biết cách tạo một cụm từ ghi nhớ thử nghiệm một cách thủ công, tôi khuyên bạn nên khám phá hướng dẫn này:

https://planb.network/tutorials/wallet/backup/generate-mnemonic-phrase-47507d90-e6af-4cac-b01b-01a14d7a8228
Trước khi tiếp tục với việc phát sinh ví từ cụm từ ghi nhớ này, tôi sẽ giới thiệu cho bạn, trong chương tiếp theo, về cụm từ BIP39, vì nó đóng vai trò trong quá trình phát sinh, và nó ở cùng một cấp độ với cụm từ ghi nhớ.
## Cụm từ bí mật
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

Như chúng ta vừa thấy, ví HD được tạo ra từ một cụm từ ghi nhớ thường gồm 12 hoặc 24 từ. Cụm từ này rất quan trọng vì nó cho phép khôi phục tất cả các khóa của một ví trong trường hợp thiết bị vật lý của nó (như một ví cứng, chẳng hạn) bị mất. Tuy nhiên, nó tạo thành một điểm thất bại duy nhất, bởi vì nếu nó bị xâm phạm, kẻ tấn công có thể ăn cắp tất cả bitcoin. Đây là nơi cụm từ bí mật BIP39 đóng vai trò.

### Cụm từ bí mật BIP39 là gì?

Cụm từ bí mật là một mật khẩu tùy chọn, mà bạn có thể tự do chọn, được thêm vào cụm từ ghi nhớ trong quá trình phát sinh khóa để tăng cường bảo mật cho ví.

Hãy cẩn thận, cụm từ bí mật không nên bị nhầm lẫn với mã PIN của ví cứng hoặc mật khẩu được sử dụng để mở khóa truy cập vào ví trên máy tính của bạn. Không giống như tất cả các yếu tố này, cụm từ bí mật đóng vai trò trong quá trình phát sinh khóa ví của bạn. **Điều này có nghĩa là không có nó, bạn sẽ không bao giờ có thể khôi phục được bitcoin của mình.**

Cụm từ bí mật hoạt động cùng với cụm từ ghi nhớ, thay đổi hạt giống từ đó các khóa được tạo ra. Như vậy, ngay cả khi ai đó có được cụm từ 12 hoặc 24 từ của bạn, mà không có cụm từ bí mật, họ không thể truy cập vào quỹ của bạn. Sử dụng một cụm từ bí mật cơ bản tạo ra một ví mới với các khóa khác biệt. Thay đổi (ngay cả một chút) cụm từ bí mật sẽ tạo ra một ví khác nhau.

![CYP201](assets/fr/041.webp)

### Tại sao bạn nên sử dụng cụm từ bí mật?

Cụm từ bí mật là tùy ý và có thể là bất kỳ sự kết hợp ký tự nào do người dùng chọn. Sử dụng cụm từ bí mật do đó mang lại một số lợi ích. Đầu tiên, nó giảm mọi rủi ro liên quan đến việc cụm từ ghi nhớ bị xâm phạm bằng cách yêu cầu một yếu tố thứ hai để truy cập vào quỹ (trộm cắp, truy cập vào nhà bạn, v.v.).

Tiếp theo, nó có thể được sử dụng một cách chiến lược để tạo ra một ví dụ như để đối mặt với các ràng buộc vật lý để ăn cắp quỹ của bạn như cuộc tấn công nổi tiếng "_cuộc tấn công bằng cờ lê 5 đô la_". Trong kịch bản này, ý tưởng là có một ví không có cụm từ bí mật chỉ chứa một lượng nhỏ bitcoin, đủ để thỏa mãn một kẻ tấn công tiềm năng, trong khi có một ví ẩn. Ví sau sử dụng cùng một cụm từ ghi nhớ nhưng được bảo vệ bằng một cụm từ bí mật bổ sung.
Cuối cùng, việc sử dụng cụm từ bí mật là thú vị khi người ta muốn kiểm soát sự ngẫu nhiên của việc tạo ra hạt giống của ví HD.
### Làm thế nào để chọn một cụm từ bí mật tốt?

Để cụm từ bí mật có hiệu quả, nó phải đủ dài và ngẫu nhiên. Giống như một mật khẩu mạnh, tôi khuyên bạn nên chọn một cụm từ bí mật càng dài và ngẫu nhiên càng tốt, với sự đa dạng của chữ cái, số và biểu tượng để làm cho bất kỳ cuộc tấn công bằng lực brút không thể xảy ra.
Cũng rất quan trọng khi lưu cụm từ bí mật này một cách đúng đắn, giống như cách bạn lưu cụm từ ghi nhớ. **Mất nó có nghĩa là mất quyền truy cập vào bitcoin của bạn**. Tôi khuyên bạn không nên chỉ nhớ nó bằng trái tim, vì điều này làm tăng một cách không hợp lý nguy cơ mất mát. Lý tưởng nhất là ghi nó ra một phương tiện vật lý (giấy hoặc kim loại) tách biệt khỏi cụm từ ghi nhớ. Bản sao lưu này rõ ràng phải được lưu trữ ở một nơi khác với nơi bạn lưu cụm từ ghi nhớ để ngăn chặn việc cả hai bị xâm phạm cùng một lúc.
![CYP201](assets/fr/042.webp)

Trong phần tiếp theo, chúng ta sẽ khám phá cách hai yếu tố này tại cơ sở của ví của bạn — cụm từ ghi nhớ và cụm từ bí mật — được sử dụng để suy ra các cặp khóa được sử dụng trong *scriptPubKey* khóa UTXO của bạn.

# Tạo Ví Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>

## Tạo Hạt Giống và Khóa Chính
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Một khi cụm từ ghi nhớ và cụm từ bí mật tùy chọn được tạo ra, quá trình suy ra một ví HD Bitcoin có thể bắt đầu. Cụm từ ghi nhớ đầu tiên được chuyển đổi thành hạt giống, là cơ sở cho tất cả các khóa của ví.

![CYP201](assets/fr/043.webp)

### Hạt Giống của một Ví HD

Tiêu chuẩn BIP39 định nghĩa hạt giống là một chuỗi 512-bit, phục vụ như điểm xuất phát cho việc suy ra tất cả các khóa của một ví HD. Hạt giống được suy ra từ cụm từ ghi nhớ và cụm từ bí mật có thể có sử dụng thuật toán **PBKDF2** (*Password-Based Key Derivation Function 2*) mà chúng ta đã thảo luận trong chương 3.3. Trong hàm suy ra này, chúng ta sẽ sử dụng các tham số sau:

- $m$ : cụm từ ghi nhớ;
- $p$ : một cụm từ bí mật tùy chọn do người dùng chọn để tăng cường bảo mật cho hạt giống. Nếu không có cụm từ bí mật, trường này được để trống;
- $\text{PBKDF2}$ : hàm suy ra với $\text{HMAC-SHA512}$ và $2048$ lần lặp;
- $s$: hạt giống ví 512-bit.
Bất kể độ dài cụm từ ghi nhớ được chọn (132 bit hoặc 264 bit), hàm PBKDF2 luôn tạo ra một đầu ra 512-bit, và do đó hạt giống luôn có kích thước này.

### Sơ Đồ Suy Ra Hạt Giống với PBKDF2

Phương trình sau minh họa việc suy ra hạt giống từ cụm từ ghi nhớ và cụm từ bí mật:


$$

s = \text{PBKDF2}_{\text{HMAC-SHA512}}(m, p, 2048)

$$

![CYP201](assets/fr/044.webp)

Giá trị của hạt giống do đó bị ảnh hưởng bởi giá trị của cụm từ ghi nhớ và cụm từ bí mật. Bằng cách thay đổi cụm từ bí mật, một hạt giống khác nhau được thu được. Tuy nhiên, với cùng một cụm từ ghi nhớ và cụm từ bí mật, cùng một hạt giống luôn được tạo ra, vì PBKDF2 là một hàm định hình. Điều này đảm bảo rằng cùng một cặp khóa có thể được truy xuất thông qua các bản sao lưu của chúng ta.

**Lưu ý:** Trong ngôn ngữ thông thường, thuật ngữ "hạt giống" thường được sử dụng, do lạm dụng ngôn ngữ, để chỉ cụm từ ghi nhớ. Thực tế, trong trường hợp không có cụm từ bí mật, một cái đơn giản là mã hóa của cái kia. Tuy nhiên, như chúng ta đã thấy, trong thực tế kỹ thuật của ví, hạt giống và cụm từ ghi nhớ thực sự là hai yếu tố riêng biệt.

Bây giờ chúng ta đã có hạt giống của mình, chúng ta có thể tiếp tục với việc suy ra ví Bitcoin của mình.
### Chìa Khóa Chính và Mã Chuỗi Chính
Sau khi thu được hạt giống, bước tiếp theo trong việc tạo ví HD bao gồm việc tính toán chìa khóa riêng tư chính và mã chuỗi chính, sẽ đại diện cho độ sâu 0 của ví của chúng ta.

Để thu được chìa khóa riêng tư chính và mã chuỗi chính, hàm HMAC-SHA512 được áp dụng cho hạt giống, sử dụng một khóa cố định "*Bitcoin Seed*" giống nhau cho tất cả người dùng Bitcoin. Hằng số này được chọn để đảm bảo rằng các phái sinh khóa là đặc thù cho Bitcoin. Dưới đây là các thành phần:
- $\text{HMAC-SHA512}$: hàm phái sinh;
- $s$: hạt giống ví 512-bit;
- $\text{"Bitcoin Seed"}$: hằng số phái sinh chung cho tất cả ví Bitcoin.


$$

\text{output} = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)

$$

Kết quả của hàm này do đó là 512 bit. Nó sau đó được chia thành 2 phần:
- 256 bit bên trái tạo thành **chìa khóa riêng tư chính**;
- 256 bit bên phải tạo thành **mã chuỗi chính**.
Toán học, hai giá trị này có thể được ghi như sau với $k_M$ là chìa khóa riêng tư chính và $C_M$ là mã chuỗi chính:
$$

k_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[:256]}

$$


$$

C_M = \text{HMAC-SHA512}(\text{"Bitcoin Seed"}, s)_{[256:]}

$$

![CYP201](assets/fr/045.webp)

### Vai Trò của Chìa Khóa Chính và Mã Chuỗi

Chìa khóa riêng tư chính được coi là chìa khóa cha, từ đó tất cả các chìa khóa riêng tư phái sinh — con, cháu, chắt, v.v. — sẽ được tạo ra. Nó đại diện cho cấp độ không trong hệ thống phân cấp phái sinh.

Mã chuỗi chính, mặt khác, giới thiệu một nguồn entropy bổ sung vào quá trình phái sinh khóa cho con, nhằm chống lại một số cuộc tấn công tiềm năng. Hơn nữa, trong ví HD, mỗi cặp khóa có một mã chuỗi độc đáo liên kết với nó, cũng được sử dụng để phái sinh khóa con từ cặp này, nhưng chúng ta sẽ thảo luận chi tiết hơn trong các chương tiếp theo.

Trước khi tiếp tục với việc phái sinh ví HD với các thành phần tiếp theo, tôi muốn, trong chương tiếp theo, giới thiệu với bạn về khóa mở rộng, thường bị nhầm lẫn với chìa khóa chính. Chúng ta sẽ xem chúng được cấu tạo như thế nào và vai trò của chúng trong ví Bitcoin.

## Khóa Mở Rộng
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Một khóa mở rộng đơn giản là sự kết hợp của một khóa (dù là riêng tư hay công khai) và mã chuỗi liên kết với nó. Mã chuỗi này rất quan trọng cho việc phái sinh khóa con vì, không có nó, việc phái sinh khóa con từ một khóa cha là không thể, nhưng chúng ta sẽ khám phá quy trình này một cách chính xác hơn trong chương tiếp theo. Những khóa mở rộng do đó cho phép tổng hợp tất cả thông tin cần thiết để phái sinh khóa con, qua đó đơn giản hóa quản lý tài khoản trong một ví HD.

![CYP201](assets/fr/046.webp)

Khóa mở rộng bao gồm hai phần:
- Phần payload, chứa khóa riêng tư hoặc công khai cũng như mã chuỗi liên kết;
- Phần metadata, là các thông tin khác nhau để tạo điều kiện tương tác giữa phần mềm và cải thiện sự hiểu biết cho người dùng.

### Cách Khóa Mở Rộng Hoạt Động
Khi khóa mở rộng chứa một khóa riêng, nó được gọi là khóa riêng mở rộng. Nó được nhận diện bởi tiền tố của nó chứa từ khóa `prv`. Ngoài khóa riêng, khóa riêng mở rộng cũng chứa mã chuỗi liên kết tương ứng. Với loại khóa mở rộng này, có thể suy ra tất cả các loại khóa riêng con, và do đó bằng cách cộng và nhân đôi các điểm trên đường cong elliptic, nó cũng cho phép suy ra toàn bộ khóa công khai con.

Khi khóa mở rộng không chứa khóa riêng mà thay vào đó là một khóa công khai, nó được gọi là khóa công khai mở rộng. Nó được nhận diện bởi tiền tố của nó chứa từ khóa `pub`. Rõ ràng, ngoài khóa, nó cũng chứa mã chuỗi liên kết tương ứng. Khác với khóa riêng mở rộng, khóa công khai mở rộng chỉ cho phép suy ra các khóa công khai con "bình thường" (nghĩa là không thể suy ra các khóa con "cứng"). Chúng ta sẽ xem trong chương tiếp theo ý nghĩa của các thuật ngữ "bình thường" và "cứng".

Nhưng dù sao đi nữa, khóa công khai mở rộng không cho phép suy ra các khóa riêng con. Do đó, ngay cả khi ai đó có quyền truy cập vào một `xpub`, họ sẽ không thể chi tiêu các quỹ liên quan, vì họ sẽ không có quyền truy cập vào các khóa riêng tương ứng. Họ chỉ có thể suy ra các khóa công khai con để quan sát các giao dịch liên quan.

Đối với phần tiếp theo, chúng ta sẽ áp dụng ký hiệu sau:
- $K_{\text{PAR}}$: một khóa công khai cha;
- $k_{\text{PAR}}$: một khóa riêng cha;
- $C_{\text{PAR}}$: một mã chuỗi cha;
- $C_{\text{CHD}}$: một mã chuỗi con;
- $K_{\text{CHD}}^n$: một khóa công khai con bình thường;
- $k_{\text{CHD}}^n$: một khóa riêng con bình thường;
- $K_{\text{CHD}}^h$: một khóa công khai con cứng;
- $k_{\text{CHD}}^h$: một khóa riêng con cứng.

![CYP201](assets/fr/047.webp)

### Cấu Trúc của một Khóa Mở Rộng

Một khóa mở rộng được cấu trúc như sau:
- **Phiên Bản**: Mã phiên bản để xác định bản chất của khóa (`xprv`, `xpub`, `yprv`, `ypub`...). Chúng ta sẽ xem ở cuối chương này những chữ cái `x`, `y`, và `z` tương ứng với gì.
- **Độ Sâu**: Cấp độ phân cấp trong ví HD so với khóa chính (0 đối với khóa chính).
- **Dấu Vân Tay Cha**: 4 byte đầu tiên của băm HASH160 của khóa công khai cha được sử dụng để suy ra khóa có trong payload.
- **Số Chỉ Mục**: Định danh của khóa con trong số các khóa anh em, tức là, trong số tất cả các khóa ở cùng mức suy ra có cùng khóa cha.
- **Mã Chuỗi**: Một mã duy nhất 32 byte để suy ra các khóa con.
- **Khóa**: Khóa riêng (được tiền tố bởi 1 byte cho kích thước) hoặc khóa công khai.
- **Checksum**: Một checksum được tính toán với hàm HASH256 (SHA256 kép) cũng được thêm vào, cho phép xác minh tính toàn vẹn của khóa mở rộng trong quá trình truyền dẫn hoặc lưu trữ.

Định dạng hoàn chỉnh của một khóa mở rộng do đó là 78 byte không kể checksum, và 82 byte với checksum. Sau đó, nó được chuyển đổi sang Base58 để tạo ra một biểu diễn dễ đọc cho người dùng. Định dạng Base58 giống như được sử dụng cho địa chỉ nhận *Legacy* (trước *SegWit*).

| Thành Phần           | Mô Tả                                                                                                        | Kích Thước      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ | --------- |
| Phiên Bản           | Chỉ ra liệu khóa là công khai (`xpub`, `ypub`) hay riêng tư (`xprv`, `zprv`), cũng như phiên bản của khóa mở rộng | 4 byte   |
| Độ Sâu             | Cấp độ trong hệ thống phân cấp so với khóa chính                                                                  | 1 byte    |
| Dấu Vân Tay Cha    | 4 byte đầu tiên của HASH160 của khóa công khai cha                                                                | 4 byte   |
| Số Thứ Tự          | Vị trí của khóa trong thứ tự các khóa con                                                                         | 4 byte   |
| Mã Chuỗi           | Được sử dụng để tạo ra các khóa con                                                                                | 32 byte  |
| Khóa               | Khóa riêng tư (với tiền tố 1 byte) hoặc khóa công khai                                                            | 33 byte  |
| Mã Kiểm Tra        | Mã kiểm tra để xác minh tính toàn vẹn                                                                               | 4 byte   |

Nếu một byte được thêm vào khóa riêng tư, đó là vì khóa công khai nén dài hơn khóa riêng tư một byte. Byte bổ sung này, được thêm vào đầu của khóa riêng tư dưới dạng `0x00`, làm cho kích thước của chúng bằng nhau, đảm bảo rằng payload của khóa mở rộng có cùng chiều dài, cho dù đó là khóa công khai hay khóa riêng tư.

### Tiền Tố Khóa Mở Rộng
Như chúng ta vừa thấy, khóa mở rộng bao gồm một tiền tố chỉ ra cả phiên bản của khóa mở rộng và bản chất của nó. Ký hiệu `pub` chỉ ra rằng nó đề cập đến khóa công khai mở rộng, và ký hiệu `prv` chỉ ra khóa riêng tư mở rộng. Chữ cái bổ sung ở cơ sở của khóa mở rộng giúp chỉ ra liệu tiêu chuẩn được theo dõi là Legacy, SegWit v0, SegWit v1, v.v.
Dưới đây là bảng tổng kết các tiền tố được sử dụng và ý nghĩa của chúng:

| Base 58 Prefix  | Base 16 Prefix  | Network | Purpose             | Associated Scripts  | Derivation            | Key Type     |
| --------------- | --------------- | ------- | ------------------- | ------------------- | --------------------- | ------------ |
| `xpub`          | `0488b21e`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | public       |
| `xprv`          | `0488ade4`      | Mainnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/0'`, `m/86'/0'` | private      |
| `tpub`          | `043587cf`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | public       |
| `tprv`          | `04358394`      | Testnet | Legacy and SegWit V1 | P2PK / P2PKH / P2TR | `m/44'/1'`, `m/86'/1'` | private      |
| `ypub`          | `049d7cb2`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | public       |
| `yprv`          | `049d7878`      | Mainnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/0'`             | private      |
| `upub`          | `049d7cb2`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | public       |
| `uprv`          | `044a4e28`      | Testnet | Nested SegWit       | P2WPKH in P2SH      | `m/49'/1'`             | private      |
| `zpub`          | `04b24746`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | public       |
| `zprv`          | `04b2430c`      | Mainnet | SegWit V0           | P2WPKH              | `m/84'/0'`             | private      |
| `vpub`          | `045f1cf6`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | public       |
| `vprv`          | `045f18bc`      | Testnet | SegWit V0           | P2WPKH              | `m/84'/1'`             | private      |


### Chi Tiết về Các Yếu Tố của Khóa Mở Rộng

Để hiểu rõ hơn về cấu trúc bên trong của một khóa mở rộng, hãy lấy một khóa mở rộng làm ví dụ và phân tích nó. Dưới đây là một khóa mở rộng:

- **Trong Base58**:

```text
xpub6CTNzMUkzpurBWaT4HQoYzLP4uBbGJuWY358Rj7rauiw4rMHCyq3Rfy9w4kyJXJzeFfyrKLUar2rUCukSiDQFa7roTwzjiAhyQAdPLEjqHT
```

- **Trong hệ thập lục phân**:

```text
0488B21E036D5601AD80000000C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A89303772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF50658051F067C3A
```

Khóa mở rộng này được phân tích thành nhiều yếu tố riêng biệt:

1. **Phiên bản**: `0488B21E`

4 byte đầu tiên là phiên bản. Ở đây, nó tương ứng với một khóa công khai mở rộng trên Mainnet với mục đích phát sinh là *Legacy* hoặc *SegWit v1*.

2. **Độ sâu**: `03`

Trường này chỉ ra mức độ phân cấp của khóa trong ví HD. Trong trường hợp này, một độ sâu của `03` có nghĩa là khóa này là ba cấp độ phát sinh dưới khóa chính.

3. **Dấu vân tay của cha mẹ**: `6D5601AD`
Đây là 4 byte đầu tiên của băm HASH160 của khóa công khai cha mẹ được sử dụng để tạo ra `xpub` này.
4. **Số chỉ mục**: `80000000`

Chỉ số này chỉ vị trí của khóa trong số các con của khóa cha mẹ. Tiền tố `0x80` chỉ ra rằng khóa được tạo ra theo cách cứng cáp, và vì phần còn lại được điền bằng số không, nó chỉ ra rằng khóa này là khóa đầu tiên trong số các khóa anh em có thể có.

5. **Mã chuỗi**: `C605DF9FBD77FD6965BD02B77831EC5C78646AD3ACA14DC3984186F72633A893`
6. **Khóa Công Khai**: `03772CCB99F4EF346078D167065404EED8A58787DED31BFA479244824DF5065805`
7. **Checksum**: `1F067C3A`

Checksum tương ứng với 4 byte đầu tiên của băm (SHA256 kép) của tất cả những thứ khác.

Trong chương này, chúng ta đã khám phá ra rằng có hai loại khóa con khác nhau. Chúng ta cũng học được rằng việc tạo ra những khóa con này đòi hỏi một khóa (dù là khóa riêng tư hay khóa công khai) và mã chuỗi của nó. Trong chương tiếp theo, chúng ta sẽ xem xét chi tiết bản chất của những loại khóa khác nhau này và cách tạo ra chúng từ khóa cha mẹ và mã chuỗi của chúng.

## Tạo ra Cặp Khóa Con
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Việc tạo ra cặp khóa con trong ví HD Bitcoin dựa trên một cấu trúc phân cấp cho phép tạo ra một số lượng lớn khóa, trong khi tổ chức những cặp này vào các nhóm khác nhau thông qua các nhánh. Mỗi cặp con được tạo ra từ một cặp cha mẹ có thể được sử dụng trực tiếp trong *scriptPubKey* để khóa bitcoin, hoặc làm điểm bắt đầu để tạo ra nhiều khóa con hơn, và cứ thế, tạo ra một cây khóa.

Tất cả những việc tạo ra này bắt đầu với khóa chính và mã chuỗi chính, đó là cha mẹ đầu tiên ở mức độ sâu 0. Chúng, theo một cách nào đó, là Adam và Eva của các khóa trong ví của bạn, tổ tiên chung của tất cả các khóa được tạo ra.

![CYP201](assets/fr/048.webp)

Hãy khám phá cách hoạt động xác định này.

### Các Loại Tạo ra Khóa Con Khác Nhau

Như chúng ta đã đề cập sơ lược trong chương trước: khóa con được chia thành hai loại chính:
1. **Khóa con bình thường** ($k_{\text{CHD}}^n, K_{\text{CHD}}^n$): Những khóa này được tạo ra từ khóa công khai mở rộng ($K_{\text{PAR}}$), hoặc khóa riêng tư mở rộng ($k_{\text{PAR}}$), bằng cách đầu tiên tạo ra khóa công khai.
2. **Khóa con cứng cáp** ($k_{\text{CHD}}^h, K_{\text{CHD}}^h$): Những khóa này chỉ có thể được tạo ra từ khóa riêng tư mở rộng ($k_{\text{PAR}}$) và do đó không thể nhìn thấy bởi những người quan sát chỉ có khóa công khai mở rộng.
Mỗi cặp khóa con được xác định bởi một **chỉ số** 32-bit (được gọi là $i$ trong các phép tính của chúng tôi). Các chỉ số cho khóa thông thường nằm trong khoảng từ $0$ đến $2^{31}-1$, trong khi đó các chỉ số cho khóa cứng nằm trong khoảng từ $2^{31}$ đến $2^{32}-1$. Những con số này được sử dụng để phân biệt các cặp khóa anh em trong quá trình suy rộng. Thực tế, mỗi cặp khóa cha mẹ phải có khả năng suy rộng ra nhiều cặp khóa con. Nếu chúng ta áp dụng cùng một phép tính một cách hệ thống từ khóa cha mẹ, tất cả các khóa anh em thu được sẽ giống hệt nhau, điều này không mong muốn. Chỉ số do đó giới thiệu một biến số thay đổi phép tính suy rộng, cho phép phân biệt mỗi cặp anh em. Ngoại trừ việc sử dụng cụ thể trong một số giao thức và tiêu chuẩn suy rộng, chúng tôi thường bắt đầu bằng cách suy rộng khóa con đầu tiên với chỉ số `0`, khóa thứ hai với chỉ số `1`, và cứ thế tiếp tục.
### Quy Trình Suy Rộng với HMAC-SHA512

Việc suy rộng mỗi khóa con dựa trên hàm HMAC-SHA512, mà chúng tôi đã thảo luận trong Phần 2 về hàm băm. Nó nhận hai đầu vào: mã chuỗi cha $C_{\text{PAR}}$ và sự kết hợp của khóa cha (hoặc khóa công khai $K_{\text{PAR}}$ hoặc khóa riêng tư $k_{\text{PAR}}$, tùy thuộc vào loại khóa con mong muốn) và chỉ số. Đầu ra của HMAC-SHA512 là một chuỗi 512-bit, được chia thành hai phần:
- **32 byte đầu tiên** (hoặc $h_1$) được sử dụng để tính toán cặp khóa con mới.
- **32 byte cuối cùng** (hoặc $h_2$) phục vụ như là mã chuỗi mới $C_{\text{CHD}}$ cho cặp khóa con.

Trong tất cả các phép tính của chúng tôi, tôi sẽ ký hiệu $\text{hash}$ là đầu ra của hàm HMAC-SHA512.

![CYP201](assets/fr/049.webp)

#### Suy Rộng Khóa Riêng Tư Con từ Khóa Riêng Tư Cha

Để suy rộng khóa riêng tư con $k_{\text{CHD}}$ từ khóa riêng tư cha $k_{\text{PAR}}$, có hai kịch bản có thể xảy ra tùy thuộc vào việc khóa cứng hay khóa thông thường được mong muốn.

Đối với **khóa con thông thường** ($i < 2^{31}$), việc tính toán $\text{hash}$ như sau:


$$

\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, G \cdot k_{\text{PAR}} \Vert i)

$$
Trong phép tính này, chúng ta thấy rằng hàm HMAC của chúng ta nhận hai đầu vào: trước tiên, mã chuỗi cha, và sau đó là sự kết hợp của chỉ số với khóa công khai liên kết với khóa riêng tư cha. Khóa công khai cha được sử dụng ở đây vì chúng ta đang tìm cách suy rộng một khóa con thông thường, không phải một khóa cứng.
Bây giờ chúng ta có một $\text{hash}$ 64-byte mà chúng ta sẽ chia thành 2 phần 32 byte mỗi phần: $h_1$ và $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}_{[:32]} \quad, \quad h_2 = \text{hash}_{[32:]}

$$

Khóa riêng tư con $k_{\text{CHD}}^n$ sau đó được tính toán như sau:


$$

k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n

$$
Trong phép tính này, thao tác $\text{parse256}(h_1)$ bao gồm việc giải thích 32 byte đầu tiên của $\text{hash}$ như một số nguyên 256-bit. Số này sau đó được cộng với khóa riêng của cha, tất cả được lấy modulo $n$ để giữ cho phép tính nằm trong phạm vi của đường cong elliptic, như chúng ta đã thấy trong phần 3 về chữ ký số. Do đó, để suy ra một khóa riêng con bình thường, mặc dù khóa công khai của cha được sử dụng làm cơ sở cho phép tính trong các đầu vào của hàm HMAC-SHA512, việc có khóa riêng của cha vẫn luôn cần thiết để hoàn thành phép tính.
Từ khóa riêng con này, có thể suy ra khóa công khai tương ứng bằng cách áp dụng ECDSA hoặc Schnorr. Như vậy, chúng ta thu được một cặp khóa hoàn chỉnh.

Sau đó, phần thứ hai của $\text{hash}$ đơn giản được giải thích là mã chuỗi cho cặp khóa con mà chúng ta vừa suy ra:


$$

C\_{\text{CHD}} = h_2

$$

Dưới đây là biểu đồ mô tả tổng quan quá trình suy ra:

![CYP201](assets/fr/050.webp)

Đối với **khóa con cứng** ($i \geq 2^{31}$), phép tính của $\text{hash}$ như sau:


$$

hash = \text{HMAC-SHA512}(C_{\text{PAR}}, 0x00 \Vert k_{\text{PAR}} \Vert i)

$$

Trong phép tính này, chúng ta thấy rằng hàm HMAC của chúng ta nhận hai đầu vào: trước tiên, mã chuỗi của cha, và sau đó là sự nối của chỉ số với khóa riêng của cha. Khóa riêng của cha được sử dụng ở đây vì chúng ta đang tìm cách suy ra một khóa con cứng. Hơn nữa, một byte bằng `0x00` được thêm vào ở đầu khóa. Thao tác này làm cho độ dài của nó khớp với độ dài của một khóa công khai nén.
Vì vậy, bây giờ chúng ta có một $\text{hash}$ 64 byte mà chúng ta sẽ chia thành 2 phần 32 byte mỗi phần: $h_1$ và $h_2$:
$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

Khóa riêng con $k_{\text{CHD}}^h$ sau đó được tính như sau:


$$

k_{\text{CHD}}^h = \text{parse256}(h_1) + k_{\text{PAR}} \mod n

$$

Tiếp theo, chúng ta đơn giản giải thích phần thứ hai của $\text{hash}$ là mã chuỗi cho cặp khóa con mà chúng ta vừa suy ra:


$$

C\_{\text{CHD}} = h_2

$$

Dưới đây là biểu đồ mô tả tổng quan quá trình suy ra:

![CYP201](assets/fr/051.webp)

Chúng ta có thể thấy rằng quá trình suy ra bình thường và quá trình suy ra cứng hoạt động theo cùng một cách, với điểm khác biệt này: quá trình suy ra bình thường sử dụng khóa công khai của cha làm đầu vào cho hàm HMAC, trong khi quá trình suy ra cứng sử dụng khóa riêng của cha.

#### Suy ra khóa công khai con từ khóa công khai của cha
Nếu chúng ta chỉ biết khóa công khai của cha mẹ $K_{\text{PAR}}$ và mã chuỗi liên kết $C_{\text{PAR}}$ tương ứng, tức là, một khóa công khai mở rộng, thì có thể suy ra các khóa công khai con $K_{\text{CHD}}^n$, nhưng chỉ áp dụng cho các khóa con bình thường (không cứng). Nguyên tắc này đặc biệt cho phép theo dõi các chuyển động của một tài khoản trong ví Bitcoin từ `xpub` (*chỉ xem*).

Để thực hiện tính toán này, chúng ta sẽ tính $\text{hash}$ với chỉ số $i < 2^{31}$ (suy ra bình thường):


$$

\text{hash} = \text{HMAC-SHA512}(C_{\text{PAR}}, K_{\text{PAR}} \Vert i)

$$

Trong tính toán này, chúng ta thấy rằng hàm HMAC của chúng ta nhận hai đầu vào: trước tiên là mã chuỗi liên kết của cha mẹ, sau đó là sự nối của chỉ số với khóa công khai của cha mẹ.

Vậy, bây giờ chúng ta có một $hash$ 64 byte mà chúng ta sẽ chia thành 2 phần mỗi phần 32 byte: $h_1$ và $h_2$:


$$

\text{hash} = h_1 \Vert h_2

$$


$$

h_1 = \text{hash}[:32] \quad, \quad h_2 = \text{hash}[32:]

$$

Khóa công khai con $K_{\text{CHD}}^n$ sau đó được tính như sau:


$$

K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}

$$
Nếu $\text{parse256}(h_1) \geq n$ (thứ tự của đường cong elliptic) hoặc nếu $K_{\text{CHD}}^n$ là điểm tại vô cực, suy ra là không hợp lệ, và một chỉ số khác phải được chọn.
Trong tính toán này, hoạt động $\text{parse256}(h_1)$ bao gồm việc giải thích 32 byte đầu tiên của $\text{hash}$ như một số nguyên 256-bit. Số này được sử dụng để tính toán một điểm trên đường cong elliptic thông qua phép cộng và nhân đôi từ điểm sinh $G$. Điểm này sau đó được cộng với khóa công khai của cha mẹ để thu được khóa công khai con bình thường. Do đó, để suy ra một khóa công khai con bình thường, chỉ cần khóa công khai của cha mẹ và mã chuỗi liên kết của cha mẹ; khóa riêng của cha mẹ không bao giờ tham gia vào quá trình này, không giống như việc tính toán khóa riêng của con mà chúng ta đã thấy trước đó.

Tiếp theo, mã chuỗi liên kết của con đơn giản là:


$$

C\_{\text{CHD}} = h_2

$$

Dưới đây là biểu đồ mô tả tổng quan về quá trình suy ra:

![CYP201](assets/fr/052.webp)

### Sự tương ứng giữa khóa công khai và khóa riêng của con

Một câu hỏi có thể nảy sinh là làm thế nào một khóa công khai con bình thường suy ra từ khóa công khai của cha mẹ có thể tương ứng với một khóa riêng con bình thường suy ra từ khóa riêng của cha mẹ tương ứng. Mối liên kết này chính xác được đảm bảo bởi các tính chất của đường cong elliptic. Thực vậy, để suy ra một khóa công khai con bình thường, HMAC-SHA512 được áp dụng theo cùng một cách, nhưng đầu ra của nó được sử dụng khác nhau:
   - **Khóa riêng con bình thường**: $k_{\text{CHD}}^n = \text{parse256}(h_1) + k_{\text{PAR}} \mod n$
   - **Khóa công khai con bình thường**: $K_{\text{CHD}}^n = G \cdot \text{parse256}(h_1) + K_{\text{PAR}}$
Cảm ơn việc thêm vào và nhân đôi các phép toán trên đường cong elliptic, cả hai phương pháp đều tạo ra kết quả nhất quán: khóa công khai được tạo ra từ khóa riêng của con giống hệt với khóa công khai của con được tạo trực tiếp từ khóa công khai của cha.

### Tóm tắt các loại phái sinh

Để tóm tắt, dưới đây là các loại phái sinh khả dĩ:

$$
\begin{array}{|c|c|c|c|}
\hline
\rightarrow & \text{PAR} & \text{CHD} & \text{n/h} \\
\hline
k_{\text{PAR}} \rightarrow k_{\text{CHD}} & k_{\text{PAR}} & \{ k_{\text{CHD}}^n, k_{\text{CHD}}^h \} & \{ n, h \} \\
k_{\text{PAR}} \rightarrow K_{\text{CHD}} & k_{\text{PAR}} & \{ K_{\text{CHD}}^n, K_{\text{CHD}}^h \} & \{ n, h \} \\
K_{\text{PAR}} \rightarrow k_{\text{CHD}} & K_{\text{PAR}} & \times & \times \\
K_{\text{PAR}} \rightarrow K_{\text{CHD}} & K_{\text{PAR}} & K_{\text{CHD}}^n & n \\
\hline
\end{array}
$$

Để tóm tắt, cho đến nay bạn đã học cách tạo ra các yếu tố cơ bản của ví HD: cụm từ ghi nhớ, hạt giống và sau đó là khóa chính và mã chuỗi chính. Bạn cũng đã khám phá cách phái sinh các cặp khóa con trong chương này. Trong chương tiếp theo, chúng ta sẽ khám phá cách các phái sinh này được tổ chức trong ví Bitcoin và cấu trúc nào cần theo dõi để cụ thể nhận được các địa chỉ nhận cũng như các cặp khóa được sử dụng trong *scriptPubKey* và *scriptSig*.

## Cấu Trúc Ví và Đường Dẫn Phái Sinh
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Cấu trúc phân cấp của ví HD trên Bitcoin cho phép tổ chức các cặp khóa theo nhiều cách khác nhau. Ý tưởng là phái sinh, từ khóa riêng chính và mã chuỗi chính, nhiều cấp độ sâu khác nhau. Mỗi cấp độ được thêm vào tương ứng với việc phái sinh một cặp khóa con từ một cặp khóa cha.

Theo thời gian, các BIP khác nhau đã giới thiệu các tiêu chuẩn cho các đường dẫn phái sinh này, nhằm mục đích chuẩn hóa việc sử dụng chúng trên các phần mềm khác nhau. Vì vậy, trong chương này, chúng ta sẽ khám phá ý nghĩa của từng cấp độ phái sinh trong ví HD, theo các tiêu chuẩn này.

### Các Cấp Độ Phái Sinh của một Ví HD

Các đường dẫn phái sinh được tổ chức thành các lớp cấp độ, từ cấp độ 0, đại diện cho khóa chính và mã chuỗi chính, đến các lớp phụ để phái sinh địa chỉ được sử dụng để khóa UTXOs. Các BIP (*Đề Xuất Cải Tiến Bitcoin*) định rõ tiêu chuẩn cho mỗi lớp, giúp hài hòa các thực hành trên các phần mềm quản lý ví khác nhau.

Một đường dẫn phái sinh, do đó, đề cập đến chuỗi các chỉ số được sử dụng để phái sinh các khóa con từ một khóa chính.

**Cấp độ 0: Khóa Chính (BIP32)**

Cấp độ này tương ứng với khóa riêng chính và mã chuỗi chính của ví. Nó được biểu diễn bằng ký hiệu $m/$.

**Cấp độ 1: Mục đích (BIP43)**
Mục tiêu xác định cấu trúc logic của quá trình suy luận. Ví dụ, một địa chỉ P2WPKH sẽ có $/84'/$ tại độ sâu 1 (theo BIP84), trong khi một địa chỉ P2TR sẽ có $/86'/$ (theo BIP86). Lớp này tạo điều kiện tương thích giữa các ví bằng cách chỉ ra các số chỉ mục tương ứng với các số BIP.

Nói cách khác, một khi bạn có khóa chính và mã chuỗi chính, chúng phục vụ như một cặp khóa cha để suy ra một cặp khóa con. Chỉ mục được sử dụng trong quá trình suy ra này có thể là, ví dụ, $/84'/$ nếu ví được dự định sử dụng kịch bản loại SegWit v0. Cặp khóa này sau đó ở độ sâu 1. Vai trò của nó không phải là để khóa bitcoin, mà chỉ đơn giản là phục vụ như một điểm dừng trong hệ thống phân cấp suy ra.

**Độ Sâu 2: Loại Tiền Tệ (BIP44)**

Từ cặp khóa ở độ sâu 1, một quá trình suy ra mới được thực hiện để thu được cặp khóa ở độ sâu 2. Độ sâu này cho phép phân biệt các tài khoản Bitcoin với các loại tiền điện tử khác trong cùng một ví.

Mỗi loại tiền tệ có một chỉ mục duy nhất để đảm bảo tính tương thích trên các ví đa tiền tệ. Ví dụ, đối với Bitcoin, chỉ mục là $/0'/$ (hoặc `0x80000000` trong ký hiệu thập lục phân). Các chỉ mục tiền tệ được chọn trong phạm vi từ $2^{31}$ đến $2^{32}-1$ để đảm bảo suy ra cứng.

Để cho bạn các ví dụ khác, dưới đây là các chỉ mục của một số loại tiền tệ:
- $1'$ (`0x80000001`) cho bitcoin thử nghiệm;
- $2'$ (`0x80000002`) cho Litecoin;
- $60'$ (`0x8000003c`) cho Ethereum...

**Độ Sâu 3: Tài Khoản (BIP32)**

Mỗi ví có thể được chia thành nhiều tài khoản, được đánh số từ $2^{31}$, và được biểu diễn ở độ sâu 3 bởi $/0'/$ cho tài khoản đầu tiên, $/1'/$ cho tài khoản thứ hai, và tiếp tục như vậy. Nói chung, khi đề cập đến một khóa mở rộng `xpub`, nó đề cập đến các khóa ở độ sâu suy ra này.

Sự phân chia thành các tài khoản khác nhau là tùy chọn. Mục tiêu là để đơn giản hóa việc tổ chức ví cho người dùng. Trên thực tế, thường chỉ một tài khoản được sử dụng, thường là tài khoản đầu tiên theo mặc định. Tuy nhiên, trong một số trường hợp, nếu người ta muốn phân biệt rõ ràng các cặp khóa cho các mục đích khác nhau, điều này có thể hữu ích. Ví dụ, có thể tạo một tài khoản cá nhân và một tài khoản chuyên nghiệp từ cùng một hạt giống, với các nhóm khóa hoàn toàn riêng biệt từ độ sâu suy ra này.
**Độ Sâu 4: Chuỗi (BIP32)**
Mỗi tài khoản được xác định tại độ sâu 3 sau đó được cấu trúc thành hai chuỗi:
- **Chuỗi bên ngoài**: Trong chuỗi này, những gì được biết đến là "địa chỉ công khai" được suy ra. Những địa chỉ nhận này được dùng để khóa UTXOs đến từ các giao dịch bên ngoài (nghĩa là, bắt nguồn từ việc tiêu thụ UTXOs không thuộc về bạn). Nói một cách đơn giản, chuỗi bên ngoài này được sử dụng bất cứ khi nào người ta muốn nhận bitcoin. Khi bạn nhấp vào "*nhận*" trong phần mềm ví của mình, luôn luôn là một địa chỉ từ chuỗi bên ngoài được cung cấp cho bạn. Chuỗi này được biểu diễn bởi một cặp khóa suy ra với chỉ mục $/0/$.
- **Chuỗi bên trong (tiền thối)**: Chuỗi này được dành riêng cho các địa chỉ nhận khóa bitcoin đến từ việc tiêu thụ UTXOs thuộc về bạn, nói cách khác, là các địa chỉ tiền thối. Nó được xác định bởi chỉ mục $/1/$.

**Độ Sâu 5: Chỉ Mục Địa Chỉ (BIP32)**
Cuối cùng, độ sâu 5 đại diện cho bước cuối cùng của quá trình phát sinh trong ví. Mặc dù kỹ thuật có thể tiếp tục vô hạn, nhưng các tiêu chuẩn hiện tại dừng lại ở đây. Tại độ sâu cuối cùng này, các cặp khóa sẽ thực sự được sử dụng để khóa và mở khóa các UTXO được phát sinh. Mỗi chỉ số cho phép phân biệt giữa các cặp khóa anh em: do đó, địa chỉ nhận đầu tiên sẽ sử dụng chỉ số $/0/$, địa chỉ thứ hai sử dụng chỉ số $/1/$, và cứ thế tiếp tục.
![CYP201](assets/fr/053.webp)

### Ký Hiệu Của Đường Dẫn Phát Sinh

Đường dẫn phát sinh được viết bằng cách phân tách mỗi cấp độ bằng một dấu gạch chéo ($/$). Mỗi dấu gạch chéo như vậy chỉ ra một sự phát sinh từ một cặp khóa cha mẹ ($k_{\text{PAR}}$, $K_{\text{PAR}}$, $C_{\text{PAR}}$) sang một cặp khóa con ($k_{\text{CHD}}$, $K_{\text{CHD}}$, $C_{\text{CHD}}$). Số được ghi ở mỗi độ sâu tương ứng với chỉ số được sử dụng để phát sinh khóa này từ cha mẹ của nó. Dấu nháy đơn ($'$) đôi khi được đặt bên phải của chỉ số chỉ ra một sự phát sinh cứng ($k_{\text{CHD}}^h$, $K_{\text{CHD}}^h$). Đôi khi, dấu nháy này được thay thế bằng một $h$. Trong trường hợp không có dấu nháy đơn hoặc $h$, đó là một sự phát sinh bình thường ($k_{\text{CHD}}^n$, $K_{\text{CHD}}^n$).
Như chúng ta đã thấy trong các chương trước, chỉ số khóa cứng bắt đầu từ $2^{31}$, hoặc `0x80000000` trong hệ thập lục phân. Do đó, khi một chỉ số được theo sau bởi một dấu nháy đơn trong một đường dẫn phát sinh, $2^{31}$ phải được cộng vào số được chỉ ra để thu được giá trị thực sự sử dụng trong hàm HMAC-SHA512. Ví dụ, nếu đường dẫn phát sinh chỉ ra $/44'/$, chỉ số thực tế sẽ là:
$$

i = 44 + 2^{31} = 2\,147\,483\,692

$$

Trong hệ thập lục phân, đây là `0x8000002C`.

Bây giờ chúng ta đã hiểu các nguyên tắc chính của đường dẫn phát sinh, hãy lấy một ví dụ! Dưới đây là đường dẫn phát sinh cho một địa chỉ nhận Bitcoin:


$$

m / 84' / 0' / 1' / 0 / 7

$$

Trong ví dụ này:
- $84'$ chỉ ra tiêu chuẩn P2WPKH (SegWit v0);
- $0'$ chỉ ra tiền tệ Bitcoin trên mainnet;
- $1'$ tương ứng với tài khoản thứ hai trong ví;
- $0$ chỉ ra rằng địa chỉ nằm trên chuỗi bên ngoài;
- $7$ chỉ ra địa chỉ bên ngoài thứ 8 của tài khoản này.

### Tóm Tắt Cấu Trúc Phát Sinh

| Độ Sâu | Mô Tả              | Ví Dụ Tiêu Chuẩn                   |
| ------ | ------------------ | --------------------------------- |
| 0      | Khóa Chính         | $m/$                              |
| 1      | Mục Đích           | $/86'/$ (P2TR)                    |
| 2      | Tiền Tệ            | $/0'/$ (Bitcoin)                  |
| 3      | Tài Khoản          | $/0'/$ (Tài khoản đầu tiên)       |
| 4      | Chuỗi              | $/0/$ (bên ngoài) hoặc $/1/$ (thay đổi)|
| 5      | Chỉ Số Địa Chỉ     | $/0/$ (địa chỉ đầu tiên)          |
Trong chương tiếp theo, chúng ta sẽ khám phá xem "*output script descriptors*" là gì, một sự đổi mới gần đây được giới thiệu trong Bitcoin Core giúp đơn giản hóa việc sao lưu ví Bitcoin.
## Output script descriptors
<chapterId>e4f1c2d3-9b8a-4d3e-8f2a-7b6c5d4e3f2a</chapterId>
Người ta thường nói rằng chỉ cần cụm từ ghi nhớ là đủ để khôi phục quyền truy cập vào ví. Trên thực tế, mọi thứ phức tạp hơn một chút. Trong chương trước, chúng ta đã xem xét cấu trúc phái sinh của ví HD, và bạn có thể đã nhận thấy quy trình này khá phức tạp. Đường dẫn phái sinh chỉ cho phần mềm biết hướng nào để phái sinh các khóa của người dùng. Tuy nhiên, khi khôi phục ví Bitcoin, nếu không biết những đường dẫn này, chỉ có cụm từ ghi nhớ thôi là không đủ. Nó cho phép lấy khóa chính và mã chuỗi chính, nhưng sau đó cần phải biết các chỉ số được sử dụng để đạt đến các khóa con.

Lý thuyết, sẽ cần phải lưu không chỉ cụm từ ghi nhớ của ví mà còn cả các đường dẫn đến các tài khoản mà chúng ta sử dụng. Trên thực tế, thường có thể lấy lại quyền truy cập vào các khóa con mà không cần thông tin này, miễn là đã tuân theo các tiêu chuẩn. Bằng cách kiểm tra từng tiêu chuẩn một, thường là có thể lấy lại quyền truy cập vào các bitcoin. Tuy nhiên, điều này không được đảm bảo và đặc biệt phức tạp đối với người mới bắt đầu. Ngoài ra, với sự đa dạng hóa của các loại script và sự xuất hiện của các cấu hình phức tạp hơn, thông tin này có thể trở nên khó khăn để suy luận, do đó biến dữ liệu này thành thông tin riêng tư và khó khôi phục bằng cách sử dụng lực lượng cưỡng bức. Đó là lý do tại sao một sự đổi mới gần đây đã được giới thiệu và bắt đầu được tích hợp vào phần mềm ví yêu thích của bạn: các *output script descriptors*.

### Descriptor là gì?

Các "*output script descriptors*", hay đơn giản là "*descriptors*", là các biểu thức có cấu trúc mô tả đầy đủ một script đầu ra (*scriptPubKey*) và cung cấp tất cả thông tin cần thiết để theo dõi các giao dịch liên quan đến một script cụ thể. Chúng giúp quản lý khóa trong ví HD bằng cách cung cấp một mô tả chuẩn hóa và đầy đủ về cấu trúc ví và các loại địa chỉ được sử dụng.

Lợi ích chính của các descriptor nằm ở khả năng của chúng trong việc đóng gói tất cả thông tin thiết yếu để khôi phục một ví vào một chuỗi duy nhất (ngoài cụm từ khôi phục). Bằng cách lưu một descriptor cùng với các cụm từ ghi nhớ liên quan, trở nên có thể khôi phục các khóa riêng tư bằng cách biết chính xác vị trí của chúng trong hệ thống phân cấp. Đối với ví multisig, mà ban đầu việc sao lưu phức tạp hơn, descriptor bao gồm `xpub` của mỗi yếu tố, do đó đảm bảo khả năng tái tạo địa chỉ trong trường hợp có vấn đề.

### Cấu trúc của một descriptor

Một descriptor bao gồm một số yếu tố:
* Các hàm script như `pk` (*Pay-to-PubKey*), `pkh` (*Pay-to-PubKey-Hash*), `wpkh` (*Pay-to-Witness-PubKey-Hash*), `sh` (*Pay-to-Script-Hash*), `wsh` (*Pay-to-Witness-Script-Hash*), `tr` (*Pay-to-Taproot*), `multi` (*Chữ ký đa phần*), và `sortedmulti` (*Chữ ký đa phần với khóa được sắp xếp*);
* Đường dẫn phái sinh, ví dụ, `[d34db33f/44h/0h/0h]` chỉ đường dẫn tài khoản phái sinh và dấu vân tay khóa chính cụ thể;
* Khóa ở các định dạng khác nhau như khóa công khai dạng hex hoặc khóa công khai mở rộng (`xpub`);
* Một mã kiểm tra, đi trước bởi một dấu hash, để xác minh tính toàn vẹn của descriptor.
Ví dụ, một mô tả cho ví P2WPKH (SegWit v0) có thể trông như sau:
```text
wpkh([cdeab12f/84h/0h/0h]xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U/<0;1>/*)#jy0l7nr4
```

Trong mô tả này, hàm phái sinh `wpkh` chỉ ra một loại kịch bản *Pay-to-Witness-Public-Key-Hash*. Nó được theo sau bởi đường dẫn phái sinh chứa:
* `cdeab12f`: dấu vân tay khóa chính;
* `84h`: biểu thị việc sử dụng mục đích BIP84, dành cho địa chỉ SegWit v0;
* `0h`: chỉ ra rằng đó là tiền BTC trên mainnet;
* `0h`: tham chiếu đến số tài khoản cụ thể được sử dụng trong ví.

Mô tả cũng bao gồm khóa công khai mở rộng được sử dụng trong ví này:

```text
xpub6CUGRUonZSQ4TWtTMmzXdrXDtyPWKiKbERr4d5qkSmh5h17C1TjvMt7DJ9Qve4dRxm91CDv6cNfKsq2mK1rMsJKhtRUPZz7MQtp3y6atC1U
```

Tiếp theo, ký hiệu `/<0;1>/*` chỉ ra rằng mô tả có thể tạo ra địa chỉ từ chuỗi bên ngoài (`0`) và chuỗi bên trong (`1`), với một ký tự đại diện (`*`) cho phép phái sinh tuần tự nhiều địa chỉ theo cách có thể cấu hình, tương tự như quản lý "giới hạn khoảng trống" trên phần mềm ví truyền thống.
Cuối cùng, `#jy0l7nr4` đại diện cho checksum để xác minh tính toàn vẹn của mô tả.
Bây giờ bạn đã biết mọi thứ về hoạt động của ví HD trên Bitcoin và quá trình phái sinh cặp khóa. Tuy nhiên, trong những chương cuối, chúng tôi chỉ giới hạn ở việc tạo ra khóa riêng và khóa công khai, mà không đề cập đến việc xây dựng địa chỉ nhận. Đây chính xác sẽ là chủ đề của chương tiếp theo!

## Địa Chỉ Nhận
<chapterId>ca80a89d-f8da-4e09-8c35-43179b65bced</chapterId>

Địa chỉ nhận là các thông tin được nhúng trong *scriptPubKey* để khóa UTXOs mới được tạo. Nói một cách đơn giản, một địa chỉ phục vụ để nhận bitcoin. Hãy khám phá hoạt động của chúng liên quan đến những gì chúng ta đã nghiên cứu trong các chương trước.

### Vai Trò của Địa Chỉ Bitcoin trong Kịch Bản

Như đã giải thích trước đó, vai trò của một giao dịch là chuyển quyền sở hữu bitcoin từ đầu vào sang đầu ra. Quá trình này bao gồm việc tiêu thụ UTXOs làm đầu vào trong khi tạo ra UTXOs mới làm đầu ra. Những UTXOs này được bảo vệ bởi kịch bản, định nghĩa các điều kiện cần thiết để mở khóa quỹ.
Khi một người dùng nhận được bitcoin, người gửi tạo ra một đầu ra UTXO và khóa nó bằng một *scriptPubKey*. Script này chứa các quy tắc thường chỉ định các chữ ký và khóa công khai cần thiết để mở khóa UTXO này. Để chi tiêu UTXO này trong một giao dịch mới, người dùng phải cung cấp thông tin được yêu cầu thông qua một *scriptSig*. Việc thực thi *scriptSig* kết hợp với *scriptPubKey* phải trả về "true" hoặc `1`. Nếu điều kiện này được đáp ứng, UTXO có thể được chi tiêu để tạo ra một UTXO mới, chính nó được khóa bởi một *scriptPubKey* mới, và cứ thế tiếp tục.
![CYP201](assets/fr/054.webp)

Chính xác thì trong *scriptPubKey* là nơi tìm thấy các địa chỉ nhận. Tuy nhiên, việc sử dụng của chúng thay đổi tùy thuộc vào tiêu chuẩn script được áp dụng. Dưới đây là bảng tóm tắt thông tin chứa trong *scriptPubKey* theo tiêu chuẩn được sử dụng, cũng như thông tin được mong đợi trong *scriptSig* để mở khóa *scriptPubKey*.

| Tiêu Chuẩn         | *scriptPubKey*                                              | *scriptSig*                     | *redeem script*     | *witness*                                |
| ------------------ | ----------------------------------------------------------- | ------------------------------- | ------------------- | ---------------------------------------- |
| P2PK               | `<pubkey> OP_CHECKSIG`                                      | `<signature>`                   |                     |                                          |
| P2PKH              | `OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG` | `<signature> <public key>`      |                     |                                          |
| P2SH               | `OP_HASH160 <scriptHash> OP_EQUAL`                          | `<data pushes> <redeem script>` | Dữ liệu tùy ý       |                                          |
| P2WPKH             | `0 <pubKeyHash>`                                            |                                 |                     | `<signature> <public key>`               |
| P2WSH              | `0 <witnessScriptHash>`                                     |                                 |                     | `<data pushes> <witness script>`         |
| P2SH-P2WPKH        | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <pubKeyHash>`    | `<signature> <public key>`               |
| P2SH-P2WSH         | `OP_HASH160 <redeemScriptHash> OP_EQUAL`                    | `<redeem script>`               | `0 <scriptHash>`    | `<data pushes> <witness script>`         |
| P2TR (key path)    | `1 <public key>`                                            |                                 |                     | `<signature>`                            |
| P2TR (script path) | `1 <public key>`                                            |                                 |                     | `<data pushes> <script> <control block>` |

*Nguồn: Bitcoin Core PR review club, Ngày 7 tháng 7 năm 2021 - Gloria Zhao*

Các opcode được sử dụng trong một script được thiết kế để thao tác thông tin, và nếu cần, để so sánh hoặc kiểm tra nó. Hãy lấy ví dụ về một script P2PKH, được viết như sau:

```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Như chúng ta sẽ thấy trong chương này, `<pubKeyHash>` thực sự đại diện cho payload của địa chỉ nhận được sử dụng để khóa UTXO. Để mở khóa *scriptPubKey* này, cần phải cung cấp một *scriptSig* chứa:

```text
<signature> <public key>
```
Trong ngôn ngữ kịch bản, "stack" là một cấu trúc dữ liệu "*LIFO*" ("*Last In, First Out*" - "Vào sau, ra trước") được sử dụng để tạm thời lưu trữ các phần tử trong quá trình thực thi kịch bản. Mỗi thao tác kịch bản đều thao tác với stack này, nơi các phần tử có thể được thêm vào (*push*) hoặc loại bỏ (*pop*). Kịch bản sử dụng các stack này để đánh giá biểu thức, lưu trữ biến tạm thời và quản lý điều kiện.
Quá trình thực thi kịch bản mà tôi vừa đưa ra làm ví dụ tuân theo quy trình này:

- Chúng ta có *scriptSig*, *ScriptPubKey*, và stack:

![CYP201](assets/fr/055.webp)

- *scriptSig* được đẩy vào stack:

![CYP201](assets/fr/056.webp)

- `OP_DUP` nhân bản khóa công khai được cung cấp trong *scriptSig* trên stack:

![CYP201](assets/fr/057.webp)

- `OP_HASH160` trả về băm của khóa công khai vừa được nhân bản:

![CYP201](assets/fr/058.webp)

- `OP_PUSHBYTES_20 <pubKeyHash>` đẩy địa chỉ Bitcoin chứa trong *scriptPubKey* vào stack:

![CYP201](assets/fr/059.webp)

- `OP_EQUALVERIFY` xác minh rằng khóa công khai đã băm khớp với địa chỉ nhận được cung cấp:

![CYP201](assets/fr/060.webp)
`OP_CHECKSIG` kiểm tra chữ ký chứa trong *scriptSig* sử dụng khóa công khai. Opcode này cơ bản thực hiện một quá trình xác minh chữ ký như chúng tôi đã mô tả trong phần 3 của khóa học này:
![CYP201](assets/fr/061.webp)

- Nếu `1` còn lại trên stack, thì kịch bản là hợp lệ:

![CYP201](assets/fr/062.webp)

Vì vậy, để tóm tắt, kịch bản này cho phép xác minh, với sự giúp đỡ của chữ ký số, rằng người dùng tuyên bố sở hữu UTXO này và muốn chi tiêu nó thực sự sở hữu khóa riêng liên kết với địa chỉ nhận được sử dụng trong quá trình tạo UTXO này.

### Các loại địa chỉ Bitcoin khác nhau

Trong quá trình phát triển của Bitcoin, một số mô hình kịch bản chuẩn đã được thêm vào. Mỗi mô hình sử dụng một loại địa chỉ nhận khác nhau. Dưới đây là cái nhìn tổng quan về các mô hình kịch bản chính có sẵn đến nay:

**P2PK (*Pay-to-PubKey*)**:

Mô hình kịch bản này được giới thiệu trong phiên bản đầu tiên của Bitcoin bởi Satoshi Nakamoto. Kịch bản P2PK khóa bitcoin trực tiếp sử dụng khóa công khai thô (do đó, không sử dụng địa chỉ nhận với mô hình này). Cấu trúc của nó đơn giản: nó chứa một khóa công khai và yêu cầu một chữ ký số tương ứng để mở khóa quỹ. Kịch bản này thuộc về tiêu chuẩn "*Legacy*".

**P2PKH (*Pay-to-PubKey-Hash*)**:

Giống như P2PK, kịch bản P2PKH được giới thiệu ngay từ khi Bitcoin ra đời. Khác với người tiền nhiệm, nó khóa bitcoin sử dụng băm của khóa công khai, thay vì sử dụng trực tiếp khóa công khai thô. *scriptSig* sau đó phải cung cấp khóa công khai liên kết với địa chỉ nhận, cũng như một chữ ký hợp lệ. Các địa chỉ tương ứng với mô hình này bắt đầu với `1` và được mã hóa trong *base58check*. Kịch bản này cũng thuộc về tiêu chuẩn "*Legacy*".

**P2SH (*Pay-to-Script-Hash*)**:
Được giới thiệu vào năm 2012 với BIP16, mô hình P2SH cho phép sử dụng băm của một kịch bản tùy ý trong *scriptPubKey*. Kịch bản băm này, được gọi là "*redeemScript*", chứa các điều kiện để mở khóa quỹ. Để chi tiêu một UTXO bị khóa bằng P2SH, cần phải cung cấp một *scriptSig* chứa *redeemScript* gốc cũng như dữ liệu cần thiết để xác thực nó. Mô hình này đặc biệt được sử dụng cho multisigs cũ. Các địa chỉ liên kết với P2SH bắt đầu bằng `3` và được mã hóa trong *base58check*. Kịch bản này cũng thuộc về tiêu chuẩn "*Legacy*".

**P2WPKH (*Pay-to-Witness-PubKey-Hash*)**:
Kịch bản này tương tự như P2PKH, vì nó cũng khóa bitcoins bằng cách sử dụng băm của một khóa công khai. Tuy nhiên, không giống như P2PKH, *scriptSig* được chuyển sang một phần riêng biệt được gọi là "*Witness*". Đôi khi điều này được gọi là "*scriptWitness*" để chỉ bộ bao gồm chữ ký và khóa công khai. Mỗi đầu vào SegWit có *scriptWitness* riêng của mình, và tập hợp các *scriptWitnesses* tạo thành trường *Witness* của giao dịch. Việc di chuyển dữ liệu chữ ký này là một đổi mới được giới thiệu bởi bản cập nhật SegWit, nhằm mục đích đặc biệt là ngăn chặn sự biến đổi của giao dịch do chữ ký ECDSA.

Địa chỉ P2WPKH sử dụng mã hóa *bech32* và luôn bắt đầu bằng `bc1q`. Loại kịch bản này tương ứng với đầu ra SegWit phiên bản 0.

**P2WSH (*Pay-to-Witness-Script-Hash*)**:

Mô hình P2WSH cũng được giới thiệu với bản cập nhật SegWit vào tháng 8 năm 2017. Tương tự như mô hình P2SH, nó khóa bitcoins bằng cách sử dụng băm của một kịch bản. Sự khác biệt chính nằm ở cách chữ ký và kịch bản được tích hợp vào giao dịch. Để chi tiêu bitcoins bị khóa với loại kịch bản này, người nhận phải cung cấp kịch bản gốc, được gọi là *witnessScript* (tương đương với *redeemScript* trong P2SH), cùng với dữ liệu cần thiết để xác thực *witnessScript* này. Cơ chế này cho phép thực hiện các điều kiện chi tiêu phức tạp hơn, như multisigs.

Địa chỉ P2WSH sử dụng mã hóa *bech32* và luôn bắt đầu bằng `bc1q`. Kịch bản này cũng tương ứng với đầu ra SegWit phiên bản 0.

**P2TR (*Pay-to-Taproot*)**:

Mô hình P2TR được giới thiệu với việc triển khai Taproot vào tháng 11 năm 2021. Nó dựa trên giao thức Schnorr cho việc tổng hợp khóa mật mã, cũng như trên một cây Merkle cho các kịch bản thay thế, được gọi là MAST (*Merkelized Alternative Script Tree*). Không giống như các loại kịch bản khác, nơi điều kiện chi tiêu được công bố công khai (hoặc khi nhận hoặc khi chi tiêu), P2TR cho phép ẩn các kịch bản phức tạp sau một khóa công khai duy nhất, rõ ràng.

Về mặt kỹ thuật, một kịch bản P2TR khóa bitcoins trên một khóa công khai Schnorr duy nhất, được ký hiệu là $Q$. Khóa này $Q$ thực sự là sự tổng hợp của một khóa công khai $P$ và một khóa công khai $M$, cái sau được tính từ gốc Merkle của một danh sách *scriptPubKey*. Bitcoins bị khóa với loại kịch bản này có thể được chi tiêu theo hai cách:
- Bằng cách công bố một chữ ký cho khóa công khai $P$ (*key path*).
- Bằng cách thỏa mãn một trong các kịch bản chứa trong cây Merkle (*script path*).
P2TR do đó mang lại sự linh hoạt lớn, khi nó cho phép khóa bitcoin bằng một khóa công khai duy nhất, với nhiều script tùy chọn, hoặc cả hai cùng một lúc. Lợi ích của cấu trúc cây Merkle này là chỉ có script sử dụng để chi tiêu được tiết lộ trong giao dịch, nhưng tất cả các script thay thế khác vẫn được giữ bí mật.

P2TR tương ứng với đầu ra SegWit phiên bản 1, điều này có nghĩa là chữ ký cho các đầu vào P2TR được lưu trữ trong phần *Witness* của giao dịch, và không phải trong *scriptSig*. Địa chỉ P2TR sử dụng mã hóa *bech32m* và bắt đầu với `bc1p`, nhưng chúng khá đặc biệt vì không sử dụng hàm băm cho việc xây dựng của chúng. Thực tế, chúng trực tiếp đại diện cho khóa công khai $Q$ được định dạng đơn giản với metadata. Do đó, đây là một mô hình script gần với P2PK.

Bây giờ chúng ta đã nắm được lý thuyết, hãy chuyển sang thực hành! Trong chương tiếp theo, tôi đề xuất việc tạo ra cả địa chỉ SegWit v0 và địa chỉ SegWit v1 từ một cặp khóa.

## Phát Sinh Địa Chỉ
<chapterId>3ebdc750-4135-4881-b07e-08965941b93e</chapterId>

Hãy cùng nhau khám phá cách tạo ra một địa chỉ nhận từ một cặp khóa nằm, ví dụ, ở độ sâu 5 của một ví HD. Địa chỉ này sau đó có thể được sử dụng trong phần mềm ví để khóa một UTXO.

Vì quá trình tạo ra một địa chỉ phụ thuộc vào mô hình script được chọn, hãy tập trung vào hai trường hợp cụ thể: tạo ra một địa chỉ SegWit v0 trong P2WPKH và một địa chỉ SegWit v1 trong P2TR. Hai loại địa chỉ này bao phủ đại đa số các sử dụng ngày nay.

### Nén Khóa Công Khai

Sau khi thực hiện tất cả các bước phát sinh từ khóa chính đến độ sâu 5 sử dụng các chỉ số phù hợp, chúng ta nhận được một cặp khóa ($k$, $K$) với $K = k \cdot G$. Mặc dù có thể sử dụng khóa công khai này như là để khóa quỹ với tiêu chuẩn P2PK, đó không phải là mục tiêu của chúng ta ở đây. Thay vào đó, chúng ta nhắm đến việc tạo ra một địa chỉ trong P2WPKH trong trường hợp đầu tiên, và sau đó trong P2TR cho một ví dụ khác.

Bước đầu tiên là nén khóa công khai $K$. Để hiểu rõ quá trình này, hãy trước hết nhớ lại một số nguyên tắc cơ bản được đề cập trong phần 3.
Một khóa công khai trên Bitcoin là một điểm $K$ nằm trên một đường cong elliptic. Nó được biểu diễn dưới dạng $(x, y)$, nơi $x$ và $y$ là tọa độ của điểm. Trong dạng không nén, khóa công khai này có kích thước 520 bit: 8 bit cho tiền tố (giá trị ban đầu là `0x04`), 256 bit cho tọa độ $x$, và 256 bit cho tọa độ $y$.
Tuy nhiên, đường cong elliptic có tính chất đối xứng đối với trục x: cho một tọa độ $x$ cụ thể, chỉ có hai giá trị có thể cho $y$: $y$ và $-y$. Hai điểm này nằm ở hai bên của trục x. Nói cách khác, nếu chúng ta biết $x$, chỉ cần chỉ rõ $y$ là chẵn hay lẻ để xác định chính xác điểm trên đường cong.
Để nén một khóa công khai, chỉ cần mã hóa $x$, chiếm 256 bit, và thêm một tiền tố để chỉ định tính chẵn lẻ của $y$. Phương pháp này giảm kích thước của khóa công khai xuống còn 264 bit thay vì 520 bit ban đầu. Tiền tố `0x02` chỉ ra rằng $y$ là số chẵn, và tiền tố `0x03` chỉ ra rằng $y$ là số lẻ.
Hãy lấy một ví dụ để hiểu rõ hơn, với một khóa công khai chưa nén:

```text
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Nếu chúng ta phân tích khóa này, chúng ta có:
   - Tiền tố: `04`;
   - $x$: `678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6`;
   - $y$: `49f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f`

Ký tự thập lục phân cuối cùng của $y$ là `f`. Trong hệ đếm cơ số 10, `f = 15`, tương ứng với một số lẻ. Do đó, $y$ là số lẻ, và tiền tố sẽ là `0x03` để chỉ ra điều này.

Khóa công khai nén trở thành:

```text
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```
Thao tác này áp dụng cho tất cả các mô hình script dựa trên ECDSA, tức là tất cả ngoại trừ P2TR sử dụng Schnorr. Trong trường hợp của Schnorr, như đã giải thích trong phần 3, chúng ta chỉ giữ lại giá trị của $x$, không thêm tiền tố để chỉ định tính chẵn lẻ của $y$, không giống như ECDSA. Điều này được thực hiện nhờ việc chọn một tính chẵn lẻ duy nhất một cách tùy ý cho tất cả các khóa. Điều này cho phép giảm nhẹ không gian lưu trữ cần thiết cho các khóa công khai.
### Phát sinh địa chỉ SegWit v0 (bech32)

Bây giờ, sau khi chúng ta đã có được khóa công khai nén, chúng ta có thể phát sinh một địa chỉ nhận SegWit v0 từ nó.

Bước đầu tiên là áp dụng hàm băm HASH160 lên khóa công khai nén. HASH160 là sự kết hợp của hai hàm băm liên tiếp: SHA256, theo sau là RIPEMD160:


$$

\text{HASH160}(K) = \text{RIPEMD160}(\text{SHA256}(K))

$$

Đầu tiên, chúng ta băm khóa qua SHA256:

```text
SHA256(K) = C489EBD66E4103B3C4B5EAFF462B92F5847CA2DCE0825F4997C7CF57DF35BF3A
```

Sau đó, chúng ta băm kết quả qua RIPEMD160:

```text
RIPEMD160(SHA256(K)) = 9F81322CC88622CA4CCB2A52A21E2888727AA535
```
Chúng tôi đã thu được một băm 160-bit của khóa công khai, đây chính là phần được gọi là payload của địa chỉ. Payload này đại diện cho phần trung tâm và quan trọng nhất của địa chỉ. Nó cũng được sử dụng trong *scriptPubKey* để khóa các UTXO.

Tuy nhiên, để làm cho payload này dễ sử dụng hơn với con người, metadata được thêm vào. Bước tiếp theo bao gồm việc mã hóa băm này thành các nhóm 5 bit dưới dạng thập phân. Sự chuyển đổi thập phân này sẽ hữu ích cho việc chuyển đổi thành *bech32*, được sử dụng bởi địa chỉ sau-SegWit. Băm nhị phân 160-bit do đó được chia thành 32 nhóm 5 bit:

$$
\begin{array}{|c|c|}
\hline
\text{5 bits} & \text{Decimal} \\
\hline
10011 & 19 \\
11110 & 30 \\
00000 & 0 \\
10011 & 19 \\
00100 & 4 \\
01011 & 11 \\
00110 & 6 \\
01000 & 8 \\
10000 & 16 \\
11000 & 24 \\
10001 & 17 \\
01100 & 12 \\
10100 & 20 \\
10011 & 19 \\
00110 & 6 \\
01011 & 11 \\
00101 & 5 \\
01001 & 9 \\
01001 & 9 \\
01010 & 10 \\
00100 & 4 \\
00111 & 7 \\
10001 & 17 \\
01000 & 8 \\
10001 & 17 \\
00001 & 1 \\
11001 & 25 \\
00111 & 7 \\
10101 & 21 \\
00101 & 5 \\
00101 & 5 \\
10101 & 21 \\
\hline
\end{array}
$$
Vậy, chúng ta có:

```text
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
```

Một khi băm được mã hóa thành các nhóm 5 bit, một checksum được thêm vào địa chỉ. Checksum này được sử dụng để xác minh rằng payload của địa chỉ không bị thay đổi trong quá trình lưu trữ hoặc truyền tải. Ví dụ, nó cho phép phần mềm ví kiểm tra xem bạn có nhập sai địa chỉ nhận hay không. Nếu không có sự xác minh này, bạn có thể vô tình gửi bitcoin đến một địa chỉ không chính xác, dẫn đến mất tiền vĩnh viễn, vì bạn không sở hữu khóa công khai hoặc khóa riêng tư liên quan. Do đó, checksum là một biện pháp bảo vệ chống lại lỗi của con người.

Đối với các địa chỉ *Legacy* cũ của Bitcoin, checksum được tính đơn giản từ phần đầu của băm địa chỉ với hàm HASH256. Với sự giới thiệu của SegWit và định dạng *bech32*, mã BCH (*Bose, Ray-Chaudhuri, và Hocquenghem*) hiện được sử dụng. Những mã sửa lỗi này được sử dụng để phát hiện và sửa chữa lỗi trong chuỗi dữ liệu. Chúng đảm bảo rằng thông tin truyền đi đến nơi nhận một cách nguyên vẹn, ngay cả trong trường hợp của những thay đổi nhỏ. Mã BCH được sử dụng trong nhiều lĩnh vực, như SSD, DVD, và mã QR. Ví dụ, nhờ có mã BCH, một mã QR bị che khuất một phần vẫn có thể được đọc và giải mã.

Trong bối cảnh của Bitcoin, mã BCH cung cấp một sự cân bằng tốt hơn giữa kích thước và khả năng phát hiện lỗi so với các hàm băm đơn giản được sử dụng cho địa chỉ *Legacy*. Tuy nhiên, trên Bitcoin, mã BCH chỉ được sử dụng cho việc phát hiện lỗi, không phải sửa lỗi. Do đó, phần mềm ví sẽ báo địa chỉ nhận không chính xác nhưng sẽ không tự động sửa chữa nó. Sự hạn chế này là cố ý: cho phép sửa chữa tự động sẽ giảm khả năng phát hiện lỗi.

Để tính checksum với mã BCH, chúng ta cần chuẩn bị một số yếu tố:
- **Phần Dễ Đọc Cho Con Người (HRP - *Human Readable Part*)**: Đối với mạng chính của Bitcoin, HRP là `bc`;
HRP phải được mở rộng bằng cách tách mỗi ký tự thành hai phần:
- Lấy các ký tự của HRP trong ASCII:
	- `b`: `01100010`
- `c`: `01100011`
- Trích xuất 3 bit quan trọng nhất và 5 bit ít quan trọng nhất:
  - 3 bit quan trọng nhất: `011` (3 trong hệ thập phân)
  - 3 bit quan trọng nhất: `011` (3 trong hệ thập phân)
  - 5 bit ít quan trọng nhất: `00010` (2 trong hệ thập phân)
  - 5 bit ít quan trọng nhất: `00011` (3 trong hệ thập phân)

Với dấu phân cách `0` giữa hai ký tự, sự mở rộng của HRP do đó là:

```text
03 03 00 02 03
```

- **Phiên bản chứng nhận (witness version)**: Đối với SegWit phiên bản 0, đó là `00`;

- **Payload**: Các giá trị thập phân của hash khóa công khai;

- **Dành trữ cho checksum**: Chúng ta thêm 6 số không `[0, 0, 0, 0, 0, 0]` vào cuối chuỗi.

Tất cả dữ liệu kết hợp để nhập vào chương trình để tính toán checksum như sau:

```text
HRP = 03 03 00 02 03
SEGWIT v0 = 00
HASH = 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21
CHECKSUM = 00 00 00 00 00 00

INPUT = 03 03 00 02 03 00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 00 00 00 00 00 00
```

Việc tính toán checksum khá phức tạp. Nó liên quan đến số học trường hữu hạn đa thức. Chúng tôi sẽ không chi tiết việc tính toán này ở đây và sẽ chuyển thẳng đến kết quả. Trong ví dụ của chúng tôi, checksum thu được trong hệ thập phân là:

```text
10 16 11 04 13 18
```

Bây giờ chúng ta có thể xây dựng địa chỉ nhận bằng cách nối theo thứ tự các yếu tố sau:
- **Phiên bản SegWit**: `00`
- **Payload**: Hash khóa công khai
- **Checksum**: Các giá trị thu được ở bước trước (`10 16 11 04 13 18`)

Điều này cho chúng ta trong hệ thập phân:

```text
00 19 30 00 19 04 11 06 08 16 24 17 12 20 19 06 11 05 09 09 10 04 07 17 08 17 01 25 07 21 09 09 21 10 16 11 04 13 18
```

Sau đó, mỗi giá trị thập phân phải được ánh xạ vào ký tự *bech32* của nó sử dụng bảng chuyển đổi sau:

$$
\begin{array}{|c|c|c|c|c|c|c|c|c|}
\hline
 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
\hline
+0 & q & p & z & r & y & 9 & x & 8 \\
\hline
+8 & g & f & 2 & t & v & d & w & 0 \\
\hline
+16 & s & 3 & j & n & 5 & 4 & k & h \\
\hline
+24 & c & e & 6 & m & u & a & 7 & l \\
\hline
\end{array}
$$

Để chuyển đổi một giá trị thành một ký tự *bech32* sử dụng bảng này, chỉ cần tìm giá trị trong cột đầu tiên và hàng đầu tiên mà, khi cộng lại, cho kết quả mong muốn. Sau đó, lấy ký tự tương ứng. Ví dụ, số thập phân `19` sẽ được chuyển đổi thành chữ `n`, bởi vì $19 = 16 + 3$.
Bằng cách ánh xạ tất cả giá trị của chúng ta, chúng ta nhận được địa chỉ sau:

```
qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Tất cả những gì còn lại là thêm HRP `bc`, chỉ ra rằng đó là một địa chỉ cho Bitcoin mainnet, cũng như dấu phân cách `1`, để nhận được địa chỉ nhận hoàn chỉnh:

```
bc1qn7qnytxgsc3v5nxt9ff2y83g3pe849942stydj
```

Đặc điểm của bảng chữ cái *bech32* này là nó bao gồm tất cả các ký tự chữ và số trừ `1`, `b`, `i`, và `o` để tránh sự nhầm lẫn về mặt hình ảnh giữa các ký tự tương tự, đặc biệt trong quá trình nhập hoặc đọc bởi con người.

Tóm lại, đây là quy trình suy ra:

![CYP201](assets/fr/065.webp)

Đây là cách để suy ra một địa chỉ nhận P2WPKH (SegWit v0). Bây giờ chúng ta hãy chuyển sang địa chỉ P2TR (SegWit v1 / Taproot) và khám phá quy trình tạo ra chúng.

### Suy Ra Địa Chỉ SegWit v1 (bech32m)

Đối với địa chỉ Taproot, quy trình tạo ra có một số điểm khác biệt nhỏ. Hãy cùng xem xét điều này!

Từ bước nén khóa công khai, một sự khác biệt đầu tiên xuất hiện so với ECDSA: các khóa công khai được sử dụng cho Schnorr trên Bitcoin chỉ được biểu diễn bởi hoành độ ($x$) của chúng. Do đó, không có tiền tố, và khóa nén đo chính xác 256 bit.
Như chúng ta đã thấy trong chương trước, một kịch bản P2TR khóa bitcoin trên một khóa công khai Schnorr duy nhất, được chỉ định bởi $Q$. Khóa này $Q$ là sự tổng hợp của hai khóa công khai: $P$, một khóa công khai nội bộ chính, và $M$, một khóa công khai được suy ra từ gốc Merkle của một danh sách *scriptPubKey*. Bitcoin bị khóa với loại kịch bản này có thể được chi tiêu theo hai cách:
- Bằng cách công bố một chữ ký cho khóa công khai $P$ (*con đường khóa*);
- Bằng cách thỏa mãn một trong các kịch bản bao gồm trong cây Merkle (*con đường kịch bản*).

Trên thực tế, hai khóa này không thực sự được "tổng hợp." Khóa $P$ thay vì vậy được điều chỉnh bởi khóa $M$. Trong mật mã học, "điều chỉnh" một khóa công khai có nghĩa là sửa đổi khóa này bằng cách áp dụng một giá trị cộng gọi là "tweak." Thao tác này cho phép khóa đã sửa đổi vẫn tương thích với khóa riêng tư gốc và tweak. Về mặt kỹ thuật, một tweak là một giá trị vô hướng $t$ được cộng vào khóa công khai ban đầu. Nếu $P$ là khóa công khai gốc, khóa đã điều chỉnh trở thành:


$$

P' = P + tG

$$

Nơi $G$ là sinh của đường cong elliptic được sử dụng. Thao tác này tạo ra một khóa công khai mới được suy ra từ khóa gốc, trong khi vẫn giữ các tính chất mật mã học cho phép sử dụng nó.
Nếu bạn không cần thêm các kịch bản thay thế (chi tiêu độc quyền qua *key path*), bạn có thể tạo một địa chỉ Taproot dựa hoàn toàn vào khóa công khai hiện có ở độ sâu 5 trong ví của bạn. Trong trường hợp này, cần tạo một kịch bản không thể chi tiêu cho *script path*, nhằm đáp ứng yêu cầu của cấu trúc. Sau đó, tweak $t$ được tính toán bằng cách áp dụng một hàm băm có gắn thẻ, **`TapTweak`**, trên khóa công khai nội bộ $P$:
$$

t = \text{H}\_{\text{TapTweak}}(P)

$$

trong đó:
- **$\text{H}_{\text{TapTweak}}$** là một hàm băm SHA256 có gắn thẻ với thẻ `TapTweak`. Nếu bạn không quen với hàm băm có gắn thẻ là gì, tôi mời bạn tham khảo chương 3.3;
- $P$ là khóa công khai nội bộ, được biểu diễn ở dạng nén 256-bit, chỉ sử dụng tọa độ $x$.

Khóa công khai Taproot $Q$ sau đó được tính toán bằng cách cộng tweak $t$, nhân với bộ sinh đường cong elliptic $G$, vào khóa công khai nội bộ $P$:


$$

Q = P + t \cdot G

$$
Một khi khóa công khai Taproot $Q$ được thu được, chúng ta có thể tạo địa chỉ nhận tương ứng. Khác với các định dạng khác, địa chỉ Taproot không được thiết lập dựa trên băm của khóa công khai. Do đó, khóa $Q$ được chèn trực tiếp vào địa chỉ, một cách nguyên thủy.

Để bắt đầu, chúng ta trích xuất tọa độ $x$ của điểm $Q$ để thu được một khóa công khai nén. Trên payload này, một mã kiểm tra được tính toán sử dụng mã BCH, giống như với địa chỉ SegWit v0. Tuy nhiên, chương trình được sử dụng cho địa chỉ Taproot khác một chút. Thực tế, sau khi giới thiệu định dạng *bech32* với SegWit, một lỗi đã được phát hiện: khi ký tự cuối cùng của một địa chỉ là `p`, việc chèn hoặc loại bỏ `q` ngay trước `p` này không làm cho mã kiểm tra trở nên không hợp lệ. Mặc dù lỗi này không có hậu quả đối với SegWit v0 (nhờ vào một ràng buộc kích thước), nó có thể gây ra vấn đề trong tương lai. Lỗi này do đó đã được sửa chữa cho địa chỉ Taproot, và định dạng mới được sửa chữa được gọi là "*bech32m*".

Địa chỉ Taproot được tạo ra bằng cách mã hóa tọa độ $x$ của $Q$ trong định dạng *bech32m*, với các yếu tố sau:
- **Phần HRP (*Human Readable Part*)**: `bc`, để chỉ mạng Bitcoin chính;
- **Phiên bản**: `1` để chỉ Taproot / SegWit v1;
- **Mã kiểm tra**.

Địa chỉ cuối cùng sẽ có định dạng:

```
bc1p[Qx][checksum]
```

Mặt khác, nếu bạn muốn thêm các kịch bản thay thế ngoài việc chi tiêu với khóa công khai nội bộ (*script path*), việc tính toán địa chỉ nhận sẽ khác một chút. Bạn sẽ cần bao gồm băm của các kịch bản thay thế trong việc tính toán tweak. Trong Taproot, mỗi kịch bản thay thế, nằm ở cuối cây Merkle, được gọi là một "lá".

Một khi các kịch bản thay thế khác nhau được viết, bạn phải đưa chúng qua một hàm băm có gắn thẻ `TapLeaf`, kèm theo một số metadata:


$$

\text{h}_{\text{leaf}} = \text{H}_{\text{TapLeaf}} (v \Vert sz \Vert S)

$$

Với:
- $v$: số phiên bản kịch bản (mặc định `0xC0` cho Taproot);
- $sz$: kích thước của script được mã hóa theo định dạng *CompactSize*; 
- $S$: script.

Các hash script khác nhau ($\text{h}_{\text{leaf}}$) được sắp xếp theo thứ tự từ điển trước tiên. Sau đó, chúng được nối lại với nhau thành từng cặp và đưa qua hàm băm có gắn thẻ `TapBranch`. Quá trình này được lặp lại từng bước để xây dựng cây Merkle:
$$
\text{h}_{\text{branch}} = \text{H}_{\text{TapBranch}}(\text{h}_{\text{leaf1}} \Vert \text{h}_{\text{leaf2}})
$$

Chúng ta tiếp tục bằng cách nối kết quả thành từng cặp, đưa chúng qua hàm băm có gắn thẻ `TapBranch` ở mỗi bước, cho đến khi chúng ta thu được gốc của cây Merkle:

![CYP201](assets/fr/066.webp)

Sau khi tính toán được gốc Merkle $h_{\text{root}}$, chúng ta có thể tính toán tweak. Để làm điều này, khóa công khai nội bộ của ví $P$ được nối với gốc $h_{\text{root}}$, và kết quả được đưa qua hàm băm có gắn thẻ `TapTweak`:

$$
t = \text{H}_{\text{TapTweak}}(P \Vert h_{\text{root}})
$$

Cuối cùng, giống như trước đây, khóa công khai Taproot $Q$ được tạo bằng cách thêm khóa công khai nội bộ $P$ với tích của tweak $t$ và điểm tạo $G$:

$$
Q = P + t \cdot G
$$

Sau đó, việc tạo địa chỉ sẽ tiếp tục theo cùng một quy trình, sử dụng khóa công khai $Q$ thô làm payload, cùng với một số siêu dữ liệu bổ sung.


Và đó là tất cả! Chúng ta đã đến cuối khóa học CYP201. Nếu bạn thấy khóa học này hữu ích, tôi sẽ rất biết ơn nếu bạn có thể dành vài phút để đánh giá cao nó trong chương đánh giá tiếp theo. Đừng ngần ngại chia sẻ nó với người thân yêu của bạn hoặc trên các mạng xã hội của bạn. Cuối cùng, nếu bạn muốn nhận bằng chứng nhận cho khóa học này, bạn có thể tham gia kỳ thi cuối cùng ngay sau chương đánh giá.

# Kết luận
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Đánh giá khóa học này
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Bài kiểm tra cuối cùng
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>

## Kết luận
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

Chúng ta đã đến cuối khóa đào tạo CYP201. Tôi hy vọng nó đã hữu ích trong hành trình học Bitcoin của bạn và đã giúp bạn hiểu rõ hơn về cách hoạt động của các ví HD mà bạn sử dụng hàng ngày. Cảm ơn bạn đã theo dõi khóa học này đến cuối!

Theo tôi, kiến thức về ví này là cơ bản, vì nó kết nối khía cạnh lý thuyết của Bitcoin với việc sử dụng thực tế. Thực tế, nếu bạn sử dụng Bitcoin, bạn nhất thiết phải xử lý phần mềm ví. Hiểu cách hoạt động bên trong của chúng cho phép bạn thực hiện các chiến lược bảo mật hiệu quả trong khi nắm vững các cơ chế cơ bản, rủi ro và điểm yếu tiềm ẩn. Nhờ đó, bạn có thể sử dụng Bitcoin an toàn và tự tin hơn.

Nếu bạn chưa làm điều này, tôi mời bạn đánh giá và bình luận về khóa đào tạo này. Điều đó sẽ giúp tôi rất nhiều. Bạn cũng có thể chia sẻ khóa đào tạo này trên mạng xã hội của mình để lan truyền kiến thức này đến càng nhiều người càng tốt.

Để tiếp tục hành trình của bạn xuống hang thỏ, tôi đặc biệt khuyến nghị khóa đào tạo **BTC204**, mà tôi cũng đã sản xuất trên Plan ₿ Network. Nó dành riêng cho quyền riêng tư Bitcoin và khám phá các chủ đề chính: Mô hình quyền riêng tư là gì? Phân tích chuỗi hoạt động như thế nào? Làm thế nào để sử dụng Bitcoin tối ưu để tối đa hóa quyền riêng tư của bạn? Một bước tiếp theo hợp lý để nâng cao kỹ năng của bạn!

https://planb.network/courses/btc204

Ngoài ra, để tiếp tục đào sâu kiến thức của bạn trong vũ trụ Bitcoin, chúng tôi mời bạn khám phá các khóa học khác có sẵn trên Plan ₿ Network như:

#### Học cách tạo cộng đồng Bitcoin của bạn với
https://planb.network/courses/btc302

#### Khám phá Lightning Network với
https://planb.network/courses/lnp201

#### Khám phá tư duy kinh tế của Trường phái Áo với
https://planb.network/courses/eco201

#### Khám phá lịch sử nguồn gốc của Bitcoin với
https://planb.network/courses/his201

#### Khám phá sự phát triển của tự do qua các thời đại với
https://planb.network/courses/phi201
$$




