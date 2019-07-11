import subprocess
import os
import sys

# What is the site name?
if len(sys.argv) < 2:
    print("What is the site name?")
    sys.exit()
sitename = sys.argv[1]

# Remove contents of remote source directory
subprocess.call(
 "ssh alex@{} 'rm -r ~/{}/source/* >& /dev/null'".format(sitename, sitename), shell=True
)

# What files are being tracked by git?
tracked_files = subprocess.check_output("git ls-files", shell=True).decode()
tracked_files = list(filter(bool, tracked_files.split("\n")))

# Push source code to remote
for file_ in tracked_files:
    directory = "/".join(file_.split("/")[:-1])
    subprocess.call(
     "ssh alex@{} 'mkdir -p ~/{}/source/{}'".format(sitename, sitename, directory), shell=True
    )
    subprocess.call(
     "scp -r ./{} alex@{}:~/{}/source/{}".format(file_, sitename, sitename, file_), shell=True
    )

# Turn off Debug
subprocess.call(
 "ssh alex@{} 'sed -i s/\"DEBUG = True\"/\"DEBUG = False\"/g ~/{}/source/core/settings.py'".format(sitename, sitename),
 shell=True
)

# Add allowed hosts
subprocess.call(
 "ssh alex@{} 'sed -i s/\"ALLOWED_HOSTS = \[\]\"/\"ALLOWED_HOSTS = \[£'{}£', £'www.{}£'\]\"/g ~/{}/source/core/settings.py'".format(sitename, sitename, sitename, sitename),
 shell=True
)
subprocess.call(
 "ssh alex@{} 'sed -i s/£/\\\"/g ~/{}/source/core/settings.py'".format(sitename, sitename),
 shell=True
)

# Add google analytics
# if sitename == "harston.io":
#     subprocess.call(
#      "ssh {} 'sed -i s/\"<!--analytics-->\"/\"\{{% include \\\"analytics.html\\\" %\}}\"/g ~/{}/source/blog/templates/base.html'".format(sitename, sitename),
#      shell=True
#     )

# Upload the secret settings
subprocess.call(
 "scp -r ./core/secrets.py alex@{}:~/{}/source/core/secrets.py".format(sitename, sitename), shell=True
)

# Switch to postgres database remotely

subprocess.call(
    "ssh alex@{} 'sed -i s/\"= local\"/\"= live\"/g ~/{}/source/core/secrets.py'".format(sitename, sitename),
    shell=True
)


# Install pip packages
subprocess.call(
 "ssh alex@{} '~/{}/env/bin/pip install -r ~/{}/source/requirements.txt'".format(sitename, sitename, sitename),
 shell=True
)

# Apply migrations
subprocess.call(
 "ssh alex@{} '~/{}/env/bin/python ~/{}/source/manage.py migrate'".format(sitename, sitename, sitename),
 shell=True
)

# Deploy static files
subprocess.call(
 "ssh alex@{} 'cd ~/{}/source && ../env/bin/python manage.py collectstatic --noinput'".format(sitename, sitename),
 shell=True
)