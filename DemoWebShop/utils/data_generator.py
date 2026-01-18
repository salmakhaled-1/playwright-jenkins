import uuid
import time

def generate_email():
    return f"user_{int(time.time())}_{uuid.uuid4().hex[:6]}@testmail.com"

def generate_password():
    return f"Pass@{uuid.uuid4().hex[:8]}"

def generate_name():
    return f"User{uuid.uuid4().hex[:5]}"