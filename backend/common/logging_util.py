import json
import logging


def log_event(event_name, log_data, logging_module='django_default', level='INFO'):
    logger = logging.getLogger(logging_module)
    try:
        msg = {"ev": event_name, "data": log_data}
        logger.log(msg=json.dumps(msg), level=getattr(logging, level))
    except Exception as e:
        print('ERROR')
        return
