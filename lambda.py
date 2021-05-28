import base64
import ast

import boto3
import uuid
import time
import random
import json


def lambda_handler(event, context):
    ending = base64.b64encode(bytes('/n', 'utf-8'))
    for r in range(len(event['records'])):
        data = event['records'][r]["data"]
        data_string = base64.b64decode(data.encode("ascii")).decode("ascii") + '\n'
        event['records'][r]["data"] = base64.b64encode(data_string.encode("ascii")).decode("ascii")

    return {'records': event['records']}
