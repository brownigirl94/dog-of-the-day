# ~ Fun & fresh doggos ~

## Running the app
Because you totally NEED this app running on your desktop background
Prerequisites: 
- Download Docker and have it running
- Download this repository, leave it in ~/Downloads
Steps:
1. Open Terminal and run these Commands
    cd ~/Downloads/dog-of-the-day
    docker build -t juliaabigaila/doggos .
    docker run -p 8888:5000 --name doggos juliaabigaila/doggos
2. Open your favorite browser and type in this address:
http://localhost:8888/

## Thanks to
- Docker for creating a good starting point of a [tutorial](https://github.com/docker/labs/blob/master/beginner/chapters/webapps.md) (though note if you are following the tutorial you will need to make a few modifications - reach out to me if you have any questions)
- My mom for giving birth to me
- Dogs for keeping me happy
