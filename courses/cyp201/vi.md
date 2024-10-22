---
name: Giới thiệu về Mật mã học Bitcoin
goal: Hiểu về việc tạo ví Bitcoin từ góc độ mật mã học
objectives:
  - Làm sáng tỏ thuật ngữ mật mã học liên quan đến Bitcoin.
  - Nắm vững cách tạo ví Bitcoin.
  - Hiểu về cấu trúc của ví Bitcoin.
  - Hiểu về địa chỉ và đường dẫn phái sinh.
---

# Hành trình vào thế giới Mật mã học

Bạn có bị cuốn hút bởi Bitcoin không? Tự hỏi một ví Bitcoin hoạt động như thế nào? Hãy chuẩn bị sẵn sàng cho một hành trình hấp dẫn vào thế giới mật mã học! Loïc, chuyên gia của chúng tôi, sẽ hướng dẫn bạn qua những phức tạp trong việc tạo ví Bitcoin, giải mã những bí ẩn đằng sau các thuật ngữ kỹ thuật đáng sợ như băm, phái sinh khóa, và đường cong elliptic.

Khóa học này không chỉ trang bị cho bạn kiến thức để hiểu về cấu trúc của ví Bitcoin mà còn chuẩn bị cho bạn sẵn sàng đào sâu vào thế giới mật mã học thú vị. Vậy, bạn đã sẵn sàng tham gia vào hành trình này chưa? Hãy tham gia cùng chúng tôi và biến sự tò mò của bạn thành chuyên môn!

+++

# Giới thiệu
<partId>32960669-d13a-592f-a053-37f70b997cbf</partId>

## Giới thiệu về Mật mã học
<chapterId>fb4e8857-ea35-5a8a-ae8a-5300234e0104</chapterId>

### Khóa học này có dành cho bạn không? CÓ!

Chúng tôi rất vui mừng chào đón bạn đến với khóa học mới có tên "Crypto 301: Giới thiệu về Mật mã học và Ví HD", do chuyên gia trong lĩnh vực, Loïc Morel, dẫn dắt. Khóa học này sẽ đưa bạn vào thế giới mật mã học hấp dẫn, một ngành khoa học cơ bản của toán học đảm bảo việc mã hóa và bảo mật dữ liệu của bạn.

Trong cuộc sống hàng ngày, và đặc biệt trong lĩnh vực Bitcoin, mật mã học đóng một vai trò quan trọng. Các khái niệm liên quan đến mật mã học, như khóa riêng, khóa công khai, địa chỉ, đường dẫn phái sinh, seed và entropy, là cốt lõi của việc sử dụng và tạo ví Bitcoin. Trong suốt khóa học này, Loïc sẽ giải thích chi tiết cách khóa riêng được tạo ra và chúng liên kết với địa chỉ như thế nào. Loïc cũng sẽ dành một giờ để giải thích chi tiết toán học của đường cong elliptic. Ngoài ra, bạn sẽ hiểu tại sao việc sử dụng HMAC SHA512 quan trọng để bảo vệ ví của bạn và sự khác biệt giữa seed và cụm từ ghi nhớ là gì.
Mục tiêu cuối cùng của khóa học này là để bạn có thể hiểu các quy trình kỹ thuật liên quan trong việc tạo một ví HD và các phương pháp mật mã học được sử dụng. Trải qua nhiều năm, ví Bitcoin đã phát triển để trở nên dễ sử dụng hơn, an toàn hơn và được chuẩn hóa nhờ vào các BIP cụ thể. Loïc sẽ giúp bạn hiểu những BIP này để nắm bắt được những lựa chọn mà các nhà phát triển Bitcoin và các nhà mật mã học đã thực hiện. Như tất cả các khóa học do trường đại học của chúng tôi cung cấp, khóa học này hoàn toàn miễn phí và mã nguồn mở. Điều này có nghĩa là bạn có thể tự do tham gia và sử dụng nó theo ý muốn của mình. Chúng tôi mong chờ nhận được phản hồi của bạn vào cuối khóa học thú vị này.

### Sân khấu thuộc về giáo sư!

Xin chào mọi người, tôi là Loïc Morel, người hướng dẫn bạn qua cuộc khám phá kỹ thuật này về mật mã học được sử dụng trong ví Bitcoin.

Hành trình của chúng ta bắt đầu với việc khám phá sâu vào các hàm băm mật mã học. Cùng nhau, chúng ta sẽ phân tích cấu trúc bên trong của SHA256 thiết yếu và khám phá các thuật toán dành riêng cho phái sinh.

Chúng ta sẽ tiếp tục cuộc phiêu lưu bằng cách giải mã thế giới bí ẩn của chữ ký số. Bạn sẽ khám phá cách ma thuật của đường cong elliptic áp dụng cho những chữ ký này, và chúng ta sẽ làm sáng tỏ cách tính khóa công khai từ khóa riêng. Và tất nhiên, chúng ta sẽ đi sâu vào quy trình của chữ ký số.

Tiếp theo, chúng ta sẽ quay ngược thời gian để xem sự phát triển của ví Bitcoin, và chúng ta sẽ khám phá các khái niệm về entropy và số ngẫu nhiên. Chúng ta sẽ xem xét cụm từ ghi nhớ nổi tiếng, đồng thời cũng chạm vào passphrase. Bạn thậm chí còn có cơ hội trải nghiệm điều độc đáo bằng cách tạo seed từ 128 lần lắc xúc xắc!
Với những nền tảng vững chắc này, chúng ta sẽ sẵn sàng cho phần quan trọng: tạo một ví Bitcoin. Từ sự ra đời của seed và master key, đến việc nghiên cứu các extended keys, và sự phái sinh của các cặp child key, mỗi bước sẽ được phân tích kỹ lưỡng. Chúng ta cũng sẽ thảo luận về cấu trúc của ví và các con đường phái sinh.

Để kết thúc, chúng ta sẽ kết thúc hành trình của mình bằng cách xem xét các địa chỉ Bitcoin. Chúng ta sẽ giải thích cách chúng được tạo ra và vai trò thiết yếu của chúng trong việc hoạt động của ví Bitcoin.

Hãy tham gia cùng tôi trong hành trình hấp dẫn này, và chuẩn bị sẵn sàng để khám phá thế giới của mật mã học như chưa từng có trước đây. Bỏ lại những quan niệm trước cửa và mở lòng mình với một cách hiểu mới về Bitcoin và cấu trúc cơ bản của nó.

# Hàm Băm
<partId>3713fee1-2ec2-512e-9e97-b6da9e4d2f17</partId>

## Giới thiệu về hàm băm mật mã liên quan đến Bitcoin
<chapterId>dba011f5-1805-5a48-ac2b-4bd637c93703</chapterId>

Chào mừng bạn đến với phiên hôm nay, dành riêng cho việc đắm chìm sâu vào thế giới mật mã của hàm băm, một trụ cột quan trọng của bảo mật giao thức Bitcoin. Hãy tưởng tượng hàm băm như một robot giải mã mật mã cực kỳ hiệu quả, biến đổi thông tin với bất kỳ kích thước nào thành một dấu vân tay số duy nhất và cố định, được gọi là "hash," "digest," hoặc "checksum."
Tóm lại, hàm băm nhận một thông điệp đầu vào với kích thước tùy ý và chuyển đổi nó thành một dấu vân tay đầu ra cố định.

Mô tả hồ sơ của hàm băm mật mã đòi hỏi phải hiểu hai đặc tính thiết yếu: tính không thể đảo ngược và khả năng chống giả mạo.

Tính không thể đảo ngược, hay khả năng chống preimage, có nghĩa là việc tính toán đầu ra từ đầu vào có thể thực hiện dễ dàng, nhưng việc tính toán đầu vào từ đầu ra là không thể.
Đó là một hàm một chiều.

![image](assets/image/section1/0.webp)

Khả năng chống giả mạo đến từ việc thậm chí chỉ một sự thay đổi nhỏ nhất của đầu vào cũng sẽ dẫn đến một đầu ra hoàn toàn khác biệt.
Những hàm này cho phép xác minh tính toàn vẹn của phần mềm được tải xuống.

![image](assets/image/section1/1.webp)

Một đặc tính quan trọng khác mà chúng sở hữu là khả năng chống va chạm và chống second preimage. Một va chạm xảy ra khi hai đầu vào khác nhau tạo ra cùng một đầu ra.
Chắc chắn, trong vũ trụ băm, va chạm là không thể tránh khỏi, nhưng một hàm băm mật mã tốt giảm thiểu chúng đáng kể. Rủi ro phải đủ thấp để có thể coi là không đáng kể. Đó giống như mỗi hash là một ngôi nhà trong một thành phố rộng lớn; mặc dù số lượng ngôi nhà khổng lồ, một hàm băm tốt đảm bảo rằng mỗi ngôi nhà có một địa chỉ duy nhất.

Khả năng chống second preimage phụ thuộc vào khả năng chống va chạm; nếu có khả năng chống va chạm, thì cũng có khả năng chống second preimage.
Với một thông tin đầu vào được áp đặt cho chúng ta, chúng ta phải tìm một đầu vào thứ hai, khác với cái đầu tiên, tạo ra một va chạm trong đầu ra hash của hàm. Khả năng chống second preimage tương tự như khả năng chống va chạm, ngoại trừ việc đầu vào được áp đặt.
Giờ đây, hãy cùng điều hướng qua những vùng nước động của các hàm băm lỗi thời. SHA0, SHA1, và MD5 hiện được coi là những vỏ sò gỉ sét trong đại dương của băm mật mã. Chúng thường được khuyến cáo không sử dụng vì đã mất khả năng chống va chạm. Nguyên tắc pigeonhole giải thích tại sao, mặc dù nỗ lực hết sức, việc tránh va chạm là không thể do giới hạn của kích thước đầu ra. Để thực sự được coi là an toàn, một hàm băm phải chống lại va chạm, second preimages, và preimages.

Một yếu tố then chốt trong giao thức Bitcoin, hàm băm SHA-256 là thuyền trưởng của con tàu. Các hàm khác, như SHA-512, được sử dụng cho việc phái sinh với HMAC và PBKDF. Ngoài ra, RIPMD160 được sử dụng để giảm một dấu vân tay xuống còn 160 bit. Khi chúng ta đề cập đến HASH256 và HASH160, chúng ta đang nói đến việc sử dụng băm kép với SHA-256 và RIPMD.
SHA256(SHA256(thông điệp))$$
Đối với HASH160, đây là một hash kép của thông điệp sử dụng SHA256 trước, sau đó là RIPMD160.
$$
RIPMD160(SHA256(thông điệp))
$$
Việc sử dụng HASH160 đặc biệt có lợi vì nó cho phép bảo mật của SHA-256 trong khi giảm kích thước của dấu vân tay.

Tóm lại, mục tiêu cuối cùng của một hàm băm mật mã là biến đổi thông tin kích thước tùy ý thành một dấu vân tay cố định kích thước. Để được công nhận là an toàn, nó phải có một số điểm mạnh: không thể đảo ngược, kháng sự can thiệp, kháng va chạm, và kháng ảnh trước thứ hai.

![hình ảnh](assets/image/section1/2.webp)

