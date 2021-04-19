from krpc import connect, Client
from System.Config import KrpcStreamConfig


def get_krpc_client() -> Client:
    return connect(name=KrpcStreamConfig.NAME,
                   address=KrpcStreamConfig.ADDRESS,
                   rpc_port=KrpcStreamConfig.RPC_PORT,
                   stream_port=KrpcStreamConfig.STREAM_PORT)
