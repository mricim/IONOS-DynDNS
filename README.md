# IONOS DynDNS Dockerized

This project offers a Dockerized solution for dynamic DNS updates using the IONOS DNS API, now with enhanced security through non-root execution.

## Getting Started

These instructions will help you set up and run the IONOS-DynDNS container.

### Prerequisites

Ensure either of the following is installed on your system:

- [Docker Compose](https://www.docker.com/compose/) installed on your system.
- [Docker](https://www.docker.com/) installed on your system.

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/mricim/IONOS-DynDNS
   cd IONOS-DynDNS
   ```

2. Edit the `docker-compose.yml` file and adjust the `LOOP_TIME` environment variable.
Setting it to 0 will disable the loop.

3. Configure your domains and subdomains in the `config.py` file. Maintain the format:

    ```python
    SERVICES = [
        ["A", ["www.host1.com","host1.com", "subdomain.host2.com"], "API_PREFIX_1", "API_SECRET_1"],
        ["AAAA", ["host3.com"], "API_PREFIX_2", "API_SECRET_2"],
    ]
    ```

4. Build and start the Docker container:

    ```bash
    docker-compose up --build
    ```

## Without Docker Compose

You can use this without Docker Compose, only with Docker.
1. Uncomment the line `COPY config.py /app/config.py` in the `Dockerfile`
2. Now you can use `docker run .`. If you don't want it to loop, change `ENV LOOP_TIME=15` to `ENV LOOP_TIME=0`

## Notes

This repository is designed to allow you to edit the `config.py` file on the fly, and the changes will be reflected in the next iteration.
However, you can remove this option if desired. Just delete `volumes:` from the `docker-compose.yml` file and uncomment the line `COPY config.py /app/config.py` in the `Dockerfile`.

### Note for Non-Root User Execution:
The Dockerfile has been updated to execute the container with a **non-root** user (`nonrootuser`). This enhances security by reducing the container's privileges. Ensure that the user running the container has the necessary permissions, and the Docker socket permissions have been appropriately configured.


# Acknowledgments

Gratitude to [Lázaro Blanc](https://github.com/lazaroblanc) for his original contribution to the project. Our work is built upon the foundation of his [IONOS-DynDNS](https://github.com/lazaroblanc/IONOS-DynDNS) repository, and we appreciate his dedication and effort.

<div align="center">
<hr>
<table>
<tr>
<td colspan=2>
<h2>🐛 Bug reports & Feature requests 🆕</h2>
If you've found a bug or want to request a new feature please <a href="https://github.com/mricim/IONOS-DynDNS/issues/new">open a new <b>Issue</b></a>
<br><br>
</td>
</tr>
<tr>
<td>
<h2>🤝 Contributing</h2>
✅ Pull requests are welcome!
<br><br>
</td>
<td>
<h2>📃 License</h2>
Published under the <b>Apache License 2.0</b><br>
Please see the <a href="./LICENSE"><b>License</b></a> for details
<br><br>
</td>
</tr>
</table>
</div>