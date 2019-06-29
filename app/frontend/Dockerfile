FROM python:3.6

RUN pip install bottle

ADD frontend_webapp.py /frontend_webapp.py
ADD frontend_domain.py /frontend_domain.py

EXPOSE 8000
CMD ["python", "/frontend_webapp.py"]