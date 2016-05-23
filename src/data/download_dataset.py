import os
import zipfile
import logging

from six.moves.urllib.request import urlretrieve

last_percent_reported = None
def download_progress_hook(count, blockSize, totalSize):
    """A hook to report the progress of a downloads. This is mostly intended for users with
    slow internet connections. Reports every 1% change in downloads progress.
    """
    global last_percent_reported
    percent = int(count * blockSize * 100 / totalSize)

    if last_percent_reported != percent:
        if percent % 5 == 0:
            logging.info("%s%%" % percent)
        last_percent_reported = percent


def maybe_download(url, filename, dir, expected_bytes=None, force=False):
    """Download a file if not present, and make sure it's the right size."""

    fullfilename = os.path.join(dir, filename)
    if force or not os.path.exists(fullfilename):
        logging.info('Attempting to download %s' % filename)
        filename, _ = urlretrieve(url + filename, fullfilename, reporthook=download_progress_hook)
        logging.info('Download Complete!')

    statinfo = os.stat(fullfilename)
    if statinfo.st_size == expected_bytes or expected_bytes is None:
        logging.info('Found and verified %s' % filename)
    else:
        raise Exception(
            'Failed to verify ' + filename + '. Can you get to it with a browser?')
    return fullfilename


def maybe_extract(fullfilename, dir, force=False):
    """Unzip a file in dir if not present."""

    filename = os.path.basename(fullfilename)
    targetfilename, file_extension = os.path.splitext(filename) # remove extension from filename
    targetfullfilename = os.path.join(dir, targetfilename)
    if os.path.isfile(targetfullfilename) and not force:
        # You may override by setting force=True.
        logging.info('%s already present - Skipping extraction of %s.' % (targetfilename, fullfilename))
    else:
        logging.info('Extracting data for %s. Please wait.' % fullfilename)
        with zipfile.ZipFile(fullfilename) as zf:
            zf.extractall(dir)
    return targetfullfilename

logging.basicConfig(level=logging.INFO)

train_filename = maybe_download('https://dl.dropboxusercontent.com/u/27773716/', 'train.csv.zip', '../../data/downloads', 571133917)
test_filename = maybe_download('https://dl.dropboxusercontent.com/u/27773716/', 'test.csv.zip', '../../data/downloads', 116454883)

train_folders = maybe_extract(train_filename, '../../data/raw')
test_folders = maybe_extract(test_filename, '../../data/raw')
