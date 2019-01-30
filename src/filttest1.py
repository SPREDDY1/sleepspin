from wonambi.dataset import Dataset
from wonambi.detect.spindle import DetectSpindle
from wonambi.detect import spindle
from wonambi.dataset import ChanTime
from datetime import timedelta
from wonambi.trans.filter import filter_
path='C:\\MyFol\\pyatomws\\wnbi\\w.edf'
dset = Dataset(filename=path,IOClass = None ,bids=False)
print(type(dset))
print(dset.header)

#print('Channel names:' + dset.return_hdr()[5]['label']._repr_())
cti=dset.read_data(chan=['LP3'],begtime=None,endtime=None,begsam=None,endsam=None,s_freq=None)
x=filter_(ftype='butter',data=cti,axis='time',low_cut=1.0,high_cut=70.0)

print(x.data)
print(x.axis['chan'])
print(x.axis['time'])