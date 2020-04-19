# CORD19-Search-Engine

ISC-446 final project

### Project Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

## How to execute the project

- Clone this repository by running:

  ```bash
  git clone https://github.com/lyriad/CORD19-Search-Engine.git
  ```

- Execute the project by running: 
  - **Note:** keep in mind that after installing new dependencies and adding them in the `requirements.txt` you'll have to run this command once again.

  ```bash
  docker-compose up
  ```

  **Note:** To run it as a daemon

  ```bash
  docker-compose up -d
  ```

  The server will be up and running in port [5000](http://0.0.0.0:8080).

- Once you are done with the project run

  ```bash
  docker-compose down
  ```