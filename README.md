```txt
  _  _   _    
 /_//_' /_//_/
/      /   _/ 
               
  __/_ _ _/_  _
_\ /  /_|/  _\ 
```

## What is pepy-stats?

`pepy-stats` is a repository that, on a daily schedule at approximately 8 AM UTC:

- Fetches total download statistics from [PePy](https://pepy.tech/) for [a few Python packages on PyPi](https://pypi.org/user/lettsmt/), and
- Publishes those statistics to various webpages [like this](https://michaelthomasletts.github.io/pepy-stats/boto3-refresh-session.json).

**The purpose of this software is to make _customizable_ [Shields badges](https://shields.io/badges) possible with download statistics from PePy.**

Unfortunately, [the badge offered by PePy](https://pepy.tech/projects/boto3-refresh-session?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=line&versions=2.0.1%2C2.0.0%2C1.3.22) is not highly customizable. [Even after recent updates following a GitHub issue I opened](https://github.com/psincraian/pepy/issues/763#issuecomment-3222413682). And [Shield's badge](https://shields.io/badges) doesn't offer total downloads. Only daily, weekly, and monthly are available. :smirk: This is irksome for me, as I enjoy customizing markdown documents with Shields badges using consistent colors, styles, and logos! :art:

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

So you successfully added your Python package(s) to this repository or installed the CLI and published some total download statistics to wherever you're hosting them. Great! But now what . . . ?

Well, the total download statistics collected by _this_ repository are published to a webpage, which can be found using the below URL pattern.

`https://michaelthomasletts.github.io/pepy-stats/<package name>.json`.

If you are self-hosting statistics then, of course, I cannot help you with what your URL pattern will look like 😬 . . . but I digress . . . 

Anyway, the markdown for creating a Shields badge using one of those URLs may look something like this:

```markdown
[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json)](https://pepy.tech/projects/boto3-refresh-session)
```

Which, using the above markdown code, returns a Shields badge like this:

[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json)](https://pepy.tech/projects/boto3-refresh-session)

But with a little magic . . . 🪄

```markdown
[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json&style=social&logo=python&labelColor=555&color=FF0000)](https://pepy.tech/projects/boto3-refresh-session)
```

We could get something like this! :relieved:

[![Downloads](https://img.shields.io/endpoint?url=https%3A%2F%2Fmichaelthomasletts.github.io%2Fpepy-stats%2Fboto3-refresh-session.json&style=social&logo=python&labelColor=555&color=FF0000)](https://pepy.tech/projects/boto3-refresh-session)
