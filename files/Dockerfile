FROM python:3-alpine

# Sets the default value for LOOP_TIME if undefined
ENV LOOP_TIME=15

# Create a non-privileged user
RUN adduser -D -u 10001 nonrootuser

# Install the dependencies
RUN pip install requests

# Set the working directory and change the owner to the unprivileged user
WORKDIR /app
RUN chown nonrootuser /app

# Download the main script or use the local copy
#RUN wget https://raw.githubusercontent.com/lazaroblanc/IONOS-DynDNS/main/ionos_dyndns.py && chmod +rxxx ionos_dyndns.py
COPY original-repo/ionos_dyndns.py ./
RUN chmod +x ionos_dyndns.py

# Only in case of not using "docker-compose"
# COPY config.py /app/config.py

# Copy "entrypoint.py" and give execute permissions to the script
COPY files/entrypoint.py ./
RUN chmod +x entrypoint.py

# Use the non-root user
USER nonrootuser

# Specify the Python interpreter in the ENTRYPOINT, without "-u" buffer so that prints appear in the container log
ENTRYPOINT ["python", "-u", "/app/entrypoint.py"]