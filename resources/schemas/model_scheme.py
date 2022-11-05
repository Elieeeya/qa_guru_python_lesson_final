from pytest_voluptuous import S

create_item = S({
    'method': str,
    'result': {
        'color': str,
        'description': str,
        'id': str,
        'name': str,
        'params': str,
        'price': int,
        'section': str
    },
    'status': str

})

get_item = S({
    'method': str,
    'result': {
        "id": str,
        "name": str,
        "section": str,
        "description": str,
        "color": str,
        "size": str,
        "price": int,
        "params": str,
        "photo": str
    },
    'status': str

})

update_item = S({
    'method': str,
    'result': str,
    'status': str

})


info_bd = S({
    'method': str,
    'result': [{'_lng': None,
                'action': None,
                'category': str,
                'colors': None,
                'description': str,
                'enable': str,
                'image': None,
                'last_id': str,
                'params': str,
                'photos': None,
                'price': str,
                'sizes': None,
                'sort': None,
                'title': str
                }],
    'status': 'ok'
})


delete_item = S({
    'method': str,
    'result': str,
    'status': str

})
