from os import chdir, listdir, makedirs, path
from shutil import copy
from subprocess import check_call
from tempfile import gettempdir

tempdir = gettempdir()

repodir = path.dirname(path.realpath(__file__))

# The directory where the generated files will be copied
targetdir = path.join(repodir, 'edited-files')
makedirs(targetdir, exist_ok=True)

# Copy files from the JIT cache to `targetdir`
jitcachedir = [i for i in listdir(tempdir) if i.startswith('devito-jitcache')]
if len(jitcachedir) != 1:
    # No idea why we should ever end up here, but just in case...
    raise ValueError("Something broken with the Devito JIT-cache directory. "
                     "Please ask one of the lab helpers for instructions on "
                     "how to proceed")
jitcachedir = path.join(tempdir, jitcachedir.pop())
for i in listdir(jitcachedir):
    if i.endswith('.c'):
        targetfile = path.join(jitcachedir, i)
        copy(targetfile, targetdir)
        print("Copied `%s` to `%s`" % (targetfile, targetdir))

# Copy env file
envfile = path.join(repodir, 'env.sh')
if not path.exists(envfile):
    raise ValueError("Cannot find env.sh file. Have you accidentally removed it?")
copy(envfile, targetdir)

# Make sure we are in the root repo directory
chdir(repodir)

# git-add copied files
check_call(['git', 'add', 'edited-files/'])

# git-commit and git-push staged files
check_call(['git', 'commit', '-am', 'Push files edited with JIT-BACKDOOR'])
check_call(['git', 'push'])
