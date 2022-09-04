test_json_positive_post = (
    ({"id": 10,"name": "doggie","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, {'id': 10,'category': {'id': 1,'name': 'Dogs'},'name': 'doggie','photoUrls': ['string'],'tags': [{'id': 0,'name': 'string'}],'status': 'available'}),
    ({"id": 11,"name": "doggie2","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, {'id': 11,'category': {'id': 1,'name': 'Dogs'},'name': 'doggie2','photoUrls': ['string'],'tags': [{'id': 0,'name': 'string'}],'status': 'available'})
)
test_json_negative_post = (
    ({"name": "doggie","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, 500),
    ({"name": "doggie2","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, 500)
)
test_json_positive_put = (
    ({"id": 10,"name": "doggie2","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, {"id": 10,"category": {"id": 1,"name": "Dogs"},"name": "doggie2","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}),
    ({"id": 11,"name": "doggie4","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, {"id": 11,"category": {"id": 1,"name": "Dogs"},"name": "doggie4","photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"})
)
test_json_negative_put = (
    ({"name": "doggie2","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, 500),
    ({"name": "doggie4","category": {"id": 1,"name": "Dogs"},"photoUrls": ["string"],"tags": [{"id": 0,"name": "string"}],"status": "available"}, 500)
)
test_json_positive_get = (('available', 200), ('pending', 200), ('sold', 200))
test_json_negative_get = (('avilable', 400), ('', 400))
