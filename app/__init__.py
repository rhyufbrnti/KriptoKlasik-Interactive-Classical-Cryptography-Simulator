from flask import Flask, render_template, session, redirect, url_for

def create_app():
    app = Flask(__name__)
    app.secret_key = 'rahasia_negara_bnn_atau_semacamnya' # Wajib ada agar session bisa berjalan
    
    # Import Blueprints
    from app.ciphers.caesar import bp as caesar_bp
    from app.ciphers.vigenere import bp as vigenere_bp
    from app.ciphers.affine import bp as affine_bp
    from app.ciphers.hill import bp as hill_bp
    from app.ciphers.playfair import bp as playfair_bp

    # Register Blueprints
    app.register_blueprint(caesar_bp, url_prefix='/caesar')
    app.register_blueprint(vigenere_bp, url_prefix='/vigenere')
    app.register_blueprint(affine_bp, url_prefix='/affine')
    app.register_blueprint(hill_bp, url_prefix='/hill')
    app.register_blueprint(playfair_bp, url_prefix='/playfair')

    # Route halaman utama
    @app.route('/')
    def index():
        return render_template('index.html')

    # === FITUR HISTORY (POIN 10) ===
    
    @app.route('/history')
    def history():
        # Mengambil data riwayat dari session, jika kosong kembalikan list kosong []
        history_data = session.get('history', [])
        return render_template('history.html', history=history_data)

    @app.route('/clear-history')
    def clear_history():
        # Menghapus 'history' dari session
        session.pop('history', None)
        # Setelah dihapus, kembalikan user ke halaman history yang sudah kosong
        return redirect(url_for('history'))

    return app