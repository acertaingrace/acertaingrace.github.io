---
layout: w-nav 
title: "Newsboat"
---

# Newsboat

## tt-rss

I'm using [Tiny Tiny RSS](https://tt-rss.org/) to sync my feed across my phone and desktop.

## Awrit

The browser I use on the desktop is [Awrit](https://github.com/chase/awrit). It uses Kitty terminal graphics to render the webpage in the terminal just like it would in a normal browser.

## Termux

I can't use Awrit on Termux because I would need an X server for graphics and also because limited storage space. But, to be honest, it's probably better for the links to redirect to the local browser than in the terminal; to do that, add `browser termux-open-url` to the config file.

## Twit2RSS

This is a simple project that uses a Selenium Twitter scraper, Bash script, R Script. The Twitter scraper used is [godkingjay/selenium-twitter-scraper](https://github.com/godkingjay/selenium-twitter-scraper).

Bash is used to call the scraper and the R script. The scraper scrapes the tweets and outputs a csv. The R script is used to convert the csv to an RSS xml file.
