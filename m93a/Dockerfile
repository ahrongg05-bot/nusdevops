
FROM python:3.11-slim
#FROM chooses the base Docker image.
#Here, it uses:
#Python version 3.11
#slim = a smaller/lightweight Linux image
#So this means: “Start with a small environment that already has Python 3.11 installed.”


WORKDIR /app
#Creates/sets /app as the working directory inside the container.
#After this, Docker commands basically operate from: /app. think of it like cd /app

COPY . .
#Copies files from your current project folder on your computer into the container's current working directory.
# first. . means current folder on your comp
# second . means current folder in the container (which is /app)


CMD ["python", "hello.py"]
#This tells Docker what command to run when the container starts.