=====================================
Integration Between Sales And Project
=====================================

Installation
============

* `Install <https://odoo-development.readthedocs.io/en/latest/odoo/usage/install-module.html>`__ this module in a usual way

Configuration
=============

* User must have access to create/write Project Task in order to convert to task.
Optional:
* Go to Sales settings via under `Configuration` >> `Settings`.
* Set Default Project and Stage for created tasks.
* Check `Allow Convert **state name**` field if you want allow to convert in current stage.
* Go to stage settings via Project menu >> Stages option. Open/create new stage form and check ``Allow Convert Task to Quotation`` in order allow converting tasks to quotation in current stage.
* User must have access to create/write sale orders in order to convert to quotation.

Usage
=====

* Open menu ``Sales >> Quotations/Sale Order >> Choose SO``.
* If so in allowed state, there will be button ``Convert to Task``.
* Open menu ``Project >> Tasks >> Choose task``.
* If task in configured stage, there will be button ``Convert to Quotation``.
