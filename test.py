# Андрей Лисов, 16-я когорта — Финальный проект. Инженер по тестированию плюс

import funct
import data

def test_get_order_track():
    track = funct.create_order(data.order).json()["track"]
    response = funct.get_order_track(track)
    assert response.status_code == 200
