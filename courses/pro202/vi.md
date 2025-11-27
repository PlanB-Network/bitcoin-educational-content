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

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Toán học để triển khai Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Mật mã đường cong Elliptic

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Bitcoin Giao dịch hoạt động bên trong

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Phân tích giao dịch và chữ ký ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Xác thực giao dịch và tập lệnh Bitcoin

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Xây dựng giao dịch và trả tiền theo kịch bản Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Mạng lưới hoạt động bên trong Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Khối Bitcoin và Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Giao tiếp mạng và cây Merkle

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Giao tiếp nút nâng cao và Chứng kiến tách biệt

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Phần cuối


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Đánh giá & Xếp hạng


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Phần kết luận


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
