# simulate a steady number of concurrent users perfomring actions(login, view users, create users)

from locust import HttpUser, between, task
import random 
import string

def random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=6)) + "@example.com"

class LoadTestUser(HttpUser):
    wait_time = between(1,3) # Simulate a user waiting between 1 to 3 seconds between actions
    
    def on_start(self):
        self.login()
        
    def login(self):
        response = self.client.post("/api/login", json={
            "email": "admin@example.com",
            "password": "adminpassword"
        })
        
        self.token = response.json().get("token")
        if self.token:
            self.client.headers.update({"Authorization": f"Bearer {self.token}"})
        else:
            print("Login failed. Response:", response.text)
    
    @task(3)
    def view_users(self):
        self.client.get("/api/users")
        
    @task(1)
    def create_user(self):
        self.client.post("/api/users", json={
            "name": "Load Tester",
            "email": random_email(),
            "role": "user"
        })    
