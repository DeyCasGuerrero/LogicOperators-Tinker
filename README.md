# DATOS

## Sección de Introducción
Esta app se basa en el modelo MVC (Modelo, vista, controlador) esto debido a preferencias propias ante este tipo de apps. 

# LIBRERIA
- Introducción
  La libreria que uso para hacer la GUI es tkinter, esto debido a que facilita el desarrollo de interfaz de aplicaciones de escritorio.
  Tambien vamos a hacer uso de PrettyTable para que genere las tablas lógicas.
- Instalación
  1. Requisitos
     Necesitas installar tkinter en tu proyecto para poder usarlo. Para verificar si tienes Tkinter usa "python -m tkinter" en tu terminal.
     Aqui puedes entrar a su documentacion [Ir a Google](https://docs.python.org/3/library/tkinter.html)
  
  3. Pasos de instalación
     Para instalar la libreria de python usa "pip install tk".
     Y por ultimo para llamar a la libreria en tu clase usa "import tkinter as tk" (eso dependerá de como desees nombrarlo).
     
     Tambien necesitarás instalar PrettyTable con el siguiente comando"pip install prettytable" y lo llamaras en tu clase de esta manera "from prettytable import PrettyTable".

## Sección del Modelo
En la app Se cuentra la carpetas Model, Controller y View.

1. **MODEL:**
   - En esta carpeta se encuentra una clase, esta maneja toda la logica de los datos.
2. **View:**
   - Aquí se encuentra la parte con la que el usuario interactuará (La vista), encontramos el diseño de la interfaz grafica usando Tkinter.
3. **CONTROLLER:**
   - En el controlador se encuentra funciones como la enviar los datos, y generar las tablas con PrettyTable.
     Esta se encarga de controlar como se muestran los datos.


     
