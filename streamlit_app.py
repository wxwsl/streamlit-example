from flask import request

client_ip = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')
print("Client IP Address:", client_ip)
