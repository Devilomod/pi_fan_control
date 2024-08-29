FROM python:3
COPY fan_control.py /usr/src/app/fan_control.py
WORKDIR /usr/src/app
CMD ["python", "./fan_control.py"]
