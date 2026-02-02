---
name: Lập trình Bitcoin
goal: Xây dựng một thư viện Bitcoin hoàn chỉnh từ đầu và hiểu rõ nền tảng mật mã của Bitcoin.
objectives: 

 - Triển khai các phép toán số học trường hữu hạn và phép toán đường cong elliptic trong Python.
 - Xây dựng và phân tích các giao dịch Bitcoin bằng lập trình.
 - Tạo địa chỉ mạng thử nghiệm và phát sóng các giao dịch trên mạng.
 - Nắm vững nền tảng toán học đằng sau mô hình bảo mật của Bitcoin.

---
# Hành trình khám phá các kịch bản và chương trình của Bitcoin


Khóa học chuyên sâu kéo dài hai ngày này, do Jimmy Song giảng dạy, sẽ đưa bạn đi sâu vào nền tảng kỹ thuật của Bitcoin bằng cách xây dựng một thư viện Bitcoin hoàn chỉnh từ đầu. Bắt đầu với các kiến thức toán học cơ bản về trường hữu hạn và đường cong elliptic, bạn sẽ tiến đến phân tích cú pháp giao dịch, thực thi kịch bản và giao tiếp mạng. Thông qua các bài tập lập trình thực hành trong Jupyter notebooks, bạn sẽ tạo địa chỉ testnet của riêng mình, xây dựng các giao dịch thủ công và phát sóng chúng trực tiếp lên mạng—đồng thời hiểu sâu sắc các nguyên tắc mật mã giúp Bitcoin an toàn và không cần tin tưởng.


Chúc bạn có một chuyến đi vui vẻ!


+++

# Giới thiệu


<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>


## Tổng quan khóa học


<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>


Chào mừng bạn đến với khóa học PRO 202 _**Lập trình Bitcoin**_, một hành trình chuyên sâu đưa bạn từ số học trường hữu hạn đến việc xây dựng và phát sóng các giao dịch thực tế trên Testnet của Bitcoin.


Trong khóa học này, bạn sẽ từng bước xây dựng thư viện Bitcoin bằng Python đồng thời nắm vững các kiến thức cơ bản về mật mã, giao thức và phần mềm cần thiết để hiểu chính xác về tính bảo mật và hoạt động bên trong của Bitcoin. Phương pháp của PRO 202 hoàn toàn mang tính thực hành: mọi khái niệm đều được triển khai ngay lập tức trong Jupyter notebooks, đảm bảo lý thuyết và mã lập trình bổ trợ lẫn nhau.


### Các Khái Niệm Toán Học Cơ Bản cho Bitcoin


Phần đầu tiên này thiết lập nền tảng toán học thiết yếu. Bạn sẽ triển khai các phép toán số học trường hữu hạn và các phép toán trên đường cong elliptic (luật nhóm, phép cộng, phép nhân đôi, phép nhân vô hướng...) — những điều kiện tiên quyết cho ECDSA. Mục tiêu có hai phần: hiểu cấu trúc đại số cho phép tạo ra chữ ký mật mã và xây dựng các công cụ Python đáng tin cậy để thao tác với chúng.


Tiếp theo, bạn sẽ chính thức hóa các thành phần của ECDSA: tạo khóa, định dạng điểm, băm, tạo chữ ký và xác minh. Phần này kết nối trực tiếp lý thuyết với thực tiễn, nhấn mạnh các chi tiết triển khai và tính mạnh mẽ của mô hình bảo mật cơ bản.


### Cơ chế hoạt động bên trong của giao dịch Bitcoin


Trong phần thứ hai, bạn sẽ phân tích cấu trúc của một giao dịch Bitcoin: UTXO, đầu vào/đầu ra, chuỗi, kịch bản, mã hóa, và hơn thế nữa. Bạn sẽ viết mã để xây dựng, ký và xác minh các giao dịch, từ đó hiểu chính xác những gì được cam kết bởi hàm băm và lý do tại sao.


Tiếp theo, bạn sẽ triển khai một trình thực thi _Script_ tối thiểu, xem xét các mã lệnh chính và xác thực các đường dẫn chi tiêu. Mục tiêu là giúp bạn có khả năng kiểm toán hành vi giao dịch, chẩn đoán các lỗi xác thực và suy luận về tính an toàn của các chính sách chi tiêu.


### Cơ chế hoạt động bên trong mạng Bitcoin


Trong phần thứ ba, bạn sẽ đặt các giao dịch vào trong hệ thống tổng thể: cấu trúc khối, tiêu đề, độ khó và cơ chế Proof-of-Work. Bạn sẽ xử lý các thông điệp giao thức, tiêu đề khối và cây Merkle.


Cuối cùng, bạn sẽ nghiên cứu về giao tiếp giữa các nút ngang hàng, tối ưu hóa tin nhắn và giới thiệu về SegWit.


Cũng như mọi khóa học khác trên Plan ₿ Academy, phần cuối cùng bao gồm một bài kiểm tra đánh giá được thiết kế để củng cố kiến thức của bạn. Sẵn sàng khám phá cơ chế hoạt động bên trong của Bitcoin và viết mã vận hành nó chưa? Hãy bắt đầu nào!










# Các Khái Niệm Toán Học Cơ Bản cho Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Toán học ứng dụng trong triển khai Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>


