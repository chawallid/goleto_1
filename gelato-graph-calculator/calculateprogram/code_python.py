import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def FirstDev(wave=None,x=None,s=None,g=None):
    xx = x.shape[0]
    xy = x.shape[1]
    sd1= np.zeros([xx,xy])
    for i in range(int(s + g / 2 + 0.5), int(xy - s - g / 2 + 0.5)):
        sa=np.mean(x[:,int(i - s - g / 2 + 0.5):int(i - g / 2 - 0.5)], axis = 1)
        sc=np.mean(x[:,int(i + g / 2 + 0.5):int(i + g / 2 - 0.5 + s)], axis = 1)
        sd1[:,i]=sc - sa

    plt.figure(figsize=(10,3))
    plt.subplot(121)
    for i in range (x.shape[0]):  
        plt.plot(wave,x[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    
    plt.subplot(122)
    for i in range (x.shape[0]):  
        plt.plot(wave,sd1[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('Log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    plt.show() 
    return sd1
def SecondDev(wave,x,s,g,):
    xx = x.shape[0]
    xy = x.shape[1]
    sd2= np.zeros([xx,xy])
    for i in range(int(np.dot(3 / 2,s) + g + 0.5),int(xy - np.dot(3 / 2,s) - g + 0.5)):
        x_c=np.mean(x[:,int(i + s / 2 + g + 0.5):int(i +  np.dot(3 / 2,s) + g - 0.5)],axis = 1)
        x_a=np.mean(x[:,int(i - np.dot(3 / 2,s) - g + 0.5):int(i - s / 2 - g - 0.5)],axis = 1)
        x_b=np.mean(x[:,int(i - s / 2 + 0.5):int(i + s / 2 - 0.5)],axis = 1)
        sd2[:,i]=(x_c) - np.dot(2,(x_b)) + (x_a)

    plt.figure(figsize=(10,3))
    plt.subplot(121)
    for i in range (x.shape[0]):  
        plt.plot(wave,x[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    
    plt.subplot(122)
    for i in range (x.shape[0]):  
        plt.plot(wave,sd2[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('Log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    # plt.show()
    return  plt,sd2
def meancen2(wave=None,x=None):
    xx = x.shape[0]
    xy = x.shape[1]
    mean_x=np.sum(x,axis =0)
    mean_x=mean_x / xx
    meand=np.tile(mean_x,(xx,1))
    meanC=(x - meand)
    plt.figure(figsize=(10,3))
    
    plt.subplot(121)
    for i in range (x.shape[0]):  
        plt.plot(wave,x[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    
    plt.subplot(122)
    for i in range (x.shape[0]):  
        plt.plot(wave,meanC[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('Log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    # plt.show()
    return  plt,meanC
def snv(wave,x):
    xx = x.shape[0]
    xy = x.shape[1]
    mean_x=np.mean(x,axis =1)
    std_d=np.std(x,axis=1)
    meand=np.tile(mean_x,(xy,1)).T
    stdd=np.tile(std_d,(xy,1)).T
    
    snv_data= (x - meand) / stdd
    
    plt.figure(figsize=(10,3))
    plt.subplot(121)
    for i in range (x.shape[0]):  
        plt.plot(wave,x[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    
    plt.subplot(122)
    for i in range (x.shape[0]):  
        plt.plot(wave,snv_data[i])
    plt.xlabel('wavelenght, nm')
    plt.ylabel('Log 1/R')
    plt.xlim(np.min(wave),np.max(wave))
    # plt.show()
    return  plt,snv_data
def msc(sp,nargout=1):
    if nargout == 1:
        nos = x.shape[0]
        wave = x.shape[1]
        meansp=np.mean(sp,axis=0)
        lbd=np.array(range(0,wave))
        Ym=np.polyfit(lbd,meansp,1)
        slopem=Ym[0]
        interm=Ym[1]
        Y=np.zeros([nos,2])
        for i in range(0,nos):
            Y[i,:]=np.polyfit(lbd,sp[i,:],1)
        slope=np.tile(Y[:,0],(wave,1)).T
        inter=np.tile(Y[:,1],(wave,1)).T
        spmsc=(sp - inter) / slope
        spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
        return spmsc
    
    if nargout == 2:
        nos = x.shape[0]
        wave = x.shape[1]
        meansp=np.mean(sp,axis=0)
        lbd=np.array(range(0,wave))
        
        Ym=np.polyfit(lbd,meansp,1)
        mscval=np.copy(Ym)
        slopem=Ym[0]
        interm=Ym[1]
        Y=np.zeros([nos,2])
        for i in range(0,nos):
            Y[i,:]=np.polyfit(lbd,sp[i,:],1)
        slope=np.tile(Y[:,0],(wave,1)).T
        inter=np.tile(Y[:,1],(wave,1)).T
        spmsc=(sp - inter) / slope
        spmsc=np.multiply(spmsc,slopem) + np.tile(interm,(nos,wave))
        
        return spmsc,mscval


