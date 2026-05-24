import numpy as np
import math
from flask import Blueprint, render_template, request, session

bp = Blueprint('hill', __name__)

def mod_inverse(a, m):
    """Mencari a^-1 mod m"""
    try:
        return pow(int(a), -1, m)
    except ValueError:
        return None

def get_key_matrix(key_string, n):
    """
    Mengubah string kata kunci menjadi matriks nxn (2x2 atau 3x3).
    Jika string kurang, akan di-padding dengan 'A'.
    """
    key_string = ''.join([c for c in key_string if c.isalpha()]).upper()
    if len(key_string) < n * n:
        key_string += 'A' * ((n * n) - len(key_string))
    key_string = key_string[:n * n]
    
    matrix = [ord(c) - 65 for c in key_string]
    return np.array(matrix).reshape(n, n)

def process_hill(text, key_string, n, mode='encrypt'):
    """
    Fungsi inti Hill Cipher.
    """
    steps = []
    
    # 1. Bersihkan teks, hanya ambil alfabet, jadikan uppercase
    clean_text = ''.join([c for c in text if c.isalpha()]).upper()
    if not clean_text:
        return "", [], "Teks harus mengandung setidaknya satu huruf alfabet."

    # 2. Padding teks jika panjangnya tidak habis dibagi dimensi matriks (n)
    while len(clean_text) % n != 0:
        clean_text += 'X' # Tambahkan 'X' sebagai padding (umum di kriptografi)
        
    # 3. Buat matriks kunci K
    K = get_key_matrix(key_string, n)
    
    # 4. Hitung Determinan
    # Menggunakan np.round karena hasil determinan numpy bisa berupa float (misal 24.9999999)
    det = int(np.round(np.linalg.det(K))) % 26
    inv_det = mod_inverse(det, 26)
    
    if inv_det is None:
        return "", [], f"Matriks kunci tidak valid! Determinan = {det}. Determinan dan 26 harus saling prima agar bisa didekripsi. Coba gunakan kata kunci lain."

    # 5. Jika mode dekripsi, ubah K menjadi K_inverse mod 26
    if mode == 'decrypt':
        # Adjugate matrix = det(K) * K^-1
        adj = np.round(np.linalg.det(K) * np.linalg.inv(K)).astype(int) % 26
        K = (inv_det * adj) % 26

    result_text = ""
    
    # 6. Proses per blok (sepanjang n)
    for i in range(0, len(clean_text), n):
        block = clean_text[i:i+n]
        # Ubah blok teks menjadi vektor kolom
        P = np.array([ord(c) - 65 for c in block]).reshape(n, 1)
        
        # Operasi utama: C = (K * P) mod 26
        C = np.dot(K, P) % 26
        
        # Ubah kembali vektor hasil menjadi teks
        result_block = ''.join([chr(int(val[0]) + 65) for val in C])
        result_text += result_block
        
        # Simpan langkah-langkah untuk UI
        steps.append({
            'block_in': block,
            'vector_in': P.tolist(),    # .tolist() agar bisa dibaca Jinja2 di HTML
            'matrix': K.tolist(),
            'vector_out': C.tolist(),
            'block_out': result_block
        })
        
    return result_text, steps, None

@bp.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    steps = None
    error_message = None
    
    text_input = ""
    key_input = "HILL" # Contoh kata kunci 4 huruf untuk matriks 2x2
    n_size = 2
    mode = "encrypt"
    
    if request.method == 'POST':
        text_input = request.form.get('text', '')
        key_input = request.form.get('key', 'HILL')
        try:
            n_size = int(request.form.get('n_size', 2))
        except ValueError:
            n_size = 2
            
        mode = request.form.get('mode', 'encrypt')
        
        if text_input and key_input:
            result_text, steps, error_message = process_hill(text_input, key_input, n_size, mode)
            
            # Jika sukses dan tidak ada error, simpan ke riwayat
            if not error_message:
                if 'history' not in session:
                    session['history'] = []
                
                session['history'].insert(0, {
                    'cipher': 'Hill',
                    'mode': mode,
                    'input': text_input[:50] + "..." if len(text_input) > 50 else text_input,
                    'key': f"Matrix {n_size}x{n_size} ({key_input.upper()})",
                    'result': result_text
                })
                session['history'] = session['history'][:10]
                session.modified = True
            
    return render_template(
        'hill.html', 
        result_text=result_text, 
        steps=steps, 
        text_input=text_input, 
        key_input=key_input, 
        n_size=n_size,
        mode=mode,
        error_message=error_message
    )