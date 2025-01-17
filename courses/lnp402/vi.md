---
name: Phát triển trên Lightning với SDK
goal: Nâng cao kỹ năng phát triển Lightning của bạn với khóa học trung cấp về Rust và SDK.
objectives:
  - Làm quen với Ngôn ngữ Rust
  - Hiểu tại sao sử dụng Rust để phát triển Bitcoin
  - Nắm bắt cơ bản về SDK
---

# Nâng cao kỹ năng phát triển LN của bạn

Chào mừng bạn đến với hành trình LN của mình với SDK.

Trong khóa học này, bạn sẽ học cơ bản về sách Rust, sau đó tiếp tục với một số lập trình LN sử dụng SDK, và kết thúc với một số bài tập thực hành. Các giáo viên từ nhiều lĩnh vực khác nhau sẽ hướng dẫn bạn đến kỹ năng thực hành và giải thích các thách thức khác nhau mà các kỹ sư LN hiện nay thường gặp phải.

Khóa học này được quay trong một hội thảo TRỰC TIẾP do Fulgur'Ventures tổ chức trong sự kiện LN Tuscany vào tháng 10 năm 2023.

Chúc bạn học tốt!

+++

# Giới thiệu
<partId>594ab43f-7216-5326-ab41-f92b85be4581</partId>

## Chương trình học & giới thiệu
<chapterId>36526df2-66a2-58df-8f38-378fb553f08c</chapterId>

### Giới thiệu

Chào mừng bạn đến với khóa học lập trình nâng cao về SDK. Trong khóa đào tạo này, bạn sẽ học cơ bản về Rust, sau đó tập trung vào BTC & Rust, và kết thúc với một số bài tập thực hành sử dụng SDK.

Khóa đào tạo này hiện chỉ có sẵn bằng tiếng Anh và là một phần của hội thảo trực tiếp được tổ chức vào tháng 10 vừa qua tại Tuscany bởi Fulgure Venture. Chương trình của sự kiện TRỰC TIẾP có thể được tìm thấy bên dưới, và khóa đào tạo này sẽ tập trung vào tuần đầu tiên chỉ. Nửa sau được nhắm đến RGB và có thể được tìm thấy trong khóa học RGB.

### Giáo viên

Xin cảm ơn các giáo viên đã tham gia vào chương trình này:

- Alekos: "Hey, tôi là một lập trình viên và hacker người Ý. Tôi đã làm việc trên các dự án như bitcoindevkit, magicalbitcoin và h4ckbs"
- Andrei: "Chuyên gia Lightning tại LIPA"
- Gabriel: "Tôi viết mã và làm đủ thứ."
- Jesse de Wit: "Người hâm mộ mạng Lightning | nhà phát triển | Breez"

### Lịch trình hội thảo

Tuần 1 của sự kiện LN Tuscany
![hình ảnh](assets/1.webp)

Một khi bạn đã hoàn thành khóa học này, nếu bạn quan tâm đến khóa đào tạo tiếp theo, đây là phần thứ hai của lịch trình:
![hình ảnh](assets/2.webp)

Chúc bạn học tốt.

# Học cách lập trình với sách Rust
<partId>152b58c9-fb33-5d3b-9c15-64919869aa34</partId>

## Giới thiệu về Rust (1/7)
<chapterId>af7108eb-4974-5ac2-9784-d2a5c0d77a45</chapterId>
<professor>radio-talent</professor>

![video](https://www.youtube.com/watch?v=aZYhDXE_Gas)

## Giới thiệu về Rust (2/7)
<chapterId>918ca359-c123-5414-af01-253016670f3a</chapterId>

![video](https://youtu.be/Xm8eCv4LQPc)

## Giới thiệu về Rust (3/7)
<chapterId>0278ed13-68b6-59e1-97c5-f8dde505549b</chapterId>

![video](https://youtu.be/R8NeHvHT0uc)

## Giới thiệu về Rust (4/7)
<chapterId>915e523a-8fbd-5789-ab42-99b56a2a16c3</chapterId>

![video](https://youtu.be/et8pKvYiO4c)

## Giới thiệu về Rust (5/7)
<chapterId>96d54999-cdbc-5601-acac-1bc7acbe2eb7</chapterId>

![video](https://youtu.be/PxQkVmxOc40)

## Giới thiệu về Rust (6/7)
<chapterId>a66c63ed-9514-51d1-b3a0-c8edb57603bb</chapterId>

![video](https://youtu.be/3C6hl9BW-Ho)

## Giới thiệu về Rust (7/7)
<chapterId>21cf8dab-239a-580a-85cd-34326aeb1b26</chapterId>

![video](https://youtu.be/SBDcb_AauHM)

# Rust & BTC
<partId>0f4f2ff0-7f41-5ce3-8f64-9ecff69c5355</partId>

## Tại sao Rust cho Bitcoin
<chapterId>92f13f36-70bd-5b00-8c6c-fcd1a1bd1531</chapterId>

![video](https://youtu.be/veLj2w6ulpc)

## Mô hình lỗi
<chapterId>1a648363-0aff-54dd-a79d-ead75231e5d6</chapterId>

![video](https://youtu.be/X3VKhLtKTRU)

## Unniffit
<chapterId>fe1be3e3-2288-5a10-b64b-9ba72fb985d1</chapterId>

![video](https://youtu.be/zro9GQpJrH0)

## Đặc tính bất đồng bộ
<chapterId>e1610abe-574c-5995-abe4-a92b0dca4c93</chapterId>

![video](https://youtu.be/cz66eTfk0lw)
# Phát triển LNP/BP với SDK
<partId>42e8e0f8-1c07-5c71-8378-c57afb38e25d</partId>
## Node LN trên SDK
<chapterId>643e4670-bb1f-581f-a102-f84e8e5d2a02</chapterId>

![video](https://youtu.be/aEzpxuhLdeo)

## Breez sdk
<chapterId>52f20a4d-7d81-58e4-be00-9d39334352af</chapterId>

![video](https://youtu.be/M3ad9BE6ovo)

## Greenlight cho lipa
<chapterId>7ba30435-d26e-5e6f-a973-94080d44bf27</chapterId>

![video](https://youtu.be/gKiIPF4apeE)

## Breez sdk cho lipa
<chapterId>93d87d63-dd7b-5e05-ad2e-dda12915ea32</chapterId>

![video](https://youtu.be/6VaIVvBKjLY)

# Kết luận
<partId>aff1e861-e6a3-58ad-af6a-33ceaedbda99</partId>



## Nhận xét & Đánh giá
<chapterId>9331e519-9e5c-5639-9d0d-055587d8ba4c</chapterId>
<isCourseReview>true</isCourseReview>

## Lời kết
<chapterId>d47b792e-d269-595b-9290-4788aba6e298</chapterId>
<isCourseConclusion>true</isCourseConclusion>
