# پروژه آزمایشگاه نرم افزار: رابط برنامه‌نویسی ثبت‌نام دانشگاه

![CI Pipeline](https://github.com/dinpajuhmohammadhashem-create/SE-Lab-Final-MohammadHashemDinpajuh/actions/workflows/ci.yml/badge.svg)

## مشخصات 
- **استاد:** دکتر پگاه ظفرمند
- **نام دانشجو:** محمدهاشم دین پژوه
- **شماره دانشجویی:** ۴۰۳۷۳۵۸۷۴

---

## ساختار پوشه‌های پروژه
```text
📦 SE-Lab-Final-MohammadHashemDinpajuh
 ┣ 📂 .github/workflows   # فایل‌های تنظیمات CI/CD (GitHub Actions)
 ┣ 📂 docs                # مستندات پروژه (نمودارها و داستان‌های کاربر)
 ┣ 📂 src                 # کدهای منبع پروژه
 ┃ ┣ 📂 test              # تست‌های واحد (Unit Tests)
 ┃ ┗ 📜 main.py           # فایل اصلی راه‌اندازی REST API
 ┗ 📜 README.md           # مستندات اصلی مخزن
```

---

## دستورات نصب و اجرا (گام به گام)
برای اجرای این پروژه روی سیستم خود، مراحل زیر را به ترتیب در ترمینال وارد کنید:

**۱. نصب پیش‌نیازها و کتابخانه‌ها:**
```bash
pip install fastapi uvicorn pydantic pytest httpx
```

**۲. اجرای سرور (REST API):**
```bash
uvicorn src.main:app --reload
```

**۳. اجرای تست‌های واحد (Unit Tests):**
```bash
python -m pytest src/test/test_main.py -v
```

---

## لینک Swagger UI
پس از اجرای سرور با دستورات بالا، مستندات خودکار و رابط کاربری API در لینک زیر در دسترس خواهد بود:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