![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


### Bitcoin - Những nền tảng lập trình: Các cấu trúc toán học cốt lõi


Khóa học này cô đọng những kiến thức toán học thiết yếu đằng sau các hệ thống mã hóa của Bitcoin thành một quy trình làm việc thực tiễn cao. Các khái niệm được giải thích, minh họa bằng ví dụ, và sau đó được triển khai trong Jupyter Notebook. Ý tưởng chủ đạo rất đơn giản: bạn chỉ thực sự hiểu một thuật toán mã hóa cơ bản khi bạn tự viết mã cho nó. Trong suốt hai ngày học, học viên sẽ truy cập địa chỉ mạng thử nghiệm generate, xây dựng và phát sóng các giao dịch, và cuối cùng tương tác với mạng mà không cần đến trình khám phá khối. Tất cả những điều này đòi hỏi một nền tảng vững chắc về trường hữu hạn và đường cong elip.


### Trường hữu hạn: Động cơ số học của mật mã học


Trường hữu hạn F(p) là một hệ thống số học được định nghĩa bởi một số nguyên tố p, chứa các phần tử từ 0 đến p–1. Trường nguyên tố đảm bảo rằng mọi phần tử khác 0 đều có phần tử nghịch đảo và tất cả các phép toán đều nằm trong phạm vi trường. Phép toán số học được thực hiện bằng cách sử dụng phép toán modulo p cho phép cộng, trừ và nhân. Hàm `pow(base, exp, mod)` của Python cho phép lũy thừa modulo hiệu quả, rất quan trọng đối với các số mũ lớn được sử dụng trong các hoạt động mã hóa thực tế.


#### Hành vi nhân

Nhân bất kỳ phần tử k nào khác 0 với tất cả các phần tử của một trường số nguyên tố sẽ tạo ra một hoán vị của trường đó. Thuộc tính này đảm bảo tính đồng nhất và ngăn ngừa các điểm yếu về cấu trúc, khiến các trường số nguyên tố trở nên lý tưởng cho việc tạo khóa an toàn và chữ ký số.


#### Phép chia và Định lý nhỏ Fermat

Phép chia được thực hiện thông qua nghịch đảo phép nhân. Định lý nhỏ Fermat phát biểu rằng:

n^(p–1) ≡ 1 (mod p),

Vì vậy, nghịch đảo là n^(p–2). Python hỗ trợ trực tiếp điều này với `pow(n, -1, p)`. Các phép toán này xuất hiện liên tục trong các thuật toán mã hóa cơ bản của ECDSA và Bitcoin.


### Đường cong Elliptic: Cấu trúc phi tuyến tính cho bảo mật khóa công khai


Đường cong elip tuân theo phương trình y² = x³ + ax + b. Bitcoin sử dụng secp256k1, được định nghĩa là y² = x³ + 7 trên một trường hữu hạn. Các điểm trên một đường cong elip tạo thành một nhóm toán học theo phép cộng điểm. Một đường thẳng đi qua hai điểm P và Q cắt đường cong tại điểm thứ ba R; phản chiếu R qua trục x ta được P + Q. Hệ thống này có tính chất kết hợp và bao gồm một phần tử đơn vị: điểm vô cực.


Việc nhân đôi một điểm sử dụng đường tiếp tuyến thay vì đường cát tuyến, với độ dốc được suy ra từ đạo hàm của đường cong. Mặc dù các công thức này liên quan đến phép tính vi phân và tích phân trên tập số thực, chúng trở nên hoàn toàn rời rạc và chính xác khi đường cong được xác định trên một trường hữu hạn — bối cảnh được sử dụng trong Bitcoin.


### Từ Toán học đến Mật mã Bitcoin


Trường hữu hạn cung cấp phép toán số học xác định và khả nghịch; đường cong elliptic cung cấp cấu trúc phi tuyến tính, trong đó việc tính toán k·P rất dễ dàng nhưng việc đảo ngược nó lại bất khả thi về mặt tính toán. Kết hợp cả hai tạo nên nền tảng cho các khóa công khai/riêng tư, chữ ký ECDSA và bảo mật giao dịch của Bitcoin. Hiểu được những nguyên tắc cơ bản này giúp sinh viên có thể trực tiếp triển khai các khóa, giao dịch và chữ ký mà không cần đến các lớp trừu tượng hoặc công cụ bên ngoài.


## Mật mã đường cong Elliptic

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>


![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


Chương này giới thiệu các đường cong elip được định nghĩa trên trường hữu hạn và giải thích lý do tại sao chúng tạo thành xương sống toán học của mật mã Bitcoin. Trong khi các đường cong elip trên tập số thực trông mượt mà và liên tục, việc áp dụng cùng các phương trình đó trên trường hữu hạn tạo ra một tập hợp các điểm rời rạc, phân tán. Mặc dù có sự khác biệt về mặt hình ảnh, tất cả các công thức cộng điểm, độ dốc và quy tắc đại số đều hoạt động chính xác như nhau—chỉ có phép toán số học thay đổi thành phép toán số học modulo. Bitcoin sử dụng đường cong y² = x³ + 7 (secp256k1), bảo toàn tính đối xứng và hành vi phi tuyến tính cần thiết cho bảo mật mật mã.


### Xác minh các điểm và triển khai trường hữu hạn


Một điểm nằm trên đường cong elliptic trường hữu hạn nếu tọa độ của nó thỏa mãn phương trình đường cong theo modulo p. Việc xác minh một điểm như (73,128) trên F₁₃₇ yêu cầu kiểm tra xem y² mod p có bằng x³ + 7 mod p hay không. Việc triển khai điều này trong mã lập trình bao gồm việc tạo ra các lớp cho các phần tử trường hữu hạn và các điểm trên đường cong. Việc nạp chồng toán tử đảm bảo rằng tất cả các phép toán số học—cộng, nhân, lũy thừa, chia—đều được thực hiện tự động theo modulo p. Khi các khái niệm trừu tượng này tồn tại, các hoạt động mật mã nâng cao hơn sẽ trở nên dễ dàng hơn để viết và suy luận.


#### Tính chất của nhóm và phép cộng điểm

Các điểm trên đường cong elip tạo thành một nhóm toán học dưới phép cộng. Nhóm này thỏa mãn tính chất đóng, tính chất kết hợp, tính chất đơn vị (điểm vô cực) và tính chất nghịch đảo (phản xạ qua trục x). Các phép dựng hình học xác nhận các tính chất này, làm cho phép nhân vô hướng (P được cộng với chính nó nhiều lần) được xác định rõ ràng. Các quy tắc nhóm này cho phép mật mã đường cong elip và đảm bảo hành vi nhất quán, có thể dự đoán được dưới các phép toán điểm lặp lại.


### Các nhóm tuần hoàn và bài toán logarit rời rạc


Việc chọn một điểm sinh G trên một đường cong cho phép ta tạo ra một nhóm tuần hoàn: G, 2G, 3G, …, nG = 0. Các điểm này xuất hiện phi tuyến tính và khó dự đoán, ngay cả khi được tạo ra theo trình tự. Tính khó dự đoán này tạo nên nền tảng cho bài toán logarit rời rạc: việc tính P = sG rất dễ dàng, nhưng việc xác định s từ P lại bất khả thi về mặt tính toán đối với các nhóm lớn. Hàm một chiều này chính là điều làm cho mật mã khóa công khai trở nên an toàn. Các giá trị vô hướng (khóa riêng) được viết bằng chữ thường; các điểm (khóa công khai) được viết bằng chữ hoa.


#### Phép nhân vô hướng hiệu quả

Để tính toán sG một cách hiệu quả, các thuật toán sử dụng thuật toán nhân đôi và cộng: quét biểu diễn nhị phân của số vô hướng, nhân đôi điểm ở mỗi bước và chỉ cộng G khi bit là 1. Điều này giảm phép tính từ O(n) phép cộng xuống O(log n), cho phép thực hiện các hoạt động mã hóa thực tế ngay cả với số vô hướng 256 bit.


#### Đường cong secp256k1 trong Bitcoin


Bitcoin sử dụng đường cong secp256k1, được định nghĩa bởi y² = x³ + 7 trên trường số nguyên tố, trong đó p = 2²⁵⁶ − 2³² − 977. Điểm sinh G có tọa độ cố định được chọn bằng quy trình NUMS ("không có gì trong tay áo") mang tính xác định. Bậc nhóm n là một số nguyên tố lớn gần với 2²⁵⁶, đảm bảo rằng mọi điểm khác 0 đều tạo ra cùng một nhóm. Kích thước của 2²⁵⁶ (~10⁷⁷) là cực kỳ lớn, khiến việc tấn công vét cạn để tìm ra khóa riêng là bất khả thi về mặt vật lý. Ngay cả một nghìn tỷ siêu máy tính hoạt động trong một nghìn tỷ năm cũng không thể làm giảm không gian khóa một cách đáng kể.


### Khóa công khai, khóa riêng tư và mã số định danh SEC


Khóa riêng là một số ngẫu nhiên s; khóa công khai là P = sG. Vì việc giải bài toán logarit rời rạc là không khả thi, nên P có thể được chia sẻ mà không tiết lộ s. Khóa công khai phải được tuần tự hóa để truyền bằng định dạng SEC. Định dạng SEC không nén sử dụng 65 byte: tiền tố 0x04 + tọa độ x + tọa độ y. Định dạng nén chỉ sử dụng 33 byte: tiền tố 0x02 hoặc 0x03 (tùy thuộc vào tính chẵn lẻ của y) + tọa độ x. Bitcoin ban đầu sử dụng khóa không nén nhưng hiện nay ưu tiên sử dụng khóa nén để tăng hiệu quả.


#### Bitcoin Address Sáng tạo


Địa chỉ Bitcoin là mã băm của khóa công khai, chứ không phải là chính khóa thô. Để chuyển đổi một địa chỉ thành generate, ta thực hiện các bước sau: mã hóa khóa công khai theo định dạng SEC, tính toán mã băm 160 (SHA-256 sau đó là RIPEMD-160), thêm tiền tố mạng (0x00 cho mainnet, 0x6F cho mạng thử nghiệm), tính toán tổng kiểm tra bằng cách sử dụng SHA-256 kép, thêm bốn byte tổng kiểm tra đầu tiên và mã hóa kết quả bằng Base58. Quá trình mã hóa này loại bỏ các ký tự không rõ ràng và bao gồm tổng kiểm tra để ngăn ngừa lỗi sao chép. Quy trình nhiều bước này che giấu khóa công khai cho đến khi có giao dịch chi tiêu, thêm mã định danh mạng và đảm bảo các địa chỉ dễ đọc, chống lỗi.


# Cơ chế hoạt động bên trong của giao dịch Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Phân tích giao dịch và chữ ký ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>


![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


### Tìm hiểu về ECDSA: Nền tảng chữ ký số của Bitcoin


Bitcoin dựa trên ECDSA, một lược đồ chữ ký dựa trên đường cong elip, cung cấp tính bảo mật mạnh mẽ với kích thước khóa nhỏ hơn nhiều so với RSA. Tính bảo mật của nó đến từ bài toán logarit rời rạc trên đường cong elip: cho P = eG, việc tính toán P rất dễ dàng, nhưng việc suy ra e từ P lại bất khả thi về mặt tính toán. Sự bất đối xứng này cho phép mã hóa khóa công khai trong khi vẫn giữ an toàn cho các khóa riêng tư.


#### Mã hóa DER của chữ ký ECDSA


Bitcoin mã hóa chữ ký ECDSA bằng định dạng DER:


- 0x30 (dấu hiệu trình tự)
- độ dài byte
- 0x02 + độ dài + R byte
- 0x02 + độ dài + S byte


Điều này làm tăng chi phí xử lý, mở rộng chữ ký 64 byte lên khoảng 71–72 byte. Taproot loại bỏ sự thiếu hiệu quả này bằng cách áp dụng chữ ký Schnorr có kích thước cố định.


### Cam kết và quy trình ký kết


Chữ ký ECDSA dựa trên phương trình cam kết: UG + VP = KG. Người ký chọn các giá trị U và V khác 0, và một số ngẫu nhiên K, chứng minh rằng họ biết khóa riêng mà không tiết lộ nó. Thông điệp được băm thành Z, một số ngẫu nhiên K được tạo ra, R là tọa độ x của KG, và S = (Z + RE)/K. Chữ ký là cặp (R, S). Bảo mật phụ thuộc rất nhiều vào việc sử dụng một số K duy nhất, không thể dự đoán được — nếu K được sử dụng lại hoặc bị rò rỉ, khóa riêng sẽ bị xâm phạm. Các triển khai hiện đại sử dụng việc tạo K xác định (RFC 6979) để tránh các lỗi của bộ tạo số ngẫu nhiên.


#### Xác minh chữ ký

Với Z, (R, S) và khóa công khai P, người xác minh tính toán U = Z/S và V = R/S, sau đó kiểm tra xem tọa độ x của UG + VP có bằng R hay không. Điều này hoạt động vì đại số xác minh tái tạo KG mà không cần khóa riêng. Việc làm giả chữ ký sẽ yêu cầu giải quyết bài toán logarit rời rạc hoặc phá vỡ hàm băm.


#### Chữ ký Schnorr và bối cảnh lịch sử


Chữ ký Schnorr có tính toán gọn gàng hơn và hỗ trợ các tính năng tổng hợp, nhưng đã được cấp bằng sáng chế khi Bitcoin ra mắt. ECDSA cung cấp một giải pháp thay thế miễn phí, mặc dù phức tạp hơn và yêu cầu chữ ký lớn hơn. Sau khi bằng sáng chế hết hạn, Bitcoin đã bổ sung chữ ký Schnorr thông qua Taproot, cung cấp chữ ký cố định 64 byte và cải thiện quyền riêng tư. ECDSA vẫn được hỗ trợ để đảm bảo khả năng tương thích với các hệ thống cũ.



### Cấu trúc giao dịch và đầu vào/đầu ra


Một giao dịch Bitcoin bao gồm:


- phiên bản (4 byte, little-endian)
- danh sách đầu vào
- danh sách đầu ra
- thời gian khóa (4 byte)


Các tham chiếu đầu vào đề cập đến các UTXO trước đó bằng mã băm giao dịch và chỉ mục đầu ra của chúng, và bao gồm một kịch bản mở khóa (scriptSig) và một số thứ tự được sử dụng cho khóa thời gian hoặc RBF. Các tham chiếu đầu ra chỉ định số tiền (8 byte) và kịch bản khóa (scriptPubKey), xác định các điều kiện chi tiêu. Địa chỉ Bitcoin là biểu diễn của các kịch bản này.


#### Mô hình UTXO

Bitcoin theo dõi các UTXO chưa được sử dụng thay vì số dư tài khoản. UTXO phải được sử dụng toàn bộ — việc sử dụng một phần là không thể. Để sử dụng 1 BTC từ 100 BTC trong UTXO, giao dịch phải bao gồm một UTXO trả lại tiền thừa. Nếu quên UTXO trả lại tiền thừa, số tiền còn lại sẽ trở thành phí khai thác.


#### Tuần tự hóa và phân tích cú pháp giao dịch


Các giao dịch sử dụng định dạng nhị phân nhỏ gọn. Sau trường phiên bản, một biến kiểu varint mã hóa số lượng đầu vào. Các đầu vào bao gồm:


- Mã băm giao dịch trước đó (32 byte)
- chỉ mục đầu ra (4 byte)
- scriptSig (varstr)
- chuỗi (4 byte)


Đầu ra bao gồm một lượng 8 byte và scriptPubKey (varstr). Thời gian khóa kiểm soát thời điểm giao dịch trở nên hợp lệ. Quá trình tuần tự hóa sử dụng thứ tự little-endian cho hầu hết các số nguyên. Trình phân tích cú pháp tiêu thụ các byte theo trình tự và ủy thác cho các lớp chuyên biệt cho đầu vào, đầu ra và tập lệnh.


### Phí, Thay đổi và Tính linh hoạt


Phí được tính ngầm định:

Phí = tổng (giá trị đầu vào) – tổng (giá trị đầu ra).

Bất kỳ giá trị nào chưa được gán sẽ trở thành phí, do đó việc xây dựng đầu ra tiền thừa chính xác là rất cần thiết. Trước SegWit, chữ ký cho phép sự thay đổi linh hoạt—việc sửa đổi S thành N-S tạo ra một giao dịch hợp lệ mới với ID khác. Bitcoin hiện thực thi quy tắc S thấp, và SegWit tách biệt chữ ký khỏi phép tính txid, làm cho ID ổn định và cho phép các giao thức lớp thứ hai như Lightning.


## Xác thực tập lệnh và giao dịch Bitcoin

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>


![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


Bitcoin Script là một ngôn ngữ hợp đồng thông minh nhỏ gọn, dựa trên ngăn xếp, định nghĩa cách thức chi tiêu tiền điện tử. Mỗi đầu ra đều mang một scriptPubKey (script khóa) và mỗi đầu vào đều mang một scriptSig (script mở khóa). Cả hai cùng nhau tạo thành một chương trình phải được đánh giá là "đúng" thì giao dịch chi tiêu mới hợp lệ. Script được thiết kế không phải là ngôn ngữ Turing-complete để tất cả các đường dẫn thực thi đều có thể dự đoán được và dễ dàng xác thực trên toàn mạng.


### Mô hình vận hành và thực thi kịch bản


Một kịch bản là một chuỗi các phần tử dữ liệu và mã lệnh. Dữ liệu được đẩy (chữ ký, khóa công khai, hàm băm) được đặt vào ngăn xếp, trong khi các mã lệnh bắt đầu bằng `OP_` biến đổi ngăn xếp. Sau khi thực thi, phần tử trên cùng của ngăn xếp phải khác 0 để thành công. Ví dụ: `OP_DUP` sao chép phần tử trên cùng, `OP_HASH160` áp dụng SHA256 sau đó là RIPEMD160, và `OP_CHECKSIG` xác minh chữ ký so với hàm băm của giao dịch và khóa công khai, đẩy 1 nếu hợp lệ, 0 nếu không hợp lệ. Các quy tắc phân tích cú pháp phân biệt giữa dữ liệu thô (có tiền tố độ dài) và mã lệnh (được tra cứu theo giá trị byte), và một máy ảo nhỏ thực thi chúng một cách xác định trên mỗi nút.


### P2PK và P2PKH: Các mô hình thanh toán cốt lõi


Mô hình sớm nhất, Pay-to-Public-Key (P2PK), khóa tiền điện tử trực tiếp vào một khóa công khai hoàn chỉnh: scriptPubKey là `<pubkey> OP_CHECKSIG`, và scriptSig chỉ là một chữ ký. Nó đơn giản nhưng tốn nhiều không gian lưu trữ và làm lộ khóa công khai trước khi tiền được sử dụng.


#### P2PKH và Địa chỉ

Giao thức Pay-to-Public-Key-Hash (P2PKH) cải tiến điều này bằng cách khóa vào một mã băm 20 byte của khóa công khai. Tham số scriptPubKey là `OP_DUP OP_HASH160 <pubkey_hash> OP_EQUALVERIFY OP_CHECKSIG`, và tham số scriptSig cung cấp `<signature> <pubkey>`. Quá trình thực thi kiểm tra xem mã băm của khóa công khai được cung cấp có khớp với giá trị đã cam kết hay không, sau đó xác minh chữ ký. Điều này giúp che giấu khóa công khai cho đến khi đến thời điểm chi tiêu, giảm kích thước và phù hợp với định dạng địa chỉ mainnet quen thuộc “1…”.


### Xác thực giao dịch và băm chữ ký


Một nút xác thực giao dịch phải đảm bảo:

1) Mỗi đầu vào tham chiếu đến một đầu ra hiện có, chưa được sử dụng.

2) Tổng giá trị đầu vào ≥ tổng giá trị đầu ra (phần chênh lệch là phí).

3) Mỗi scriptSig mở khóa chính xác scriptPubKey được tham chiếu.


Việc xác thực chữ ký yêu cầu xây dựng lại chính xác thông điệp đã được ký, được gọi là sighash. Đối với ECDSA cũ, quá trình xác thực sẽ xóa tất cả các scriptSig, thay thế scriptSig của đầu vào hiện tại bằng scriptPubKey tương ứng, thêm một loại băm 4 byte (thường là `SIGHASH_ALL`), và băm kép kết quả. Giá trị 256 bit đó là thứ mà `OP_CHECKSIG` sử dụng. Các loại băm thay thế (ví dụ: `SINGLE`, `NONE`, có hoặc không có `ANYONECANPAY`) thay đổi các phần của giao dịch được cam kết, cho phép các trường hợp sử dụng đặc thù như tài trợ hợp tác hoặc các giao dịch được chỉ định một phần, nhưng chúng hiếm khi được sử dụng trong thực tế.


#### Băm bậc hai và SegWit

Vì mỗi đầu vào trong một giao dịch cũ yêu cầu tính toán sighash riêng biệt trên một cấu trúc bao gồm tất cả các đầu vào, thời gian xác thực có thể tăng theo cấp số nhân với số lượng đầu vào. Các giao dịch đa đầu vào lớn trước đây từng gây ra sự chậm trễ đáng kể trong quá trình xác thực. SegWit đã thiết kế lại việc tính toán sighash để lưu trữ các phần được chia sẻ và giảm độ phức tạp xuống thời gian tuyến tính, cải thiện khả năng mở rộng và làm cho các cuộc tấn công từ chối dịch vụ trở nên khó khăn hơn.


### Những câu đố về kịch bản và bài học về bảo mật


Script có thể thể hiện nhiều hơn là chỉ đơn giản "một chữ ký sẽ mở khóa số tiền này". Các câu đố Script chứng minh điều này bằng cách mã hóa các điều kiện tùy ý—các bài toán toán học, thử thách tìm ảnh ngược của hàm băm, hoặc thậm chí là phần thưởng va chạm—trong đó bất kỳ ai cung cấp dữ liệu chính xác đều có thể sử dụng số tiền đó. Tuy nhiên, các đầu ra chỉ dựa vào dữ liệu công khai (không có chữ ký) dễ bị tấn công "front-running" của thợ đào: một khi giải pháp hợp lệ xuất hiện trong mempool, bất kỳ thợ đào nào cũng có thể sao chép nó và chuyển hướng khoản thanh toán cho chính họ.


Bài học thực tiễn là các hợp đồng trong thế giới thực hầu như luôn bao gồm kiểm tra chữ ký, ngay cả khi chúng chứa logic phức tạp hơn như đa chữ ký, khóa thời gian hoặc khóa băm. Chữ ký ràng buộc giải pháp với một bên cụ thể, bảo toàn động cơ và ngăn chặn người khác đánh cắp khoản thanh toán. Hiểu mô hình ngăn xếp của Script, các mẫu chuẩn và những cạm bẫy tinh vi là điều cần thiết để thiết kế các hợp đồng thông minh Bitcoin an toàn và để hiểu cách các giao dịch thực sự được xác thực trên mạng.


## Xây dựng giao dịch và trả tiền theo kịch bản Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>


![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


### Giao dịch tòa nhà Bitcoin và P2SH


Quá trình xây dựng giao dịch Bitcoin kết nối kiến thức lý thuyết về giao thức với việc triển khai thực tiễn. Một giao dịch chọn các UTXO để chi tiêu, xây dựng các đầu ra bằng các tập lệnh khóa, tạo chữ ký cho mỗi đầu vào và tuần tự hóa mọi thứ theo đúng định dạng mà các nút mong đợi. Quá trình này đòi hỏi phải hiểu về việc tạo sighash, hành vi của Script và xử lý phí và tiền thừa chính xác.


### Cấu trúc giao dịch cơ bản


Mỗi đầu vào giao dịch tham chiếu đến một đầu ra trước đó của txid và chỉ mục. Đầu ra chỉ định số lượng tính bằng satoshi và các tập lệnh khóa. Sự khác biệt giữa tổng số đầu vào và tổng số đầu ra là phí. Để ký một đầu vào, một phiên bản đã được sửa đổi của giao dịch được tuần tự hóa, mã sighash của nó được tính toán và khóa riêng ký vào đó. Chữ ký và khóa công khai thu được tạo thành ScriptSig. Sau khi mọi đầu vào được ký, giao dịch thô có thể được phát sóng lên mạng.


### Giao dịch đa chữ ký


Phương pháp đa chữ ký cơ bản sử dụng `OP_CHECKMULTISIG` để yêu cầu m-of-n chữ ký. Do một lỗi sai lệch một đơn vị ban đầu, OP_CHECKMULTISIG tiêu tốn thêm một phần tử ngăn xếp, yêu cầu `OP_0` ban đầu trong ScriptSig. Phương pháp đa chữ ký cơ bản hoạt động được nhưng không hiệu quả: tất cả các khóa công khai đều xuất hiện dưới dạng on-chain, khiến scriptPubKeys trở nên lớn, tốn kém và khó mã hóa thành địa chỉ. Những hạn chế này đã thúc đẩy sự ra đời của phương pháp trả phí để tạo script-hash.


#### Kiến trúc P2SH

P2SH ẩn các kịch bản phức tạp đằng sau một mã băm HASH160 20 byte. Khóa công khai kịch bản (scriptPubKey) được cố định: `OP_HASH160 <mã băm 20 byte> OP_EQUAL`. Kịch bản chuộc lại cơ bản—chứa chữ ký đa chữ ký, khóa thời gian hoặc các điều kiện khác—chỉ được tiết lộ và thực thi khi chi tiêu. Người gửi chỉ thấy mã băm, trong khi người nhận quản lý kịch bản chuộc lại một cách riêng tư. Thiết kế này giúp giảm kích thước của on-chain, cải thiện tính bảo mật và cho phép thực hiện các hợp đồng phức tạp mà không gây gánh nặng cho người gửi.


### Chi tiêu và triển khai P2SH


Để sử dụng đầu ra P2SH, ScriptSig phải bao gồm dữ liệu mở khóa cần thiết *cộng với* chính kịch bản đổi thưởng. Quá trình xác thực diễn ra trong hai bước:

1) HASH160(redeem_script) phải khớp với mã băm scriptPubKey.

2) Sau khi xác minh, kịch bản đổi thưởng sẽ được thực thi với dữ liệu được cung cấp.