Kết thúc cuộc khám phá này, chúng ta đã làm sáng tỏ các hàm băm mật mã, nêu bật các ứng dụng của chúng trong giao thức Bitcoin, và phân tích các mục tiêu cụ thể của chúng. Chúng ta đã học được rằng để các hàm băm được coi là an toàn, chúng phải chống lại ảnh trước, ảnh trước thứ hai, va chạm, và can thiệp. Chúng ta cũng đã bao quát các loại hàm băm khác nhau được sử dụng trong giao thức Bitcoin. Trong phiên tiếp theo, chúng ta sẽ đi sâu vào cốt lõi của hàm băm SHA256 và khám phá những toán học thú vị tạo nên đặc điểm độc đáo của nó.

## Cơ Chế Hoạt Động của SHA256
<chapterId>905eb320-f15b-5fb6-8d2d-5bb447337deb</chapterId>

Chào mừng bạn đến với tiếp tục hành trình thú vị qua mê cung mật mã của hàm băm. Hôm nay, chúng ta sẽ khám phá bí mật của SHA256, một quy trình phức tạp nhưng tài tình mà chúng ta đã giới thiệu trước đó.

Nhắc lại, mục đích của hàm băm SHA256 là nhận một thông điệp đầu vào với bất kỳ kích thước nào và tạo ra một băm 256-bit làm đầu ra.

### Tiền xử lý

Hãy tiến xa hơn trong mê cung này bằng cách bắt đầu với tiền xử lý của SHA256.

#### Thêm Bit Đệm

Mục tiêu của bước đầu tiên này là có một thông điệp được cân bằng thành một bội số của 512 bit. Để đạt được điều này, chúng ta sẽ thêm các bit đệm vào thông điệp.

Hãy để M là kích thước thông điệp ban đầu.
Hãy để 1 là một bit dành cho dấu phân cách.
Hãy để P là số bit được sử dụng cho đệm, và 64 là số bit dành riêng cho giai đoạn tiền xử lý thứ hai.
Tổng số phải là một bội số của 512 bit, được biểu diễn bởi n.

![hình ảnh](assets/image/section1/3.webp)

Ví dụ với một thông điệp đầu vào 950 bit:

```
Bước 1: Xác định kích thước; số bit mong muốn cuối cùng.
Bội số đầu tiên của 512 > (M + 64 + 1) (với M = 950) là 1024.
1024 = 2 * 512
Vậy n = 2.

Bước 2: Xác định P, số bit đệm cần thiết để đạt được số bit mong muốn cuối cùng.
-> M + 1 + P + 64 = n * 512
-> M + 1 + P + 64 = 2 * 512
-> 950 + 1 + P + 64 = 1024
-> P = 1024 - 1 - 64 - 950
-> P = 9

Vì vậy, cần thêm 9 bit đệm để có một thông điệp được cân bằng thành một bội số của 512.
```

Và bây giờ?
Ngay sau thông điệp ban đầu, dấu phân cách 1 theo sau là P, trong ví dụ của chúng ta là chín 0, cần được thêm vào.

```
thông điệp + 1 000 000 000
```

#### Đệm Kích Thước
Chúng ta bây giờ chuyển sang giai đoạn thứ hai của quá trình tiền xử lý, bao gồm việc thêm biểu diễn nhị phân của kích thước thông điệp ban đầu tính bằng bit.
Hãy xem lại ví dụ với đầu vào là 950 bit:

```
Biểu diễn nhị phân của số 950 là: 11 1011 0110

Chúng ta sử dụng 64 bit dự trữ từ bước trước. Chúng ta thêm các số không để làm tròn 64 bit của chúng ta thành đầu vào cân bằng. Sau đó, chúng ta kết hợp thông điệp ban đầu, các bit đệm, và đệm kích thước để nhận được đầu vào cân bằng của chúng ta.
```

Dưới đây là kết quả:

![image](assets/image/section1/4.webp)

### Xử Lý

#### Hiểu Biết Cơ Bản

##### Hằng Số và Vectơ Khởi Tạo

Bây giờ, chúng ta chuẩn bị cho các bước đầu tiên của quá trình xử lý hàm SHA-256. Giống như trong bất kỳ công thức nấu ăn nào, chúng ta cần một số nguyên liệu cơ bản, mà chúng ta gọi là hằng số và vectơ khởi tạo.

Các vectơ khởi tạo, từ A đến H, là 32 bit đầu tiên của phần thập phân của căn bậc hai của 8 số nguyên tố đầu tiên. Chúng sẽ phục vụ như là giá trị cơ sở trong các bước xử lý ban đầu. Giá trị của chúng được biểu diễn ở dạng thập lục phân.

Các hằng số K, từ 0 đến 63, đại diện cho 32 bit đầu tiên của phần thập phân của căn bậc ba của 64 số nguyên tố đầu tiên. Chúng được sử dụng trong mỗi vòng của hàm nén. Giá trị của chúng cũng được biểu diễn ở dạng thập lục phân.

![image](assets/image/section1/5.webp)

##### Các Phép Toán Được Sử Dụng

Trong hàm nén, chúng ta sử dụng các toán tử cụ thể như XOR, AND, và NOT. Chúng ta xử lý các bit một cách riêng lẻ theo vị trí của chúng, sử dụng toán tử XOR và bảng chân lý. Toán tử AND được sử dụng để trả về 1 chỉ khi cả hai toán hạng đều bằng 1, và toán tử NOT được sử dụng để trả về giá trị đối lập của một toán hạng. Chúng ta cũng sử dụng phép toán SHR để dịch chuyển các bit sang phải bởi một số lượng đã chọn.

Bảng chân lý:

![image](assets/image/section1/6.webp)

Các phép dịch bit:

![image](assets/image/section1/7.webp)

#### Hàm Nén

Trước khi áp dụng hàm nén, chúng ta chia đầu vào thành các khối 512 bit. Mỗi khối sẽ được xử lý độc lập với những khối khác.

Mỗi khối 512-bit sau đó được chia tiếp thành các phần 32-bit gọi là W. Như vậy, W(0) đại diện cho 32 bit đầu tiên của khối 512-bit. W(1) đại diện cho 32 bit tiếp theo, và cứ thế, cho đến khi chúng ta đạt được 512 bit của khối.

Một khi tất cả các hằng số K và các phần W được xác định, chúng ta có thể thực hiện các phép tính sau cho mỗi phần W trong mỗi vòng.

Chúng ta thực hiện 64 vòng tính toán trong hàm nén. Trong vòng cuối cùng, tại "Đầu ra của hàm", chúng ta sẽ có một trạng thái trung gian sẽ được cộng vào trạng thái ban đầu của hàm nén.

Sau đó, chúng ta lặp lại tất cả các bước này của hàm nén trên khối 512-bit tiếp theo, cho đến khối cuối cùng.

Tất cả các phép cộng trong hàm nén là phép cộng modulo 2^32 để luôn giữ được tổng 32-bit.

![image](assets/image/section1/9.webp)

![image](assets/image/section1/8.webp)

##### Một Vòng của Hàm Nén

![image](assets/image/section1/11.webp)

![image](assets/image/section1/10.webp)

Hàm nén sẽ được thực hiện 64 lần. Chúng ta có các phần W và các hằng số K đã được xác định trước làm đầu vào.
Các ô vuông/ dấu chéo màu đỏ tương ứng với một phép cộng modulo 2^32-bit.
Các đầu vào A, B, C, D, E, F, G, H sẽ được liên kết với một giá trị 32-bit để tạo thành tổng cộng 256 bit. Chúng ta cũng có một chuỗi mới A, B, C, D, E, F, G, H làm đầu ra. Đầu ra này sau đó sẽ được sử dụng làm đầu vào cho vòng tiếp theo và cứ tiếp tục như vậy cho đến hết vòng thứ 64.

Giá trị của chuỗi đầu vào cho vòng đầu tiên của hàm nén tương ứng với các vector khởi tạo đã được đề cập trước đó.
Nhắc lại, các vector khởi tạo đại diện cho 32 bit đầu tiên của các phần thập phân của căn bậc hai của 8 số nguyên tố đầu tiên.

Dưới đây là một ví dụ về một vòng:

![image](assets/image/section1/12.1.webp)

##### Trạng Thái Trung Gian

Nhắc lại, thông điệp được chia thành các khối 512 bit, sau đó được chia thành các mảnh 32-bit. Đối với mỗi khối 512-bit, chúng ta áp dụng 64 vòng của hàm nén.
Trạng thái trung gian tương ứng với kết thúc của 64 vòng của một khối. Giá trị của chuỗi đầu ra từ vòng thứ 64 này được sử dụng làm giá trị khởi tạo cho chuỗi đầu vào của vòng đầu tiên của khối tiếp theo.

![image](assets/image/section1/12.2.webp)

#### Tổng Quan về Hàm Băm

![image](assets/image/section1/13.webp)

Chúng ta có thể nhận thấy rằng đầu ra của mảnh thông điệp 512-bit đầu tiên tương ứng với các vector khởi tạo của chúng ta như đầu vào cho mảnh thông điệp 512-bit thứ hai, và cứ tiếp tục như vậy.

Đầu ra của vòng cuối cùng, của mảnh cuối cùng, tương ứng với kết quả cuối cùng của hàm SHA256.

Kết luận, chúng tôi muốn nhấn mạnh vai trò quan trọng của các phép tính được thực hiện trong các hộp CH, MAJ, σ0, và σ1. Những hoạt động này, cùng với những hoạt động khác, là những người bảo vệ đảm bảo sự kiên cố của hàm băm SHA256 chống lại các cuộc tấn công, làm cho nó trở thành lựa chọn ưu tiên để bảo vệ nhiều hệ thống số, đặc biệt là trong giao thức Bitcoin. Rõ ràng, mặc dù phức tạp, vẻ đẹp của SHA256 nằm ở khả năng tìm ra đầu vào từ băm, trong khi việc xác minh băm cho một đầu vào cho trước là một hành động cơ học đơn giản.

## Các thuật toán được sử dụng cho việc suy ra
<chapterId>cc668121-7789-5e99-bf5e-1ba085f4f5f2</chapterId>

Các thuật toán suy ra HMAC và PBKDF2 là các thành phần chính trong cơ chế bảo mật của giao thức Bitcoin. Chúng ngăn chặn một loạt các cuộc tấn công tiềm năng và đảm bảo tính toàn vẹn của ví Bitcoin.
HMAC và PBKDF2 là các công cụ mật mã được sử dụng cho các nhiệm vụ khác nhau trong Bitcoin. HMAC chủ yếu được sử dụng để chống lại các cuộc tấn công mở rộng độ dài khi suy ra ví Định Hình Phân Cấp (HD), trong khi PBKDF2 được sử dụng để chuyển đổi cụm từ ghi nhớ thành một hạt giống.

#### HMAC-SHA512

Cặp HMAC-SHA512 có hai đầu vào: một thông điệp m (Đầu vào 1) và một khóa K do người dùng tự chọn (Đầu vào 2). Nó cũng có một đầu ra cố định: 512 bit.

