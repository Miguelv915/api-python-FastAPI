import sqlite3

conn = sqlite3.connect("ventas.db")
cur = conn.cursor()

cur.executescript("""
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS productos (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT    NOT NULL,
        precio REAL    NOT NULL
    );

    CREATE TABLE IF NOT EXISTS clientes (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT    NOT NULL,
        email  TEXT    NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS ventas (
        id          INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id  INTEGER NOT NULL REFERENCES clientes(id),
        producto_id INTEGER NOT NULL REFERENCES productos(id),
        fecha       TEXT    NOT NULL DEFAULT (date('now'))
    );
""")

cur.executemany(
    "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
    [
        ("Laptop",   1200.00),
        ("Monitor",   350.00),
        ("Teclado",    45.00),
        ("Mouse",      20.00),
    ],
)

cur.executemany(
    "INSERT INTO clientes (nombre, email) VALUES (?, ?)",
    [
        ("Ana García",    "ana@example.com"),
        ("Luis Pérez",    "luis@example.com"),
        ("Marta López",   "marta@example.com"),
    ],
)

conn.commit()
conn.close()
print("Base de datos 'ventas.db' creada con datos de prueba.")
