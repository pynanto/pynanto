from d3.common.rpc.rpc_handlers import RpcHandlers
from d3.server.api_handlers import handler_selection, handler_product

rpc_handlers = RpcHandlers()

rpc_handlers.register(handler_selection.handle)
rpc_handlers.register(handler_product.handle)
