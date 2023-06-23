import pandas as pd
import matplotlib.pyplot as plt

    
class analysis_model:
    _data=_ids=None
    _m=_me=_s=_r=None
    y=cont=None
    def __init__(self,dt,y,c):
        self._data = dt
        self.y=y
        self.cont=c
        self._ids = range(len(self._data))
        self._mean('Trade Value')
        self._median('Trade Value')
        self._std('Trade Value')
        self._range()
        


    def _mean(self,col):
        self._m = self._data[col].mean()
        return self._m
    def _median(self,col):
        self._me = self._data[col].median()
        return self._me
    def _std(self,col):
        self._s = self._data[col].std()
        return self._s
    def _range(self):
        self._r=0
        for x in self._data['Trade Value']:
            if (x>(self._m-self._s)and x<(self._m+self._s)):
                self._r+= 1
        return self._r

    def gen_chart_b(self,t=1):
        from errno import EEXIST
        from os import makedirs,path
        try:
            makedirs("C:\Group2MTEanalysisModel")
        except OSError as e:
            if e.errno == EEXIST and path.isdir("C:\Group2MTEanalysisModel"):
                pass
            else:
                raise

        if t==0:
            plt.plot(self._data[str('Country')],self._data['Trade Value'], marker = '+')
            plt.ylabel('Trade value')
            plt.xlabel('Country')
            plt.xticks(rotation =85)
            plt.savefig('C:\Group2MTEanalysisModel\{}-petrol-export-histogram-for-{}.png'.format(self.cont,self.y),bbox_inches='tight')
            #plt.show()
        elif t==1:
            self._data.set_index('Country', inplace = True)
            fig,ax=plt.subplots(figsize=(15,10))
            plt.ticklabel_format(style='plain', axis='y')
            self._data['Trade Value'].plot.bar(width=0.8)
            plt.suptitle('Exporters of Crude Petroleum 2016 in Asia')
            plt.xlabel('Countries')
            plt.ylabel('Trade Value')
            plt.yscale('log')
            plt.savefig('C:\Group2MTEanalysisModel\{}-petrol-export-Bar-chart-for-{}.png'.format(self.cont,self.y),bbox_inches='tight')
            #plt.show()
        elif t==2:
            plt.axhline(y=self._m-self._s,color='b',linestyle = 'dashed',label='lower range bound')
            plt.axhline(y=self._m+self._s,color='r',linestyle = 'dotted',label='upper range bound')
            plt.scatter(y=self._data['Trade Value'],x=range(len(self._data['Trade Value'])))
            plt.xticks(ticks=self._ids,rotation=75)
            plt.legend(bbox_to_anchor=(1.0,1),loc = 'upper center')
            plt.suptitle('Plot of countries in the range of one standard deviation from the mean')
            plt.xlabel('Countries')
            plt.ylabel('Range')
            plt.savefig('C:\Group2MTEanalysisModel\{}-scattrer-plot-for-{}.png'.format(self.cont,self.y),bbox_inches='tight')
            #plt.show()
