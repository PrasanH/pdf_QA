# Create docker image file

# use the python official image, ver 3.10 from Docker Hub
FROM python:3.10.16-bullseye

# Set the working dir ( inside the container)
WORKDIR /app

# Copy the project folder and other necessary files/folders into the container at /app
COPY requirements.txt /app
COPY project /app


# Install any needed packages in requirements.txt
# no-cache-dir : reduces image size by preventing cache 
RUN pip install --no-cache-dir -r requirements.txt



#Expose the port, 8501 is the default port for streamlit
EXPOSE 8501

#Run home.py when the container launches
CMD [ "streamlit", "run", "Home.py" ]


# create a .dockerignore and add files like .env, .trunk etc

# run--->  docker build -t image_name .  (including the dot. dot . tells Docker to use the current directory as the context. )
# Note!!!! Without dot, you get error:  'docker buildx build' requires 1 argument

# then -->  docker run -it -p 99:8501 chat_jarvis  (select any port like 99 for PORT MAPPING)

# docker run -it --env-file path-to/.env -p 99:8501 chat_jarvis 
# docker run -it --env-file project/.env -p 99:8501 chat_jarvis 