Khi tạo chữ ký cho đầu vào P2SH, quy trình sighash sử dụng tập lệnh đổi thưởng thay cho scriptPubKey. Mỗi người ký phải sở hữu toàn bộ tập lệnh đổi thưởng để có được chữ ký hợp lệ cho generate. Địa chỉ P2SH sử dụng byte phiên bản 0x05 trên mainnet (địa chỉ “3…”) và 0xC4 trên mạng thử nghiệm (địa chỉ “2…”).


#### Các cân nhắc thực tiễn về an ninh


Mất tập lệnh rút tiền đồng nghĩa với việc mất tiền: việc chi tiêu yêu cầu cả khóa riêng tư và chính tập lệnh rút tiền đó. Người tham gia Multisig phải xác minh rằng khóa công khai của họ đã được bao gồm chính xác trước khi chấp nhận tiền gửi. P2SH hỗ trợ các cấu trúc nâng cao như đa chữ ký, khóa thời gian và khóa băm, nhưng lỗi trong logic của tập lệnh có thể khóa tiền vĩnh viễn, vì vậy việc thử nghiệm trên mạng thử nghiệm là rất cần thiết.


P2SH cải thiện quyền riêng tư bằng cách ẩn các điều kiện chi tiêu cho đến lần chi tiêu đầu tiên, nhưng một khi kịch bản đổi thưởng xuất hiện trong on-chain, nó sẽ hiển thị vĩnh viễn. Mặc dù vậy, những lợi ích về kích thước nhỏ hơn, khả năng tương thích ngược và hỗ trợ hợp đồng linh hoạt đã biến P2SH thành một cột mốc quan trọng, ảnh hưởng đến các bản nâng cấp sau này như SegWit và Taproot.


