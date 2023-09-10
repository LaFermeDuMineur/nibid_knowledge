import logging
import subprocess
import time
import os

import requests  # Thoses packages need to be installed
import yaml
import colorlog
import click

# Logging part
DEFAULT = 1
INFO = 2
SUCCESS = 3
ABORTED = 4
WARNING = 5
FAILED = 6
logging.addLevelName(DEFAULT, 'INFO')
logging.addLevelName(INFO, 'INFO')
logging.addLevelName(SUCCESS, 'SUCCESS')
logging.addLevelName(ABORTED, 'ABORTED')
logging.addLevelName(WARNING, 'WARNING')
logging.addLevelName(FAILED, 'FAILED')
color_mapping = {
    "DEFAULT": 'grey',
    "INFO": 'cyan',
    'SUCCESS': 'green',
    "ABORTED": 'yellow',
    "WARNING": 'purple',
    "FAILED": 'red'
}
log_pattern = "%(asctime)s %(log_color)s%(levelname)s%(reset)s | %(name)s | %(log_color)s%(message)s"
formatter = colorlog.ColoredFormatter(log_pattern, log_colors=color_mapping)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger = logging.getLogger('gen_wallet')
logger.addHandler(handler)
logger.setLevel(DEFAULT)

#  CONFIG PART
wallet_password = os.getenv('NIBIRU_ADDR_PASSWORD')  # put your password prompt

def fire_cmd(name):
    args = 'nibiru keys add {} -y'.format(name)
    logger.log(INFO, 'Gonna play {}'.format(args))
    process = subprocess.Popen([args],
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               universal_newlines=True,
                               shell=True)
    if wallet_password != '':
        process.communicate(wallet_password)

@click.command()
@click.option('--wallet_base_name', '-w', type=str, help='wallet base name prefix')
@click.option('--number', '-n', type=str, help='number of walelt to generate as suffix')
def loop_wallet(wallet_base_name, number):
    for i in range(number):
        fire_cmd(wallet['name'])
        


if __name__ == '__main__':
    loop_wallet()
