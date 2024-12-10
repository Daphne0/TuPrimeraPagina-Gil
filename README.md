# Sistema de Gestión de Pedidos - Django

Este proyecto es un sistema de gestión de pedidos para una pastelería. Permite gestionar clientes, productos y pedidos. Los usuarios pueden crear, buscar y ver clientes, productos y pedidos. Este proyecto está desarrollado utilizando Django con el patrón MVT (Modelo, Vista, Template).

## Requisitos

Para correr este proyecto en tu máquina local, necesitarás tener instalados los siguientes programas:

- Python 3.x
- Django 5.x
- SQLite3 (para la base de datos, es el predeterminado en Django)

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd TuPrimeraPagina+Gil
2. **Crear un entorno virtual**
python -m venv venv
3.**Activar el entorno virtual**
.\venv\Scripts\activate
4.**Instalar dependencias**
pip install -r requirements.txt
5. **Realizar las migraciones de la base de datos**
python manage.py migrate
6. **Correr el servidor de desarrollo**
python manage.py runserver



Funcionalidades
Crear Cliente: Se puede crear un cliente proporcionando su nombre, teléfono y dirección.
Crear Producto: Se puede crear un producto con nombre, tipo y precio.
Crear Pedido: Se pueden crear pedidos, asignando productos a un cliente.
Buscar Cliente: Permite buscar clientes por nombre.

Para ir al inicio accede a http://127.0.0.1:8000/
Crear Cliente: Accede a http://127.0.0.1:8000/crear-cliente/ para crear un nuevo cliente. Puedes llenar un formulario con los datos del cliente, y una vez creado, serás redirigido a la página de inicio.
Crear Producto: Accede a http://127.0.0.1:8000/crear-producto/ para agregar un nuevo producto. Completa el formulario con los detalles del producto y guarda los cambios.
Crear Pedido: Dirígete a http://127.0.0.1:8000/crear-pedido/ para realizar un pedido. Deberás seleccionar un cliente y añadir productos al pedido.
Buscar Cliente: En http://127.0.0.1:8000/buscar-cliente/, puedes buscar clientes por su nombre. El sistema mostrará una lista de clientes que coincidan con tu búsqueda.