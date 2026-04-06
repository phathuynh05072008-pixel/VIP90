# 🎓 Khóa VIP 90 - Hướng dẫn sử dụng

## 📋 Cấu trúc file

```
c:\VIP90\
├── index.html          # Trang web chính
└── README.md          # File này
```

## 🚀 Cách chạy

### Step 1: Mở trang web
Mở trình duyệt (Chrome, Firefox, Edge, v.v.) và vào:
```
file:///c:/VIP90/index.html
```

**Xong!** Trang web đã sẵn sàng sử dụng. 🎉

---

## ✨ Tính năng

### 📚 Quản lý tuần học
- Dropdown "Chọn Tuần Học" (Tuần 1 → Tuần 14)
- Mỗi tuần có 5 bài học
- Nhấn vào bài để phát file audio

### 🏠 Nút Trang Chủ
- Quay lại trạng thái ban đầu
- Reset tất cả nội dung

### 🌐 Công cụ dịch thuật
- Nhập text tiếng Anh
- Nhấn **🔄 Dịch với DeepL**
- Mở tab mới → dịch sang tiếng Việt với DeepL (chất lượng cao)

---

## 💾 Thêm file audio

### Cách 1: Đặt file cùng thư mục
```
c:\VIP90\
├── index.html
├── lesson1-1.m4a
├── lesson1-2.m4a
└── ...
```

Rồi click nút bài học → phát file

### Cách 2: Tạo thư mục riêng
Tạo thư mục `audio/`:
```
c:\VIP90\
├── index.html
└── audio\
    ├── lesson1-1.m4a
    ├── lesson1-2.m4a
    └── ...
```

Rồi update trong `index.html`:
```javascript
onclick="loadAudio('audio/lesson1-1.m4a', 'Bài 1')"
```

---

## 🖼️ Thêm ảnh banner

Tạo thư mục `images/`:
```
c:\VIP90\
├── index.html
└── images\
    ├── week1-banner.jpg
    ├── week2-banner.jpg
    └── ...
```

Rồi uncomment trong `index.html`:
```html
<img src="images/week1-banner.jpg" alt="Tuần 1">
```

---

## 📞 Thêm thông tin liên hệ

Mở `index.html` và tìm phần footer, thay:
```html
<p>📧 Email: <a href="mailto:contact@example.com">contact@example.com</a></p>
<p>📱 Điện thoại: +84 XXX XXX XXX</p>
```

Bằng thông tin thực của bạn.

---

## 🎨 Tùy chỉnh giao diện

Tất cả CSS nằm trong thẻ `<style>` ở đầu file. Bạn có thể sửa:
- **Màu sắc**: `#2c3e50`, `#3498db`, v.v.
- **Font size**: Tìm `font-size`
- **Spacing**: Sửa `padding`, `margin`

---

## 💡 Tips

- Trang web **không cần internet** để chạy (trừ phần dịch DeepL)
- Bạn có thể **up GitHub** như file HTML bình thường
- Dùng **Live Server** (VSCode extension) để preview dễ hơn

---

## ❓ Nếu có vấn đề

### Lỗi: File audio không phát
- Kiểm tra đường dẫn file trong `onclick="loadAudio('...')"`
- Chắc chắn file .m4a tồn tại trong thư mục

### Lỗi: Ảnh không hiển thị
- Uncomment dòng `<img src="...">` trong code
- Kiểm tra file ảnh tồn tại

### Dịch không mở được DeepL
- Kiểm tra kết nối internet
- Thử copy text → paste vào DeepL.com thủ công

---

**Trang web được tạo bởi Claude Code** ❤️
