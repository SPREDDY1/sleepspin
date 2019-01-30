from wonambi.dataset import Dataset
from wonambi.detect.spindle import DetectSpindle
from wonambi.detect import spindle
from wonambi.dataset import ChanTime
from datetime import timedelta,datetime
import numpy as np
import matplotlib.pyplot as plt
from wonambi.trans.filter import filter_

class spindec:
    def _init_(self):
        print('simple')

    def spinreturn(self,cti_lp):
        spin=DetectSpindle(method='Lacourse2018',
                           #frequency=(9,15),
                           duration=None, merge=False)
        """
        # ****Moelle2011
        spin.frequency = (9,15)
        spin.rolloff = 1.7
        spin.moving_rms = {'dur': .2,
                           'step': None }
        spin.smooth = {'dur': .2,
                       'win': 'flat'}
        spin.det_thresh = 1.5
        spin.duration =(0.5,3)
        spin.det_remez = {'freq': spin.frequency,
                          'rolloff': spin.rolloff,
                           'dur': 1.18 }
        """
        # *** Lacourse2018
        spin.frequency =(11,16)
        spin.duration = (.3,2.5)
        spin.det_butter = {'freq': spin.frequency,
                           'order': 20}
        spin.det_butter2 = {'freq': (.3, 30),
                            'order': 10}
        spin.windowing = win = {'dur': .3,
                                'step': .1}
        spin.moving_ms = {'dur': win['dur'],
                          'step': win['step']}
        spin.moving_power_ratio = {'dur': win['dur'],
                                   'step': win['step'],
                                   'freq_narrow': spin.frequency,
                                   'freq_broad': (4.5, 30),
                                   'fft_dur': 2}
        spin.zscore = {'dur': 30,
                       'step': None,
                       'pcl_range': (10, 90)}
        spin.moving_covar = {'dur': win['dur'],
                             'step': win['step']}
        spin.moving_sd = {'dur': win['dur'],
                          'step': win['step']}
        spin.abs_pow_thresh = 1.25
        spin.rel_pow_thresh = 1.6
        spin.covar_thresh = 1.3
        spin.corr_thresh = 0.69
        # ********

        print(spin._str_())
        desp = spin._call_(data=cti_lp, parent=None)
        print(desp.std)
        print(desp.mean)
        print(desp.det_value)
        print(desp.sel_value)
        print(len(desp.events))
        print(type(desp.events))
        spinlist = desp.events[20:24]
        return spinlist

def main():
    path='\w.edf'
    dset = Dataset(filename=path,IOClass = None ,bids=False)
    print(type(dset))
    print(dset.header)
    rec_st_time = dset.header['start_time']
    print(rec_st_time)
    s = datetime(2018, 1, 15, 12, 31, 11)
    e = datetime(2018, 1, 15, 13, 32, 11)
    cti_lp=dset.read_data(chan=['RF3'],begtime=s,endtime=e,begsam=None,endsam=None,s_freq=512)
    cti_lpx=filter_(ftype='butter',data=cti_lp,axis='time',low_cut=1.0,high_cut=70.0)
    cdata = cti_lpx.data[0][0]
    ctime = cti_lpx.axis['time'][0]
    cxdata=cti_lpx.data[0][0]
    cxtime =cti_lpx.axis['time'][0]
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(ctime,cdata,label='RF chan')
    plt.xlabel('Time:' + s.strftime("%m/%d/%Y -%H:%M:%S %p"))
    plt.ylabel('RF Signal')
    plt.subplot(2,1,2)
    plt.plot(cxtime,cxdata,label='RF chan-filterd')
    plt.xlabel('Time:' + s.strftime("%m/%d/%Y -%H:%M:%S %p"))
    plt.ylabel('RF Signal')
    plt.grid(True)
    plt.title("RF signal plot")
    plt.legend()
    plt.show()
    """
    sig = np.vstack((cdata,ctime))
    print(cdata.size)
    print(ctime.size)
    print(sig.dtype)
    print(sig.size)
    print(sig.ndim)
    print(type(sig))
    print(sig)
    """
    ev = spindec()
    events = ev.spinreturn(cti_lp=cti_lpx)
    print('simple2')
    j=1
    plt.figure(2)
    for i in events:
        print(str(j)+' --- '+i._repr_())
        st=np.where(ctime==i['start'])[0][0]
        ed=np.where(ctime==i['end'])[0][0]
        print(type(rec_st_time))
        print(rec_st_time)
        print(st)
        print(ed)
        print(ctime[st])
        print(ctime[ed])
        x=st.astype(np.float64)
        sp_st_time =rec_st_time+timedelta(milliseconds=x) #512).astype(np.float64))
        print(sp_st_time._repr_())
        plt.subplot(2,2,j)
        plt.plot(ctime[st:ed],cdata[st:ed],label='RFchannel')
        plt.xlabel('Time: '+sp_st_time.strftime("%m/%d/%Y -%H:%M:%S %p"))
        plt.ylabel('RF Signal')
        plt.grid(True)
        j=j+1

    plt.title("RF signal plot")
    plt.legend()
    plt.show()

    """
    st=np.where(ctime==15848.146484375)
    en=np.where(ctime==15848.71484375)
    s=st[0][0]
    e=en[0][0]
    print(s)
    print(e)
    print(ctime[s:e])
    print('********')
    print(cdata[s:e])
    plt.figure(1)
    plt.subplot(211)
    plt.plot(ctime[s:e],cdata[s:e],label='LPchannel')
    plt.xlabel('Time')
    plt.ylabel('LP Signal')
    plt.grid(True)
    plt.title("LP signal plot")
    plt.legend()
    plt.show()
    """
if __name__ == "_main_":
    main()