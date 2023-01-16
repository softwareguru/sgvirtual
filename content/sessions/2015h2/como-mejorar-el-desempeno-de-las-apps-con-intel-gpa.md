---
title: "Cómo mejorar el desempeño de las apps con Intel GPA"
speakers:
 - Arturo Jamaica
date: 2015-10-21T12:00:00
time_start: 2015-10-21T12:00:00
time_end: 2015-10-21T13:00:00
video: https://youtu.be/MTWKIVq6sD8
slides: https://slideshare.net/slideshow/embed_code/key/aLQfXjgSjsl8HX
---

<p>En esta sesión mostraremos cómo podemos analizar y mejorar el desempeño de los gráficos en nuestras aplicaciones móviles utilizando <a href="https://software.intel.com/en-us/gpa" target="_blank">Intel Graphics Performance Analyzer (GPA)</a>.</p>

<p dir="ltr">Intel GPA es un conjunto de herramientas que permiten a los desarrolladores analizar el desempeño de sus aplicaciones para encontrar cuellos de botella y oportunidades de optimización. Está compuesta por los siguientes módulos:</p>

<p dir="ltr">System Analyzer. Muestra información de desempeño del CPU, GPU y consumo de energía en tiempo real. Permite realizar experimentos de optimización con OpenGL sin necesidad de recompilar el código.</p>

<p dir="ltr">Platform Analyzer. Sincroniza los relojes de todo el sistema y permite visualizar cómo se reparte el tiempo de ejecución de una app entre el CPU y el GPU. También muestra información de desempeño a nivel de sistema, incluyendo actividad de los threads y cambios de contexto.</p>

<p dir="ltr">Graphics Frame Analyzer. Herramienta de depuración y optimización de cuadros (frames) individuales. Permite explorar el impacto en desempeño que tiene cada elemento gráfico específico durante el rendereo de un cuadro.</p>