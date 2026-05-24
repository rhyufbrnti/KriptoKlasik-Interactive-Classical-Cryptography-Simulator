import math
from flask import Blueprint, render_template, request, session

bp = Blueprint('affine', __name__)

def mod_inverse(a, m):
    """
    Mencari nilai a^-1 mod m.
    Di Python 3.8+, kita bisa menggunakan pow(a, -1, m).
    """
    try:
        return pow(a, -1, m)
    except ValueError:
        return None  # Jika tidak ada inverse

def process_affine(text, a, b, mode='encrypt'):
    """
    Fungsi inti Affine Cipher.
    Menghasilkan teks final dan daftar langkah perhitungan per karakter.
    """
    result_text = ""
    steps = []
    
    # Hitung nilai inverse dari a jika mode adalah dekripsi
    a_inv = mod_inverse(a, 26)
    
    for char in text:
        step_detail = {
            'original': char,
            'is_alpha': False,
            'result': char,
            'formula': '-',
            'explanation': 'Bukan alfabet, dibiarkan'
        }
        
        if char.isalpha():
            step_detail['is_alpha'] = True
            is_upper = char.isupper()
            base_ascii = 65 if is_upper else 97
            
            char_val = ord(char) - base_ascii
            
            if mode == 'encrypt':
                # Rumus Enkripsi: C = (a*P + b) mod 26
                new_val = (a * char_val + b) % 26
                step_detail['formula'] = f"({a} × {char_val} + {b}) mod 26 = {new_val}"
                step_detail['explanation'] = f"P = '{char}' ({char_val}) ➔ C = '{chr(new_val + base_ascii)}'"
            else:
                # Rumus Dekripsi: P = a^-1 * (C - b) mod 26
                new_val = (a_inv * (char_val - b)) % 26
                step_detail['formula'] = f"{a_inv} × ({char_val} - {b}) mod 26 = {new_val}"
                step_detail['explanation'] = f"C = '{char}' ({char_val}), a^-1 = {a_inv} ➔ P = '{chr(new_val + base_ascii)}'"
            
            result_char = chr(new_val + base_ascii)
            result_text += result_char
            step_detail['result'] = result_char
                
        else:
            result_text += char
            
        steps.append(step_detail)
        
    return result_text, steps

@bp.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    steps = None
    text_input = ""
    a_val = 5
    b_val = 8
    mode = "encrypt"
    error_message = None
    
    if request.method == 'POST':
        text_input = request.form.get('text', '')
        mode = request.form.get('mode', 'encrypt')
        
        try:
            a_val = int(request.form.get('a', 5))
            b_val = int(request.form.get('b', 8))
        except ValueError:
            error_message = "Nilai Kunci A dan B harus berupa angka/integer."
            a_val, b_val = 5, 8
            
        # VALIDASI KUNCI A: Syarat mutlak Affine Cipher
        if math.gcd(a_val, 26) != 1:
            error_message = f"Nilai A={a_val} tidak valid! Nilai A dan 26 harus saling prima (GCD harus 1). Pilih angka lain seperti 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, atau 25."
        
        if text_input and not error_message:
            result_text, steps = process_affine(text_input, a_val, b_val, mode)
            
            # Simpan riwayat
            if 'history' not in session:
                session['history'] = []
            
            session['history'].insert(0, {
                'cipher': 'Affine',
                'mode': mode,
                'input': text_input,
                'key': f"a={a_val}, b={b_val}",
                'result': result_text
            })
            session['history'] = session['history'][:10]
            session.modified = True
            
    return render_template(
        'affine.html', 
        result_text=result_text, 
        steps=steps, 
        text_input=text_input, 
        a_val=a_val, 
        b_val=b_val, 
        mode=mode,
        error_message=error_message
    )