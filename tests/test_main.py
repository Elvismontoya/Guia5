from app.main import create_app

app = create_app()
client = app.test_client()

def test_index():
    r = client.get("/")
    assert r.status_code == 200
    assert b"Calculadora" in r.data

def test_suma():
    r = client.get("/suma/4/5")
    assert r.status_code == 200
    assert r.get_json()["resultado"] == 9

def test_resta():
    r = client.get("/resta/10/4")
    assert r.status_code == 200
    assert r.get_json()["resultado"] == 6

def test_mul():
    r = client.get("/mul/3/7")
    assert r.status_code == 200
    assert r.get_json()["resultado"] == 21

def test_div():
    r = client.get("/div/20/5")
    assert r.status_code == 200
    assert r.get_json()["resultado"] == 4

def test_div_cero():
    r = client.get("/div/10/0")
    assert r.status_code == 400
    assert "dividir" in r.get_json()["error"]
