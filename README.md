```markdown
  _  _   _    
 /_//_' /_//_/
/      /   _/ 
               
  __/_ _ _/_  _
_\ /  /_|/  _\ 
```

## What is pepy-stats?

`pepy-stats` is a repository that, on a daily schedule at approximately 8 AM UTC:

- Fetches total download statistics from PePy for a few Python packages on PyPi, and
- Publishes those statistics to various webpages [like this](https://michaelthomasletts.github.io/pepy-stats/boto3-refresh-session.json).

**The purpose of this software is to make _customizable_ [shields badges](https://shields.io/badges) possible with download statistics from PePy.**

Unfortunately, [the badge offered by PePy](https://pepy.tech/projects/boto3-refresh-session?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=2.0.1%2C2.0.0%2C1.3.22) is not too customizable. :smirk: This is a bit irksome for me, as I enjoy customizing markdown documents with shields badges using consistent color and logos! :art:

If anyone finds themselves in a similar predicament but doesn't feel like building their own mini-service for hosting downloads statistics themselves then then open an [issue](https://github.com/michaelthomasletts/pepy-stats/issues). I totally get it! :smiley: I'll happily add your Python package [here](https://github.com/michaelthomasletts/pepy-stats/blob/3846bac0cfbca8e072a4bf09795aea0ca4417c3c/script.py#L9). 

Statistics collected by this repository can be found at the following URL pattern:

`https://michaelthomasletts.github.io/pepy-stats/<package name>.json`.

The markdown for creating a shields badge using one of those URLs may look something like this:

```markdown
[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json)](https://pepy.tech/projects/boto3-refresh-session)
```

Which, using that code, returns a shields badge like this:

[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json)](https://pepy.tech/projects/boto3-refresh-session)

Auf wiedersehen! :relieved:
