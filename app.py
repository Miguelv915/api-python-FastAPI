import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DB = "ventas.db"


def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row  # permite acceder a columnas por nombre
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@app.get("/productos")
def listar_productos():
    conn = get_conn()
    try:
        rows = conn.execute("SELECT id, nombre, precio FROM productos").fetchall()
        return jsonify([dict(r) for r in rows])
    finally:
        conn.close()


@app.post("/ventas")
def registrar_venta():
    data = request.get_json(silent=True) or {}
    cliente_id  = data.get("cliente_id")
    producto_id = data.get("producto_id")

    if cliente_id is None or producto_id is None:
        return jsonify({"error": "Se requieren cliente_id y producto_id"}), 400

    conn = get_conn()
    try:
        cur = conn.execute(
            "INSERT INTO ventas (cliente_id, producto_id) VALUES (?, ?)",
            (cliente_id, producto_id),
        )
        conn.commit()
        venta = conn.execute(
            "SELECT id, cliente_id, producto_id, fecha FROM ventas WHERE id = ?",
            (cur.lastrowid,),
        ).fetchone()
        return jsonify(dict(venta)), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": str(e)}), 422
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
