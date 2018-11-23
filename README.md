# Cross2Rekordbox_XML

Tool to fix beatgrid offsets in rekordbox.xml exported by Mixvibes Cross.

This tool has been tested on the following software versions:

* Cross 3.4.3
* Rekordbox 3.3.0

_**This project is still in alpha!**_

---

## Setup

To install setup environment run in terminal:

```text
python setup.py install
```

## Usage

```text
Cross2Rekordbox_XML [-h] [-d] [-v] [-D]

Tool to fix beatgrid offsets in rekordbox.xml exported by Mixvibes Cross.

optional arguments:
  -h, --help     show this help message and exit
  -d, --dump     Dump fixed XML to standard output instead of file
  -v, --verbose  Display a list of items fixed in the output file
  -D, --debug    Enable debug mode
```

[The source for this project is available here][src].

---

This is the README file for the project.

The file should use UTF-8 encoding and can be written using
[reStructuredText][rst] or [markdown][md use] with the appropriate [key set][md
use]. It will be used to generate the project webpage on PyPI and will be
displayed as the project homepage on common code-hosting services, and should be
written for that purpose.

Typical contents for this file would include an overview of the project, basic
usage examples, etc. Generally, including the project changelog in here is not a
good idea, although a simple “What's New” section for the most recent version
may be appropriate.

[src]: https://github.com/binaryguru/cross2rekordbox_xml
[rst]: http://docutils.sourceforge.net/rst.html
[md]: https://tools.ietf.org/html/rfc7764#section-3.5 "CommonMark variant"
[md use]: https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
