# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:56:58 2017

@author: jaehyuk
"""
import numpy as np
import scipy.stats as ss

def basket_check_args(spot, vol, corr_m, weights):
    '''
    This function simply checks that the size of the vector (matrix) are consistent
    '''
    
    

def basket_price_mc_cv(strike, spot, vol, texp, cor_m, \
                       intr=0.0, divr=0.0, cp_sign=1):
    
    assert( basket_check_args(spot, vol, corr_m, weights) )


def basket_price_mc(strike, spot, vol, texp, cor_m, \
                    intr=0.0, divr=0.0, cp_sign=1, bsm=True):
    vol_std = vol * np.sqrt(texp)
    div_fac = np.exp(-texp*divr)
    disc_fac = np.exp(-texp*intr)
    forward = spot / disc_fac * div_fac

    if( vol_std <= 0.0 ):
        return( disc_fac*max(cp_sign*(forward-strike), 0.0) )
    
    d1 = np.log(forward/strike)/vol_std + 0.5*vol_std
    d2 = d1 - vol_std

    price = cp_sign * disc_fac \
        * ( forward * ss.norm.cdf(cp_sign*d1) - strike * ss.norm.cdf(cp_sign*d2) )
    return price

def basket_price_norm_analytic(\
strike, spot, vol, texp, weight, cor_m, intr=0.0, divr=0.0, cp_sign=1):
    
    '''
    1. compute the forward of the basket
    2. compute the normal volatility of basket
    3. plug in the forward and volatility to the normal price formula
    you may copy & paste the normal price formula from your previous HW.
    '''
    
    return 0.0
