import requests

def test_get_user():
    res = requests.get("https://fakestoreapi.com/products")
    print(res)
    assert res.status_code == 200