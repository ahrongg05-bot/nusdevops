build_version = 42

environment = "staging"

servers = ["web01", "web02", "db01"]

deployments = {
    "dev": "v1.2.3",
    "staging": "v1.3.0",
    "production": "v2.0.1"
}

for server in servers:
    print(f"Deploying to {server} with version {deployments[environment]}")
## servers is the web
# deployment is the "DEV/STAGING/PRODUCTION" then envrionment is ASSIGNMENT

#set up .venv
# open new terminal
# check that is the named file " .venv" is created
# check version use python ---version