Hãy ghi chú:
- m: thông điệp kích thước tùy ý do người dùng chọn (đầu vào 1)
- K: khóa tùy ý do người dùng chọn (đầu vào 2)
- K': khóa K đã được điều chỉnh kích thước. Nó đã được điều chỉnh cho vừa với kích thước B của các khối.
- ||: phép nối.
- opad: hằng số được định nghĩa bởi byte 0x5c lặp lại B lần.
- ipad: hằng số được định nghĩa bởi byte 0x36 lặp lại B lần.
- B: Kích thước của các khối của hàm băm được sử dụng.

![image](assets/image/section1/14.webp)
HMAC-SHA512, nhận một thông điệp và một khóa làm đầu vào, tạo ra một đầu ra cố định. Để đảm bảo tính thống nhất, khóa được điều chỉnh dựa trên kích thước của các khối được sử dụng trong hàm băm. Trong bối cảnh của việc phát sinh ví HD, HMAC-SHA-512 được sử dụng. Nó hoạt động với các khối 1024-bit (128-byte) và điều chỉnh khóa một cách phù hợp. Nó sử dụng các hằng số OPAD (0x5c) và IPAD (0x36), được lặp lại khi cần thiết để tăng cường bảo mật.

Quy trình HMAC-SHA-512 bao gồm việc nối kết kết quả của SHA-512 áp dụng cho khóa XOR OPAD và khóa XOR IPAD với thông điệp. Khi sử dụng với các khối 1024-bit (128-byte), khóa đầu vào được thêm vào các số không nếu cần thiết, sau đó XOR với IPAD và OPAD. Khóa đã được chỉnh sửa sau đó được nối kết với thông điệp.

![image](assets/image/section1/15.webp)

Việc bổ sung một giá trị salt vào mã chuỗi tăng cường bảo mật cho các khóa được phát sinh. Không có nó, một cuộc tấn công có thể xâm phạm toàn bộ ví và ăn cắp tất cả bitcoin.

PBKDF2 được sử dụng để chuyển đổi một cụm từ ghi nhớ thành một hạt giống. Thuật toán này thực hiện 2048 vòng sử dụng HMAC SHA512. Thông qua các thuật toán phát sinh này, các đầu vào khác nhau có thể tạo ra một đầu ra độc đáo và cố định, giúp giảm thiểu vấn đề về các cuộc tấn công mở rộng độ dài có thể xảy ra với các hàm băm thuộc gia đình SHA-2.

Một cuộc tấn công mở rộng độ dài khai thác một tính chất cụ thể của một số hàm băm mật mã. Trong một cuộc tấn công như vậy, một kẻ tấn công đã có hash của một thông điệp không biết trước có thể sử dụng nó để tính toán hash của một thông điệp dài hơn, là một phần mở rộng của thông điệp gốc. Điều này thường có thể thực hiện mà không cần biết nội dung của thông điệp gốc, có thể dẫn đến những lỗ hổng bảo mật đáng kể nếu loại hàm băm này được sử dụng cho các nhiệm vụ như xác minh tính toàn vẹn.

![image](assets/image/section1/16.webp)

Kết luận, các thuật toán HMAC và PBKDF2 đóng vai trò quan trọng trong bảo mật của việc phát sinh ví HD trong giao thức Bitcoin. HMAC-SHA-512 được sử dụng để bảo vệ chống lại các cuộc tấn công mở rộng độ dài, trong khi PBKDF2 cho phép chuyển đổi cụm từ ghi nhớ thành hạt giống. Mã chuỗi thêm một nguồn entropy bổ sung trong việc phát sinh khóa, đảm bảo sự vững chắc của hệ thống.

# Chữ ký số
<partId>76b58a00-0c18-54b9-870d-6b7e34029db8</partId>

## Chữ ký số và Đường cong Elliptic
<chapterId>c9dd9672-6da1-57f8-9871-8b28994d4c1a</chapterId>

Những bitcoin nổi tiếng này được lưu trữ ở đâu? Không phải trong một ví Bitcoin, như một số người có thể nghĩ. Trên thực tế, một ví Bitcoin lưu trữ các khóa riêng cần thiết để chứng minh quyền sở hữu của bitcoin. Chính bitcoin được ghi lại trên blockchain, một cơ sở dữ liệu phi tập trung lưu trữ tất cả các giao dịch.

Trong hệ thống Bitcoin, đơn vị tính là bitcoin (chú ý là "b" viết thường). Nó có thể chia nhỏ đến tám chữ số thập phân, với đơn vị nhỏ nhất là satoshi. UTXOs, hay "Unspent Transaction Outputs," đại diện cho các đầu ra giao dịch chưa được tiêu thuộc về một khóa công khai được liên kết toán học với một khóa riêng. Để tiêu những bitcoin này, người ta phải có khả năng thỏa mãn điều kiện chi tiêu của giao dịch. Một điều kiện chi tiêu điển hình bao gồm việc chứng minh cho phần còn lại của mạng lưới rằng người dùng là chủ sở hữu hợp pháp của khóa công khai liên kết với UTXO. Để làm điều này, người dùng phải chứng minh sở hữu khóa riêng tương ứng với khóa công khai liên kết với mỗi UTXO mà không tiết lộ khóa riêng.

Đây là nơi chữ ký số xuất hiện. Nó phục vụ như một bằng chứng toán học về việc sở hữu một khóa riêng liên kết với một khóa công khai cụ thể. Kỹ thuật bảo vệ dữ liệu này chủ yếu dựa trên một lĩnh vực hấp dẫn của mật mã học gọi là mật mã học đường cong elliptic (ECC).

Chữ ký có thể được xác minh một cách toán học bởi các thành viên khác trong mạng lưới Bitcoin.
Để đảm bảo an ninh cho các giao dịch, Bitcoin dựa vào hai giao thức chữ ký số: ECDSA (Elliptic Curve Digital Signature Algorithm) và Schnorr. ECDSA đã được tích hợp vào Bitcoin kể từ khi nó được ra mắt vào năm 2009, trong khi chữ ký Schnorr được thêm vào gần đây hơn vào tháng 11 năm 2021. Mặc dù cả hai giao thức đều dựa trên mật mã học đường cong elliptic và sử dụng các cơ chế toán học tương tự, chúng chủ yếu khác biệt về cấu trúc chữ ký.

Trong khóa học này, chúng ta sẽ giới thiệu về thuật toán ECDSA.

### Đường cong elliptic là gì?

Mật mã học đường cong elliptic là một tập hợp các thuật toán sử dụng đường cong elliptic cho các tính chất hình học và toán học đa dạng của nó trong bối cảnh mật mã, với độ an toàn dựa trên độ khó của việc tính toán logarit rời rạc.

Đường cong elliptic hữu ích trong nhiều ứng dụng mật mã trong giao thức Bitcoin, từ trao đổi khóa đến mã hóa không đối xứng và chữ ký số.

Đường cong elliptic có những tính chất thú vị:

- Đối xứng: Bất kỳ đường thẳng không dọc nào cắt qua hai điểm trên đường cong elliptic sẽ gặp đường cong tại một điểm thứ ba.
- Bất kỳ đường thẳng không dọc nào tiếp xúc với đường cong tại một điểm sẽ luôn gặp đường cong tại một điểm thứ hai duy nhất.

Giao thức Bitcoin sử dụng một đường cong elliptic cụ thể gọi là Secp256k1 cho các hoạt động mật mã của mình.

Trước khi đi sâu vào các cơ chế chữ ký này, điều quan trọng là phải hiểu đường cong elliptic là gì. Một đường cong elliptic được định nghĩa bởi phương trình y² = x³ + ax + b. Mỗi điểm trên đường cong này có một đối xứng đặc trưng quan trọng cho việc sử dụng của nó trong mật mã.

Cuối cùng, các đường cong elliptic khác nhau được công nhận là an toàn cho việc sử dụng mật mã. Đường cong được biết đến nhiều nhất có thể là secp256r1. Tuy nhiên, đối với Bitcoin, Satoshi Nakamoto đã chọn một đường cong khác: secp256k1.

Đường cong này được định nghĩa bởi các tham số a=0 và b=7, và phương trình của nó là y² = x³ + 7 modulo n, nơi n đại diện cho số nguyên tố quyết định thứ tự của đường cong.

Hình ảnh đầu tiên đại diện cho đường cong secp256k1 trên trường số thực và phương trình của nó.
Hình ảnh thứ hai là biểu diễn của đường cong secp256k1 trên trường ZP, trường của các số tự nhiên dương, modulo p nơi p là một số nguyên tố. Nó trông giống như một đám mây điểm. Chúng ta sử dụng trường của các số tự nhiên dương này để tránh xấp xỉ.
p là một số nguyên tố, và đó là thứ tự của đường cong được sử dụng.
Cuối cùng, phương trình được sử dụng trong giao thức Bitcoin là:$$
y^2 = (x^3 + 7) mod(p) $$
Phương trình của đường cong elliptic trong Bitcoin tương ứng với phương trình cuối cùng trong hình ảnh trước.

Trong phần tiếp theo của khóa học này, chúng ta sẽ sử dụng các đường cong trên trường số thực chỉ để dễ dàng hiểu hơn.

## Tính khóa công khai từ khóa riêng
<chapterId>fcb2bd58-5dda-5ecf-bb8f-ad1a0561ab4a</chapterId>

Đầu tiên, hãy khám phá thế giới của Elliptic Curve Digital Signature Algorithm (ECDSA). Bitcoin sử dụng thuật toán chữ ký số này để liên kết khóa riêng và khóa công khai. Trong hệ thống này, khóa riêng là một số 256-bit ngẫu nhiên hoặc giả ngẫu nhiên. Tổng số khả năng cho một khóa riêng lý thuyết là 2^256, nhưng thực tế, nó ít hơn một chút. Để chính xác, một số khóa riêng 256-bit không hợp lệ cho Bitcoin.
Để tương thích với Bitcoin, một khóa riêng phải nằm trong khoảng từ 1 đến n-1, nơi n biểu thị thứ tự của đường cong elliptic. Điều này có nghĩa là tổng số khả năng cho một khóa riêng Bitcoin gần bằng 1.158 x 10^77. Để đặt vào một góc nhìn, số lượng này tương đương với số lượng nguyên tử có mặt trong vũ trụ quan sát được.
![image](assets/image/section2/3.webp)

Khóa riêng độc nhất, được ký hiệu là k, sau đó được sử dụng để xác định một khóa công khai.

Khóa công khai, được ký hiệu là K, là một điểm trên đường cong elliptic được suy ra từ khóa riêng thông qua các thuật toán không thể đảo ngược như ECDSA. Khi chúng ta biết khóa riêng, việc truy xuất khóa công khai rất dễ dàng, nhưng khi chỉ có khóa công khai, việc truy xuất khóa riêng là không thể. Tính không thể đảo ngược này là nền tảng của bảo mật ví Bitcoin.

Khóa công khai dài 512 bit vì nó tương ứng với một điểm trên đường cong với tọa độ x là 256 bit và tọa độ y là 256 bit. Tuy nhiên, nó có thể được nén thành một số 264-bit.

![image](assets/image/section2/4.webp)

