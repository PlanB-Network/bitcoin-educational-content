---
name: Hướng dẫn chạy nền tảng Plan ₿ Academy cục bộ
description: Làm thế nào để chạy Plan ₿ Academy trong môi trường cục bộ để kiểm tra các đóng góp nội dung hoặc thực hiện hiệu đính (proofreading)/xem xét nội dung giáo dục trên Plan ₿ Academy?
---
![github](assets/cover.webp)

## Tóm tắt

Hướng dẫn này cung cấp các bước chi tiết để thiết lập Hệ thống Quản lý Khóa học Bitcoin từ Plan ₿ Academy trên máy tính cá nhân của bạn bằng cách sử dụng Docker, các khóa ảo (dummy keys) và cấu hình repository.

Nếu bạn không hiểu phần trên, đừng lo lắng - hướng dẫn này dành cho bạn!

---
## Cách chạy hệ thống quản lý khóa học Bitcoin trên máy tính cá nhân

Hướng dẫn này cung cấp các bước chi tiết để thiết lập nền tảng, xử lý khóa ảo và tùy chỉnh repository. Hãy làm theo các bước bên dưới để tránh các sự cố thường gặp và cấu hình môi trường cục bộ của bạn một cách chính xác.

**1. Điều kiện tiên quyết**


- Máy tính chạy Linux đã cài đặt Docker và Docker Compose (theo một sốt phản hồi, hệ thống cũng có thể hoạt động trên Windows).
- Phiên bản `nodejs` phù hợp (phiên bản đã được thử nghiệm: 22.12.0)
- `pnpm` đã được cài đặt trên hệ thống.
- Git đã được cấu hình để clone repostiories.

**2. Clone repository**

Clone repository về máy tính của bạn:

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Cấu hình các biến môi trường**

- Sao chép file `.env.example`:

```bash
cp .env.example .env
```

- Chỉnh sửa file `.env` (không có phần `.example` trong tên file). Bây giờ bạn cần thêm các khóa ảo cho những biến bắt buộc. Ví dụ:

⚠️ **Đây là bước bắt buộc. Nếu bỏ qua sẽ dẫn đến lỗi, chẳng hạn như các container không thể kết nối với nhau.**

Đừng quên thêm Github PAT (Personal Access Token) riêng của bạn vào file này.

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Cài đặt các thư viện phụ thuộc (dependencies)**

Hãy đảm bảo bạn đã cài đặt phiên bản `nodejs` phù hợp. Tính đến tháng 12/2024, phiên bản `22.12.0` (LTS) đã được kiểm thử và hoạt động ổn định.

⚠️ **Phiên bản `nodejs` trong repository của Ubuntu 22.04 là 12.22.9: quá cũ để cài đặt `pnpm`**

Để cài đặt `nodejs`, bạn có thể tham khảo hướng dẫn [tại đây](https://nodejs.org/en/download/package-manager). Ví dụ, bạn có thể cài đặt bằng `nvm`.

---
Trước khi tiến hành cài đặt các package cần thiết bằng `pnpm`, hãy đảm bảo rằng tất cả các dependency hệ thống đã được cài đặt bằng lệnh sau:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Trong thư mục `../Bitcoin-learning-management-system/`, chạy lệnh sau để cài đặt `pnpm`

```bash
pnpm install
```

__MẸO:__ Đừng quên thường xuyên cập nhật các dependencíe cũng như chính `pnpm`.

**5. Chạy các container**

Trong thư mục `../Bitcoin-learning-management-system/`, khởi động môi trường phát triển với Docker:

```bash
docker compose up --build -V
```

Bạn cũng có thể dùng lệnh sau nếu không muốn hiển thị log trong terminal:

```bash
docker compose up -d --build -V
```

Docker sẽ build và khởi động toàn bộ các container cần thiết.

**6. Truy cập ứng dụng**

Khi các container đã khởi động, hãy truy cập vào giao diện tại:

[http://localhost:8181](http://localhost:8181)

![Plan ₿ Academy Local](assets/en/1.webp)

**Lưu ý**: Ứng dụng sẽ tự động tải lại nếu bạn thay đổi bất kỳ file nguồn nào.

**7. Cấu hình schema cơ sở dữ liệu**

Trong lần chạy đầu tiên, bạn cần thực hiện migration cho cơ sở dữ liệu.

Chạy lệnh migration sau:

```markdown
pnpm run dev:db:migrate
```

**8. Import dữ liệu từ repository**

Để import dữ liệu vào database, hãy gửi request tới API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Sửa lỗi truy cập Sync Volume**

Nếu bạn gặp lỗi truy cập với ổ đĩa `cdn` và `sync`, hãy chạy:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```
Sau đó chạy lệnh:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Academy Local](assets/en/2.webp)

**10. Tùy chỉnh repository (không bắt buộc)**

Nếu bạn cần sử dụng một bản fork hoặc một nhánh cụ thể:

- Chỉnh sửa file `.env` và cập nhật các biến sau:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

- Khởi động lại Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

- Đồng bộ lại dữ liệu từ repository:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Hướng dẫn này đảm bảo nền tảng được thiết lập đúng với các khóa ảo, các dependencies được cài đặt và repository được tùy chỉnh đầy đủ. 

🎉 Chúc bạn cài đặt thành công!

**Các lệnh hỗ trợ thêm**

Dừng tất cả các container

```
docker compose down
```

Dọn dẹp (prune) tất cả container và ổ đĩa hiện có:

```
docker container prune -f
docker volume prune --all
```

Tạo lại container với cùng lệnh như trong hướng dẫn chính thức và chạy script đồng bộ:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
