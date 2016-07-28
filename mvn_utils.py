
import os
import urllib
from shutil import copyfile
import hashlib
import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise



def sha1(str):
    sha1 = hashlib.sha1()
    sha1.update(str)
    return sha1.hexdigest()

def serialize(data, id):
    return

def load(data, id):
    return

def normalize_id(id):
    return id.replace('.', '_').replace(':', '__')

cache_counter = 0
cache_miss = 1

mem_cache = {}


def print_stats():
    print '{0} out of {1} HTTP requests done ({2}% cache miss)'.format(
        cache_miss,
        cache_counter,
        str(round(100 * float(cache_miss)/float(cache_counter),2))
    )

def read_remote_file(url, invalidate_cache=False):
    global cache_counter
    global cache_miss

    if url.startswith('local:'):
        return ''

    if not os.path.isdir(os.getcwd() + '/buck-out/'):
        print 'Run script from main dir'
        exit(1)

    cksum = sha1(url)
    if mem_cache.get(cksum):
        return mem_cache.get(cksum)

    cache_counter = cache_counter + 1

    dir = os.environ['HOME'] + '/.bucken/cache/{0}/{1}/'.format(cksum[0:2], cksum[2:4])
    mkdir_p(dir)

    cache = dir + cksum

    if os.path.isfile(cache):
        if invalidate_cache:
            os.remove(file)
            return read_remote_file(url)
        else:
            content = open(cache, 'r').read()
            mem_cache[cksum] = content
            return content

    cache_miss = cache_miss + 1
    rf = urllib.urlopen(url)

    if rf.getcode() == 404:
        lf = open(cache, 'w')
        lf.write('')
        mem_cache[cksum] = ''
        return ''

    content = rf.read()

    lf = open(cache, 'w')
    lf.write(content)
    mem_cache[cksum] = content
    return content
