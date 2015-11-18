Description
===========
Install and configure Kubernetes on CoreOS cluster.

Version 1.0-43p
-------------

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-kubernetes/1.0-43p/meta.yml)

Attributes
----------

Configurations
--------------
 - Kubernetes 1.1.1 release
 - Coreos (us-east-1/ami-68bdc102), AWS EC2 m1.small, core

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
  - S3 bucket with Chef recipes: ** (TBD)
  - If Chef is not installed: ** (TBD)

Implementation notes
--------------------
 - Installation via user-data cloud-config

