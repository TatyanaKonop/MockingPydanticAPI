def get_object(client, param):
    return client.get(param)

def post_object(client, param, **kwargs):
    return client.post(param, **kwargs)


# def put_object(client, **kwargs):
#     ROUTE_METHOD = 'update'
#     return client.put(routes.Routes.OBJECT_PUT.format(ROUTE_METHOD), **kwargs)
#
#
# def delete_object(client, **kwargs):
#     ROUTE_METHOD = 'delete'
#
#     return client.request(
#         method="DELETE",
#         url=routes.Routes.OBJECT_DELETE.format(ROUTE_METHOD),
#         **kwargs
#     )