Điểm sinh (G) là điểm trên đường cong từ đó tất cả các khóa công khai được tạo ra trong giao thức Bitcoin. Nó có tọa độ x và y cụ thể, thường được biểu diễn bằng hệ thập lục phân. Đối với secp256k1, tọa độ của G là, bằng hệ thập lục phân:

- `Gx = 79BE667E F9DCBBAC 55A06295 CE870B07 029BFCDB 2DCE28D9 59F2815B 16F81798`
- `Gy = 483ADA77 26A3C465 5DA4FBFC 0E1108A8 FD17B448 A6855419 9C47D08F FB10D4B8`
Điểm này hữu ích cho việc suy ra tất cả các khóa công khai. Để tính khóa công khai K, chỉ cần nhân điểm G với khóa riêng k, sao cho: K = k.G

Chúng ta sẽ nghiên cứu cách thêm và nhân các điểm trên đường cong elliptic.

#### Phép cộng và nhân đôi điểm trên đường cong elliptic

##### Cộng hai điểm M + L

Một trong những tính chất đáng chú ý của đường cong elliptic là một đường thẳng không dọc cắt đường cong tại hai điểm cũng sẽ cắt nó tại một điểm thứ ba, gọi là điểm O trong ví dụ của chúng ta. Tính chất này được sử dụng để xác định điểm U, là điểm đối diện của điểm O.

M + L = U

![image](assets/image/section2/5.webp)

##### Cộng một điểm với chính nó = Nhân đôi điểm

Việc cộng một điểm G với chính nó được thực hiện bằng cách vẽ một tiếp tuyến tại điểm đó trên đường cong. Tiếp tuyến này, theo các tính chất của đường cong elliptic, sẽ cắt đường cong tại một điểm duy nhất thứ hai -J. Điểm đối diện của điểm này, J, là kết quả của việc cộng điểm G với chính nó.
G + G = J

Thực tế, điểm G là điểm bắt đầu để tính toán tất cả các khóa công khai của người dùng hệ thống Bitcoin.

![image](assets/image/section2/6.webp)

#### Phép nhân vô hướng trên đường cong elliptic

Phép nhân vô hướng của một điểm với n tương đương với việc cộng điểm đó với chính nó n lần.

Tương tự như nhân đôi điểm, phép nhân vô hướng của điểm G với một điểm n được thực hiện bằng cách vẽ một tiếp tuyến tại điểm G. Tiếp tuyến này, theo các tính chất của đường cong elliptic, sẽ cắt đường cong tại một điểm duy nhất thứ hai -2G. Điểm đối diện của điểm này, 2G, là kết quả của việc cộng điểm G với chính nó.
Nếu n = 4, thì thao tác được lặp lại cho đến khi đạt được 4G.
![image](assets/image/section2/7.webp)

Dưới đây là một ví dụ tính toán cho 3G:

![image](assets/image/section2/8.webp)

Những thao tác trên các điểm của một đường cong elliptic là cơ sở để tính toán khóa công khai. Việc suy ra khóa công khai khi biết khóa riêng là rất dễ dàng.
Khóa công khai là một điểm trên đường cong elliptic, nó là kết quả của việc cộng và nhân đôi điểm G k lần. Với k = khóa riêng.

Trong ví dụ này:

- Khóa riêng k = 4
- Khóa công khai K = kG = 4G

![image](assets/image/section2/9.webp)

Biết khóa riêng k, việc tính toán khóa công khai K là dễ dàng. Tuy nhiên, không thể lấy lại khóa riêng dựa trên khóa công khai. Đây có phải là kết quả của một phép cộng hoặc nhân đôi các điểm không?

Trong bài học tiếp theo, chúng ta sẽ khám phá cách tạo một chữ ký số sử dụng thuật toán ECDSA với khóa riêng để chi tiêu bitcoin.

## Ký bằng khóa riêng
<chapterId>bb07826f-826e-5905-b307-3d82001fb778</chapterId>

Quy trình chữ ký số là một phương pháp chính để chứng minh rằng bạn là người giữ khóa riêng mà không tiết lộ nó. Điều này được thực hiện sử dụng thuật toán ECDSA, bao gồm việc xác định một nonce duy nhất, tính toán một số cụ thể V, và tạo một chữ ký số gồm hai phần, S1 và S2.
Luôn luôn sử dụng một nonce duy nhất là rất quan trọng để tránh các cuộc tấn công an ninh. Một ví dụ nổi tiếng về điều gì có thể xảy ra khi quy tắc này không được tuân thủ là việc hack PlayStation 3, đã bị xâm phạm do việc tái sử dụng nonce.

![](assets/image/section2/10.webp)

Các bước:

- Xác định một nonce v, là một số ngẫu nhiên duy nhất.
  Nonce = Số Chỉ Sử Dụng Một Lần.
  Nó được xác định bởi người thực hiện chữ ký.
- Tính toán bằng cách cộng và nhân đôi các điểm trên đường cong elliptic từ điểm G, vị trí của V trên đường cong elliptic.
  Sao cho V = v.G
  x và y là tọa độ của V trên mặt phẳng.
- Tính S1.
  S1 = x mod n với n = thứ tự của đường cong và x là một tọa độ của V trên mặt phẳng.
  Lưu ý: Số lượng khóa công khai có thể có lớn hơn số điểm trên đường cong elliptic trong trường số nguyên dương hữu hạn được sử dụng trong Bitcoin.
  Thứ tự của đường cong chỉ tương ứng với các khả năng mà khóa công khai có thể nhận trên đường cong.
- Tính S2.
  H(Tx) = Hash của giao dịch
  k = khóa riêng
- Tính chữ ký: sự kết hợp của S1 + S2.
- Tính P, phép tính xác minh chữ ký.
  K = khóa công khai

Ví dụ, để thu được khóa công khai 3G, bạn vẽ một tiếp tuyến tới điểm G, tính ngược của -G để thu được 2G, và sau đó cộng G và 2G. Để thực hiện một giao dịch, bạn phải chứng minh rằng bạn biết số 3 bằng cách mở khóa các bitcoin liên kết với khóa công khai 3G.

Để tạo một chữ ký số và chứng minh rằng bạn biết khóa riêng liên kết với khóa công khai 3G, trước tiên bạn tính một nonce, sau đó là điểm V liên kết với nonce này (trong ví dụ được đưa ra, đó là 4G). Sau đó, bạn tính điểm T bằng cách cộng khóa công khai 3G và điểm V, điều này cho kết quả là 7G.

![image](assets/image/section2/11.webp)

Hãy đơn giản hóa quy trình chữ ký số.
Trong hình ảnh trước, khóa riêng k = 3.
Chúng ta có thể dễ dàng tính toán khóa công khai K tương ứng với khóa riêng này: K = 3G. Sau đó, chúng ta tạo một nonce một cách giả ngẫu nhiên: v = 4. Từ nonce này, có thể tính toán V sao cho: V = v.G = 4G.

Từ điểm V này, chúng ta tính toán điểm T sao cho:
T = t.G = 7G (với t = 7).

Bây giờ là lúc để tiến hành xác minh chữ ký số.

Xác minh chữ ký số là một bước quan trọng trong việc sử dụng thuật toán ECDSA, cho phép xác nhận tính xác thực của một thông điệp đã ký mà không cần khóa riêng của người gửi. Dưới đây là cách thức hoạt động chi tiết:

Trong ví dụ của chúng ta, chúng ta có hai giá trị quan trọng: t và V.
t là một giá trị số (7 trong ví dụ này), và V là một điểm trên đường cong elliptic (được biểu diễn bởi 4G ở đây). Những giá trị này được tạo ra trong quá trình tạo chữ ký số và sau đó được gửi kèm với thông điệp để cho phép xác minh.

Khi người xác minh nhận được thông điệp, họ cũng sẽ nhận được hai giá trị này, t và V.

Dưới đây là các bước mà người xác minh sẽ thực hiện để xác nhận chữ ký:

1. Đầu tiên, họ sẽ tính hash của thông điệp, mà chúng ta sẽ gọi là H.
2. Sau đó, họ sẽ tính u1 và u2. Để làm điều này, họ sẽ sử dụng các công thức sau:
   - u1 = H /\* (S2)^-1 mod n
   - u2 = T /\* (S2)^-1 mod n
     Nơi S2 là phần thứ hai của chữ ký số, n là thứ tự của đường cong elliptic, và (S2)^-1 là nghịch đảo của S2 mod n.
3. Người xác minh sau đó sẽ tính một điểm P' trên đường cong elliptic sử dụng công thức: P' = u1 _ G + u2 _ K
   - G là điểm sinh của đường cong
   - K là khóa công khai của người gửi
4. Người xác minh sau đó sẽ tính I', đơn giản là tọa độ x của điểm P' modulo n.
5. Cuối cùng, người xác minh sẽ xác nhận rằng I' bằng với t. Nếu đúng như vậy, chữ ký được coi là hợp lệ. Nếu không, chữ ký là không hợp lệ.
Quy trình này đảm bảo rằng chỉ có người gửi sở hữu khóa riêng tương ứng mới có thể tạo ra một chữ ký qua quá trình xác minh này.

Trong thuật ngữ đơn giản hơn:
Người tạo chữ ký sẽ cung cấp số t (trong ví dụ của chúng ta, t = 7) và điểm V cho người xác minh.

Không thể xác định khóa công khai hoặc khóa riêng từ số 7 và số V.

Các bước để xác minh chữ ký số như sau:

- Trên đường cong, người xác minh thêm điểm của khóa công khai vào điểm V để lấy điểm T'.
- Người xác minh tính số t.G.
- Người xác minh kiểm tra kết quả của t.G có thực sự bằng với số T' hay không.

Kết luận, xác minh chữ ký số là một thủ tục thiết yếu trong các giao dịch Bitcoin. Nó đảm bảo rằng thông điệp đã ký không bị thay đổi trong quá trình truyền và người gửi thực sự là chủ sở hữu của khóa riêng. Kỹ thuật xác thực số này dựa trên các nguyên tắc toán học phức tạp, bao gồm cả số học đường cong elliptic, trong khi vẫn bảo mật khóa riêng. Nó cung cấp một nền tảng an ninh vững chắc cho các giao dịch mật mã.

Điều đó được nói, việc quản lý những khóa này, cũng như việc tạo ra chúng, là một câu hỏi thiết yếu khác trong Bitcoin. Làm thế nào để tạo ra một cặp khóa mới? Làm thế nào để tổ chức một cách an toàn và hiệu quả một lượng lớn khóa? Làm thế nào để khôi phục chúng nếu cần thiết?
Để trả lời những câu hỏi này và mở rộng hiểu biết của bạn về bảo mật mã hóa, khóa học tiếp theo của chúng tôi sẽ tập trung vào khái niệm về Ví Phân Cấp Xác Định (Hierarchical Deterministic Wallets - HD wallets) và việc sử dụng cụm từ ghi nhớ. Những cơ chế này cung cấp những cách thức tinh tế để quản lý hiệu quả các khóa tiền mã hóa của bạn trong khi tăng cường bảo mật.

# Cụm từ ghi nhớ
<partId>4070af16-c8a2-58b5-9871-a22c86c07458</partId>

## Sự phát triển của ví Bitcoin
<chapterId>9d9acd5d-a0e5-5dfd-b544-f043fae8840f</chapterId>

