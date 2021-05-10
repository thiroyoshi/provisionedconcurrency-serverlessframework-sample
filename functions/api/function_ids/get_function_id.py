#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json


def lambda_handler(event, context):

    body = {"function_id": os.getenv('FANCTION_ID')}

    return {
        "statusCode": 200,
        "body": json.dumps(body, ensure_ascii=False)
    }