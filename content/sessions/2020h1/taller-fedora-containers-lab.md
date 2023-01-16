---
title: "Taller: Fedora Containers Lab"
speakers:
 - Alex Callejas
date: 2020-04-20T12:00:00
time_start: 2020-04-20T12:00:00
time_end: 2020-04-20T13:00:00
video: https://youtu.be/Pb27CYlkCJA
slides: https://darkaxl017.fedorapeople.org/slides/FedoraContainersLab-SGVirtual.pdf
---

<p>En este taller vamos a mostrar cómo crear y manejar contenedores desde cero.</p>

<p>Usando ejercicios sencillos, con skopeo, podman y buildah mostraremos cómo crear contenedores básicos basados en imagenes del registro fedora, hasta contenedores personalizados basados en Docker y posteriormente cómo usar estos contenedores para aprender los principios de Kubernetes.</p>

<h3 id="requisitos">Requisitos</h3>

<ul>
 <li>Kernel con soporte para KVM (fedora, Debian, Arch, etc). Ver&nbsp;<a href="https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-virtualization/">más información</a></li>
 <li>Mínimo 5G de espacio en disco disponible.</li>
 <li>Tener instalados los siguientes paquetes:&nbsp;<code>qemu-kvm virt-manager virt-viewer libguestfs-tools virt-install genisoimage</code></li>
 <li>Descargar la imagen de&nbsp;<a href="https://alt.fedoraproject.org/cloud/">Fedora 31 Cloud Base</a>&nbsp;(descargar “Cloud Base Image for Openstack”).</li>
</ul>