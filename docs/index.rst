******************
IATI Documentation
******************

**API documentation renderer trial — Swagger UI.**

This page embeds the *Widgets API* reference using `Swagger UI
<https://github.com/swagger-api/swagger-ui>`_, the original OpenAPI renderer,
with its built-in "Try it out" console. Swagger UI has no theme presets, so the
IATI brand colour (``#155366``) is applied via plain CSS overrides; edit
``docs/_static/api/swagger-ui.html`` to re-theme.

.. note::

   The "Try it out" console sends real requests. Against a live API it needs
   CORS enabled on the server (or a proxy).

.. raw:: html

   <div style="position: relative; left: 50%; width: 100vw; margin-left: -50vw;">
     <iframe
       src="_static/api/swagger-ui.html"
       title="Widgets API reference (Swagger UI)"
       style="display: block; width: 100%; height: 88vh; border: 0;"
       loading="lazy">
     </iframe>
   </div>


.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 3
    :caption: Documentation

    Home <self>