# Cơ chế hoạt động bên trong mạng lưới Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Khối Bitcoin và Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>


![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


Các khối Bitcoin nhóm các giao dịch lại với nhau và bảo mật chúng bằng proof of work. Mỗi khối bao gồm một tiêu đề 80 byte cộng với một danh sách các giao dịch. Mặc dù việc tạo ra một khối hợp lệ tốn nhiều năng lượng, nhưng việc xác minh một khối lại rất rẻ: lưu trữ tất cả khoảng 900.000 tiêu đề chỉ cần khoảng 72 MB, cho phép ngay cả các thiết bị nhỏ cũng có thể xác minh proof of work của chuỗi một cách hiệu quả.


### Giao dịch Coinbase và phần thưởng khối


Mỗi khối bắt đầu bằng chính xác một giao dịch Coinbase—đây là cách duy nhất để bitcoin mới được đưa vào lưu thông. Nó có mã băm prev-tx bằng 0 và chỉ mục là 0xffffffff, xác định duy nhất nó. Phần thưởng bắt đầu ở mức 50 BTC và giảm một nửa sau mỗi 210.000 khối (50, 25, 12,5, 6,25, 3,125, …). Thợ đào cũng bao gồm phí giao dịch. Vì nonce 4 byte quá nhỏ đối với các ASIC hiện đại, thợ đào sửa đổi dữ liệu trong giao dịch Coinbase để thay đổi gốc Merkle và tạo thêm không gian tìm kiếm. BIP34 yêu cầu nhúng chiều cao khối vào scriptSig của Coinbase để đảm bảo mỗi Coinbase txid là duy nhất.


### Các trường tiêu đề khối và tín hiệu Soft Fork


Phần tiêu đề 80 byte chứa:


- phiên bản (4 byte)
- Mã băm khối trước đó (32 byte)
- Gốc Merkle (32 byte)
- dấu thời gian (4 byte)
- bit (mục tiêu độ khó, 4 byte)
- nonce (4 byte)


Số phiên bản đã phát triển thành một hệ thống tín hiệu trường bit thông qua BIP9, cho phép các thợ đào phối hợp sự sẵn sàng cho soft-fork. Dấu thời gian là giá trị thời gian Unix 32 bit và sẽ cần được cập nhật vào khoảng năm 2106.


#### Trường bit và mục tiêu

Trường bit mã hóa mục tiêu ở dạng rút gọn: mục tiêu = hệ số × 256^(số mũ−3). Các hàm băm khối hợp lệ phải có giá trị số nhỏ hơn mục tiêu này. Vì các hàm băm được hiểu là các số nguyên little-endian, nên các hàm băm hợp lệ thường xuất hiện với nhiều số 0 ở cuối khi hiển thị ở dạng thập lục phân.


### Khó khăn, Xác nhận và Điều chỉnh


Độ khó được định nghĩa là lowest_target / current_target, thể hiện mức độ khó của mining hiện nay so với độ khó dễ nhất có thể. Việc xác thực chỉ yêu cầu so sánh mã băm của tiêu đề với mục tiêu — cực kỳ đơn giản so với mining.


Cứ sau mỗi 2016 khối, Bitcoin điều chỉnh độ khó để nhắm mục tiêu khoảng thời gian tạo khối là ~10 phút. Việc điều chỉnh so sánh thời gian thực tế của 2016 khối trước đó với khoảng thời gian dự kiến là hai tuần. Giới hạn được đặt ra để hạn chế việc điều chỉnh trong phạm vi gấp bốn lần. Các sự kiện lớn trong thế giới thực—chẳng hạn như lệnh cấm mining của Trung Quốc—đã chứng minh khả năng phục hồi của cơ chế này khi tốc độ băm giảm mạnh và độ khó được điều chỉnh giảm xuống để bù đắp.


### Trợ cấp khối và tổng Supply


Mức trợ cấp ở độ cao h được tính như sau: trợ cấp = 5.000.000.000 >> (h // 210.000). Điều này tạo ra lịch trình giảm một nửa hội tụ về tổng nguồn cung khoảng 21 triệu BTC. Tổng của dãy số hình học (50 + 25 + 12,5 + …) × 210.000 giải thích giới hạn này. Thợ đào có thể nhận ít hơn mức trợ cấp cho phép nhưng không bao giờ nhiều hơn, nếu không khối sẽ trở nên không hợp lệ. Khi mức trợ cấp giảm dần qua các lần giảm một nửa liên tiếp, phí giao dịch trở thành một thành phần ngày càng quan trọng trong doanh thu của thợ đào và an ninh mạng dài hạn.


## Truyền thông mạng và cây Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>


![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


### Kiến trúc mạng Bitcoin


Mạng ngang hàng (peer-to-peer) của Bitcoin hoạt động như một hệ thống lan truyền thông tin phi tập trung, nơi các nút chuyển tiếp các giao dịch và khối mà không cần tin tưởng lẫn nhau. Các nút mới khởi tạo bằng cách liên hệ với các hạt giống DNS được mã hóa cứng do các nhà phát triển cốt lõi duy trì. Các hạt giống DNS này trả về địa chỉ IP của các nút đang hoạt động, cho phép các nút khám phá mạng và sau đó yêu cầu thêm các nút khác thông qua getaddr. Việc kết nối mạng được cố ý không đặt nặng vấn đề đồng thuận, vì vậy các triển khai có thể khác nhau miễn là các quy tắc đồng thuận không thay đổi.


### Cấu trúc thông điệp và sự bắt tay


Tất cả các thông điệp Bitcoin P2P đều sử dụng một cấu trúc gói cố định: một giá trị ma thuật 4 byte (F9BEB4D9 cho mainnet), một lệnh ASCII 12 byte, độ dài tải trọng little-endian 4 byte, một mã kiểm tra 4 byte (4 byte đầu tiên của hash256) và tải trọng. Các lệnh phổ biến bao gồm version, verack, inv, getdata, tx, block, getheaders, headers, ping và pong.


Quá trình bắt tay bắt đầu khi một nút kết nối gửi một thông điệp phiên bản. Bên nhận phản hồi bằng thông điệp verack và phiên bản của chính nó. Sau khi cả hai bên trao đổi hai thông điệp này, kết nối được kích hoạt và các nút có thể bắt đầu chuyển tiếp thông tin về kho hàng và dữ liệu.


### Cây Merkle và rễ cây Merkle


Bitcoin lưu trữ một gốc Merkle 32 byte duy nhất trong mỗi tiêu đề khối như một cam kết cho tất cả các giao dịch trong khối. Các giao dịch được băm (hash256), ghép cặp, nối lại và băm lặp đi lặp lại cho đến khi chỉ còn một giá trị băm duy nhất. Khi một cấp có số lượng lẻ, giá trị băm cuối cùng sẽ được sao chép. Về mặt nội bộ, các giá trị băm là big-endian, trong khi dữ liệu khối được tuần tự hóa sử dụng little-endian, yêu cầu đảo ngược trước và sau khi xây dựng cây.


#### Merkle Proofs và SPV

Bằng chứng Merkle cho phép xác minh rằng một giao dịch được bao gồm trong một khối mà không cần tải xuống toàn bộ khối. Bằng chứng bao gồm các hàm băm anh em dọc theo đường dẫn đến gốc. Các máy khách SPV nhẹ chỉ lưu trữ tiêu đề khối và yêu cầu các bằng chứng này từ các nút đầy đủ. Vì cây Merkle phát triển theo hàm logarit, việc chứng minh sự có mặt trong một khối với hàng nghìn giao dịch chỉ cần vài trăm byte.


Taproot mở rộng khái niệm này bằng cách cam kết các điều kiện chi tiêu vào một cây kịch bản Merkle (MAST), chỉ tiết lộ nhánh được thực thi cùng với bằng chứng Merkle. Điều này cải thiện cả hiệu quả và tính bảo mật.


### Vận hành mạng và đồng bộ hóa khối


Các nút sử dụng getdata để yêu cầu giao dịch hoặc khối, chỉ định ID loại (1=giao dịch, 2=khối, 3=khối đã lọc, 4=khối nhỏ gọn) cộng với một mã định danh 32 byte. Để đồng bộ hóa chuỗi, các nút gửi getheader với mã băm của khối bắt đầu, nhận được tối đa 2000 tiêu đề phản hồi. Mỗi tiêu đề được trả về có 80 byte theo sau là số lượng giao dịch giả bằng không.


Việc xác minh đầy đủ các khối đã nhận yêu cầu hai bước kiểm tra:

1. Mã băm của khối phải nhỏ hơn giá trị mục tiêu được mã hóa trong trường bit.

2. Gốc Merkle được tính toán từ tất cả các giao dịch (với việc xử lý thứ tự byte thích hợp) phải khớp với gốc của tiêu đề.


Chỉ khi cả hai điều kiện đều được thỏa mãn thì một nút mới chấp nhận khối, phản ánh nguyên tắc "không tin tưởng, phải xác minh" của Bitcoin.


## Giao tiếp nút nâng cao và chứng nhân tách biệt

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>


![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)


Phiên này kết hợp mạng P2P tiên tiến với Segregated Witness, cho thấy phần mềm Bitcoin hiện đại tương tác trực tiếp với các nút như thế nào trong khi sử dụng cấu trúc giao dịch tương thích với SegWit. Các nhà phát triển sẽ học cách truy xuất khối, quét các giao dịch liên quan và xây dựng giao dịch chỉ bằng cách sử dụng giao tiếp mạng thô—không cần đến trình khám phá khối.


### Truy xuất giao dịch dựa trên khối và quyền riêng tư


Ví điện tử phải phát hiện các khoản thanh toán đến bằng cách quét các khối để tìm các đầu ra khớp với scriptPubKey của chúng. Việc truy xuất toàn bộ khối bảo vệ quyền riêng tư tốt hơn so với việc yêu cầu các giao dịch riêng lẻ, điều này làm rò rỉ các tín hiệu mạnh về hoạt động của người dùng. Ngay cả các yêu cầu khối cũng có thể làm rò rỉ thông tin trên các chuỗi có khối lượng giao dịch thấp, khiến các bộ lọc khối nhỏ gọn (BIP158) trở nên cần thiết cho các máy khách nhẹ bảo vệ quyền riêng tư. Các bộ lọc có thể tạo ra kết quả dương tính giả nhưng không bao giờ tạo ra kết quả âm tính giả, cho phép máy khách chỉ tải xuống các khối có khả năng liên quan mà không tiết lộ địa chỉ cụ thể.


### Tương tác mạng Trustless


Quy trình `get_block` thể hiện cách sử dụng mạng đúng cách: gửi getdata, nhận một khối, sau đó xác minh độc lập gốc Merkle và proof of work của nó. Một khối chỉ được chấp nhận nếu băm tiêu đề nhận được khớp với băm được yêu cầu và gốc Merkle được tính toán của nó khớp với tiêu đề. Điều này thể hiện nguyên tắc “không tin tưởng, hãy xác minh”, đảm bảo ngay cả các nút mạng độc hại cũng không thể lừa các nút chấp nhận dữ liệu đã bị thay đổi.


#### Truy xuất giao dịch từ các khối

Các giao dịch của một khối có thể được quét để tìm các scriptPubKey trùng khớp bằng cách sử dụng phương pháp lặp đơn giản. Ví điện tử trong môi trường sản xuất thực hiện việc này liên tục khi các khối mới xuất hiện, chứng minh quyền sở hữu đầu ra một cách nghiêm ngặt thông qua xác thực mật mã chứ không dựa vào API của bên thứ ba.


### Mục tiêu và thiết kế của SegWit


Cơ chế Chứng thực Tách biệt (SegWit) đã khắc phục tính dễ bị thao túng của giao dịch bằng cách loại bỏ dữ liệu chữ ký khỏi phép tính txid. Điều này cho phép tạo ra các chuỗi giao dịch được ký trước đáng tin cậy và giúp Lightning Network trở nên khả thi. SegWit cũng tăng dung lượng khối bằng cách sử dụng "trọng lượng khối": các nút cũ vẫn thấy các khối ≤1 MB, trong khi các nút được nâng cấp xác thực lên đến 4 MB bao gồm cả dữ liệu chứng thực. Các chương trình chứng thực có phiên bản (cho đến nay là v0–v1) tạo ra một lộ trình nâng cấp có cấu trúc cho các loại tập lệnh trong tương lai.


#### P2WPKH (Tên gốc: SegWit)


P2WPKH thay thế cấu trúc P2PKH cũ bằng một đoạn mã 22 byte: OP_0 + push20 + hash160(pubkey). Việc chi tiêu sẽ chuyển chữ ký và khóa công khai vào một trường chứng thực riêng biệt.


- Các nút trước SegWit: xem phần “bất kỳ ai cũng có thể chi tiêu”, coi đó là hợp lệ.
- Các nút sau SegWit: nhận dạng OP_0 + hàm băm 20 byte và xác thực bằng dữ liệu chứng thực.


Sự tách biệt này khắc phục tính dễ bị thao túng và giảm chi phí. Người làm chứng sử dụng số lượng chứng từ thay thế, tiếp theo là chữ ký và khóa công khai.


#### P2SH-P2WPKH (Tương thích ngược với SegWit)


Để cho phép các ví cũ gửi tiền đến địa chỉ SegWit, các tập lệnh P2WPKH có thể được gói gọn trong P2SH.


- scriptPubKey: standard P2SH hash160(redeemScript)
- scriptSig: tập lệnh redeemScript (chương trình P2WPKH)
- chứng nhân: chữ ký + khóa công khai


Các lớp xác thực:

1. Các node trước BIP16 chấp nhận redeemScript là hợp lệ.

2. Các nút sau BIP16 đánh giá nó, để lại OP_0 + hash trên ngăn xếp.

3. Các nút SegWit thực hiện xác thực đầy đủ thông tin chứng thực.


#### P2WSH dành cho các kịch bản phức tạp


P2WSH tổng quát hóa SegWit cho các kịch bản đa chữ ký và nâng cao bằng cách cam kết sử dụng SHA256(script) thay vì hash160. Một chồng chứng thực đa chữ ký 2 trên 3 điển hình:


- phần tử rỗng (lỗi CHECKMULTISIG)
- sig1
- sig2
- kịch bản chứng thực (kịch bản đa chữ ký)


Các nút SegWit xác minh SHA256 (witnessScript) khớp với hàm băm scriptPubKey rồi thực thi nó. Việc sử dụng SHA256 và hàm băm 32 byte cho phép phân biệt P2WSH với P2WPKH và tăng cường bảo mật.


#### P2SH-P2WSH (Khả năng tương thích tối đa)


Các kịch bản SegWit phức tạp cũng có thể được đóng gói bằng P2SH:


- scriptSig: chuộcScript (OP_0 + hàm băm 32 byte)
- nhân chứng: chữ ký + witnessScript


Quá trình xác thực trải qua ba thế hệ quy tắc, giống hệt như với P2SH-P2WPKH. Lớp bao bọc này rất cần thiết cho các triển khai Lightning đời đầu cần đa chữ ký mà không có tính dễ bị thay đổi. Mặc dù P2WSH gốc được ưa chuộng hiện nay, nhưng dạng được bao bọc đảm bảo khả năng tương thích trên các hệ thống wallet cũ hơn.


### Tác động của SegWit


SegWit đã cung cấp:


- ID giao dịch ổn định
- mức phí thấp hơn thông qua dữ liệu nhân chứng được giảm giá
- Thông lượng khối cao hơn thông qua trọng lượng khối
- Khả năng tương thích với các nút cũ
- Một lộ trình nâng cấp sạch sẽ cho Taproot và các phần mở rộng trong tương lai.


Cùng với tương tác mạng không cần tin tưởng, những công cụ này tạo thành xương sống cho sự phát triển Bitcoin hiện đại.



# Phần cuối


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Đánh giá & Xếp hạng


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Bài kiểm tra cuối kỳ


<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>



<isCourseExam>true</isCourseExam>

## Phần kết luận



<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>


<isCourseConclusion>true</isCourseConclusion>