<div align="center">

# 🎮 Dangasa Control

**Ko'z qimiriltish va qo'l harakatlari orqali kompyuterni boshqarish tizimi**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.8-00A98F?style=for-the-badge&logo=google&logoColor=white)](https://mediapipe.dev)

</div>

---

## 📖 Loyiha haqida

**Dangasa Control** — bu vebkamera orqali foydalanuvchining ko'z qimiriltishi va qo'l harakatlarini real vaqtda aniqlab, ularni klaviatura buyruqlariga aylantiradigan aqlli boshqaruv tizimi.

> **Asosiy g'oya:** Kompyuterni qo'l bilan tegmasdan, faqat ko'z va barmoq harakatlari orqali boshqarish.

### Qanday ishlaydi?

| Harakat | Natija | Tafsilot |
|---------|--------|----------|
| 👁️ Ko'zni 0.4s yumib oching | `DOWN` tugmasi bosiladi | EAR (Eye Aspect Ratio) algoritmi orqali ko'z holati aniqlanadi |
| ☝️ Barmoqni chegaradan yuqoriga ko'taring | `UP` tugmasi bosiladi | MediaPipe Hands orqali ko'rsatkich barmoq koordinatasi kuzatiladi |

---

## 🎬 Demo

<div align="center">
  <video src="https://github.com/devbexruz/dangasa_control/raw/main/Result.mp4" width="50%" autoplay loop muted controls></video>
</div>

---

## ✨ Xususiyatlar

- **Ko'z qimiriltishini aniqlash** — EAR (Eye Aspect Ratio) algoritmi yordamida chap ko'z holatini real vaqtda kuzatish
- **Qo'l harakatlarini tanish** — MediaPipe Hands modeli orqali barmoq uchlari koordinatasini aniqlash
- **Vaqt filtri** — Tasodifiy ko'z yumilishlarni filtrlash uchun 0.4 soniyalik minimal muddat
- **Real vaqtda vizualizatsiya** — Ekranda joriy holat, chegara chizig'i va buyruqlar ko'rsatiladi
- **Yengil va tezkor** — Minimal kutubxonalar bilan ishlaydi, qo'shimcha hardware talab qilinmaydi

---

## 🛠️ Texnologiyalar

| Texnologiya | Vazifasi |
|-------------|----------|
| [OpenCV](https://opencv.org) | Vebkameradan kadr olish, tasvirni qayta ishlash va vizualizatsiya |
| [MediaPipe](https://mediapipe.dev) | Yuz mesh (468 nuqta) va qo'l skeleti (21 nuqta) aniqlash |
| [PyAutoGUI](https://pyautogui.readthedocs.io) | Aniqlangan gesturalarni klaviatura tugmalari sifatida yuborish |

---

## 📋 Talablar

- **Python** 3.8 yoki undan yuqori
- **Vebkamera** (ichki yoki tashqi)
- **Operatsion tizim:** Windows / macOS / Linux

---

## 🚀 O'rnatish

### 1. Repozitoriyani klonlash

```bash
git clone https://github.com/devbexruz/dangasa_control.git
cd dangasa_control
```

### 2. Virtual muhit yaratish (tavsiya etiladi)

```bash
python -m venv venv
```

**Aktivlashtirish:**

| OS | Buyruq |
|----|--------|
| Windows | `venv\Scripts\activate` |
| macOS / Linux | `source venv/bin/activate` |

### 3. Kutubxonalarni o'rnatish

```bash
pip install -r requirements.txt
```

### 4. Dasturni ishga tushirish

```bash
python main.py
```

---

## 🎯 Foydalanish

1. Dasturni ishga tushirgandan so'ng vebkamera avtomatik yonadi
2. Ekranda **sariq chegara chizig'i** ko'rinadi — bu barmoq uchun yuqori chegara

### Buyruqlar

| Buyruq | Qanday bajarish | Vizual signal |
|--------|-----------------|---------------|
| **DOWN** | Ko'zni kamida **0.4 soniya** yumib turing, keyin oching | Yashil "TAYYOR (Oching!)" → "DOWN!" |
| **UP** | Ko'rsatkich barmoqni sariq chiziqdan **tepaga** ko'taring | Ko'k "UP!" |

### Maslahatlar

- Ko'zni juda tez yumsangiz (0.4 soniyadan kam), buyruq berilmaydi — bu tasodifiy ko'z yumilishni filtrlash uchun
- Dasturdan chiqish uchun `ESC` tugmasini bosing
- Kadr horizontol aks ettirilgan (mirror), shuning uchun harakatlar tabiiy ko'rinadi

---

## 📁 Loyiha tuzilishi

```
dangasa_control/
├── main.py              # Asosiy dastur — kamera, aniqlash va boshqaruv logikasi
├── requirements.txt     # Python kutubxonalari ro'yxati
├── Result.mp4           # Natijani ko'rsatuvchi demo video
└── Readme.md            # Loyiha hujjatlari
```

---

## ⚙️ Texnik tafsilotlar

### EAR (Eye Aspect Ratio) algoritmi

Ko'z ochiq yoki yumiq ekanligini aniqlash uchun **EAR** formulasi ishlatiladi:

$$EAR = \frac{\|p_1 - p_5\| + \|p_2 - p_4\|}{2 \cdot \|p_0 - p_3\|}$$

- **EAR < 0.20** → Ko'z yumilgan deb hisoblanadi
- Ko'z kamida **0.4 soniya** yumiq tursa va keyin ochilsa → `DOWN` buyrug'i yuboriladi

### Qo'l aniqlash

- MediaPipe Hands modeli **21 ta landmark** nuqtasini aniqlaydi
- **8-indeksli nuqta** (ko'rsatkich barmoq uchi) `y` koordinatasi kuzatiladi
- Agar `y < 0.4` (ekran balandligining 40%) → `UP` buyrug'i yuboriladi

---

## 🤝 Hissa qo'shish

1. Repozitoriyani fork qiling
2. Yangi branch yarating (`git checkout -b feature/yangi-xususiyat`)
3. O'zgarishlarni commit qiling (`git commit -m "Yangi xususiyat qo'shildi"`)
4. Branch ga push qiling (`git push origin feature/yangi-xususiyat`)
5. **Pull Request** oching

---

## 📄 Litsenziya

Ushbu loyiha [MIT License](LICENSE) ostida tarqatiladi.

---

## 📬 Muallif

**devbexruz** — [GitHub profili](https://github.com/devbexruz)

---

<div align="center">

⭐ Agar loyiha sizga yoqgan bo'lsa, **star** qo'yishni unutmang!

</div>

