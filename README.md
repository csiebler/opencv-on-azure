# Dockerized OpenCV for batch processing video content on Azure

This Docker image copies a video file from an Azure Blob container, executes `OpenCV` via `opencv.py` on the video, and writes the generate results to another Azure Blob container.

Build container locally:

```
docker build . --tag opencv-count-frames:v0
```

Push to Azure Container Registry:

```
docker tag opencv-count-frames:v0 myazurecontainerregistry.azurecr.io/opencv-count-frames:v0
docker push myazurecontainerregistry.azurecr.io/opencv-count-frames
```

Required environment variables during execution:

```
# Storage Account details
ACCOUNT_NAME=
SAS_TOKEN=

# Download container and filename for video
DOWNLOAD_CONTAINER_NAME=
DOWNLOAD_FILE_NAME=

# Upload container and filename for results
UPLOAD_CONTAINER_NAME=
UPLOAD_FILE_NAME=
```

Or directly run via CLI:

```
docker run --rm \
  --env ACCOUNT_NAME='accountname' \
  --env SAS_TOKEN='sv=2017-11-09&........' \
  --env DOWNLOAD_CONTAINER_NAME='videos' \
  --env DOWNLOAD_FILE_NAME='test.mp4' \
  --env UPLOAD_CONTAINER_NAME='results' \
  --env UPLOAD_FILE_NAME='test.csv' \
  <image_name>
```