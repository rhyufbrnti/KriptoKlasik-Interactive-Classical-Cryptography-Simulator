from flask import Blueprint, render_template, request, session

bp = Blueprint('vigenere', __name__)

def process_vigenere(text, key, mode='encrypt'):
    """
    Fungsi inti Vigenère Cipher.
    Menghasilkan teks final dan daftar langkah perhitungan per karakter.
    """
    result_text = ""
    steps = []
    
    # Bersihkan key: buang spasi/simbol dan jadikan huruf kapital semua untuk standarisasi perhitungan
    clean_key = ''.join([c for c in key if c.isalpha()]).upper()
    
    # Fallback jika key kosong atau tidak mengandung huruf
    if not clean_key:
        clean_key = "A" # Key 'A' bernilai 0, artinya tidak ada pergeseran
        
    key_length = len(clean_key)
    key_index = 0 # Indeks untuk melacak huruf key mana yang sedang digunakan
    
    for char in text:
        step_detail = {
            'original': char,
            'is_alpha': False,
            'key_char': '-',
            'result': char,
            'formula': '-',
            'explanation': 'Bukan alfabet, dibiarkan'
        }
        
        if char.isalpha():
            step_detail['is_alpha'] = True
            is_upper = char.isupper()
            base_ascii = 65 if is_upper else 97
            
            # Nilai huruf teks (0-25)
            char_val = ord(char) - base_ascii
            
            # Ambil huruf key saat ini dan cari nilainya (0-25)
            current_key_char = clean_key[key_index % key_length]
            key_val = ord(current_key_char) - 65
            
            step_detail['key_char'] = current_key_char
            
            # Implementasi Rumus
            if mode == 'encrypt':
                new_val = (char_val + key_val) % 26
                step_detail['formula'] = f"({char_val} + {key_val}) mod 26 = {new_val}"
                step_detail['explanation'] = f"P = '{char}' ({char_val}), K = '{current_key_char}' ({key_val}) ➔ C = '{chr(new_val + base_ascii)}'"
            else:
                new_val = (char_val - key_val) % 26
                # Jika hasil negatif, Python % otomatis menangani (misal -5 % 26 = 21),
                # Tapi untuk edukasi/laporan, kita tulis rumusnya secara jelas.
                step_detail['formula'] = f"({char_val} - {key_val}) mod 26 = {new_val}"
                step_detail['explanation'] = f"C = '{char}' ({char_val}), K = '{current_key_char}' ({key_val}) ➔ P = '{chr(new_val + base_ascii)}'"
            
            result_char = chr(new_val + base_ascii)
            result_text += result_char
            step_detail['result'] = result_char
            
            # Geser indeks key HANYA JIKA huruf alfabet diproses
            key_index += 1
                
        else:
            result_text += char
            
        steps.append(step_detail)
        
    return result_text, steps

@bp.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    steps = None
    text_input = ""
    key_input = "KUNCI"
    mode = "encrypt"
    
    if request.method == 'POST':
        text_input = request.form.get('text', '')
        key_input = request.form.get('key', 'KUNCI')
        mode = request.form.get('mode', 'encrypt')
        
        if text_input and key_input:
            result_text, steps = process_vigenere(text_input, key_input, mode)
            
            # Simpan riwayat
            if 'history' not in session:
                session['history'] = []
            
            session['history'].insert(0, {
                'cipher': 'Vigenère',
                'mode': mode,
                'input': text_input,
                'key': f"Key: {key_input}",
                'result': result_text
            })
            session['history'] = session['history'][:10]
            session.modified = True
            
    return render_template(
        'vigenere.html', 
        result_text=result_text, 
        steps=steps, 
        text_input=text_input, 
        key_input=key_input, 
        mode=mode
    )