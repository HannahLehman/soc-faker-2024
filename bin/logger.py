import logging
from socfaker import SocFaker as sc
import subprocess

# Set up logging
logging.basicConfig(filename='soclogger.log',format='%(asctime)s %(message)s', level=logging.INFO)

def generate_log():
    # Execute the flog command to generate a log
    log = subprocess.run('flog -s 10s -n 200', shell=True, capture_output=True, text=True)

    return log

# Main part of the script
if __name__ == "__main__":
    try:
        while True:
            log = generate_log()
            logging.info(log)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

