:orphan:

***************
Widgets API
***************

.. raw:: html

   <style>
     /* Keep the IATI header, but give the whole content area to the Swagger UI
        reference (rendered natively by swagger-plugin-for-sphinx). Scoped to
        this page: hide the theme's left nav, breadcrumb, footer and page title,
        and drop the content max-width/padding. */
     .iati-breadcrumb { display: none !important; }
     .globaltoc { display: none !important; }
     .iati-footer { display: none !important; }
     .iati-main { max-width: none !important; padding: 0 !important; }
     .documentwrapper { padding: 0 !important; }
     .document { width: 100% !important; }
     .body { padding: 0 !important; }
     /* Hide only the Sphinx page title (direct child of the section), not any
        heading Swagger UI renders inside the content. */
     .body > section > h1, .body > div[class*="section"] > h1 { display: none !important; }
     .body section, .body [class*="section"] { margin: 0 !important; padding: 0 !important; }
     .swagger-ui .info .title { display: block !important; }
     /* IATI brand (#155366) layered over Swagger UI's defaults. */
     .swagger-ui .topbar { display: none; }
     .swagger-ui .info { margin: 24px 16px; }
     .swagger-ui .info .title { color: #155366; }
     .swagger-ui .btn.execute { background: #155366; border-color: #155366; }
     .swagger-ui .btn.authorize { color: #155366; border-color: #155366; }
     .swagger-ui .btn.authorize svg { fill: #155366; }
     .swagger-ui .opblock.opblock-get .opblock-summary-method { background: #155366; }
     .swagger-ui .opblock.opblock-get { border-color: #155366; background: rgba(21,83,102,.04); }
     .swagger-ui .opblock.opblock-get .opblock-summary { border-color: #155366; }
     .swagger-ui a { color: #155366; }
   </style>

.. swagger-plugin:: specifications/test-widget-api.yaml

..
   "Try it out" is available by default, so swagger-options is omitted on purpose:
   in swagger-plugin-for-sphinx 7.2.1, boolean values passed via swagger-options
   render as Python True/False in the JS config and break SwaggerUIBundle.
