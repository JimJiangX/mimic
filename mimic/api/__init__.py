# vim: tabstop=4 shiftwidth=4 softtabstop=4

from oslo.config import cfg


API_SERVICE_OPTS = [
    cfg.StrOpt('mimic_api_bind_ip',
               default='0.0.0.0',
               help='IP for the Ironic API server to bind to',
               ),
    cfg.IntOpt('mimic_api_port',
               default=8080,
               help='The port for the Ironic API server',
               ),
]

CONF = cfg.CONF
CONF.register_opts(API_SERVICE_OPTS)
