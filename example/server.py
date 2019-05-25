from sanic import Sanic
from jaeger_client import Config
from sanic_opentracing import tracing

JAEGER_HOST = "localhost"

app = Sanic(__name__)

config = Config(config={'sampler': {'type': 'const', 'param': 1},
                        'logging': True,
                        'local_agent': {'reporting_host': JAEGER_HOST}},
                service_name="jaeger_opentracing_example")
jaeger_tracer = config.initialize_tracer()


@app.route("/ep1")
async def ep1(request):
    return "ep1"


@app.route("/ep2")
async def ep2(request):
    return "ep2"


_tracing = tracing.SanicOpenTracer(tracer=jaeger_tracer, trace_all_requests=True, app=app)


@app.route('/log')
@_tracing.trace()
def log(request):
    # Extract the span information for request object.
    with jaeger_tracer.start_active_span(
            'python webserver internal span of log method') as scope:
        a = 1
        b = 2
        c = a + b
        scope.span.log_kv({'event': 'my computer knows math!', 'result': c})
        return "log"


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
