# Homework Set 3 [Due by 10/10 Tues 11 PM, Group]:

Implement Monte-Carlo pricing method for basket and spread options where the underling assets follow geometric brownian motions (BSM model). Also implement analytic and MC pricing methods under normal models to use the difference as a control variate. So implement three pricing methods:

* A = MC price under BSM models
* B = MC price under normal models
* C = Analytic price under normal models

The final price (MC + control variate) is given as __A - (B-C)__.

## For advanced works (e.g., final project)
You may consider implementing other analytic methods: 

* Kirk's approximation: covered in class
* Very accurate analytic approximation for spread options: [Li et al (2006)](https://ssrn.com/abstract_id=952747)
* Survey of various methods for basket options: Krekel at al (2004), Wilmott magazine, July, 82-89
* A unified numerical method for both spread and basket options: [Choi (2017)](http://papers.ssrn.com/abstract_id=2913048)

All papers are available in CMS.
