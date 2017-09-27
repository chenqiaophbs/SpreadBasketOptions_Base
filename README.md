# Homework Set 3 [Due by 10/9 Mon 11 PM, Group]:

Implement Monte-Carlo pricing method for basket and spread options where the underling assets follow geometric brownian motions (BSM model). Also implement analytic and MC pricing methods under normal models to use the difference as a control variate. So implement three pricing methods:

* A = MC price under BSM models
* B = MC price under normal models
* C = Analytic price under normal models

The final price (MC + control variate) is given as __A - (B-C)__.

## For advanced works (e.g., final project)
You may consider implementing other analytic methods:

* Kirk's approximation: covered in class
* Li's method:
* 
