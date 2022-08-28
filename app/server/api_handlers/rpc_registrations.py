from app.common.rpc.rpc_handlers import RpcHandlers
from app.server.api_handlers import handler_product, handler_selection, handler_square

rpc_handlers = RpcHandlers()

rpc_handlers.register(handler_selection.handle)
rpc_handlers.register(handler_product.handle)
rpc_handlers.register(handler_square.handle)