Ví Phân Cấp Xác Định, thường được biết đến với tên là HD wallet, đóng một vai trò nổi bật trong hệ sinh thái tiền mã hóa. Thuật ngữ "ví" có thể gây hiểu nhầm cho những người mới tham gia lĩnh vực này, vì nó không liên quan đến việc giữ tiền hoặc các loại tiền tệ. Thay vào đó, nó đề cập đến một bộ sưu tập các khóa riêng tư mã hóa.

Những ví đầu tiên là phần mềm tổ chức các khóa được xác định riêng tư một cách giả ngẫu nhiên nhưng không có sự kết nối giữa chúng. Những ví này được gọi là "Just a Bunch Of Keys" (JBOK).

Vì các khóa không có sự kết nối với nhau, người dùng cần phải tạo một bản sao lưu mới cho mỗi cặp khóa mới được tạo.
Dù người dùng luôn sử dụng cùng một cặp khóa và làm lộ thông tin bảo mật, hoặc tạo ra một cặp khóa mới một cách ngẫu nhiên và do đó cần phải tạo một bản sao lưu mới cho những khóa này.

Tuy nhiên, sự phức tạp trong việc quản lý những khóa này được giảm bớt bởi một tập hợp các giao thức gọi là Đề Xuất Cải Tiến Bitcoin (Bitcoin Improvement Proposals - BIPs). Những đề xuất nâng cấp này nằm ở trung tâm của chức năng và bảo mật của HD wallets. Ví dụ, [BIP32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki), ra mắt vào năm 2012, đã cách mạng hóa cách thức những khóa này được tạo ra và lưu trữ bằng cách giới thiệu khái niệm về khóa được sinh ra một cách xác định và phân cấp. Ý tưởng là sinh ra tất cả các khóa một cách xác định và phân cấp từ một thông tin duy nhất: hạt giống. Điều này đơn giản hóa quá trình sao lưu những khóa này trong khi vẫn duy trì mức độ bảo mật của chúng.

Tiếp theo, [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) đã giới thiệu một đổi mới đáng kể: cụm từ ghi nhớ 24 từ. Hệ thống này đã biến một chuỗi số phức tạp và khó nhớ thành một loạt các từ thông thường, làm cho việc ghi nhớ và lưu trữ trở nên dễ dàng hơn nhiều. Ngoài ra, [BIP38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki) đã đề xuất thêm một cụm từ mật khẩu bổ sung để tăng cường bảo mật cho các khóa cá nhân. Những cải tiến liên tiếp này dẫn đến các tiêu chuẩn BIP43 và BIP44, đã chuẩn hóa cấu trúc và phân cấp của HD wallets, làm cho chúng trở nên dễ tiếp cận và thân thiện với người dùng chung.

Trong các phần tiếp theo, chúng ta sẽ đi sâu hơn vào cách thức hoạt động của HD wallets. Chúng ta sẽ thảo luận về nguyên tắc sinh khóa và xem xét các khái niệm cơ bản về entropy và sinh số ngẫu nhiên, đây là những yếu tố thiết yếu để đảm bảo bảo mật cho ví HD của bạn.

Tóm lại, điều quan trọng cần nhấn mạnh là vai trò trung tâm của BIP32 và BIP39 trong thiết kế và bảo mật của HD wallets. Những giao thức này cho phép sinh ra nhiều khóa từ một hạt giống duy nhất, được cho là một số ngẫu nhiên hoặc giả ngẫu nhiên. Ngày nay, những tiêu chuẩn này được áp dụng bởi đa số ví tiền mã hóa, dù chúng dành riêng cho một loại tiền mã hóa hay hỗ trợ nhiều loại tiền tệ.

## Entropy và Sinh Số Ngẫu Nhiên
<chapterId>b43c715d-affb-56d8-a697-ad5bc2fffd63</chapterId>
Tầm quan trọng của việc bảo mật khóa riêng trong hệ sinh thái Bitcoin là không thể phủ nhận. Chúng thực sự là viên gạch nền tảng đảm bảo an ninh cho các giao dịch Bitcoin. Để tránh bất kỳ sự dễ bị tấn công nào liên quan đến tính dự đoán, những khóa này phải được tạo ra một cách hoàn toàn ngẫu nhiên, điều này có thể nhanh chóng trở thành một công việc cực kỳ vất vả. Vấn đề là trong khoa học máy tính, việc tạo ra một số ngẫu nhiên thực sự là không thể, vì nó nhất thiết phải được suy ra từ một quá trình xác định; một đoạn mã. Đó là lý do tại sao việc tìm hiểu về các loại Bộ Sinh Số Ngẫu Nhiên (Random Number Generators - RNG) khác nhau là rất quan trọng. Các loại RNG thay đổi, từ Bộ Sinh Số Ngẫu Nhiên Giả (Pseudo-Random Number Generators - PRNG) đến Bộ Sinh Số Ngẫu Nhiên Thực (True Random Number Generators - TRNG), cũng như PRNGs kết hợp một nguồn entropy.

Entropy đề cập đến trạng thái "hỗn loạn" của một hệ thống. Từ một entropy bên ngoài, tức là một nguồn thông tin bên ngoài, có thể sử dụng một bộ sinh số ngẫu nhiên để thu được một số ngẫu nhiên.

![image](assets/image/section3/2.webp)

Hãy xem cách hoạt động của một Bộ Sinh Số Ngẫu Nhiên Giả (PRNG).

Nó nhận một hạt giống làm đầu vào, tương ứng với trạng thái nội bộ 0.
Trên trạng thái nội bộ này, một hàm biến đổi được áp dụng, và kết quả, là một số ngẫu nhiên giả, tương ứng với trạng thái nội bộ 1.
Trên trạng thái nội bộ 1 này, một lần nữa, một hàm biến đổi được áp dụng, dẫn đến một số ngẫu nhiên mới = trạng thái nội bộ 2.
Và cứ tiếp tục như vậy.

Nhược điểm chính là bất kỳ hạt giống giống nhau nào sẽ luôn tạo ra cùng một kết quả. Ngoài ra, nếu chúng ta biết kết quả của các hàm biến đổi ban đầu, chúng ta sẽ có thể lấy lại số ngẫu nhiên ở đầu ra của quá trình.

Một ví dụ về hàm biến đổi là hàm PBKDF2.

**Tóm lại, một PRNG đảm bảo an ninh mật mã phải:**

- có tính ngẫu nhiên về mặt thống kê
- không thể dự đoán
- vẫn an toàn ngay cả khi kết quả được tiết lộ
- có một chu kỳ đủ dài

![image](assets/image/section3/3.webp)

Trong trường hợp của Bitcoin, khóa riêng được tạo ra từ một mẩu thông tin duy nhất tại cơ sở của ví. Thông tin này cho phép sự phái sinh xác định và phân cấp của các cặp khóa con. Entropy là nền tảng của mọi ví HD (Hierarchical Deterministic), mặc dù không có tiêu chuẩn nào cho việc tạo ra số ngẫu nhiên này. Do đó, việc tạo ra số ngẫu nhiên là một thách thức lớn trong việc bảo mật các giao dịch Bitcoin.

## Cụm từ ghi nhớ
<chapterId>8f9340c1-e6dc-5557-a2f2-26c9669987d5</chapterId>

An ninh của một ví Bitcoin là mối quan tâm lớn đối với tất cả người dùng của nó. Một cách thiết yếu để đảm bảo sao lưu ví là tạo ra một cụm từ ghi nhớ dựa trên entropy và checksum.

![image](assets/image/section3/5.webp)

Để chuyển đổi entropy thành cụm từ ghi nhớ, chỉ cần tính toán checksum của entropy và nối entropy và checksum lại với nhau.

Một khi entropy được tạo ra, hàm SHA256 được sử dụng trên entropy để tạo ra một hash.
8 bit đầu tiên của hash được lấy ra, đó là checksum.
Cụm từ ghi nhớ là kết quả của entropy cộng với checksum.

Checksum đảm bảo việc kiểm tra độ chính xác của cụm từ khôi phục. Không có checksum này, một lỗi trong cụm từ có thể dẫn đến việc tạo ra một ví khác và do đó là mất mát tiền bạc. Checksum được thu được bằng cách đưa entropy qua hàm SHA256 và lấy ra 8 bit đầu tiên của hash.

![image](assets/image/section3/6.webp)

Có các tiêu chuẩn khác nhau cho cụm từ ghi nhớ tùy thuộc vào kích thước của entropy. Tiêu chuẩn được sử dụng phổ biến nhất cho một cụm từ khôi phục 24 từ là entropy 256 bit. Kích thước của checksum được xác định bằng cách chia kích thước của entropy cho 32.
Ví dụ, một entropy 256 bit tạo ra một checksum 8-bit. Việc nối entropy và checksum sau đó dẫn đến các kích thước tương ứng là 128 bit, 160 bit, v.v. Tùy thuộc vào kích thước của entropy, cụm từ khôi phục sẽ bao gồm 12 từ cho 128 bit, 15 từ cho 160 bit và 24 từ cho 256 bit.
**Mã hóa của cụm từ ghi nhớ:**

![hình ảnh](assets/image/section3/7.webp)

8 bit cuối cùng tương ứng với checksum.
Mỗi phân đoạn 11-bit được chuyển đổi thành số thập phân.
Mỗi số thập phân tương ứng với một từ trong danh sách 2048 từ trên BIP39. Điều quan trọng cần lưu ý là không có từ nào có cùng thứ tự của bốn chữ cái đầu tiên.

Việc sao lưu cụm từ khôi phục 24 từ là cần thiết để bảo toàn tính toàn vẹn của ví Bitcoin. Hai tiêu chuẩn được sử dụng phổ biến nhất dựa trên entropy 128 hoặc 256 bit và nối của 12 hoặc 24 từ. Thêm một cụm từ bí mật là một lựa chọn bổ sung để tăng cường bảo mật cho ví.

Kết luận, việc tạo ra một cụm từ ghi nhớ để bảo vệ ví Bitcoin là một quá trình quan trọng. Việc tuân thủ các tiêu chuẩn của cụm từ ghi nhớ dựa trên kích thước của entropy là quan trọng. Sao lưu cụm từ khôi phục 24 từ là cần thiết để ngăn chặn bất kỳ sự mất mát tiền bạc nào.

## Cụm từ bí mật
<chapterId>6a51b397-f3b5-5084-b151-cef94bc9b93f</chapterId>

Cụm từ bí mật là một mật khẩu bổ sung có thể được tích hợp vào ví Bitcoin để tăng cường bảo mật của nó. Việc sử dụng nó là tùy chọn và tùy thuộc vào quyết định của người dùng. Bằng cách thêm thông tin tùy ý mà, cùng với cụm từ ghi nhớ, cho phép tính toán hạt giống của ví, cụm từ bí mật tăng cường bảo mật của nó.

![hình ảnh](assets/image/section3/8.webp)

Cụm từ bí mật là một loại muối mật mã tùy chọn với kích thước do người dùng chọn. Nó cải thiện bảo mật của một ví HD bằng cách thêm thông tin tùy ý mà, khi kết hợp với cụm từ ghi nhớ, sẽ cho phép tính toán hạt giống.

