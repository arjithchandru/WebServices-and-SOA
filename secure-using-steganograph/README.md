# Intro

This project basically takes text input and embed it into a PNG image, and retrieve the text from the image. The text encoding into the image is lossless. Try this fun project [here](https://xelsteg.herokuapp.com), check out in youtube- [video tutorial](https://youtu.be/K04xY1empOA). This project is the web version of this project- [
Simple-Image-steganography-System](https://github.com/shafinhasnat/Simple-Image-steganography-System.git) (Under active development)


## Installation
First install docker in your system

Then run the command below.

```bash
docker pull shafinhasnat/steganography-webapp:first-commit
```

## Usage
This webapp will run on port 8080 of your docker container. Run the command below. 
```bash
docker run -d -p 5000:8080 shafinhasnat/steganography-webapp:first-commit
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
