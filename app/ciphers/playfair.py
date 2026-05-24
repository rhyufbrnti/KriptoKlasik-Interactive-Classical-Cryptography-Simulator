from flask import Blueprint, render_template, request, session

bp = Blueprint('playfair', __name__)

def generate_playfair_matrix(key):
    """
    Menghasilkan matriks 5x5 berdasarkan kata kunci.
    Huruf 'J' selalu diganti menjadi 'I'.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Tanpa J
    matrix_list = []
    
    # Bersihkan key
    clean_key = ''.join([c for c in key if c.isalpha()]).upper()
    clean_key = clean_key.replace('J', 'I')
    
    # Masukkan huruf key ke dalam list tanpa duplikat
    for char in clean_key:
        if char not in matrix_list:
            matrix_list.append(char)
            
    # Masukkan sisa alfabet
    for char in alphabet:
        if char not in matrix_list:
            matrix_list.append(char)
            
    # Ubah list 1D (25 huruf) menjadi matriks 2D (5x5)
    matrix = [matrix_list[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, char):
    """Mencari posisi (baris, kolom) sebuah huruf di dalam matriks"""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return -1, -1

def prepare_text(text):
    """
    Memformat teks: hapus non-alfabet, ganti J jadi I, dan pecah menjadi pasangan (digraph).
    Jika ada huruf kembar dalam satu pasangan, sisipkan 'X'.
    Jika panjang akhirnya ganjil, tambahkan 'X' di akhir.
    """
    clean_text = ''.join([c for c in text if c.isalpha()]).upper()
    clean_text = clean_text.replace('J', 'I')
    
    pairs = []
    i = 0
    while i < len(clean_text):
        char1 = clean_text[i]
        # Jika ini huruf terakhir, pasangkan dengan 'X'
        if i == len(clean_text) - 1:
            pairs.append(char1 + 'X')
            break
            
        char2 = clean_text[i+1]
        
        # Jika hurufnya sama (kembar), sisipkan 'X'
        if char1 == char2:
            # Jika kebetulan huruf kembarnya adalah X, sisipkan Z agar tidak rancu
            filler = 'Z' if char1 == 'X' else 'X'
            pairs.append(char1 + filler)
            i += 1 # Maju 1 langkah saja karena char2 akan dipakai di pasangan berikutnya
        else:
            pairs.append(char1 + char2)
            i += 2 # Maju 2 langkah
            
    return pairs

def process_playfair(text, key, mode='encrypt'):
    """Fungsi inti Playfair Cipher"""
    matrix = generate_playfair_matrix(key)
    pairs = prepare_text(text)
    
    result_text = ""
    steps = []
    
    shift = 1 if mode == 'encrypt' else -1
    
    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        
        rule_applied = ""
        out_pair = ""
        
        # Aturan 1: Baris yang sama
        if r1 == r2:
            out_pair += matrix[r1][(c1 + shift) % 5]
            out_pair += matrix[r2][(c2 + shift) % 5]
            rule_applied = "Baris Sama"
            
        # Aturan 2: Kolom yang sama
        elif c1 == c2:
            out_pair += matrix[(r1 + shift) % 5][c1]
            out_pair += matrix[(r2 + shift) % 5][c2]
            rule_applied = "Kolom Sama"
            
        # Aturan 3: Persegi (Beda baris, beda kolom)
        else:
            # Tetap di baris yang sama, tapi tukar kolom
            out_pair += matrix[r1][c2]
            out_pair += matrix[r2][c1]
            rule_applied = "Persegi"
            
        result_text += out_pair
        
        # Catat langkah untuk UI
        steps.append({
            'pair_in': pair,
            'pos1': f"({r1},{c1})",
            'pos2': f"({r2},{c2})",
            'rule': rule_applied,
            'pair_out': out_pair
        })
        
    return result_text, steps, matrix

@bp.route('/', methods=['GET', 'POST'])
def index():
    result_text = None
    steps = None
    matrix = None
    
    text_input = ""
    key_input = "PLAYFAIR"
    mode = "encrypt"
    
    if request.method == 'POST':
        text_input = request.form.get('text', '')
        key_input = request.form.get('key', 'PLAYFAIR')
        mode = request.form.get('mode', 'encrypt')
        
        if text_input and key_input:
            result_text, steps, matrix = process_playfair(text_input, key_input, mode)
            
            # Simpan riwayat
            if 'history' not in session:
                session['history'] = []
            
            session['history'].insert(0, {
                'cipher': 'Playfair',
                'mode': mode,
                'input': text_input[:50] + "..." if len(text_input) > 50 else text_input,
                'key': key_input.upper(),
                'result': result_text
            })
            session['history'] = session['history'][:10]
            session.modified = True
            
    return render_template(
        'playfair.html', 
        result_text=result_text, 
        steps=steps, 
        matrix=matrix,
        text_input=text_input, 
        key_input=key_input, 
        mode=mode
    )