Một khi đã được thiết lập trong quá trình tạo ví, nó là cần thiết cho việc suy ra tất cả các khóa của ví. Hàm pbkdf2 được sử dụng để tạo ra hạt giống từ cụm từ bí mật. Hạt giống này cho phép suy ra tất cả các cặp khóa con của ví. Nếu cụm từ bí mật được thay đổi, ví Bitcoin trở nên hoàn toàn khác biệt.

Cụm từ bí mật là một công cụ thiết yếu để tăng cường bảo mật cho ví Bitcoin. Nó có thể cho phép thực hiện các chiến lược bảo mật khác nhau. Ví dụ, nó có thể được sử dụng để tạo bản sao và hỗ trợ sao lưu cụm từ ghi nhớ. Nó cũng có thể cải thiện bảo mật của ví bằng cách giảm thiểu rủi ro liên quan đến việc tạo ngẫu nhiên cụm từ ghi nhớ.

Một cụm từ bí mật hiệu quả nên dài (20 đến 40 ký tự) và đa dạng (sử dụng chữ hoa, chữ thường, số và ký hiệu). Nó không nên trực tiếp liên quan đến người dùng hoặc môi trường xung quanh của họ. An toàn hơn khi sử dụng một chuỗi ký tự ngẫu nhiên thay vì một từ đơn giản làm cụm từ bí mật.

![hình ảnh](assets/image/section3/9.webp)

Một cụm từ bí mật an toàn hơn một mật khẩu đơn giản. Cụm từ bí mật lý tưởng là dài, đa dạng và ngẫu nhiên. Nó có thể tăng cường bảo mật cho một ví hoặc phần mềm nóng. Nó cũng có thể được sử dụng để tạo ra các bản sao lưu dự phòng và an toàn.

Việc chăm sóc sao lưu cụm từ bí mật là rất quan trọng để tránh mất quyền truy cập vào ví. Cụm từ bí mật là một lựa chọn cho một ví HD. Nó có thể được tạo ra một cách ngẫu nhiên với xúc xắc hoặc một trình tạo số giả ngẫu nhiên khác. Không được khuyến khích ghi nhớ cụm từ bí mật hoặc cụm từ ghi nhớ.

Trong bài học tiếp theo, chúng ta sẽ xem xét chi tiết về cách hoạt động của hạt giống và cặp khóa đầu tiên được tạo ra từ nó. Hãy tiếp tục theo dõi khóa học này để tiếp tục học hỏi. Chúng tôi mong được gặp lại bạn rất sớm.
# Tạo Ví Bitcoin
<partId>9c25e767-7eae-50b8-8c5f-679d8fc83bab</partId>
## Tạo Seed và Master Key
<chapterId>63093760-2010-5691-8d0e-9a04732ae557</chapterId>

Trong phần này của khóa học, chúng ta sẽ khám phá các bước để tạo ra một Ví Định Hình Phân Cấp (HD Wallet), cho phép việc tạo và quản lý các khóa riêng tư và công khai một cách có hệ thống và định hình.

![image](assets/image/section4/0.webp)

Nền tảng của HD Wallet dựa trên hai yếu tố thiết yếu: cụm từ ghi nhớ và cụm từ bí mật (mật khẩu bổ sung tuỳ chọn). Cả hai cùng tạo nên seed, một chuỗi số và chữ có độ dài 512 bit, phục vụ như là cơ sở để tạo ra các khóa của ví. Từ seed này, có thể tạo ra tất cả các cặp khóa con của ví Bitcoin. Seed là chìa khóa mở ra quyền truy cập vào tất cả các bitcoin liên kết với ví, cho dù bạn có sử dụng cụm từ bí mật hay không.

![image](assets/image/section4/1.webp)

Để có được seed, hàm pbkdf2 (Password-Based Key Derivation Function 2) được sử dụng với cụm từ ghi nhớ và cụm từ bí mật. Kết quả của pbkdf2 là một seed 512-bit.

Từ seed, có thể xác định master private key và chain code sử dụng thuật toán HMAC SHA-512 (Hash-based Message Authentication Code Secure Hash Algorithm 512). Thuật toán này yêu cầu một thông điệp và một khóa làm đầu vào để tạo ra kết quả. Master private key được tính toán từ seed và cụm từ "Bitcoin SEED". Cụm từ này giống nhau cho tất cả các dẫn xuất của tất cả HD wallets, đảm bảo sự nhất quán giữa các ví.

Ban đầu, hàm SHA-512 không được triển khai trong giao thức Bitcoin, đó là lý do tại sao HMAC SHA-512 được sử dụng. Việc sử dụng HMAC SHA-512 với cụm từ "Bitcoin SEED" hạn chế người dùng tạo ra một ví cụ thể cho Bitcoin. Kết quả của HMAC SHA-512 là một số 512-bit, chia thành hai phần: 256 bit bên trái đại diện cho master private key, trong khi 256 bit bên phải đại diện cho master chain code.

![image](assets/image/section4/2.webp)

Master private key là khóa cha của tất cả các khóa trong tương lai trong ví, trong khi master chain code tham gia vào việc dẫn xuất các khóa con. Quan trọng là phải lưu ý rằng không thể dẫn xuất một cặp khóa con mà không biết chain code tương ứng của cặp cha.

Một cặp khóa trong ví bao gồm một khóa riêng tư, một khóa công khai, và một chain code. Chain code giới thiệu một nguồn ngẫu nhiên trong quá trình dẫn xuất các khóa con và cô lập mỗi cặp khóa để ngăn chặn bất kỳ sự rò rỉ thông tin nào.
Quan trọng là phải lưu ý rằng master private key là khóa riêng tư đầu tiên được dẫn xuất từ seed và không có liên kết với các khóa mở rộng của ví.

Trong bài học tiếp theo, chúng ta sẽ khám phá chi tiết về các khóa mở rộng, như xPub, xPRV, zPub, và hiểu tại sao chúng được sử dụng và cách chúng được xây dựng.

## Khóa Mở Rộng
<chapterId>8dcffce1-31bd-5e0b-965b-735f5f9e4602</chapterId>

Trong phần này của bài học, chúng ta sẽ nghiên cứu về các khóa mở rộng (xPub, zPub, yPub) và các tiền tố của chúng, đóng vai trò quan trọng trong việc dẫn xuất các khóa con trong một Ví Định Hình Phân Cấp (HD Wallet).

![image](assets/image/section4/3.webp)

Khóa mở rộng khác biệt so với khóa chính. Một HD wallet tạo ra một cụm từ ghi nhớ và một seed để có được khóa chính và master chain code. Khóa mở rộng được sử dụng để dẫn xuất các khóa con và yêu cầu cả khóa cha và chain code tương ứng. Một khóa mở rộng kết hợp hai thông tin này để đơn giản hóa quá trình dẫn xuất.

![image](assets/image/section4/4.webp)
Các khóa công khai mở rộng chỉ có thể tạo ra các khóa công khai con thông thường, trong khi các khóa riêng tư mở rộng có thể tạo ra cả khóa công khai và riêng tư con, dù là thông qua quá trình tạo ra thông thường hay cứng nhắc. Quá trình tạo ra cứng nhắc là quá trình tạo ra từ khóa riêng tư cha, trong khi quá trình tạo ra thông thường tương ứng với quá trình tạo ra từ khóa công khai cha.

Sử dụng các khóa mở rộng với tiền tố XPUB cho phép tạo ra các địa chỉ mới mà không cần quay lại với các khóa riêng tư tương ứng, do đó cung cấp bảo mật tốt hơn. Metadata liên quan đến các khóa mở rộng cung cấp thông tin quan trọng về vai trò và vị trí của chúng trong hệ thống phân cấp khóa.

Các khóa mở rộng được xác định bởi các tiền tố cụ thể (XPRV, XPUB, YPUB, ZPUB) chỉ ra liệu đó là khóa riêng tư mở rộng hay khóa công khai mở rộng, cũng như mục đích cụ thể của nó. Metadata liên quan đến một khóa mở rộng bao gồm phiên bản (tiền tố), độ sâu, dấu vân tay khóa cha, chỉ số, và payload (mã chuỗi và khóa cha).

![image](assets/image/section4/5.webp)

Phiên bản tương ứng với loại khóa: xpub, xprv, ...

Độ sâu tương ứng với số lượng quá trình tạo ra giữa khóa cha và con kể từ khóa chính.

Dấu vân tay cha là 4 byte đầu tiên của hash 160 của khóa cha. Chỉ số là số thứ tự của cặp được sử dụng để tạo ra khóa mở rộng trong số các khóa cùng độ sâu. (các khóa cùng độ sâu = các khóa có cùng độ sâu) Ví dụ, nếu chúng ta muốn tạo ra xpub của tài khoản thứ 3 của mình, chỉ số của nó sẽ là 2 (vì chỉ số bắt đầu từ 0).

Payload bao gồm mã chuỗi (32 byte) và khóa cha (33 byte).

Các khóa công khai nén có kích thước 33 byte, trong khi các khóa công khai thô là 512 bit. Các khóa công khai nén giữ lại cùng một thông tin như khóa thô, nhưng với kích thước giảm. Các khóa mở rộng có kích thước 82 byte và tiền tố của chúng được biểu diễn bằng cơ số 58 thông qua chuyển đổi sang hệ thập lục phân. Checksum được tính toán sử dụng hàm băm HASH256.

![image](assets/image/section4/6.webp)

Các quá trình tạo ra nâng cao bắt đầu từ các chỉ số là lũy thừa của 2 (2^31). Điều thú vị là các tiền tố được sử dụng phổ biến nhất là xpub và zpub, tương ứng với các tiêu chuẩn di sản và segwit v1 và segwit v0.

Trong bài học tiếp theo, chúng ta sẽ tập trung vào quá trình tạo ra các cặp khóa con sử dụng kiến thức đã học về các khóa mở rộng và khóa chính của ví.

## Quá trình tạo ra các cặp khóa con
<chapterId>61c0807c-845b-5076-ad06-7f395b36adfd</chapterId>

Như đã nhắc nhở, chúng ta đã thảo luận về việc tính toán hạt giống và khóa chính, đó là các yếu tố thiết yếu đầu tiên cho tổ chức phân cấp và quá trình tạo ra của ví HD (Hierarchical Deterministic). Hạt giống, với độ dài từ 128 đến 256 bit, được tạo ra một cách ngẫu nhiên hoặc từ một cụm từ bí mật. Nó đóng vai trò quyết định trong quá trình tạo ra tất cả các khóa khác. Khóa chính là khóa đầu tiên được tạo ra từ hạt giống, và nó cho phép tạo ra tất cả các cặp khóa con khác.

Mã chuỗi chính đóng một vai trò quan trọng trong việc khôi phục ví từ hạt giống. Cần lưu ý rằng tất cả các khóa được tạo ra từ cùng một hạt giống sẽ có cùng mã chuỗi chính.

![image](assets/image/section4/7.webp)

