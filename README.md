```txt
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

**The purpose of this software is to make _customizable_ [Shields badges](https://shields.io/badges) possible with download statistics from PePy.**

Unfortunately, [the badge offered by PePy](https://pepy.tech/projects/boto3-refresh-session?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=2.0.1%2C2.0.0%2C1.3.22) is not too customizable. And [Shield's badge](https://shields.io/badges) doesn't offer total downloads. Only daily, weekly, and monthly are available. :smirk: This is a bit irksome for me, as I enjoy customizing markdown documents with Shields badges using consistent color and logos! :art:

## . . . Feeling lazy?

If anyone finds themselves in a similar predicament as me regarding the lack of badges that combine total downloads + customizability, but don't feel like building their own mini-service for hosting download statistics, then open an [issue](https://github.com/michaelthomasletts/pepy-stats/issues). I totally get it! :smiley: I'll happily add your Python package and host those statistics for you. If you like, open a pull request which updates [this line](https://github.com/michaelthomasletts/pepy-stats/blob/eb48f0ac912d7f9aa8cbe33ae29754c001b0f714/.github/workflows/update-stats.yml#L33) with your package name in the CLI command! :sunglasses: 

## Installation

You may also install `pepy-stats` yourself using the following command if you prefer to host statistics yourself:

```bash
pip install "git+https://github.com/michaelthomasletts/pepy-stats.git"
```

## Usage

`pepy-stats` includes a CLI! :sunglasses: Just install the package and you're good to go. In the below example, we pretend `abcd1234` is an API key for illustrative purposes.

```bash
# Fetch stats for one package
pepy-stats boto3-refresh-session -k abcd1234

# Multiple packages, custom folder, no abbreviation
pepy-stats boto3-refresh-session uv requests -k abcd1234 -o ~/Desktop -no-a
```

## Badging

The total download statistics collected by this repository are published to a webpage, which can be found using the below URL pattern. Of course, if you end up self-hosting then you'll need to change `michaelthomasletts`.

`https://michaelthomasletts.github.io/pepy-stats/<package name>.json`.

The markdown for creating a Shields badge using one of those URLs may look something like this:

```markdown
[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json)](https://pepy.tech/projects/boto3-refresh-session)
```

Which, using that code, returns a Shields badge like this:

[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json)](https://pepy.tech/projects/boto3-refresh-session)

But with a little magic . . . 

```markdown
[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json&style=social&logo=python&labelColor=555&color=FF0000)](https://pepy.tech/projects/boto3-refresh-session)
```

We could get something like this! :relieved:

[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json&style=social&logo=python&labelColor=555&color=FF0000)](https://pepy.tech/projects/boto3-refresh-session)
