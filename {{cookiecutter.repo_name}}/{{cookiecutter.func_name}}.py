import os
import logging

from datetime import datetime
from urllib.request import urlopen

logger = logging.getLogger()
logger.setLevel(logging.INFO)

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable


def validate(res):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    return EXPECTED in res


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        if not validate(urlopen(SITE).read()):
            raise Exception('Validation failed')
    except:
        logger.error('Check failed!')
        raise
    else:
        logger.info('Check passed!')
        return event['time']
    finally:
        logger.info('Check complete at {}'.format(str(datetime.now())))

    
# If being called locally, call the handler
if __name__ == '__main__':
    import os
    import json
    import sys 

    logging.basicConfig()
    event = {}
    context = {}

    # TODO if argv[1], read contents, parse into json
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            data = f.read()
        event = json.loads(data)

    result = lambda_handler(event, context)
    output = json.dumps(
        result,
        sort_keys=True,
        indent=4,
        separators=(',', ':')
    )
    logger.info(output)