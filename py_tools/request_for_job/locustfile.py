import time
import hashlib
from locust import HttpUser, task, between
from json import JSONDecodeError

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    # @task
    def hello_world(self):
        self.client.get("/xxxx")

    @task
    def hello_world(self):
      with self.client.post("/xxx?token=57df18a61cb3d1f8373b9a05696b4254", json={ "id": 0, 
        "hqId": 58, 
        
        "code": "aaaa", 
        "name": "aaaa", 
        "cType": "aaa", 
        "enabled": True, 
        "createdAt":1609459200000, 
        "noPoints": False}, catch_response=True) as response:
        try:
            print(response.json())
        except JSONDecodeError:
            response.failure("Response could not be decoded as JSON")
        except KeyError:
            response.failure("Response did not contain expected key 'greeting'")
      
