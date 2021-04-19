import os

import yaml

with open(os.path.abspath("System\\config.yaml")) as config_file:
    config = yaml.safe_load(config_file)
    logging = config["logging"]
    krpc_stream = config["krpc_stream"]
    vessel = config["vessel"]


class Dirs:
    HOME: str = os.path.abspath(".")
    LOGS: str = os.path.abspath(logging["dir"])


class KrpcStreamConfig:
    NAME: str = krpc_stream["name"]
    ADDRESS: str = f'{krpc_stream["address"]}'
    RPC_PORT: int = krpc_stream["rpc_port"]
    STREAM_PORT: int = krpc_stream["stream_port"]


class LoggingConfig:
    LEVEL: str = logging["level"]
    DIR: str = os.path.abspath(logging["dir"])

    class TELEMETRY:
        NAME: str = logging["telemetry"]["name"]
        FILENAME: str = logging["telemetry"]["filename"]
        FORMATTER: str = logging["telemetry"]["formatter"]

    class SYSTEM:
        NAME: str = logging["system"]["name"]
        FILENAME: str = logging["system"]["filename"]
        FORMATTER: str = logging["system"]["formatter"]


class VesselConfig:
    NAME: str = vessel["name"]
    FILEPATH: str = str(os.path.abspath(vessel["filepath"]))
