# Homework Set 3 [Due by 10/10 Tues 11 PM, Group]:

Implement Monte-Carlo pricing method for basket and spread options where the underling assets follow geometric brownian motions (BSM model). Also implement analytic and MC pricing methods under normal models to use the difference as a control variate. So implement three pricing methods:

* A = MC price under BSM models
* B = MC price under normal models
* C = Analytic price under normal models

The final price (MC + control variate) is given as __A - (B-C)__.

## Suggestions for final projects

* [Spread option] Very accurate analytic approximation for spread options by [Li et al, 2006](https://ssrn.com/abstract_id=952747). 
Also implement Kirk's approximation covered in class and [(Bjersund, Stensland 2014)](http://ssrn.com/abstract_id=1145206). Implement each method in a new class. In python notebook, summarize the method, write a quick help and report strength and weakness. Compare the three methods.

* [Basket+Asian option] Pick one method in the following 3 methods in survey of basket option pricing (Krekel at al, 2004, Wilmott magazine, July, 82-89): Implement the method in a new class. In python notebook, summarize the method, write a quick help and report strength and weakness.
  * a) Beisser's conditional expectation 
  * c) Levy's log-normal moment matching
  * d) Ju's Taylor expansion

* A unified numerical method for both spread and basket options: [Choi (2017)](http://papers.ssrn.com/abstract_id=2913048): Contact me
