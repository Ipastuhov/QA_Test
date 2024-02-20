import pytest
import requests

base_url = "https://test-vehicle.froza.ru:7879/froza_msc_test-vehicle/hs/partsticker/info"
id_partsticker1 = "9999745/2"
id_partsticker2 = "91111111111111111/2"
authorization_token = "0J/QsNGB0YLRg9GF0L7QsiDQmNCy0LDQvTpVUEBCMTlCZQ=="

# Информация по валидному партстикеру 
def test_first_url():
    url = f"{base_url}?id_partsticker={id_partsticker1}"
    payload = {}
    headers = {'Authorization': f'Basic {authorization_token}'}

    response = requests.get(url, headers=headers, data=payload)
    assert response.json()["status"] == "ok"
    assert response.status_code == 200
    print(response.text)

# Информация по неневалидному партстикеру 
def test_second_url():
    url = f"{base_url}?id_partsticker={id_partsticker2}"
    payload = {}
    headers = {'Authorization': f'Basic {authorization_token}'}

    response = requests.get(url, headers=headers, data=payload)
    assert response.status_code == 404
    assert response.json()["status"] == "error"
    assert response.json()["message"] == f"Отсутствует информация по парстикеру {id_partsticker2}"

    print(response.text)

if __name__ == "__main__":
    test_first_url()
    test_second_url()
