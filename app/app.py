import os, cv2, sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, jsonify, send_file
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
   os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

DB_PATH = "database/trilha_cloud.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            image TEXT NOT NULL,
            image_proc TEXT NOT NULL,
            ip TEXT NOT NULL
        )
        """)
        conn.commit()

init_db()


@app.route('/')
def home():
        return render_template('index.html')


@app.route('/image/<filename>')
def uploaded_file(filename):
   file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
   return send_file(file)


@app.route('/upload', methods=['POST'])
def upload_image():
   if 'image' not in request.files:
      return jsonify({'error': 'No image file uploaded'}), 400
   
   dt = datetime.now()

   file = request.files.get('image')
   filename = secure_filename(file.filename)
   originalImgPath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
   file.save(originalImgPath)

   img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
   kernel_size = (30, 30)                       # Ajuste o tamanho do kernel (quanto maior, mais desfoque)
   processedImg = cv2.blur(img, kernel_size)    # Aplicar o desfoque
   processedImgFilename = filename.rsplit('.', 1)[0].lower() + '_processed.jpg'
   processedImgPath = UPLOAD_FOLDER + processedImgFilename
   cv2.imwrite(processedImgPath, processedImg)

   with sqlite3.connect(DB_PATH) as conn:
      cursor = conn.cursor()
      cursor.execute("""
      INSERT INTO registros (datetime, image, image_proc, ip)
      VALUES (?, ?, ?, ?)
      """, (dt, originalImgPath, processedImgPath, request.remote_addr))
      conn.commit()

   return jsonify({
      "datetime": dt,
      "image": originalImgPath,
      "image_proc": processedImgPath,
      "ip": request.remote_addr
   })


@app.route('/registros', methods=['GET'])
def get_registros():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, datetime, image, image_proc, ip FROM registros")
        registros = cursor.fetchall()
    
    registros_lista = [
        {"id": row[0], "datetime": row[1], "image": row[2], "image_proc": row[3], "ip": row[4]}
        for row in registros
    ]
    
    return jsonify(registros_lista)


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
