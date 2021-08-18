import logging

from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info('Inside handler...')
    logger.info('Handler complete at {}'.format(str(datetime.now())))

    
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