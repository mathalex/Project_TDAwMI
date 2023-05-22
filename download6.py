import requests

from itertools import product
from tqdm import tqdm

DOMAIN = "https://natural-scenes-dataset.s3.amazonaws.com"
PRE_DIR = "/nsddata_timeseries/ppdata/"
POST_DIR = "/func1pt8mm/timeseries/"

DATA_DIR = "./raw/timeseries/"

subjects = [7]
sessions = range(1, 37+1)
runs = range(1, 14+1)

def get_url(subject, session, run):
  return DOMAIN + PRE_DIR + "subj0" + str(subject) + POST_DIR + "timeseries_session" + str(session).zfill(2) + "_run" + str(run).zfill(2) + ".nii.gz"

urls = []
for subject, session, run in product(*[subjects, sessions, runs]):
  urls.append(get_url(subject, session, run))

for url in tqdm(urls):
  req = requests.get(url)
  file = url.split("/")[-1]
  subject = url.split("/")[-4][5:]

  with open(DATA_DIR + "subj0" + str(subject) + "/" + file, "wb") as f:
    f.write(req.content)
    f.close()


