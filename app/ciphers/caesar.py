from flask import Blueprint, render_template, request, session

bp = Blueprint('caesar', __name__)

def process_caesar(text, shift, mode='encrypt'):
    """
    Fungsi inti Caesar Cipher.
    Menghasilkan teks final dan daftar langkah perhitungan per karakter.
    """
    result_text = ""
    steps = []
    
    # Untuk dekripsi, kita membalik arah pergeseran (shift menjadi negatif)
    actual_shift = shift if mode == 'encrypt' else -shift
    
    for char in text:
        # Template untuk log per karakter
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
            base_ascii = 65 if is_upper else 97 # A=65, a=97 di ASCII
            
            # Ubah huruf menjadi angka 0-25 (P atau C)
            char_val = ord(char) - base_ascii
            
            # Implementasi rumus: C = (P + k) mod 26 atau P = (C - k) mod 26
            new_val = (char_val + actual_shift) % 26
            
            # Ubah kembali angka menjadi huruf ASCII
            result_char = chr(new_val + base_ascii)
            
            result_text += result_char
            step_detail['result'] = result_char
            
            # Catat rumus dan penjelasan untuk ditampilkan di UI nantinya
            if mode == 'encrypt':
                step_detail['formula'] = f"({char_val} + {shift}) mod 26 = {new_val}"
                step_detail['explanation'] = f"P = '{char}' ({char_val}) ➔ C = '{result_char}' ({new_val})"
            else:
                # Agar tampilan dekripsi rumusnya enak dibaca (C - K)
                step_detail['formula'] = f"({char_val} - {shift}) mod 26 = {new_val}"
                step_detail['explanation'] = f"C = '{char}' ({char_val}) ➔ P = '{result_char}' ({new_val})"
                
        else:
            # Jika spasi atau tanda baca, tambahkan langsung tanpa diubah
            result_text += char
            
        steps.append(step_detail)
        
    return result_text, steps

@bp.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    steps = None
    text_input = ""
    shift_key = 3
    mode = "encrypt"
    
    if request.method == 'POST':
        # Menangkap data dari form (nanti dibuat di Fase 4)
        text_input = request.form.get('text', '')
        # Pastikan shift berupa integer, fallback ke 0 jika kosong/error
        try:
            shift_key = int(request.form.get('shift', 3))
        except ValueError:
            shift_key = 0
            
        mode = request.form.get('mode', 'encrypt')
        
        # Eksekusi algoritma
        if text_input:
            result_text, steps = process_caesar(text_input, shift_key, mode)
            
            # (Opsional) Menyimpan riwayat sederhana ke session untuk fitur History
            # Nanti kita akan sempurnakan fitur history di Fase 3
            if 'history' not in session:
                session['history'] = []
            
            session['history'].insert(0, {
                'cipher': 'Caesar',
                'mode': mode,
                'input': text_input,
                'key': f"Shift {shift_key}",
                'result': result_text
            })
            # Batasi history max 10 agar session tidak bengkak
            session['history'] = session['history'][:10]
            session.modified = True
            
    return render_template(
        # Akan dibuat di Fase 4
        'caesar.html', 
        result_text=result_text, 
        steps=steps, 
        text_input=text_input, 
        shift_key=shift_key, 
        mode=mode
    )