******************
IATI Documentation
******************

This is the IATI Docs Base. It documents the **Widgets API** with an interactive
reference — a renderer trial using `Swagger UI <https://github.com/swagger-api/swagger-ui>`_,
rendered **natively** by the `swagger-plugin-for-sphinx
<https://github.com/SAP/swagger-plugin-for-sphinx>`_ extension (a real Sphinx
directive; assets pinned and mirrored into the build, no CDN at load time). It
has a built-in "try it out" console.

.. raw:: html

   <p style="margin: 1.5rem 0;">
     <a href="api-reference/" target="_blank" rel="noopener"
        style="display:inline-block; padding:0.65rem 1.15rem; background:#155366;
               color:#fff; border-radius:6px; text-decoration:none; font-weight:600;">
       Open the Widgets API reference &#8599;
     </a>
   </p>
   <p style="color:#555; font-size:0.95rem;">Opens in a new tab &mdash; full width,
   with the IATI header, and the whole content area given to the reference. Pin the
   Swagger UI version in <code>docs/conf.py</code>; tweak the brand colour
   (<code>#155366</code>) in <code>docs/api-reference.rst</code>.</p>

.. note::

   The "try it out" console sends real requests. Against a live API it needs CORS
   enabled on the server (or a proxy).

.. toctree::
    :hidden:
    :titlesonly:
    :maxdepth: 3
    :caption: Documentation

    Home <self>
