========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |downloads| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/django-weasyprint-pdf/badge/?style=flat
    :target: https://readthedocs.org/projects/django-weasyprint-pdf
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/luzfcb/django-weasyprint-pdf.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/luzfcb/django-weasyprint-pdf

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/luzfcb/django-weasyprint-pdf?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/luzfcb/django-weasyprint-pdf

.. |requires| image:: https://requires.io/github/luzfcb/django-weasyprint-pdf/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/luzfcb/django-weasyprint-pdf/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/luzfcb/django-weasyprint-pdf/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/luzfcb/django-weasyprint-pdf

.. |version| image:: https://img.shields.io/pypi/v/django-weasyprint-pdf.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-weasyprint-pdf

.. |commits-since| image:: https://img.shields.io/github/commits-since/luzfcb/django-weasyprint-pdf/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/luzfcb/django-weasyprint-pdf/compare/v0.1.0...master

.. |downloads| image:: https://img.shields.io/pypi/dm/django-weasyprint-pdf.svg
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-weasyprint-pdf

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-weasyprint-pdf.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-weasyprint-pdf

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-weasyprint-pdf.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-weasyprint-pdf

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-weasyprint-pdf.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-weasyprint-pdf


.. end-badges

django helper tools to integrate with WeasyPrint

* Free software: BSD license

Installation
============

::

    pip install django-weasyprint-pdf

Documentation
=============

https://django-weasyprint-pdf.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


https://gist.github.com/luzfcb/06f957a241e7f1932724046e1ad83d67

https://github.com/Kozea/WeasyPrint/issues/76

https://github.com/Kozea/WeasyPrint/issues/181

https://gist.github.com/pikhovkin/5642563

http://stackoverflow.com/questions/39941967/generate-pdf-with-weasyprint-having-common-header-footer-and-pagination

http://stackoverflow.com/questions/30304258/weasyprint-fixed-footer-tag-overlapped-by-long-table-on-each-pdf-page

http://stackoverflow.com/questions/17843147/is-it-possible-to-do-fancy-formatting-for-page-footers-with-weasyprint?rq=1





