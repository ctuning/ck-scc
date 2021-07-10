## Collective Knowledge workflow for the Student Cluster Competition (SCC)

[![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck)
[![automation](https://github.com/ctuning/ck-guide-images/blob/master/ck-artifact-automated-and-reusable.svg)](https://cTuning.org/ae)
[![workflow](https://github.com/ctuning/ck-guide-images/blob/master/ck-workflow.svg)](https://cKnowledge.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

**All CK components can be found at [cKnowledge.io](https://cKnowledge.io) and in [one GitHub repository](https://github.com/ctuning/ck-mlops)!**

*This project is hosted by the [cTuning foundation](https://cTuning.org).*

## Introduction

This repository describes how to prepare digital artifacts 
for the [Student Cluster Competition Reproducibility Challenge](http://www.studentclustercompetition.us/)

## CK installation

You need to install the Collective Knowledge framework (CK) as described 
[here](https://github.com/ctuning/ck#Installation). 

CK is a community project to share and reuse automation tasks in the form 
of [Python actions with Unique ID, JSON meta description and standardized API](https://cKnowledge.io/actions). 
It is used to support [reproducibility initiatives](https://cTuning.org/ae) at ML&systems conferences.

If you have never used CK, we also suggest you to check 
this [blog article](https://michel.steuwer.info/About-CK) and
the [CK getting started guide](https://github.com/ctuning/ck/wiki/First-Steps).

## SCC workflow installation

You need to install this repository to be able to reuse CK-SCC automation actions as follows:

```
$ ck pull repo --url=https://github.com/ctuning/ck-scc
```

## Creating a dummy CK repository for your Digital Artifact

We assume that you were already assigned a team number {TN}. 
You can create a dummy CK repository for your artifacts as follows:

```
$ ck prepare scc-workflow
```

CK will ask you about the year of the SCC competition {YEAR} and your team number {TEAM}.
It will then create a CK repository "scc-{YEAR}-{TEAM}"
with a CK entry "scc-workflow:{YEAR}-{TEAM}" to keep your Digital Artifact.
This entry will already have a directory structure required 
for your artifact submission (taken from the CK entry 
"[scc-workflow:template](https://github.com/ctuning/ck-scc/tree/master/scc-workflow/template)").

For example, if your team number is 2 and the competition year is 2019, 
CK will create repo:scc-2019-2 with an entry scc-workflow:2019-2:

```
$ ck ls repo:scc*

 scc-2019-2

$ ls -a `ck find scc-workflow:2019-2`

 .  ..  .cm  ReproducibilityChallenge

$ ls -a `ck find scc-workflow:2019-2`/ReproducibilityChallenge

 .  ..  compile  doc  figures  run

```

## Installing dependencies

You should go to the above directory with your digital artifact and 
provide commands required to install all dependencies
for the SCC application on your machine in the following script:
```
ReproducibilityChallenge/compile/install-deps.sh
```

You and other users will be able to run this script via CK using the following CK action:
```
$ ck install_deps scc-workflow
```

You should also describe how to install all dependencies in the following ReadMe file:
```
ReproducibilityChallenge/compile/README
```

## Compiling application

You should go to the above directory with your digital artifact and 
provide all commands required to compiler the SCC application
on your machine in the following script:
```
ReproducibilityChallenge/compile/install-deps.sh
```

You and other users will be able to run this script via CK using the following CK action:
```
$ ck install_deps scc-workflow
```

You should also provide compilation instructions in the following ReadMe file:
```
ReproducibilityChallenge/compile/README
```

## Downloading input

You should go to the CK directory of your digital artifact and 
check/update all commands required to download all input files
for the SCC application in the following script:
```
ReproducibilityChallenge/run/scripts/download-data.sh
```

You and other users will be able to run this script via CK using the following CK action:
```
$ ck download_data scc-workflow
```

You should also describe how to download data in the following ReadMe file:
```
ReproducibilityChallenge/run/scripts/README
```

## Running application

You should go to the CK directory of your digital artifact and 
add all commands required to run the SCC application
in the following script:
```
ReproducibilityChallenge/run/scripts/run.sh
```

You and other users will be able to run this script via CK using the following CK action:
```
$ ck run_analysis scc-workflow
```

You should also describe how to run the SCC application in the following ReadMe file:
```
ReproducibilityChallenge/run/scripts/README
```

## Post processing and validating results

You should go to the CK directory of your digital artifact and 
add all commands required to post process and validate the results
of the SCC application in the following script:
```
ReproducibilityChallenge/run/scripts/post-process.sh
```

You and other users will be able to run this script via CK using the following CK action:
```
$ ck post_process scc-workflow
```

You should also describe how to run the SCC application in the following ReadMe file:
```
ReproducibilityChallenge/run/scripts/README
```

## Plotting graphs

You should go to the CK directory of your digital artifact and 
add all commands required to plot figures for the SCC application
in the following script:
```
ReproducibilityChallenge/figures/scripts/plot.sh
```

You and other users will be able to run this script via CK using the following CK action:
```
$ ck plot scc-workflow
```

You should also describe how to plot graphs in the following ReadMe file:
```
ReproducibilityChallenge/figures/scripts/README
```

## Packing your Digital Artifact

You can pack your Digital artifact as follows:
```
$ ck pack scc-workflow:{YEAR}-{TEAM}
```

The file "scc-{YEAR}-{TEAM}.zip" with your Digital Artifact will be created in your current directory.

## Packing the CK repository with your Digital Artifact

You can also pack and share the whole CK repository with your Digital Artifact:

```
$  ck zip repo:scc-{YEAR}-{TEAM} 
```

In such case, it will be easier for evaluators or users to unpack and test it in standard way via CK as follows:
```
$ ck add repo --zip=ckr-scc-2019-{TN}.zip --quiet
```

## Extra notes

* You can run all above actions (install_deps, compile, download_data, run_analysis, post_process and plot) using CK "run" action as follows:
```
$ ck run scc-workflow
```

* This CK repository depends on another CK repository: [ck-env](https://cKnowledge.io/c/ck-repo/ck-env).
  This dependency is described in the [.ckr.json](https://github.com/ctuning/ck-scc/blob/master/.ckr.json#L9) file.

## Future work

We plan to add [automatic detection](https://cKnowledge.io/soft) of required software, models and data sets,
[installation of missing packages](https://cKnowledge.io/packages), unified benchmarking,
and experiment reply based on the [SCC'18 CK workflow](https://github.com/ctuning/ck-scc18).
We also plan to automate visualization and comparison of results 
via universal [CK leaderboards](https://cKnowledge.io/result/sota-mlperf-inference-results-v0.5-open-available).

Please feel free to get in touch with [Grigori Fursin](https://fursin.net/research) for more details.
