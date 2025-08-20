# pepy-stats

This repository contains software that, on a daily cadence:

- Fetches total download statistics from PePy for a few personal Python packages on PyPi, and
- Publishes those statistics to various webpages, [like so](https://michaelthomasletts.github.io/pepy-stats/boto3-refresh-session.json).

The purpose of this software is to make customizable [shields badges](https://shields.io/badges) possible when using download statistics from PePy. Unfortunately, [the badge offered by PePy](https://pepy.tech/projects/boto3-refresh-session?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=2.0.1%2C2.0.0%2C1.3.22) is not too customizable. This is a bit irksome for me, as I enjoy customizing markdown documents with shields badges using consistent color and logos. 

If anyone finds themselves in a similar dilemma and wants me [to include their Python package in this repository](https://github.com/michaelthomasletts/pepy-stats/blob/3846bac0cfbca8e072a4bf09795aea0ca4417c3c/script.py#L9) then let me know!
