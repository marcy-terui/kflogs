import os
import time
import kflogs

os.system("python setup.py install")

os.system("pandoc README.md --from=markdown --to=rst > README.txt")
os.system("python setup.py sdist upload")
os.remove('README.txt')

time.sleep(60)

os.system("git tag v{}".format(kflogs.__version__))
os.system("git push origin v{}".format(kflogs.__version__))
