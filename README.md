Insert data from csv file, and count ram usage,time spent and writing speed(r/s).

# Pull repozitory and run command`

docker build .

# Run docker container with limited ram.For example`

docker run -i -t --memory="8g" {image_id or image_name}

After run in container python file.

python3 insert_db.py
