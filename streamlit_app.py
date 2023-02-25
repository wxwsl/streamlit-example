import ipinfo

access_token = "fd7290568d6d4f"  # 替换成你自己的 access token
handler = ipinfo.getHandler(access_token)

details = handler.getDetails()
latitude = details.latitude
longitude = details.longitude

print("Latitude:", latitude)
print("Longitude:", longitude)
