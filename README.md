## Collective Knowledge workflow for the Student Cluster Competition (SCC)

[![compatibility](https://github.com/ctuning/ck-guide-images/blob/master/ck-compatible.svg)](https://github.com/ctuning/ck)
[![automation](https://github.com/ctuning/ck-guide-images/blob/master/ck-artifact-automated-and-reusable.svg)](https://ReproIndex.com)
[![workflow](https://github.com/ctuning/ck-guide-images/blob/master/ck-workflow.svg)](https://cKnowledge.org)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Introduction

This repository contains an evolving [Collective Knowledge](https://github.com/ctuning/ck) 
workflow to standardize the preparation, execution and validation 
of submissions (Digital Artifact) 
for the [Student Cluster Competition Reproducibility Challenge](http://www.studentclustercompetition.us/).

## CK installation

You need to install Collective Knowledge framework (CK) as described 
[here](https://github.com/ctuning/ck#Installation). 

CK was designed to be very portable with minimal dependencies (any python and git client). 
However if you experience any problems during installation, do not hesitate to ask for help
using our [Slack channel](https://bit.ly/ck-slack) 
or [Google group](https://bit.ly/ck-google-group).

If you have never used CK, we also suggest you to check 
this [blog article](https://michel.steuwer.info/About-CK),
the [CK getting started guide](https://github.com/ctuning/ck/wiki/First-Steps),
and the [list of shared CK modules and actions](https://ReproIndex.com/components/&c=module) 
which you can reuse in your research projects.

## SCC workflow installation

You need to install this repository to be able to reuse SCC automation actions as follows:

```
$ ck pull repo --url=https://github.com/reproindex/ck-scc
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
"[scc-workflow:template](https://github.com/reproindex/ck-scc/tree/master/scc-workflow/template)").

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










## Packing your Digital Artifact

You can pack your Digital artifact as follows:
```
$ ck pack scc-workflow:{YEAR}-{TEAM}
```

CK will create a "scc-{YEAR}-{TEAM}.zip" file which you can send to evaluators

## Packing the CK repository with your Digital Artifact

You can also pack and share the whole CK repository with your Digital Artifact:

```
$  ck zip repo:scc-{YEAR}-{TEAM} 
```

In such case, evaluators or users can unpack and test it via CK as follows:
```
$ ck add repo --zip=ckr-scc-2019-{TN}.zip --quiet
```
