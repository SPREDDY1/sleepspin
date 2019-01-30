from wonambi.ioeeg import edf
from wonambi.detect.spindle import DetectSpindle
from wonambi.detect import spindle
from wonambi.dataset import detect_format
from numpy import float16,linspace

path='C:\\MyFol\\pyatomws\\wnbi\\w.edf'
x = edf.Edf(path)
print(detect_format(path))
print(type(x))
print(x.return_hdr()[0])
print('Total samples'+x.return_hdr()[4]._repr_())
print(x.return_hdr())
'''
pr int(x.return_hdr()['start_time'])
print(x.return_hdr()['label'])
print(x.return_hdr()['n_channels'])
print(x.return_hdr()['n_samples_per_second'])
'''
spin=DetectSpindle(method='Moelle2011',
                   frequency=(512,512,512),
                   duration=None, merge=False)
print(spin._str_())

print(spin.det_remez)
print('-------')
print(x.return_hdr()[2])
print(x.return_hdr()[3])
print(x.return_hdr()[5]['start_time'])
print('Records' + x.return_hdr()[5]['n_records']._repr_())
print('Channel names:' + x.return_hdr()[5]['label']._repr_())
print('Samples per second'+ x.return_hdr()[5]['n_samples_per_record']._repr_())
print('****')

ctime = linspace(start=0, stop=1, num=512, endpoint=True, dtype=float16)
chans = x.return_dat([0], 1, 111)
print(spin._call_(data=x, parent=None))
#spmol = spindle.detect_Moelle2011(dat_orig=chans, time = ctime, s_freq = 512, opts = spin)
#print(spmol)

marks = x.return_markers()
print(type(chans))
print(chans)
print(chans.ndim)
print(marks)
print('**$$$$$$***')
print(ctime)