Tổ chức phân cấp và quá trình tạo ra của ví HD cung cấp quản lý khóa và cấu trúc ví hiệu quả hơn. Các khóa mở rộng cho phép tạo ra một cặp khóa con từ một cặp khóa cha sử dụng các phép toán toán học và thuật toán cụ thể.
Có các loại cặp khóa con khác nhau, bao gồm khóa củng cố và khóa bình thường. Khóa công khai mở rộng chỉ cho phép tạo ra các khóa con công khai bình thường, trong khi khóa riêng tư mở rộng cho phép tạo ra tất cả các khóa con, cả công khai và riêng tư, dù chúng ở chế độ bình thường hay củng cố. Mỗi cặp khóa có một chỉ số cho phép phân biệt chúng với nhau.
![image](assets/image/section4/8.webp)

Quá trình tạo ra các khóa con sử dụng hàm HMAC-SHA512 với khóa cha kết hợp với chỉ số và mã chuỗi liên kết với cặp khóa. Các khóa con bình thường có chỉ số nằm trong khoảng từ 0 đến 2 mũ 31 trừ 1, trong khi các khóa con củng cố có chỉ số nằm trong khoảng từ 2 mũ 31 đến 2 mũ 32 trừ 1.

![image](assets/image/section4/9.webp)

![image](assets/image/section4/10.webp)

Có hai loại cặp khóa con: cặp củng cố và cặp bình thường. Quá trình tạo ra các khóa con sử dụng khóa công khai để tạo điều kiện chi tiêu, trong khi khóa riêng tư được sử dụng để ký. Khóa công khai mở rộng chỉ cho phép tạo ra các khóa con công khai bình thường, trong khi khóa riêng tư mở rộng cho phép tạo ra tất cả các khóa con, cả công khai và riêng tư, ở chế độ bình thường hoặc củng cố.

![image](assets/image/section4/11.webp)
![image](assets/image/section4/12.webp)

Quá trình củng cố sử dụng khóa riêng tư cha, trong khi quá trình bình thường sử dụng khóa công khai cha. Hàm HMAC-SHA512 được sử dụng cho quá trình củng cố, trong khi quá trình bình thường sử dụng một bản tóm tắt 512-bit. Khóa công khai con được thu được bằng cách nhân khóa riêng tư con với bộ sinh đường cong elliptic.

![image](assets/image/section4/13.webp)
![image](assets/image/section4/14.webp)

Việc tạo ra và tạo ra nhiều cặp khóa một cách có hệ thống theo cấp bậc cho phép tạo ra một cấu trúc cây cho quá trình tạo ra theo cấp bậc. Trong bài học tiếp theo của khóa học này, chúng ta sẽ nghiên cứu cấu trúc của ví HD cũng như các đường dẫn tạo ra, với một sự tập trung đặc biệt vào ký hiệu đường dẫn tạo ra.

## Cấu Trúc Ví và Đường Dẫn Tạo Ra
<chapterId>34e1bbda-67de-5493-b268-1fded8d67689</chapterId>

Trong chương này, chúng ta sẽ nghiên cứu cấu trúc của cây tạo ra trong một Ví Định Hình Phân Cấp (HD Wallet). Chúng ta đã khám phá tính toán hạt giống, khóa chính, và quá trình tạo ra các cặp khóa con. Bây giờ, chúng ta sẽ tập trung vào việc tổ chức các khóa trong ví.

Ví HD sử dụng các lớp độ sâu để tổ chức khóa. Mỗi quá trình tạo ra từ một cặp cha mẹ sang một cặp con tương ứng với một lớp độ sâu.

![image](assets/image/section4/15.webp)

- Độ sâu 0 tương ứng với khóa chính và mã chuỗi chính.

- Độ sâu 1 được sử dụng để tạo ra các khóa con cho một mục đích cụ thể, được xác định bởi chỉ số. Các mục đích tuân theo BIP 84 và các tiêu chuẩn Segwit v0/v1.

- Độ sâu 2 cho phép phân biệt các tài khoản cho các loại tiền điện tử hoặc mạng khác nhau. Điều này cho phép tổ chức ví dựa trên các nguồn vốn khác nhau. Đối với bitcoin, chỉ số sẽ là 0.

- Độ sâu 3 được sử dụng để tổ chức ví thành các tài khoản khác nhau, cung cấp một cấu trúc rõ ràng và tổ chức hơn.

- Độ sâu 4 tương ứng với các chuỗi ngoại và nội, được sử dụng cho các địa chỉ dự định được công bố công khai. Chỉ số 0 được liên kết với chuỗi ngoại, trong khi chỉ số 1 được liên kết với chuỗi nội. Mỗi tài khoản có hai chuỗi: chuỗi ngoại (0) và chuỗi nội (1). Độ sâu 4 cũng được sử dụng để quản lý các loại kịch bản trong trường hợp của các ví đa chữ ký.
- Mức độ 5 được sử dụng để nhận địa chỉ trong một ví tiêu chuẩn. Trong phần tiếp theo, chúng ta sẽ xem xét chi tiết hơn về việc tạo ra các cặp khóa con.
![image](assets/image/section4/16.webp)

Đối với mỗi lớp độ sâu, chúng ta sử dụng chỉ số để phân biệt các cặp khóa con.

Chỉ số không có dấu nháy đơn tương ứng với chỉ số thực tế được sử dụng, trong khi chỉ số có dấu nháy đơn tương ứng với chỉ số thực tế + 2^31. Các phái sinh cứng sử dụng chỉ số từ 2^31 đến 2^32-1. Ví dụ, chỉ số 44' tương ứng với chỉ số thực tế 2^31 + 44.

Để tạo ra một địa chỉ nhận cụ thể, chúng ta phái sinh một cặp khóa con từ khóa chính và mã chuỗi chính. Sau đó, chúng ta sử dụng chỉ số để phân biệt giữa các cặp khóa con khác nhau ở cùng một độ sâu.

Khóa mở rộng, như XPUB, cho phép bạn chia sẻ ví của mình với nhiều người. Đường dẫn phái sinh được sử dụng để phân biệt giữa chuỗi bên ngoài (địa chỉ dự định được chia sẻ) và chuỗi bên trong (địa chỉ thay đổi).

Trong chương tiếp theo, chúng ta sẽ nghiên cứu về địa chỉ nhận, lợi ích của việc sử dụng chúng, và các bước liên quan trong việc xây dựng chúng.

# Địa chỉ Bitcoin là gì?
<partId>81ec8d17-f8ee-5aeb-8035-d370866f4281</partId>

## Địa chỉ Bitcoin
<chapterId>0a887ed8-3424-5a52-98e1-e4b406150475</chapterId>

Trong chương này, chúng ta sẽ khám phá các địa chỉ nhận, đóng vai trò quan trọng trong hệ thống Bitcoin. Chúng cho phép tiền được nhận trong một giao dịch và được tạo ra từ các cặp khóa riêng và khóa công khai. Mặc dù có một loại script gọi là Pay2PublicKey cho phép khóa bitcoin vào một khóa công khai, người dùng thường thích sử dụng địa chỉ nhận thay vì script này.

![image](assets/image/section5/0.webp)

Khi người nhận muốn nhận bitcoin, họ cung cấp một địa chỉ nhận cho người gửi thay vì khóa công khai của họ. Một địa chỉ thực sự là một băm của khóa công khai, với một định dạng cụ thể. Khóa công khai được phái sinh từ khóa riêng con thông qua các phép toán toán học như cộng điểm và nhân đôi trên đường cong elliptic.

![image](assets/image/section5/1.webp)

Quan trọng là phải lưu ý rằng không thể đảo ngược từ địa chỉ sang khóa công khai, cũng như từ khóa công khai sang khóa riêng. Sử dụng địa chỉ giảm kích thước của thông tin khóa công khai, ban đầu là 512 bit.

Địa chỉ Bitcoin đã được giảm kích thước để thuận tiện sử dụng. Chúng có một mã kiểm tra, cho phép phát hiện lỗi đánh máy và giảm nguy cơ mất bitcoin. Ngược lại, khóa công khai không có mã kiểm tra, nghĩa là lỗi đánh máy có thể dẫn đến mất tiền tương ứng.

Địa chỉ cũng cung cấp một lớp bảo mật thứ hai giữa thông tin công khai và riêng tư, làm cho việc kiểm soát khóa riêng trở nên khó khăn hơn.

Rất quan trọng phải nhấn mạnh rằng mỗi địa chỉ chỉ nên được sử dụng một lần. Sử dụng lại cùng một địa chỉ gây ra vấn đề về quyền riêng tư và nên được tránh.

Các tiền tố khác nhau được sử dụng cho địa chỉ Bitcoin. Ví dụ, BC1Q tương ứng với địa chỉ Segwit V0, BC1P tương ứng với địa chỉ Taproot/Segwit V1, và các tiền tố 1 và 3 được liên kết với địa chỉ Pay2PublicKeyH/Pay2ScriptH (legacy). Trong bài học tiếp theo, chúng ta sẽ giải thích từng bước cách phái sinh một địa chỉ từ một khóa công khai.

## Làm thế nào để tạo một địa chỉ Bitcoin?
<chapterId>6dee7bf3-7767-5f8d-a01b-659b95cfe0a5</chapterId>

Trong chương này, chúng ta sẽ thảo luận về việc xây dựng một địa chỉ nhận cho các giao dịch Bitcoin. Một địa chỉ nhận là một biểu diễn chữ và số của một khóa công khai nén. Việc chuyển đổi một khóa công khai thành một địa chỉ nhận bao gồm nhiều bước.

### Bước 1: Nén khóa công khai

![image](assets/image/section5/14.webp)

Một địa chỉ được phái sinh từ một khóa công khai con.
Một khóa công khai là một điểm trên đường cong elliptic. Nhờ vào tính đối xứng của đường cong elliptic, một điểm trên đường cong elliptic sẽ có một tọa độ x liên kết với chỉ hai giá trị có thể có của y: dương hoặc âm. Tuy nhiên, trong giao thức Bitcoin, chúng ta làm việc với một tập hợp hữu hạn các số nguyên dương thay vì với tập hợp các số thực. Để phân biệt giữa hai giá trị có thể có của y, chỉ cần chỉ ra liệu y là chẵn hay lẻ.

Việc nén một khóa công khai giảm kích thước của nó từ 520 bit xuống còn 264 bit.

Chúng ta sử dụng tiền tố 0x02 cho y chẵn và 0x03 cho y lẻ. Đây là dạng nén của khóa công khai.

### Bước 2: Băm khóa công khai đã nén

![image](assets/image/section5/3.webp)

Việc băm khóa công khai đã nén được thực hiện bằng hàm SHA256. Sau đó, hàm RIPEMD160 được áp dụng lên kết quả băm.

### Bước 3: Payload = Payload địa chỉ

![image](assets/image/section5/4.webp)

Kết quả băm nhị phân của RIPEMD160(SHA256(K)) được sử dụng để tạo thành các nhóm 5 bit. Mỗi nhóm được chuyển đổi thành cơ số 16 (Hexadecimal) và/hoặc cơ số 10.

### Bước 4: Thêm metadata để tính toán checksum với chương trình BCH

![image](assets/image/section5/5.webp)

