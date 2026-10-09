# Practical 5 — Docker Image and Container Commands

These commands assume your application files (`Dockerfile`, `package.json`, `server.js`, and `.dockerignore`) are already in the same directory.

> Run the commands in the Google Cloud VM's SSH terminal, from the directory containing the `Dockerfile`. Commands use `sudo docker`, so you do not need to configure Docker group permissions.

## 1. Go to the application directory

If you are already in the directory containing your Dockerfile, skip this step. Otherwise, replace the path with your actual directory:

```bash
cd ~/cloudnative-docker-practical
ls -la
```

Confirm that `Dockerfile`, `package.json`, and `server.js` are present.

## 2. Build the Docker image

```bash
sudo docker build -t cloudnative-practical-5:1.0 .
```

The final `.` means Docker should use the current directory as the build context.

## 3. Verify the image

```bash
sudo docker images
sudo docker image inspect cloudnative-practical-5:1.0
```

## 4. Run the container

First, check whether a container with this name already exists:

```bash
sudo docker ps -a
```

If `cloudnative-app` already exists and you want to replace it for this practical, remove it:

```bash
sudo docker rm -f cloudnative-app
```

If Docker says there is no such container, continue; that is fine.

Start the application in the background:

```bash
sudo docker run -d --name cloudnative-app -p 8080:3000 cloudnative-practical-5:1.0
```

Port mapping `8080:3000` maps host port `8080` to the application's container port `3000`.

## 5. Verify that the container is running and the app responds

```bash
sudo docker ps
sudo docker logs cloudnative-app
curl http://localhost:8080
```

Expected response:

```text
Hello from Cloud Native Docker Practical 5
```

If `curl` is not installed, install it on the VM with `sudo apt update && sudo apt install -y curl`, or test from a browser on the VM if available.

## 6. Inspect and test the container

```bash
sudo docker exec cloudnative-app node --version
sudo docker inspect cloudnative-app
```

To see all containers, including stopped containers:

```bash
sudo docker ps -a
```

## 7. Stop and remove the container

```bash
sudo docker stop cloudnative-app
sudo docker ps -a
sudo docker rm cloudnative-app
sudo docker ps -a
```

The `docker rm` command removes the stopped container; it does not remove the image.

## 8. (Optional) Tag the image as `latest` and inspect its build history

```bash
sudo docker tag cloudnative-practical-5:1.0 cloudnative-practical-5:latest
sudo docker images
sudo docker history cloudnative-practical-5:1.0
```

Both tags refer to the same image content. If you created the optional `latest` tag, remove that tag before removing version `1.0`.

## 9. Delete the Docker image

Make sure no container is using the image. Then remove the optional `latest` tag if you created it, followed by the versioned image:

```bash
sudo docker rmi cloudnative-practical-5:latest
sudo docker rmi cloudnative-practical-5:1.0
```

If you did not create the `latest` tag, skip the first command.

Verify that the image is gone:

```bash
sudo docker images
sudo docker system df
```

## Troubleshooting

### Container name is already in use

A container with that name exists, even if it is stopped. Inspect it:

```bash
sudo docker ps -a
```

If you no longer need it, remove it and rerun the `docker run` command:

```bash
sudo docker rm -f cloudnative-app
sudo docker run -d --name cloudnative-app -p 8080:3000 cloudnative-practical-5:1.0
```

### Port 8080 is already in use

Check the current containers and their port mappings:

```bash
sudo docker ps
```

If another application/container is using port `8080`, stop that service/container if appropriate, or change the host side of the mapping. For example, `-p 8081:3000` maps host port `8081` to container port `3000`; then test with `curl http://localhost:8081`.

### Image cannot be deleted

Docker will not remove an image while a container still references it. Check all containers:

```bash
sudo docker ps -a
```

Remove the relevant container, then retry the image-removal command:

```bash
sudo docker rm -f cloudnative-app
sudo docker rmi cloudnative-practical-5:1.0
```

Only run cleanup commands for containers and images belonging to this practical.
