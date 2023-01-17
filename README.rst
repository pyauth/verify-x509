verify-x509: A minimalistic X.509 certificate validator
=======================================================
verify-x509 is a minimalistic implementation of X.509 certificate validation logic. It is intended for use with
applications and protocols that use X.509 PKI without TLS/SSL. Its features are:

* Certificate chain building to the Mozilla trust store
* Point-in-time validation of not-before/not-after constraints
* Plugin architecture for X.509 extension processing
* Offline operation (while OCSP responses and CRLs can be passed by the caller, verify-x509 makes no network calls)

verify-x509 implements elements of the following RFCs
RFC 5280

Installation
------------
::

    pip install verify-x509

Synopsis
--------

.. code-block:: python

    from verify_x509 import X509Verifier
    ...

Authors
-------
* Andrey Kislyuk

Links
-----
* `Project home page (GitHub) <https://github.com/pyauth/verify-x509>`_
* `Documentation <https://pyauth.github.io/verify-x509/>`_
* `Package distribution (PyPI) <https://pypi.python.org/pypi/verify-x509>`_
* `Change log <https://github.com/pyauth/verify-x509/blob/master/Changes.rst>`_
* `IETF RFC 3161: Time-Stamp Protocol (TSP) <https://www.rfc-editor.org/rfc/rfc3161.html>`_

Bugs
~~~~
Please report bugs, issues, feature requests, etc. on `GitHub <https://github.com/pyauth/verify-x509/issues>`_.

License
-------
Copyright 2022-2023, Andrey Kislyuk and verify-x509 contributors. Licensed under the terms of the
`Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_. Distribution of the LICENSE and NOTICE
files with source copies of this package and derivative works is **REQUIRED** as specified by the Apache License.
