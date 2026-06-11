# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal

A learning project: a minimal REST API for a sales database using **Flask** and **SQLite** (raw `sqlite3`, no ORM). All responses are JSON only — no frontend, no templates.

Three tables:
- `productos` (id, nombre, precio)
- `clientes` (id, nombre, email)
- `ventas` (id, cliente_id, producto_id, fecha) — with foreign keys to the other two tables

Planned endpoints:
- `GET /productos` — list all products
- `POST /ventas` — register a new sale (body: `{ "cliente_id": int, "producto_id": int }`)

## Setup

```bash
# Install Flask (only external dependency)
pip install flask

# Create the database and seed initial data
python crear_db.py

# Run the development server
python app.py
```

## Architecture

Two files are expected:

- **`crear_db.py`** — one-time script that creates `ventas.db`, all three tables with their foreign keys, and inserts seed data using `sqlite3`.
- **`app.py`** — Flask application. Each route opens a `sqlite3` connection, runs a query, and closes the connection before returning. No persistent connection or connection pool is used; the connection lifecycle is per-request.

## Testing endpoints

```bash
# List products
curl http://localhost:5000/productos

# Register a sale
curl -X POST http://localhost:5000/ventas \
  -H "Content-Type: application/json" \
  -d '{"cliente_id": 1, "producto_id": 2}'
```
