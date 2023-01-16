---
title: "Pruebas de performance ¿Realmente hacemos pruebas completas?"
speakers:
 - Miguel Angel De León Trejo
date: 2016-10-26T12:00:00
time_start: 2016-10-26T12:00:00
time_end: 2016-10-26T13:00:00
video: https://youtu.be/DpJ9_ccoOBY
slides: https://slideshare.net/slideshow/embed_code/key/B6HQXty33DNXKX
---

Desafortunadamente aún en la actualidad, no se han formalizado del todo los criterios que se deben considerar al ejecutar pruebas de performance, incluso a veces ni si quiera se tienen plenamente identificados los criterios por los cuales se puede decir que son satisfactorias.

Ejemplo: El LP o cliente dice: "Necesitamos pruebas de performance de X aplicación" 
--...Ok, y ¿qué volumetría esperamos?, ¿cuántos usuarios?, ¿en qué horarios?, ¿cuántos registros en BD?, ¿cuánto tráfico habrá por la red?...nadie sabe...pero aún así ejecutamos...y obtenemos resultados que se ven muy bonitos en X herramienta (Jmeter, LoadRunner, LoadUI, etc.) y generamos un reporte que medio interpretamos, pero ¿a quién le importa?, las gráficas se ven bonitas!!!

...y cuando salimos a producción...¿quién revisó que el pool de conexiones a BD o el pool de conexiones http no se agotara?, ¿quién se fijó que con sólo 20 conexiones concurrentes el CPU se iba al 90%?, ¿nadie notó que la memoria no se estaba liberando?, o alguien vio que la escritura en disco generaba time outs....y dónde le cambio el time out?

:( Las gráficas de nuestras herramientas no reflejan todo eso...

En la sesión propondremos algunos tips que debemos considerar mientras ejecutamos nuestras pruebas.