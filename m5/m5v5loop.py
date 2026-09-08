servers = ["web01", "web02", "db01", "cache01"]

health_status = {
    "web01": "ok",
    "web02": "fail",
    "db01": "ok",
    "cache01": "fail"
}

for server in servers:
    status = health_status[server]
    if status == "ok":
        print(f"{server} is healthy.")
    else:
        print(f"{server} failed health check")