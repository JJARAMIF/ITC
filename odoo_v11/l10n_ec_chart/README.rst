============================
Plan de Cuentas para Ecuador
============================

Agrega el plan de cuentas para Ecuador.
* Utiliza la clasificación de la Superintendencia de Compañías.
* Sigue los requerimientos para las PYMEs

Probado en la versión
=====================
11.0-20171005

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3
   
Instalación
===========

Para instalar este módulo se debe:
* Elimina el módulo l10n_ec de los addons de Odoo.
* Copia este módulo en el mismo directorio, reemplazando el anterior.
* Instalarlo de manera regular, no es necesario instalar account primero, este módulo lo instalará y configurará.

Configuración
=============

Este módulo agrega las cuentas contables según la clasificación de la Supercias, sin embargo, te damos algunas recomendaciones:
* Es conveniente eliminar las cuentas contables que no vayan a ser utilizadas por su compañía.
* Debe agregar las cuentas que no son obligatorias, pero desea utilizar.
* Debido a que Odoo no usa cuentas de total, al crear una cuenta, tenga presente la codificación estándar, por ejemplo, si requiere una cuenta de bancos y colocarla dentro de 10101, su código debe ser 10101xx.
* La cuenta

Problemas conocidos
===================

* La cuenta de transferencias por defecto usada  es la 1010199, la cual no forma parte de la especificación de la Supercias, sin embargo, es necesaria para que Odoo pueda realizar las transferencias internas, a menos que sepas lo que haces, no cambies esta configuración.
* Este plan de cuentas no incluye información de impuestos debido a que pretende ser compatible con las demás localizaciónes ecuatorianas disponibles.

Planificación
=============

* Los Diarios por defecto son creados en inglés y las secuencias no son las mejores para Ecuador, está en nuestros planes cambiar los Diarios por unos más apropiados.

Rastreo de Fallos
=================

Los errores son rastreados en Github <https://github.com/JJARAMIF/ITC/issues>`_, en caso de problemas por favor revisa si ya han sido reportados en el apartado de issues,
si los has detectado primero, por favor reportalos con la informacion debida, al menos debes indicar la versión,
los pasos para reproducir y el comportamiento esperado.

Créditos
========

* ITC Tecnologia

Contribución
------------

    * ITC Store <info@itc.ec>

Mantenimiento
-------------

.. image:: http://www.museoelrehilete.org.mx/images/areas-logos/tecnologia-logo.png
   :alt: ITC Store
   :target: http://www.itc.ec

El manetenimiento de este módulo es responsabilidad de ITC Tecnologia.

ITC, [Innovación, Tecnología, Confianza](http://www.itc.ec/), es una empresa dedicada 
al comercio de Tecnologia y desarrollo de Soluciones Integrales.
    :alt: License: AGPL-3
