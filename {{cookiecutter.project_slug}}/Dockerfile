FROM centos/python-36-centos7
WORKDIR /usr/src/app
COPY requirements_dev.txt .
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install -r requirements_dev.txt
