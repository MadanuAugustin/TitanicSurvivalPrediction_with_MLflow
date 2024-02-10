
import logging
import os
import sys



log_dir = 'logs'

log_filepath = os.path.join(log_dir, 'events_tracked')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO,
                     format='[%(asctime)s : %(levelname)s : %(module)s : %(message)s]',
                     
                     handlers=[
                        #  filehandler manages and saves all the logs
                         logging.FileHandler(log_filepath),
                        #  streamhandler prints the log in the terminal
                         logging.StreamHandler(sys.stdout)
                     ])


logger = logging.getLogger('TitanicSurvivalPrediction_with_MLflow')