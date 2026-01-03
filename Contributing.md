# How to Run this APP locally

## Build the Image
```
docker build -t IMAGE_NAME
```

## Run the Docker Image with FLask
```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" IMAGE-NAME sh -c "flask run --host 0.0.0.0"
```

## Or Run the APP by Gunicorn

```
docker run -dp 80:80 -w /app -v "$(pwd):/app" IMAGE-NAME
```