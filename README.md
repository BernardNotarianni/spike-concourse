# Playing with Concourse CI

Official web site [https://concourse-ci.org/](https://concourse-ci.org/)

Run tests:

    $ pytest

Start the web app:

    $ python3 my_webapp.py
    
Build docker image:

    $ docker build -t my-webapp . 

Start concourse server:

    $ docker-compose up -d
    
    
Initialize the pipeline:

    $ fly -t tutorial set-pipeline -c pipeline.yaml -p my-webapp -l credentials.yaml

    

Local directories are [not allowed](https://github.com/concourse/git-resource/issues/82#issuecomment-251991921).
All resources have to come from the cloud.

