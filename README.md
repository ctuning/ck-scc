## Collective Knowledge workflow for the Student Cluster Competition (SCC)

[![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck)
[![automation](https://github.com/ctuning/ck-guide-images/blob/master/ck-artifact-automated-and-reusable.svg)](https://ReproIndex.com)
[![workflow](https://github.com/ctuning/ck-guide-images/blob/master/ck-workflow.svg)](https://cKnowledge.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Introduction

This repository contains an evolving [Collective Knowledge](https://github.com/ctuning/ck) 
workflow to standardize the preparation, execution and validation 
of submissions for the [Student Cluster Competition Reproducibility Challenge](http://www.studentclustercompetition.us/).

## CK installation

You need to install Collective Knowledge framework (CK) as described 
[here](https://github.com/ctuning/ck#Installation). 

CK was designed to be very portable with minimal dependencies (any python and git client). 
However if you experience any problems during installation, do not hesitate to ask for help
using our [Slack channel](https://bit.ly/ck-slack) 
or [Google group](https://bit.ly/ck-google-group)

If you have never used CK, we also suggest you to check 
this [blog article](https://michel.steuwer.info/About-CK),
the [CK getting started guide](https://github.com/ctuning/ck/wiki/First-Steps),
and the [list of shared CK actions](https://ReproIndex.com/components) which
you can reuse in your research projects.

## SCC workflow installation

You can now install this repository with a SCC workflow as follows:

```
$ ck pull repo --url=https://github.com/reproindex/ck-scc
```

You now have an access to different 
[research automation "actions"](https://ReproIndex.com/components/&c=module) 
shared by the community.
