import mne
from mne import io
import matplotlib
import matplotlib.pyplot as plt
import time
from mne.io import find_edf_events
import numpy as np
raw =mne.io.read_raw_edf(input_fname="C:\\MyFol\\Misc\\Time\\ed\\TBI-THIPCoho.edf",stim_channel='auto',preload=False,verbose=False)
#raw.filter(1.,70.,fir_design='firwin',n_jobs=1)
#raw.set_eeg_reference()  #Needs the data set preloaded
original_level = mne.get_config('MNE_LOGGING_LEVEL', 'INFO')
mne.set_config('MNE_LOGGING_LEVEL', 'INFO')
#mne.set_log_level("INFO")
#print(mne.get_config_path())
#print(mne.get_config())


print(type(raw.info))
print(raw.info)
print('Total Channels or signals:'+str(raw.info["nchan"]))
#raw = raw.drop_channels(['LP2-F411', 'LP3-F412','LP4-F414','LP6'])
print('Updated Channels or signals:', raw.info['nchan'])
print('All channel names:'+raw.info["ch_names"]._str_())
#print('Allchannelnamlist:'+raw.ch_names._str_())

#print('Misc info about header: '+raw.info["dev_head_t"]._str_())
print('All Channel properties:'+raw.info["chs"]._str_())
print('Hipass Freq: '+raw.info["highpass"]._str_())
print('Lowpass Freq: '+raw.info["lowpass"]._str_())
print('Recorded date: '+raw.info["meas_date"]._str_())
print('Sample rate or Frequency:'+ raw.info["sfreq"]._str_())
print('Size of raw 2d-array: '+raw._sizeof().str_())
print('2nd Channel properties:'+raw.info["chs"][1]._str_())
channel_type = mne.io.pick.channel_type(raw.info, 0)
print('2nd Channel type:',channel_type)
print(raw.times.min())
print(raw.times.max())
tmin,tmax = 0,100
raw.crop(tmin,tmax ).load_data()
data, times = raw[1:2, int(raw.info["sfreq"] * 1):int(raw.info["sfreq"] * 2)]
raw.filter(1, 70., fir_design='firwin')
fdata, ftimes = raw[1:2, int(raw.info["sfreq"] * 1):int(raw.info["sfreq"] * 2)]
print(ftimes)
print('*****')
print(fdata.T)


#EEG pick up selected channel data thru types and names.
eeg_only = raw.copy().pick_types(meg=False, eeg=True)
print(eeg_only)
#pick_chans = ['EMGR1','LP1-F410','RF1-T6-W1'] # sleep Awake Activity patterns.
pick_chans = ['LP1-F410','RF1-T6-W1'] # Seizure Activity patterns .
specific_chans = raw.copy().pick_channels(pick_chans)
print(specific_chans)

plt.figure(1)
plt.subplot(211)
plt.plot(times, data.T,label='FrontalLobe')
plt.xlabel('Time')
plt.ylabel('Frontal Signal')
plt.grid(True)
plt.title("Frontal Signal Plot")
#plt.figure(2)
plt.subplot(212)
#with filter
plt.plot(ftimes, fdata.T,label='FrontalLobe-filter')
plt.xlabel('Time')
plt.ylabel('Frontal Signal')
plt.grid(True)
plt.title("Frontal Signal Plot-Filter")

plt.legend()
plt.show()

#_ = plt.plot(times, data.T)
#_ = plt.title('Sample channels')



'''
#selection thru electro location 'Right-temporal', left etc.
selection = mne.read_selection('Left-temporal')
picks = mne.pick_types(raw.info, meg=False, eeg=True, eog=False,
                       stim=False, exclude='bads', selection=selection)
'''
'''  
#print(mne.event._find_events(first_samp=raw))
print('------------------------BUILT IN MONTAGES--------------')
print(mne.channels.get_builtin_montages())
montage = mne.channels.read_montage("standard_1020")
montage.plot()
#plt.plot(raw._data[-1])
#time.sleep(60)
print('-------------------------------------------------------')
mne.channels.
mne.filter()
'''
events = mne.find_events(raw,stim_channel='STI 014',initial_event=True,consecutive=False,verbose=True) #initial_event=True, stim_channel=OSAT
print(events)
print(len(events))
print('Unique event codes:', np.unique(events[:, 2]))
#raw.plot()
#evts = find_edf_events(raw)
#print(evts)