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

- Add the neccessary environment variables in a `.env` in the root directory:
  ```bash
  MONGO_URI=mongodb://localhost:27017/db
  ```
- Execute the project by running: 
  - **Note:** keep in mind that after installing new dependencies and adding them in the `requirements.txt` you'll have to run `docker-compose up --build`.

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

  ### environment variables
  - `MONGO_URI`: URI of the database could be hosted online or local
  