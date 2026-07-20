******************
IATI Documentation
******************

**API documentation renderer trial — Stoplight Elements.**

This page embeds the *Widgets API* reference using `Stoplight Elements
<https://github.com/stoplightio/elements>`_, which adds a built-in "Try It"
console and a three-column layout. The primary colour is set to the IATI theme
brand colour (``#155366``); edit ``docs/_static/api/stoplight.html`` to
re-theme.

.. note::

   The "Try It" console sends real requests. Against a live API it needs CORS
   enabled on the server (or a proxy set via the ``tryItCorsProxy`` attribute).

.. raw:: html

   <div style="position: relative; left: 50%; width: 100vw; margin-left: -50vw;">
     <iframe
       src="_static/api/stoplight.html"
       title="Widgets API reference (Stoplight Elements)"
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
