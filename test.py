import logging
import kflogs

logger = logging.getLogger('test')
h = kflogs.KinesisFirehoseHandler(stream_name='test-kf', region_name='us-west-2')
h.setLevel(logging.DEBUG)
h.setFormatter(kflogs.SimpleJsonFormatter())
logger.addHandler(h)

logger.warning('test')