Trong trường hợp của các địa chỉ legacy, chúng ta sử dụng băm SHA256 kép để tạo ra checksum của địa chỉ. Tuy nhiên, đối với các địa chỉ Segwit V0 và V1, chúng ta dựa vào công nghệ checksum BCH để đảm bảo phát hiện lỗi. Chương trình BCH có khả năng đề xuất và sửa chữa lỗi với xác suất lỗi cực kỳ thấp. Hiện tại, chương trình BCH được sử dụng để phát hiện và đề xuất các sửa đổi cần thực hiện, nhưng nó không tự động thực hiện chúng thay mặt người dùng.

Chương trình BCH yêu cầu nhiều thông tin đầu vào, bao gồm HRP (Human Readable Part) cần được mở rộng. Việc mở rộng HRP bao gồm việc mã hóa mỗi chữ cái theo cơ số 2 dựa trên mã ASCII của chúng. Sau đó, lấy 3 bit đầu tiên của kết quả cho mỗi chữ cái và chuyển đổi chúng sang cơ số 10 (màu xanh trong hình). Chèn một dấu phân cách 0. Sau đó nối tiếp 5 bit của mỗi chữ cái đã được chuyển đổi sang cơ số 10 trước đó (màu vàng trong hình).

Việc mở rộng HRP sang cơ số 10 cho phép tách biệt 5 bit cuối cùng của mỗi ký tự, do đó tăng cường checksum.

Phiên bản Segwit V0 được biểu diễn bằng mã 00 và "payload" được hiển thị bằng màu đen, trong cơ số 10. Điều này được theo sau bởi sáu ký tự dành riêng cho checksum.

### Bước 5: Tính toán checksum với chương trình BCH

![image](assets/image/section5/6.webp)

Dữ liệu đầu vào chứa metadata sau đó được gửi đến chương trình BCH để nhận checksum trong cơ số 10.

Đây là checksum.

### Bước 6: Xây dựng địa chỉ và chuyển đổi sang Bech32

![image](assets/image/section5/7.webp)

Việc nối liền phiên bản, payload và checksum cho phép xây dựng địa chỉ. Các ký tự cơ số 10 sau đó được chuyển đổi thành ký tự Bech32 sử dụng bảng tương ứng. Bảng chữ cái Bech32 bao gồm tất cả các ký tự chữ và số, trừ 1, b, i, và o, để tránh bất kỳ sự nhầm lẫn nào.

### Bước 7: Thêm HRP và dấu phân cách

![image](assets/image/section5/8.webp)

Màu hồng, checksum.
Màu đen, payload = băm của khóa công khai.
Màu xanh, phiên bản.
Mọi thứ đều được chuyển đổi thành Bech32, sau đó thêm 'bc' cho bitcoin và '1' làm dấu phân cách, và đây là địa chỉ.
# Tiếp tục
<partId>58111408-b734-54db-9ea7-0d5b67f99f99</partId>

## Tạo một seed từ 128 lần lắc xúc xắc!
<chapterId>0f4d40a7-cf0e-5faf-bc4d-691486771ac1</chapterId>

Việc tạo ra một cụm từ ghi nhớ là bước quan trọng trong việc bảo vệ ví tiền mã hóa của bạn. Có một số phương pháp để tạo ra cụm từ ghi nhớ, tuy nhiên, chúng ta sẽ tập trung vào phương pháp tạo ra thủ công sử dụng xúc xắc. Quan trọng là phải lưu ý rằng phương pháp này không phù hợp cho ví có giá trị cao. Được khuyến nghị sử dụng phần mềm mã nguồn mở hoặc ví cứng để tạo ra cụm từ ghi nhớ. Để tạo ra một cụm từ ghi nhớ, chúng ta sẽ sử dụng xúc xắc để tạo ra thông tin nhị phân. Mục tiêu là hiểu quy trình tạo ra cụm từ ghi nhớ.

**Bước 1 - Chuẩn bị:**
Đảm bảo bạn có một bản phân phối Linux không lưu trữ, như Tails OS, được cài đặt trên một chiếc USB để tăng cường bảo mật. Lưu ý rằng hướng dẫn này không nên được sử dụng để tạo một ví chính.

**Bước 2 - Tạo một số nhị phân ngẫu nhiên:**
Chúng ta sẽ sử dụng xúc xắc để tạo ra thông tin nhị phân. Lắc một con xúc xắc 128 lần và ghi lại từng kết quả (1 cho lẻ, 0 cho chẵn).

**Bước 3 - Sắp xếp các số nhị phân:**
Sắp xếp các số nhị phân đã thu được thành các hàng 11 chữ số để thuận tiện cho việc tính toán sau này. Hàng thứ mười hai chỉ nên có 7 chữ số.

**Bước 4 - Tính toán checksum:**
4 chữ số cuối cùng cho hàng thứ mười hai tương ứng với checksum. Để tính checksum này, chúng ta cần sử dụng terminal từ một bản phân phối Linux. Được khuyến nghị sử dụng [TailOs](https://tails.boum.org/index.fr.html), đây là một bản phân phối không lưu trữ có thể khởi động từ USB. Một khi đã ở trên terminal của bạn, nhập lệnh `echo <số nhị phân> | shasum -a 254 -0`. Thay thế `<số nhị phân>` bằng danh sách 128 số không và một của bạn. Đầu ra là một hash hệ thập lục phân. Ghi lại ký tự đầu tiên của hash này và chuyển đổi nó thành nhị phân. Bạn có thể sử dụng [bảng](https://www.educative.io/answers/decimal-binary-and-hex-conversion-table) này để được hỗ trợ. Thêm checksum nhị phân (4 chữ số) vào hàng thứ mười hai của tờ của bạn.

**Bước 5 - Chuyển đổi sang thập phân:**
Để tìm các từ tương ứng với mỗi hàng của bạn, trước tiên bạn cần chuyển đổi mỗi chuỗi 11 bit sang thập phân. Tại đây, bạn không thể sử dụng bộ chuyển đổi trực tuyến vì những bit này đại diện cho cụm từ ghi nhớ của bạn. Do đó, bạn sẽ cần chuyển đổi sử dụng máy tính và một mẹo như sau: mỗi bit được liên kết với một lũy thừa của 2, vì vậy từ trái sang phải, chúng ta có 11 bậc tương ứng với 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1. Để chuyển đổi chuỗi 11 bit của bạn sang thập phân, chỉ cần cộng dồn các bậc chứa số 1. Ví dụ, đối với chuỗi 00110111011, điều này tương ứng với phép cộng sau: 256 + 128 + 32 + 16 + 8 + 2 + 1 = 443. Bây giờ bạn có thể chuyển đổi mỗi hàng sang thập phân. Và trước khi chuyển sang mã hóa thành từ, thêm +1 vào tất cả các hàng vì chỉ mục của danh sách từ BIP39 bắt đầu từ 1, không phải 0.

**Bước 8 - Tạo ra cụm từ ghi nhớ:**
Bắt đầu bằng cách in [danh sách 2048 từ](https://seedxor.com/files/wordlist.pdf) để chuyển đổi giữa các số thập phân của bạn và các từ BIP39. Điều đặc biệt của danh sách này là không có từ nào chia sẻ 4 chữ cái đầu tiên với bất kỳ từ nào khác trong từ điển này. Sau đó, tìm kiếm từ được liên kết với mỗi số thập phân của dòng bạn. **Bước 9 - Kiểm tra Cụm từ Ghi nhớ:**
Ngay lập tức kiểm tra cụm từ ghi nhớ của bạn trên Sparrow Wallet bằng cách tạo một ví từ nó. Nếu bạn nhận được lỗi checksum không hợp lệ, có khả năng bạn đã mắc lỗi tính toán. Sửa lỗi này bằng cách quay lại bước 4 và kiểm tra lại trên Sparrow Wallet. Voilà! Bạn vừa tạo một ví Bitcoin mới từ 128 lần lắc xúc xắc.

Tạo ra một cụm từ ghi nhớ là một quá trình quan trọng để bảo mật ví tiền điện tử của bạn. Được khuyến nghị sử dụng các phương pháp an toàn hơn, như sử dụng phần mềm mã nguồn mở hoặc ví cứng, để tạo ra cụm từ ghi nhớ. Tuy nhiên, việc hoàn thành xưởng này giúp hiểu rõ hơn về cách chúng ta có thể tạo một ví Bitcoin từ một số ngẫu nhiên.

## BONUS: Phỏng vấn với Théo Pantamis
<chapterId>39f0ec5a-e258-55cb-9789-bc46d314d816</chapterId>

Một phương pháp mã hóa khác được sử dụng rộng rãi trên giao thức Bitcoin là phương pháp của chữ ký số.

![video](https://youtu.be/c9MvtGJsEvY?si=bQ1N5NCd6op0G6nW)



## Đánh giá khóa học
<chapterId>0cd71541-a7fd-53db-b66a-8611b6a28b04</chapterId>
<isCourseReview>true</isCourseReview>

## Kỳ thi cuối cùng
<chapterId>a53ea27d-0f84-56cd-b37c-a66210a4b31d</chapterId>
<isCourseExam>true</isCourseExam>


## Kết luận và Kết thúc
<chapterId>d291428b-3cfa-5394-930e-4b514be82d5a</chapterId>

### Cảm ơn và tiếp tục khám phá hố thỏ

Chúng tôi xin chân thành cảm ơn bạn đã hoàn thành khóa học Crypto 301. Chúng tôi hy vọng trải nghiệm này đã mang lại cho bạn sự phong phú và giáo dục. Chúng tôi đã đề cập đến nhiều chủ đề thú vị, từ toán học đến mã hóa học đến cách thức hoạt động của giao thức Bitcoin.

Nếu bạn muốn tìm hiểu sâu hơn về chủ đề, chúng tôi có một tài nguyên bổ sung để cung cấp cho bạn. Chúng tôi đã thực hiện một cuộc phỏng vấn độc quyền với Théo Pantamis và Loïc Morel, hai chuyên gia nổi tiếng trong lĩnh vực mã hóa học. Cuộc phỏng vấn này khám phá các khía cạnh sâu rộng của chủ đề và cung cấp các góc nhìn thú vị.

Hãy thoải mái xem cuộc phỏng vấn này để tiếp tục khám phá lĩnh vực mã hóa học hấp dẫn. Chúng tôi hy vọng nó sẽ hữu ích và truyền cảm hứng cho hành trình của bạn. Một lần nữa, cảm ơn bạn đã tham gia và cam kết suốt khóa học này.

### Hỗ trợ Chúng Tôi

Khóa học này, cùng với tất cả nội dung trên trường đại học này, đã được cung cấp miễn phí cho bạn bởi cộng đồng của chúng tôi. Để hỗ trợ chúng tôi, bạn có thể chia sẻ nó với người khác, trở thành thành viên của trường đại học, và thậm chí đóng góp vào sự phát triển của nó qua GitHub. Thay mặt cho toàn bộ đội ngũ, cảm ơn bạn!

### Đánh giá khóa học

Một hệ thống đánh giá cho việc đào tạo sẽ sớm được tích hợp vào nền tảng E-learning mới này! Trong thời gian chờ đợi, cảm ơn rất nhiều vì đã tham gia khóa học, và nếu bạn thích nó, xin hãy xem xét chia sẻ nó với người khác.
