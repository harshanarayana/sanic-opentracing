import requests
import time
from opentracing_instrumentation.client_hooks import install_all_patches
from jaeger_client import Config

JAEGER_HOST = "localhost"
WEBSERVER_HOST = "localhost"

config = Config(config={'sampler': {'type': 'const', 'param': 1},
                        'logging': True,
                        'local_agent': {'reporting_host': JAEGER_HOST}},
                service_name="jaeger_opentracing_example")
tracer = config.initialize_tracer()

install_all_patches()

url = "http://{}:5000/log".format(WEBSERVER_HOST)
requests.get(url)

url = f'http://{WEBSERVER_HOST}:5000/ep1'
requests.get(url)

url = f'http://{WEBSERVER_HOST}:5000/ep2'
requests.get(url)

# allow tracer to flush the spans - https://github.com/jaegertracing/jaeger-client-python/issues/50
time.sleep(2)
tracer.close()
