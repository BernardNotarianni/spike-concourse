FROM python:3.6

RUN pip install bottle

ADD storage_webapp.py /my_webapp.py
ADD storage_domain.py /my_domain.py

EXPOSE 8000
CMD ["python", "/storage_webapp.py"]