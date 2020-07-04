## TestML
Script realizado para escribir en un archivo de Log los items que posee un Vendedor en ML



Este script esta realizado en lenguaje Python. Tiene como objetivo, escribir en un archivo .txt con el ID del vendedor y 
los items que posea, a su vez de estos items, se guardaran el ID, el Título, la Categoría y el Nombre de la categoría a la cual pertenece.

**Pre-requisitos para poder ejecutar el script**
---
- se debe poseer instalado python.
- se debe poseer instalado el paquete requests.
- se debe poseer el paquete json

En caso de no tener instalados los paquetes, realizar la instalación con el comando `python -m pip install <<PAQUETE>>`.
En caso de no tener instalado Python, acceder al siguiente link y verificar la documentación https://www.python.org/

---
**SCRIPT**

**INPUT**
El script recibe como parámetros: 
  - ID del sitio a solicitar.
  - ID del vendedor (1 hasta N).
  
**OUTPUT**
El script tiene como resultado un archivo log<currenDateTime>.txt en el cual se escriben los datos obtenidos.
```
EJ: log-03072020-23_08.txt
*******************************************************************************
Seller ID: 179571326
*******************************************************************************
Item ID: MLA863267784
Item Title: Monitor Dell P2018h Led 19.5  Negro 110v/220v
Category ID: MLA14407
Category ID: MLA-COMPUTER_MONITORS
---------------------------------------------------------------------------
Item ID: MLA852423966
Item Title: Router Cisco Rv042g Negro
Category ID: MLA430901
Category ID: MLA-ROUTERS
---------------------------------------------------------------------------
```
**Uso**
---
Para ejecutar el script desde consola, dirigirse al directorio donde se encuentra el mismo, y utilizar la siguiente línea:

`python test.py <SITE> <SELLERID1> <SELLERID2> ... <SELLERID5>`

Ej: pytho test.py MLA 179571326 123456789

*Se deben respetar los espacios en los parámetros de entrada, de lo contrario los concatenará y se considerará 1 solo*

