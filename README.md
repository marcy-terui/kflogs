kflogs
=======

[![Version](https://img.shields.io/pypi/v/kflogs.svg)](https://pypi.python.org/pypi/kflogs)

# Description

Amazon Kinesis Firehose logging handler and utilities.

# Requirements

- Python2.7 or higher
- pip

# Installation

## PyPI

```sh
pip install kflogs
```

# Usage

#### Sample Code
```sh
import logging
import kflogs

logger = logging.getLogger('foo')
handler = kflogs.KinesisFirehoseHandler(stream_name='bar')
handler.setFormatter(kflogs.SimpleJsonFormatter())
logger.addHandler(handler)

logger.warning('Warnig!!')
```

#### Sample output
```json
{
  "msecs": 146.5139389038086,
  "args": [],
  "name": "foo",
  "thread": 140735094612736,
  "created": 1492418072.146514,
  "process": 52942, "threadName":
  "MainThread", "module":
  "test", "filename":
  "test.py", "levelno": 30,
  "processName": "MainProcess",
  "pathname": "test.py",
  "lineno": 11,
  "exc_text": null,
  "exc_info": null,
  "funcName": "<module>",
  "relativeCreated": 884.4590187072754,
  "levelname": "WARNING",
  "msg": "Warnig!!"
}
```

Development
-----------

-   Source hosted at [GitHub](https://github.com/marcy-terui/kflogs)
-   Report issues/questions/feature requests on [GitHub
    Issues](https://github.com/marcy-terui/kflogs/issues)

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1.  Fork the repo
2.  Create your feature branch (`git checkout -b my-new-feature`)
3.  Commit your changes (`git commit -am 'Added some feature'`)
4.  Push to the branch (`git push origin my-new-feature`)
5.  Create new Pull Request

Authors
-------

Created and maintained by [Masashi Terui](https://github.com/marcy-terui) (<marcy9114@gmail.com>)

License
-------

MIT License (see [LICENSE](https://github.com/marcy-terui/kflogs/blob/master/LICENSE))
