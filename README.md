# Playing with Concourse CI

Official web site [https://concourse-ci.org/](https://concourse-ci.org/)

Run tests:

    $ pytest

Start the web app:

    $ python3 my_webapp.py

Start concourse server:

    $ docker-compose up -d
    
    
Local directories are [not allowed](https://github.com/concourse/git-resource/issues/82#issuecomment-251991921).
All resources have to come from the cloud.

