:orphan:

***************
Widgets API
***************

.. raw:: html

   <style>
     /* Scoped to this page: keep the IATI header, but hand the whole content
        area to the API explorer — hide the left nav, breadcrumb, footer and the
        page title, and drop the content max-width/padding. */
     .iati-breadcrumb { display: none !important; }
     .globaltoc { display: none !important; }
     .iati-footer { display: none !important; }
     .iati-main { max-width: none !important; padding: 0 !important; }
     .documentwrapper { padding: 0 !important; }
     .document { width: 100% !important; }
     .body { padding: 0 !important; }
     .body h1 { display: none !important; }
     .body section, .body [class*="section"] { margin: 0 !important; padding: 0 !important; }
     #api-explorer { display: block; width: 100%; border: 0; }
   </style>
   <iframe id="api-explorer" src="../_static/api/stoplight.html" title="Widgets API reference (Stoplight Elements)"></iframe>
   <script>
     (function () {
       var f = document.getElementById('api-explorer');
       function fit() {
         var top = f.getBoundingClientRect().top + window.scrollY;
         f.style.height = Math.max(480, window.innerHeight - top) + 'px';
       }
       window.addEventListener('resize', fit);
       window.addEventListener('load', fit);
       fit();
     })();
   </script>
