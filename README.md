# Playing with Concourse CI

Official web site [https://concourse-ci.org/](https://concourse-ci.org/)

Run tests

    $ pytest

Start the web app

    $ python3 my_webapp.py
    
Build docker image

    $ docker build -t my-webapp . 

Start concourse server

    $ docker-compose up -d
    
    
Initialize the pipeline

    $ fly -t tutorial set-pipeline -c pipeline.yml -p my-webapp -l credentials.yml
    
Activate gcloud service account

    $ gcloud auth activate-service-account --key-file=/home/bernard/gcloud-key-project-concourse.json
    
Get `kubeconfig.yml`

    $ KUBECONFIG=kubeconfig.yml gcloud --project spike-concourse container clusters get-credentials concourse --region europe-west1-c

List nodes

    $ KUBECONFIG=kubeconfig.yml kubectl get nodes


[An article](https://blog.alterway.fr/en/multi-git-branches-workflow-with-concourse-ci.html)
about multi git branches workflow on concourse, based on the [git branches](https://github.com/vito/git-branches-resource)
concourse resource.
