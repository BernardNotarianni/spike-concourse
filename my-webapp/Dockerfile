FROM python:3.6

RUN pip install bottle

ADD my_webapp.py /my_webapp.py

EXPOSE 8000
CMD ["python", "/my_webapp.py"]