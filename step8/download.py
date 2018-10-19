import urllib.request
from datetime import datetime, timedelta
import concurrent.futures
import click

_DOWNLOAD_URL_PREFIX = ""


def _get_begining_of_this_week():
  dt = datetime.today()
  begining_of_this_week = dt - timedelta(days=dt.weekday())
  return begining_of_this_week

def _download(year, week, i):
  download_url = "/".join((_DOWNLOAD_URL_PREFIX, str(year), week, str(i) + ".mp3"))
  print(download_url)
  begining_of_this_week = _get_begining_of_this_week()
  urllib.request.urlretrieve(download_url, (begining_of_this_week  + timedelta(days=(i + 2))).strftime("%Y%m%d.mp3"))

@click.command()
@click.option("--year", default=2018)
@click.option("--week", default="oct_week4")
def _run(year, week):
  with concurrent.futures.ThreadPoolExecutor(max_workers=4, thread_name_prefix="thread") as executor:
    for i in range(1, 8):
      executor.submit(_download, year, week, i)


if __name__ == '__main__':
  _run()
