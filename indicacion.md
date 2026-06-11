Actúa como un tutor experto en Python y desarrollo backend. Quiero aprender a crear una API REST básica usando el framework Flask y SQLite como base de datos. No quiero nada de frontend (nada de HTML, CSS o plantillas). El proyecto debe responder exclusivamente en formato JSON.

El sistema será una base de datos de VENTAS muy básica con tres tablas:
1. productos (id, nombre, precio)
2. clientes (id, nombre, email)
3. ventas (id, cliente_id, producto_id, fecha)

Por favor, generame una guía paso a paso que incluya:

1. El código de un script en Python para crear el archivo de la base de datos ('ventas.db'), las tres tablas con sus llaves foráneas y unos pocos datos de prueba iniciales usando la librería nativa `sqlite3`.
2. El código completo del backend en Flask que tenga las siguientes rutas (endpoints) configuradas:
   - GET `/productos`: Para listar todos los productos disponibles.
   - POST `/ventas`: Para registrar una nueva venta (recibiendo `cliente_id` y `producto_id` en formato JSON).
3. Una explicación breve de cómo Flask usa `sqlite3` para conectarse, ejecutar la consulta y cerrar la conexión de forma segura en cada petición.
4. Las instrucciones para ejecutar el servidor localmente.
5. Los comandos exactos de cURL (o ejemplos de peticiones) para probar tanto el GET como el POST desde la terminal o Postman.

Mantén el código lo más simple, limpio y directo posible. Usa SQL puro con `sqlite3`, sin usar ORMs como SQLAlchemy, ya que quiero entender la lógica desde las bases.
