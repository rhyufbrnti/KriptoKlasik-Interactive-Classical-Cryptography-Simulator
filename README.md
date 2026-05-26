<div align="center">

<!-- HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00f5ff,50:bf5fff,100:ff2d9b&height=200&section=header&text=KriptoKlasik&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Interactive%20Classical%20Cryptography%20Simulator&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<!-- BADGES -->
<p>
  <img src="https://img.shields.io/badge/Python-3.11.9-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-5.3.2-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/Deployed-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white"/>
</p>
<p>
  <img src="https://img.shields.io/badge/Status-Live-39FF14?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-ff2d9b?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Semester-6-ffe000?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Domain-.my.id-00f5ff?style=for-the-badge"/>
</p>

<h3>🔐 An educational web app to simulate and visualize 5 classical cipher algorithms<br/>with step-by-step calculations, mathematical formulas, and interactive visualizations.</h3>

<br/>

**[🌐 Live Demo](https://rhyufbrnti.my.id)** &nbsp;·&nbsp;
**[📹 Video Demo](#-video-demo)** &nbsp;·&nbsp;
**[📖 Laporan](#-laporan)** &nbsp;·&nbsp;
**[🚀 Installation](#-installation)**

<br/>

</div>

---

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h4>🎮 5 Classical Cipher Algorithms</h4>
      <ul>
        <li><b>Caesar Cipher</b> — Shift-based substitution</li>
        <li><b>Vigenère Cipher</b> — Polyalphabetic substitution</li>
        <li><b>Affine Cipher</b> — Multiplicative + additive cipher</li>
        <li><b>Hill Cipher</b> — Matrix multiplication cipher</li>
        <li><b>Playfair Cipher</b> — Digraph substitution cipher</li>
      </ul>
    </td>
    <td width="50%">
      <h4>📊 Educational Step-by-Step</h4>
      <ul>
        <li>Detailed calculation per character</li>
        <li>Mathematical formula display</li>
        <li>Matrix visualization for Hill & Playfair</li>
        <li>Alphabet ruler reference (A=0 to Z=25)</li>
        <li>Encryption/decryption history log</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <h4>🎨 Modern UI/UX</h4>
      <ul>
        <li>Cyberpunk / Game-inspired dark theme</li>
        <li>Neon color accents per algorithm</li>
        <li>Dark / Light Mode toggle</li>
        <li>Fully responsive (mobile-friendly)</li>
        <li>Smooth hover animations</li>
      </ul>
    </td>
    <td width="50%">
      <h4>⚙️ Technical</h4>
      <ul>
        <li>Flask Blueprint modular architecture</li>
        <li>Session-based history storage</li>
        <li>Input validation & error handling</li>
        <li>Deployed on Railway with custom domain</li>
        <li>SSL/HTTPS via Cloudflare</li>
      </ul>
    </td>
  </tr>
</table>

---

## 🔬 Algorithms

<details>
<summary><b>⚡ Caesar Cipher</b> — click to expand</summary>
<br/>

Caesar Cipher shifts each letter in the alphabet by a fixed number of positions `k`.

| | Formula |
|---|---|
| **Encrypt** | `C = (P + k) mod 26` |
| **Decrypt** | `P = (C - k + 26) mod 26` |

**Example:** `HELLO` with shift `3` → `KHOOR`

</details>

<details>
<summary><b>🔑 Vigenère Cipher</b> — click to expand</summary>
<br/>

Uses a repeating keyword where each character defines a different shift amount.

| | Formula |
|---|---|
| **Encrypt** | `Ci = (Pi + Ki) mod 26` |
| **Decrypt** | `Pi = (Ci - Ki + 26) mod 26` |

**Example:** `ATTACK` with key `KEY` → `KXRKGI`

</details>

<details>
<summary><b>🧮 Affine Cipher</b> — click to expand</summary>
<br/>

Combines multiplication and addition. Key `a` must satisfy `gcd(a, 26) = 1`.

| | Formula |
|---|---|
| **Encrypt** | `C = (a·P + b) mod 26` |
| **Decrypt** | `P = a⁻¹ · (C - b) mod 26` |

Valid values for `a`: `1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25`

</details>

<details>
<summary><b>📐 Hill Cipher</b> — click to expand</summary>
<br/>

Uses linear algebra — multiplies plaintext vectors by an n×n key matrix (mod 26).

| | Formula |
|---|---|
| **Encrypt** | `C = K · P (mod 26)` |
| **Decrypt** | `P = K⁻¹ · C (mod 26)` |

Supports **2×2** and **3×3** key matrices. Requires `gcd(det(K), 26) = 1`.

</details>

<details>
<summary><b>♟️ Playfair Cipher</b> — click to expand</summary>
<br/>

Encrypts letter pairs (digraphs) using a 5×5 key table generated from a keyword.

**Rules:**
- Same row → shift right
- Same column → shift down  
- Rectangle → swap columns

I and J are treated as the same letter in the 5×5 table.

</details>

---

## 🚀 Installation

### Prerequisites
- Python 3.11+
- pip

### Run Locally

```bash
# 1. Clone repository
git clone https://github.com/rhyufbrnti/KriptoKlasik-Interactive-Classical-Cryptography-Simulator.git
cd KriptoKlasik-Interactive-Classical-Cryptography-Simulator

# 2. Create virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python run.py
```

Open your browser at **http://localhost:5000** 🎉

---

## 📁 Project Structure

```
kriptografi-klasik/
│
├── app/
│   ├── __init__.py              # Flask app factory & blueprints
│   ├── ciphers/
│   │   ├── __init__.py
│   │   ├── caesar.py            # Caesar cipher logic + routes
│   │   ├── vigenere.py          # Vigenère cipher logic + routes
│   │   ├── affine.py            # Affine cipher logic + routes
│   │   ├── hill.py              # Hill cipher logic + routes
│   │   └── playfair.py          # Playfair cipher logic + routes
│   │
│   ├── static/
│   │   ├── css/style.css        # Custom cyberpunk theme
│   │   └── js/script.js
│   │
│   └── templates/
│       ├── base.html            # Base layout (sidebar + navbar)
│       ├── index.html           # Dashboard
│       ├── caesar.html
│       ├── vigenere.html
│       ├── affine.html
│       ├── hill.html
│       ├── playfair.html
│       └── history.html
│
├── Procfile                     # Railway deployment config
├── requirements.txt
├── runtime.txt                  # Python version (3.11.9)
└── run.py                       # App entry point
```

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Backend** | Python 3.11.9, Flask 3.0.3 |
| **Template Engine** | Jinja2 |
| **Matrix Operations** | NumPy 1.26.4 |
| **Frontend** | Bootstrap 5.3.2, FontAwesome 6, Vanilla JS |
| **Fonts** | Orbitron, Rajdhani, Share Tech Mono (Google Fonts) |
| **Server** | Gunicorn 22.0.0 |
| **Hosting** | Railway |
| **DNS & SSL** | Cloudflare |
| **Domain Registrar** | Exabytes (.my.id) |
| **Version Control** | Git & GitHub |

---

## 🌐 Deployment

This app is deployed on **Railway** with a custom domain via **Cloudflare DNS**.

| | |
|---|---|
| 🌍 **Live URL** | https://rhyufbrnti.my.id |
| 🚂 **Platform** | Railway |
| 🔒 **SSL** | Cloudflare (Auto HTTPS) |
| 🐍 **Runtime** | Python 3.11.9 |
| ⚙️ **Server** | Gunicorn |

---

## 📹 Video Demo

> 🎬 Link video demo akan ditambahkan setelah upload ke YouTube.

Video mencakup:
- Demonstrasi semua 5 algoritma
- Penjelasan step-by-step perhitungan
- Penjelasan bagian kode yang menantang (Hill & Playfair)

---

## 📖 Laporan

Laporan lengkap tugas tersedia di repository ini dalam format `.docx`, mencakup:
- Teori pendukung semua 5 algoritma
- Alat dan bahan
- Tutorial penggunaan aplikasi
- Referensi

---

## 👩‍💻 Author

<div align="center">
  <img src="https://github.com/rhyufbrnti.png" width="100" style="border-radius: 50%"/>
  <h3>Rahayu Febrianti</h3>
  <p>
    <b>NIM:</b> 301230057<br/>
    <b>Program Studi:</b> Informatika<br/>
    <b>Universitas:</b> Universitas Buana Perjuangan Karawang (UNIBBA)<br/>
    <b>Mata Kuliah:</b> Kriptografi — Semester 6 (2025/2026)
  </p>
  <a href="https://github.com/rhyufbrnti">
    <img src="https://img.shields.io/badge/GitHub-rhyufbrnti-181717?style=for-the-badge&logo=github"/>
  </a>
</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff2d9b,50:bf5fff,100:00f5ff&height=100&section=footer" width="100%"/>

<p><i>Made with ❤️ for Cryptography Course — Informatika UNIBBA 2026</i></p>

</div>