---
name: Lập trình Bitcoin
goal: Xây dựng một thư viện Bitcoin hoàn chỉnh từ đầu và hiểu nền tảng mật mã của Bitcoin
objectives: 

 - Triển khai các phép toán số học trường hữu hạn và đường cong elliptic trong Python
 - Xây dựng và phân tích cú pháp các giao dịch Bitcoin theo chương trình
 - Tạo địa chỉ Testnet và phát giao dịch qua mạng
 - Nắm vững nền tảng toán học cơ bản của mô hình bảo mật Bitcoin

---
# Hành trình đến các kịch bản và chương trình của Bitcoin


Khóa học chuyên sâu kéo dài hai ngày này, do Jimmy Song giảng dạy, sẽ đưa bạn đi sâu vào nền tảng kỹ thuật của Bitcoin bằng cách xây dựng một thư viện Bitcoin hoàn chỉnh từ đầu. Bắt đầu với những kiến thức toán học thiết yếu về trường hữu hạn và đường cong elliptic, bạn sẽ được hướng dẫn phân tích cú pháp giao dịch, thực thi tập lệnh và giao tiếp mạng. Thông qua các bài tập lập trình thực hành trên Jupyter notebook, bạn sẽ tự tạo Testnet, Address, xây dựng giao dịch thủ công và phát trực tiếp lên mạng—đồng thời nắm vững các nguyên lý mật mã giúp Bitcoin và Trustless bảo mật hơn.


Tận hưởng khám phá của bạn nhé!


+++

# Giới thiệu

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Tổng quan khóa học

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Chào mừng bạn đến với khóa học PRO 202 _**Programming Bitcoin**_, một hành trình chuyên sâu đưa bạn từ số học trường hữu hạn đến việc xây dựng và phát sóng các giao dịch thực trên mạng thử nghiệm của Bitcoin.

Trong khóa học này, bạn sẽ từng bước xây dựng một thư viện Bitcoin bằng Python đồng thời học các kiến thức nền tảng về mật mã học, giao thức và phần mềm cần thiết để hiểu chính xác về bảo mật và cơ chế hoạt động nội bộ của Bitcoin. Cách tiếp cận của PRO 202 hoàn toàn thực hành: mỗi khái niệm được triển khai ngay trong sổ tay Jupyter, đảm bảo lý thuyết và mã củng cố lẫn nhau.

### Các khái niệm toán học cơ bản cho Bitcoin

Phần đầu tiên này thiết lập nền tảng toán học không thể thiếu. Bạn sẽ triển khai số học trường hữu hạn và các phép toán trên đường cong elliptic (định luật nhóm, cộng, nhân đôi, nhân vô hướng...) — những điều kiện tiên quyết cho ECDSA. Mục tiêu có hai: hiểu cấu trúc đại số làm cho chữ ký mật mã trở nên khả thi và xây dựng các công cụ Python đáng tin cậy để thao tác chúng.

Sau đó, bạn sẽ chính thức hóa các thành phần của ECDSA: tạo khóa, định dạng điểm, băm, tạo và xác minh chữ ký. Phần này kết nối trực tiếp giữa lý thuyết và thực hành, nhấn mạnh các chi tiết triển khai và tính vững chắc của mô hình bảo mật cơ bản.

### Cơ chế hoạt động bên trong của giao dịch Bitcoin

Trong phần thứ hai, bạn sẽ phân tích cấu trúc của một giao dịch Bitcoin: UTXO, đầu vào/đầu ra, chuỗi, tập lệnh, mã hóa và nhiều hơn nữa. Bạn sẽ viết mã để xây dựng, ký và xác minh các giao dịch, qua đó hiểu rõ chính xác điều gì được cam kết bởi hàm băm và lý do tại sao.

Tiếp theo, bạn sẽ triển khai một trình thực thi _Script_ tối giản, xem xét các mã vận hành chính và xác thực các đường dẫn chi tiêu. Mục tiêu là giúp bạn có khả năng kiểm toán hành vi giao dịch, chẩn đoán các lỗi xác thực và đánh giá tính an toàn của các chính sách chi tiêu.

### Cơ chế hoạt động bên trong của mạng Bitcoin

Trong phần thứ ba, bạn sẽ đặt giao dịch trong hệ thống tổng thể: cấu trúc khối, tiêu đề, độ khó và cơ chế Proof-of-Work. Bạn sẽ xử lý các thông điệp giao thức, tiêu đề khối và cây Merkle.

Cuối cùng, bạn sẽ nghiên cứu giao tiếp giữa các nút ngang hàng (peer-to-peer), tối ưu hóa thông điệp và việc giới thiệu SegWit.

Giống như mọi khóa học tại Plan ₿ Academy, phần cuối cùng bao gồm một bài đánh giá được thiết kế để củng cố sự hiểu biết của bạn. Sẵn sàng khám phá cách hoạt động bên trong của Bitcoin và viết mã để vận hành nó chưa? Hãy bắt đầu nào!

# Các khái niệm toán học thiết yếu cho Bitcoin

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Toán học để triển khai Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Mật mã đường cong Elliptic

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Giao dịch hoạt động bên trong

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Phân tích giao dịch và chữ ký ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Xác thực giao dịch và tập lệnh Bitcoin

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Xây dựng giao dịch và trả tiền theo kịch bản Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Mạng lưới hoạt động bên trong Bitcoin

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Khối Bitcoin và Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Giao tiếp mạng và cây Merkle

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Giao tiếp nút nâng cao và Chứng kiến tách biệt

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Phần cuối


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Đánh giá & Xếp hạng


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Phần kết luận


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
