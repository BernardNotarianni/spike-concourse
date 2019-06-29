FROM python:3.6

RUN pip install bottle

ADD backend_webapp.py /my_webapp.py
ADD backend_domain.py /my_domain.py

EXPOSE 8000
CMD ["python", "/backend_webapp.py"]