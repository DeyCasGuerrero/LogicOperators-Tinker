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
     Aqui puedes entrar a su documentacion [Tkinter](https://docs.python.org/3/library/tkinter.html)
  
  3. Pasos de instalación
     Para instalar la libreria de python usa "pip install tk".
     Y por ultimo para llamar a la libreria en tu clase, usa "import tkinter as tk" (eso dependerá de como desees nombrarlo).
     
     Tambien necesitarás instalar PrettyTable con el siguiente comando "pip install prettytable" y lo llamaras en tu clase de esta manera "from prettytable import PrettyTable".

## Sección del Modelo
En la app se cuentra la carpetas Model, Controller y View.

1. **MODEL:**
   - En esta carpeta se encuentra una clase, esta maneja toda la logica de los datos.
2. **View:**
   - Aquí se encuentra la parte con la que el usuario interactuará (La vista), encontramos el diseño de la interfaz grafica usando Tkinter.
3. **CONTROLLER:**
   - En el controlador se encuentra funciones como la enviar los datos, y generar las tablas con PrettyTable.
     Esta se encarga de controlar como se muestran los datos.

# DATA

# Introduction Section
This app is based on the MVC(Model, View and Controller) due to personal preferences towards this type apps.

# Library
- Introduction
  The library i use to make the GUI on tkinter, because is simplifies the development of desktop application interfaces.
- Installation
  1. Requeriments 
     You need to install Tkinter in your project to be able to use it. To check if u have Tkinter, use "python -m tkinter" in your terminal.
     It's here the documentation [Tkinter](https://docs.python.org/3/library/tkinter.html)
     
  2. Installations Steps
     To install the Python library, use "pip install tk".
     And finally, to call the library in your class, use "import tkinter as tk".

     U will also need to install PrettyTable with the next command "pip install prettytable" and u can call in your class "from prettytable import PrettyTable".

## Model section
In the app there are the folders named Model, Controller and View.
1. **MODEL:**
   - In this folder, there is a class that handles all the data logic.
2. **View:**
   - Here is the part with wich the user will interact (The view). we find the design of the graphical interface using Tkinter.
3. **CONTROLLER:**
   - In the controller, there are funtions as sending the data, and generating tables with PrettyTable.
   - It is reponsible for controlling how the data is displayed.
