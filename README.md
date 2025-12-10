*****************************************************************************************************************************************************************************
<<<....::::HammerX:::...>>>
*****************************************************************************************************************************************************************************
## 🔥 HammerX - Advanced DDoS Stress Testing Tool

A powerful, multithreaded DDoS tool for HTTP, TCP, and UDP stress testing.  
Uses proxy rotation, stealth checks, and real-time reporting via Rich.

> ⚠️ **Legal Warning**: This tool is for educational and authorized testing only. Do not use against unauthorized targets. You are fully responsible for your actions.

---

## ✨ Features

- 🔰 Supports **HTTP**, **TCP**, and **UDP** flood attacks
- 🌐 Automatic **proxy fetching** from multiple sources
- 🔒 Built-in **anti-debug** and **anti-VM** checks
- 📊 Real-time attack **progress & stats** using `rich`
- 🧠 Smart header randomization & IP spoofing
- 🧵 Multi-threaded execution with customizable duration

---

## 🚀 Installation

### ✅ Requirements

- Python 3.8+
- `requests`, `rich`

### 📦 Install dependencies:

```bash
pip install -r requirements.txt
# or manually
pip install requests rich

🧠 Usage
python hammerx.py [http|tcp|udp] <target> [--port PORT] [--time SECONDS]

Examples:
HTTP Attack
python hammerx.py http https://example.com --time 60

TCP Flood
python hammerx.py tcp 192.168.1.1 --port 80 --time 30

UDP Flood
python hammerx.py udp 192.168.1.1 --port 53 --time 45

🛡️ Proxy Usage
Place your own proxies in a file named proxies.txt
If not found, proxies will be auto-fetched from online sources
Proxy format: ip:port (HTTP proxies)

📁 Output
After each attack, a JSON report will be saved as:
{
  "sent": 2350,
  "failed": 78
}

And a live table will be shown on terminal summarizing the attack.

👨‍💻 Author
KiNG_CYReX
📞 Telegram / WhatsApp: +98 990 339 0280
📧 Contact for penetration testing services and collaborations.

⚠️ Disclaimer
This project is only for educational and authorized stress testing on systems you own or have explicit permission to test.
The developer is not responsible for any misuse or illegal activities.

📜 License
This tool is provided under the MIT License.
Feel free to fork, modify, and share responsibly.
================================================================================================================================================


██╗░░██╗░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░██╗░░██╗
██║░░██║██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗╚██╗██╔╝
███████║███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝░╚███╔╝░
██╔══██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗░██╔██╗░
██║░░██║██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║██╔╝╚██╗
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝

## 🔥 HammerX - ابزار پیشرفته تست استرس DDoS

ابزاری قدرتمند و چندریسمانی برای انجام حملات استرسی (DDoS) روی پروتکل‌های HTTP، TCP و UDP.  
دارای قابلیت چرخش پراکسی، بررسی محیط ایمن، و نمایش آمار لحظه‌ای با استفاده از کتابخانه `rich`.

> ⚠️ **هشدار قانونی**: این ابزار صرفاً برای آموزش و تست‌های مجاز طراحی شده است. از آن روی اهداف غیرمجاز استفاده نکنید. شما به طور کامل مسئول استفاده خود هستید.

---

## ✨ ویژگی‌ها

- 🔰 پشتیبانی از حملات سیلابی (Flood) در حالت‌های **HTTP**، **TCP** و **UDP**
- 🌐 دریافت خودکار **پراکسی‌ها** از منابع آنلاین متعدد
- 🔒 بررسی داخلی برای **شناسایی دیباگر** و **ماشین مجازی**
- 📊 نمایش **پیشرفت و آمار حمله** به‌صورت لحظه‌ای با استفاده از `rich`
- 🧠 تولید هدرهای هوشمند و IPهای تصادفی (Spoofed)
- 🧵 اجرای چندریسمانی (Multi-threaded) با زمان‌بندی قابل تنظیم

---

## 🚀 نصب

### ✅ پیش‌نیازها

- پایتون 3.8 به بالا
- پکیج‌های `requests` و `rich`

### 📦 نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
# یا به‌صورت دستی
pip install requests rich
````

---

## 🧠 نحوه استفاده

```bash
python hammerx.py [http|tcp|udp] <هدف> [--port پورت] [--time مدت_زمان_برحسب_ثانیه]
```

### مثال‌ها:

#### حمله HTTP

```bash
python hammerx.py http https://example.com --time 60
```

#### حمله TCP

```bash
python hammerx.py tcp 192.168.1.1 --port 80 --time 30
```

#### حمله UDP

```bash
python hammerx.py udp 192.168.1.1 --port 53 --time 45
```

---

## 🛡️ استفاده از پراکسی‌ها

* پراکسی‌های خود را در فایلی با نام `proxies.txt` قرار دهید.
* اگر فایل موجود نباشد، پراکسی‌ها به‌صورت خودکار از منابع آنلاین بارگیری می‌شوند.
* فرمت پراکسی: `ip:port` (پراکسی HTTP)

---

## 📁 خروجی

پس از هر حمله، گزارشی در قالب JSON به شکل زیر ذخیره خواهد شد:

```json
{
  "sent": 2350,
  "failed": 78
}
```

و همچنین خلاصه‌ای از حمله در قالب جدول روی ترمینال نمایش داده می‌شود.

---

## 👨‍💻 نویسنده

**KiNG\_CYReX**
📞 تلگرام / واتساپ: +98 990 339 0280
📧 برای تست نفوذ یا همکاری با نویسنده تماس بگیرید.

---

## ⚠️ سلب مسئولیت

این پروژه **فقط برای آموزش و تست استرسی مجاز روی سیستم‌هایی که مالک آن هستید یا اجازه رسمی دارید**، ارائه شده است.
نویسنده هیچگونه مسئولیتی در قبال استفاده غیرقانونی یا سوء‌استفاده ندارد.

---

## 📜 مجوز

این ابزار تحت مجوز **MIT** منتشر شده است.
می‌توانید آن را فورک، ویرایش و به‌صورت مسئولانه منتشر نمایید.

```
