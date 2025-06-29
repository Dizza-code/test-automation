# performance_tests/stress_test.py

from locust import HttpUser, constant, task
import string, random

class StressTestUser(HttpUser):
    wait_time = constant(0.5)

    def on_start(self):
        response = self.client.post("/api/login", json={
            "email": "admin@example.com",
            "password": "adminpassword"
        })
        self.token = response.json().get("token")
        self.client.headers.update({"Authorization": f"Bearer {self.token}"})

    @task
    def heavy_create_users(self):
        self.client.post("/api/users", json={
            "name": "Stress User",
            "email": ''.join(random.choices(string.ascii_lowercase, k=8)) + "@test.com",
            "role": "user"
        })
