# Run the OFBiz IMAGE
DOCKER_BUILDKIT=1 docker build --tag ofbiz-docker .
# Run the OFBiz container
docker run -it -p 8443:8443 ofbiz-docker


