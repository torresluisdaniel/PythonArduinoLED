# **Control - LED**

#### **Python 3.8 - Arduino 1.8**

## **Funciones**

- Apagar LED
- Encender LED
- Comprobar conexión

Por defecto el **LED** debe ir conectado en el pin 9 del arduino, posteriormente se puede cambiar a cualquier el pin, en la sigueinte linea de codigo.

**62 - 74**

```
self.arduino.digital[9].write(1)
self.arduino.digital[9].write(0)
```

El numero **9** indica el pin del arduino puede ser cambiado por el que guste, tomando en cuneta que no debe ser un salidad analoga.

Cargar del modulo de Firmata en el **IDE** de arduino.

**Archivo/Ejemplos/Firmata/StandardFirmata**

**[Python - ](https://www.python.org/downloads/)**
**[Arduino](https://www.arduino.cc/en/Main/Software)**

> Nota: Si presenta error con los archivos como iconos o imagenes cambie la ruta de los archivos, cambiar **_".\src\ico\icono.ico"_** a **_".\ico\icono.ico_"** lo mismo para todos los archivos, ubicados en, **23, 29, 30.**

---

<p>Todos los derechos a <a href="https://www.instagram.com/luisdanieltorresacosta/">Luis Daniel Torres.</a></p>
