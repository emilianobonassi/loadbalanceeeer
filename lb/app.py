from flask import Flask, request
from flask_cors import CORS
from requests import post
import os
import random
import logging

logging.basicConfig(level=logging.INFO)

api = Flask(__name__)
CORS(api)

rpcs = os.environ['RPCS'].split(',')
api.logger.info('RPCs: %s', rpcs)

proxies = {}
if "PROXY" in os.environ:
  proxies['http'] = os.environ['PROXY']
  proxies['https'] = os.environ['PROXY']

api.logger.info('Proxies: %s', proxies)

@api.route('/', methods=['POST'])
def proxy():
  random_rpc = random.choice(rpcs)
  api.logger.info('Used RPC: ' + random_rpc)
  proxy_req = post(random_rpc, json=request.json, proxies=proxies)
  print(proxy_req.text)
  return proxy_req.json()

if __name__ == '__main__':
    api.run()