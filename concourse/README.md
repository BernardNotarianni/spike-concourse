
## Some general commands

Start concourse server

    $ docker-compose up -d
    
Initialize a pipeline

    $ fly -t tutorial set-pipeline -c pipeline.yml -p my-webapp -l credentials.yml

## Helper scripts

Create a pipeline for current branch

    $ ./create-branch-pipeline.sh

It will detect the name of the current branch and create a pipeline for it.

The branches `dev-nnn-some-branch-description` are considered as development
branches. A `dev-nnn` tag is extracted from the name and used to tag the
containers and create a corresponding namespace within the target GKE cluster.

Each development branch will have its own pipeline deploying a specific instance
of the application in a dedicated kubernetes namespace.

## Development workflow

A possible development workflow:

- open a github issue for example issue 431 about changing title
- create a branch `dev-431-change-title`
- execute the `./create-branch-pipleline.sh` to create the coresponding concourse pipeline
- code whatever need to be coded and push to the github origin branch

For each commit pushed to the branch the pipeline will build, test and deploy your
branch on the cluster with namespace = `dev-431`.

You can get the url of the application with the script `url.sh` in kubernetes
directory.

When you have finished with your branch, delete it and delete the associated
namespace with script `delete-namespace.sh`.

