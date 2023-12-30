import os
import time
import subprocess

print(f"LOOP_TIME declared with: {os.environ.get('LOOP_TIME')}")

# Calculate LOOP_TIME in seconds
loop_time_minutes = int(os.environ.get("LOOP_TIME", 15))

# Set LOOP_TIME if negative
loop_time_minutes = abs(loop_time_minutes)

loop_time_seconds = loop_time_minutes * 60


def execute_command():
    from config import SERVICES

    for service in SERVICES:
        TYPE_RECORD = service[0]
        hosts = service[1]
        API_PREFIX = service[2]
        API_SECRET = service[3]

        for host in hosts:
            print(f"Run with TYPE_RECORD={TYPE_RECORD}, HOST={host}, API_PREFIX={API_PREFIX}, API_SECRET={API_SECRET}")
            subprocess.run(["python", "/app/ionos_dyndns.py", "--" + TYPE_RECORD , "-H", host, "--api-prefix", API_PREFIX, "--api-secret", API_SECRET])


def main():

    # Ejecutar el script una vez si LOOP_TIME es 0
    if loop_time_minutes == 0:
        print("NO LOOP")
        execute_command()
    else:
        # Ejecutar el script continuamente si LOOP_TIME es positivo
        while True:
            execute_command()
            print("LOOP in: " + str(loop_time_minutes) + " minutes")
            # Esperar antes de volver a ejecutar
            time.sleep(loop_time_seconds)

if __name__ == "__main__":
    main()