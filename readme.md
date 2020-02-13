# explicit-detector

Detects whether an image is SFW or NSFW using machine learning models.

An easy to use docker-compose package which combines tensorflow 1.15.2 (python3) and the bedapudi6788/NudeNet github package
to classify a sample image in the repo, without having to go through the pain of installing dependencies.

### How to use

* Be on a Ubuntu 18.04 machine with docker and docker-compose installed
* `git clone https://github.com/barezina/explicit-detector`
* `docker-compose up --build -d` (you should see a detection at the end of the build process)
* `docker ps` to show running containers, note the running container for the detector
* `docker exec -it 0a1 bash` (where `0a1` is the container ID)
* You should land in `/nsfw`. 
* To run the classify job, run `python3 classify.py`
* To run on your own images, place the images in the cloned folder (where you checked out this repo) on your host machine, then look inside the container at `/nsfw` which is mapped verbatim. Adjust classify.py and run the script and you are racing! 
