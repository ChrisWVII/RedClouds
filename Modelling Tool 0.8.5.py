


## Martian Datacentre Modelling Tool
## Written by Chris Wallace
## Supervised by Noa Zilberman

## V0.8.5 - Added required replacements calculation - NumReplace()


#################### Import libraries: ####################

from solarsystem import Heliocentric # For planet locations (by Ioannis Nasios on github) - cite
from math import *                   # For calculating number of devices required etc.
from numpy import *                  # For vector calculations to determine distances between planets
from tkinter import *                # To make windows for ease of inputs
from csv import *                    # To read & write to Devices.csv
from datetime import *               # To get the date & time



#################### Interface windows (tkinter): ####################

def DateWindow():         # Input date
    global Date

    ## Set up window:
    w=7                        # Width of input boxes
    DatWin=Tk()                # 
    DatWin.title('Input Date') # 

    ## Labels & Entries:
    DatLab=Label(DatWin,text='Date:')       # 
    DayLab=Label(DatWin,text='DD')          # 
    Day=Entry(DatWin,width=w)               # 
    MonLab=Label(DatWin,text='MM')          # 
    Month=Entry(DatWin,width=w)             # 
    YeaLab=Label(DatWin,text='YYYY')        # 
    Year=Entry(DatWin,width=w)              # 
    SLab1=Label(DatWin,text='/')             # 
    SLab2=Label(DatWin,text='/')             # 
    SLab3=Label(DatWin,text='/')             # 
    SLab4=Label(DatWin,text='/')             # 
    TimLab=Label(DatWin,text='Time (24H):') # 
    Hour=Entry(DatWin,width=w)              # 
    CLab1=Label(DatWin,text=':')            # 
    Minute=Entry(DatWin,width=w)            # 

    ## Prefill with current date & time:
    Minute.insert(0,Date[0]) # 
    Hour.insert(0,Date[1])   # 
    Day.insert(0,Date[2])    # 
    Month.insert(0,Date[3])  # 
    Year.insert(0,Date[4])   # 

    ## Submit button:
    def GetInput():                                                                              # 
        global Date                                                                              # 
        Date=[int(Minute.get()),int(Hour.get()),int(Day.get()),int(Month.get()),int(Year.get())] # 
        DatWin.destroy()                                                                         # 
    b=Button(DatWin,text='Submit',command=GetInput)                                             #

    ## Grid: 
    DayLab.grid(row=0,column=1) # 
    SLab1.grid(row=0,column=2)  # 
    MonLab.grid(row=0,column=3) # 
    SLab2.grid(row=0,column=4)  # 
    YeaLab.grid(row=0,column=5) # 
    DatLab.grid(row=1,column=0) # 
    Day.grid(row=1,column=1)    # 
    SLab3.grid(row=1,column=2)  # 
    Month.grid(row=1,column=3)  # 
    SLab4.grid(row=1,column=4)  # 
    Year.grid(row=1,column=5)   # 
    TimLab.grid(row=2,column=0) # 
    Hour.grid(row=2,column=1)   # 
    CLab1.grid(row=2,column=2)  # 
    Minute.grid(row=2,column=3) # 
    b.grid(row=2,column=5)      # 
    DatWin.mainloop()           # 

def SNRWindow():          # Input sent amplitude & frequency
    global SentAmps,SentFreq

    ## Set up window: 
    SNRWin=Tk()               # 
    SNRWin.title('Input Signal Data') # 

    ## Labels & Entries:
    SentAmpLabel1=Label(SNRWin,text='Sent Power:')      # 
    SentAmpEntry=Entry(SNRWin)                          # 
    SentAmpLabel2=Label(SNRWin,text='W')                # 
    SentFreqLabel1=Label(SNRWin,text='Sent Frequency:') # 
    SentFreqEntry=Entry(SNRWin)                         # 
    SentFreqLabel2=Label(SNRWin,text='Hz')              # 
    SentFreqEntry.insert(0,'%.0f'%SentFreq)             # Insert current value
    SentAmpEntry.insert(0,str(SentAmps))                # Insert current value

    ## Submit Button:
    def GetSender():                                            # 
        global SentAmps,SentFreq                                # 
        SentAmps=float(SentAmpEntry.get())                      # 
        SentFreq=float(SentFreqEntry.get())                     # 
        SNRWin.destroy()                                        # 
    SubmitButton=Button(SNRWin,text='Submit',command=GetSender) # 

    ## Grid:
    SentAmpLabel1.grid(row=0,column=0)             # 
    SentFreqLabel1.grid(row=1,column=0)            # 
    SentAmpEntry.grid(row=0,column=1)              # 
    SentFreqEntry.grid(row=1,column=1)             # 
    SentAmpLabel2.grid(row=0,column=2,sticky='w')  # 
    SentFreqLabel2.grid(row=1,column=2,sticky='w') # 
    SubmitButton.grid(row=2,column=2)              #
    SNRWin.mainloop()                              # 

def BandWindow():         # Input bandwidth & message size
    global MessageSize,Bandwidth

    ## Set up window: 
    BandWin=Tk()                        # 
    BandWin.title('Input Message Data') # 

    ## Labels & Entries:
    BandwidthLabel1=Label(BandWin,text='Bandwidth:')  # 
    BandwidthEntry=Entry(BandWin)                     # 
    BandwidthLabel2=Label(BandWin,text='Mbps')        # 
    CodeRateLabel1=Label(BandWin,text='Coding Rate:') # 
    CodeRateEntry=Entry(BandWin)                      # 
    CodeRateLabel2=Label(BandWin,text='%')            # 
    MessageLabel1=Label(BandWin,text='Message Size:') # 
    MessageEntry=Entry(BandWin)                       # 
    MessageLabel2=Label(BandWin,text='MB')            # 
    MessageEntry.insert(0,str(MessageSize))           # Insert current value
    BandwidthEntry.insert(0,str(Bandwidth))           # Insert current value
    CodeRateEntry.insert(0,str(CodeRate*100))         # Insert current value


    ## Submit Button:
    def GetBand():                                             # 
        global MessageSize,Bandwidth,CodeRate                  # 
        MessageSize=float(MessageEntry.get())                  # 
        Bandwidth=float(BandwidthEntry.get())                  # 
        CodeRate=float(CodeRateEntry.get())/100                # 
        BandWin.destroy()                                      # 
    SubmitButton=Button(BandWin,text='Submit',command=GetBand) # 

    ## Grid:
    BandwidthLabel1.grid(row=0,column=0)            # 
    BandwidthEntry.grid(row=0,column=1)             # 
    BandwidthLabel2.grid(row=0,column=2,sticky='w') # 
    CodeRateLabel1.grid(row=1,column=0)             # 
    CodeRateEntry.grid(row=1,column=1)              # 
    CodeRateLabel2.grid(row=1,column=2,sticky='w')  # 
    MessageLabel1.grid(row=2,column=0)              # 
    MessageEntry.grid(row=2,column=1)               # 
    MessageLabel2.grid(row=2,column=2,sticky='w')   # 
    SubmitButton.grid(row=2,column=2)               #
    BandWin.mainloop()                              # 

def DemandWindow():       # Input demand
    global Demand

    ## Set up window: 
    DemWin=Tk()                  # 
    DemWin.title('Input Demand') # 

    ## Labels & Entries
    StorageDemandLabel=Label(DemWin,text='Storage Demand (TB):')    # 
    StorageDemandEntry=Entry(DemWin)                                # 
    ComputeDemandLabel=Label(DemWin,text='Compute Demand (Cores):') # 
    ComputeDemandEntry=Entry(DemWin)                                # 
    SpineDemandLabel=Label(DemWin,text='Spine Demand (Switches):')  # 
    SpineDemandEntry=Entry(DemWin)                                  # 

    ## Insert current values
    ComputeDemandEntry.insert(0,str(Demand['Compute'])) # 
    StorageDemandEntry.insert(0,str(Demand['Storage'])) # 
    SpineDemandEntry.insert(0,str(Demand['Spine']))     # 

    ## Submit Button:
    def GetDemand():                                            # 
        global Demand                                           # 
        Demand={'Compute':int(ComputeDemandEntry.get()),        # 
                'Storage':int(StorageDemandEntry.get()),        # 
                'Spine':int(SpineDemandEntry.get()),            # 
                'Leaf':1,'Power':1,'Cooling':1}                 # 
        DemWin.destroy()                                        # 
    DemandButton=Button(DemWin,text='Submit',command=GetDemand) #

    ## Grid: 
    ComputeDemandLabel.grid(row=0,column=0) # 
    ComputeDemandEntry.grid(row=0,column=1) # 
    StorageDemandLabel.grid(row=1,column=0) # 
    StorageDemandEntry.grid(row=1,column=1) # 
    SpineDemandLabel.grid(row=2,column=0)   # 
    SpineDemandEntry.grid(row=2,column=1)   # 
    DemandButton.grid(row=2,column=2)       # 
    DemWin.mainloop()                       # 

def AddDeviceWindow():    # Input device parameters
    global DeviceParameters
    
    ## Set up window:
    DevWin=Tk()                  # 
    DevWin.title('Input device') # 

    def Units(s=''):
        PowerUnitsLabel=Label(DevWin,text=' W ')             #
        DeviceSizeUnits=Label(DevWin,text='Ports')           # 
        if DeviceType.get()=='Storage':                      # 
            DeviceSizeUnits=Label(DevWin,text='  TB  ')      # 
        elif DeviceType.get()=='Compute':                    # 
            DeviceSizeUnits=Label(DevWin,text='Cores')       # 
        elif DeviceType.get()=='Cooling':                    # 
            DeviceSizeUnits=Label(DevWin,text=' m\u00B3/s ') # 
        elif DeviceType.get()=='Power':                      # 
            PowerUnitsLabel=Label(DevWin,text=' % ')         # 
        DeviceSizeUnits.grid(row=2,column=2)                 # 
        PowerUnitsLabel.grid(row=3,column=2)                 # 

    ##  Labels & Entries:
    DeviceNameLabel=Label(DevWin,text='Device Name:')                       # 
    DeviceNameEntry=Entry(DevWin)                                           # 
    DeviceTypeLabel=Label(DevWin,text='Type:')                              # 
    DeviceTypes=["Storage","Compute","Spine","Leaf","Power","Cooling"]      # \
    DeviceType=StringVar()                                                  #  Option Menu
    DeviceTypeMenu=OptionMenu(DevWin,DeviceType,*DeviceTypes,command=Units) # /
    DeviceSizeLabel=Label(DevWin,text='Size:')                              # 
    DeviceSizeEntry=Entry(DevWin)                                           # 
    DevicePowerLabel=Label(DevWin,text='Power consumption:')                # 
    DevicePowerEntry=Entry(DevWin)                                          # 
    DeviceMTBFLabel=Label(DevWin,text='MTBF:')                              # 
    MTBFUnitsLabel=Label(DevWin,text=' hours')                              # 
    DeviceMTBFEntry=Entry(DevWin)                                           # 

    ## Submit Button:
    def EnterButton():                                                                       # 
        global DeviceParameters                                                              # 
        DeviceParameters[DeviceNameEntry.get()]={'Type':DeviceType.get()}                    # 
        DeviceParameters[DeviceNameEntry.get()]['Size']=float(DeviceSizeEntry.get())         #
        if  DeviceType.get()=='Power':                                                       # 
            DeviceParameters[DeviceNameEntry.get()]['iPC']=float(DevicePowerEntry.get())/100 #
        else:                                                                                # 
             DeviceParameters[DeviceNameEntry.get()]['iPC']=float(DevicePowerEntry.get())    # 
        DeviceParameters[DeviceNameEntry.get()]['iMTBF']=float(DeviceMTBFEntry.get())        # 
        DevWin.destroy()                                                                     # 
    DeviceEnterButton=Button(DevWin,text='Enter',command=EnterButton)                        # 

    ## Grid:
    DeviceNameLabel.grid(row=0,column=0)   # 
    DeviceNameEntry.grid(row=0,column=1)   # 
    DeviceTypeLabel.grid(row=1,column=0)   # 
    DeviceTypeMenu.grid(row=1,column=1)    # 
    DeviceSizeLabel.grid(row=2,column=0)   # 
    DeviceSizeEntry.grid(row=2,column=1)   # 
    DevicePowerLabel.grid(row=3,column=0)  # 
    DevicePowerEntry.grid(row=3,column=1)  # 
    DeviceMTBFLabel.grid(row=4,column=0)   # 
    DeviceMTBFEntry.grid(row=4,column=1)   # 
    MTBFUnitsLabel.grid(row=4,column=2)    # 
    DeviceEnterButton.grid(row=5,column=1) # 
    DevWin.mainloop()                      # 

def SettingWindow():      # Change other variables

    SetWin=Tk()              # 
    SetWin.title('Settings') # 

    def CloseSettings(): # 
        SetWin.destroy() # 

    def GetSet():
        global EarthLink,MarsLink,NoiseAmp,Utilisation,Heat,MTTR,RunOutChance,HumanError,UpdateProportion,RackMTBF
        EarthLink=float(EarthLinkEntry.get())                  # 
        MarsLink=float(MarsLinkEntry.get())                    # 
        NoiseAmp=float(NoiseAmpEntry.get())                    # 
        Utilisation={'Storage':float(StorUtilEntry.get())/100, # 
                     'Compute':float(CompUtilEntry.get())/100, # 
                     'Spine':float(SpinUtilEntry.get())/100,   # 
                     'Leaf':float(LeafUtilEntry.get())/100,    # 
                     'Power':float(PowrUtilEntry.get())/100,   # 
                     'Cooling':float(CoolUtilEntry.get())/100, # 
                     'Racks':float(RackUtilEntry.get())/100}   # 
        MTTR=float(MTTREntry.get())                            # 
        RunOutChance=float(RunOutEntry.get())/100              # 
        HumanError=float(HumErrEntry.get())/100                # 
        UpdateProportion=float(UpPropEntry.get())/100          # 
        Heat=1-(float(HeatEntry.get())/100)                    # 
        RackMTBF=int(RackEntry.get())                          # 

    EarthLinkLabel=Label(SetWin,text='Time taken for signal to be sent through Earth\'s atmosphere:')  # 
    EarthLinkEntry=Entry(SetWin)                                                                       # 
    EarthLinkEntry.insert(0,EarthLink)                                                                 # 
    EarthLinkUnits=Label(SetWin,text='s')                                                              # 
    MarsLinkLabel=Label(SetWin,text='Time taken for signal to be sent through Mars\' atmosphere:')     # 
    MarsLinkEntry=Entry(SetWin)                                                                        # 
    MarsLinkEntry.insert(0,MarsLink)                                                                   # 
    MarsLinkUnits=Label(SetWin,text='s')                                                               # 
    NoiseAmpLabel=Label(SetWin,text='Noise recieved during Earth-Mars communications:')                # 
    NoiseAmpEntry=Entry(SetWin)                                                                        # 
    NoiseAmpEntry.insert(0,NoiseAmp)                                                                   # 
    NoiseAmpUnits=Label(SetWin,text='W')                                                               # 
    StorUtilLabel=Label(SetWin,text='Storage utilisation:')                                            # 
    StorUtilEntry=Entry(SetWin)                                                                        # 
    StorUtilEntry.insert(0,100*Utilisation['Storage'])                                                 # 
    StorUtilUnits=Label(SetWin,text='%')                                                               # 
    CompUtilLabel=Label(SetWin,text='Compute utilisation:')                                            # 
    CompUtilEntry=Entry(SetWin)                                                                        # 
    CompUtilEntry.insert(0,100*Utilisation['Compute'])                                                 # 
    CompUtilUnits=Label(SetWin,text='%')                                                               # 
    SpinUtilLabel=Label(SetWin,text='Spine utilisation:')                                              # 
    SpinUtilEntry=Entry(SetWin)                                                                        # 
    SpinUtilEntry.insert(0,100*Utilisation['Spine'])                                                   # 
    SpinUtilUnits=Label(SetWin,text='%')                                                               # 
    LeafUtilLabel=Label(SetWin,text='Leaf utilisation:')                                               # 
    LeafUtilEntry=Entry(SetWin)                                                                        # 
    LeafUtilEntry.insert(0,100*Utilisation['Leaf'])                                                    # 
    LeafUtilUnits=Label(SetWin,text='%')                                                               # 
    PowrUtilLabel=Label(SetWin,text='Power distribution utilisation:')                                 # 
    PowrUtilEntry=Entry(SetWin)                                                                        # 
    PowrUtilEntry.insert(0,100*Utilisation['Power'])                                                   # 
    PowrUtilUnits=Label(SetWin,text='%')                                                               # 
    CoolUtilLabel=Label(SetWin,text='Cooling utilisation:')                                            # 
    CoolUtilEntry=Entry(SetWin)                                                                        # 
    CoolUtilEntry.insert(0,100*Utilisation['Cooling'])                                                 # 
    CoolUtilUnits=Label(SetWin,text='%')                                                               # 
    RackUtilLabel=Label(SetWin,text='Rack utilisation:')                                               # 
    RackUtilEntry=Entry(SetWin)                                                                        # 
    RackUtilEntry.insert(0,100*Utilisation['Racks'])                                                   # 
    RackUtilUnits=Label(SetWin,text='%')                                                               # 
    MTTRLabel=Label(SetWin,text='Mean time to fix non-critical failure:')                              # 
    MTTREntry=Entry(SetWin)                                                                            # 
    MTTREntry.insert(0,MTTR)                                                                           # 
    MTTRUnits=Label(SetWin,text='hours')                                                               # 
    RunOutLabel=Label(SetWin,text='Highest acceptable chance of running out of replacements:')         # 
    RunOutEntry=Entry(SetWin)                                                                          # 
    RunOutEntry.insert(0,round(100*RunOutChance,10))                                                   # 
    RunOutUnits=Label(SetWin,text='%')                                                                 # 
    HumErrLabel=Label(SetWin,text='Percentage of failures due to human error:')                        # 
    HumErrEntry=Entry(SetWin)                                                                          # 
    HumErrEntry.insert(0,100*HumanError)                                                               # 
    HumErrUnits=Label(SetWin,text='%')                                                                 # 
    UpPropLabel=Label(SetWin,text='Percentage of downtime caused by updates & maintenance:')           # 
    UpPropEntry=Entry(SetWin)                                                                          # 
    UpPropEntry.insert(0,100*UpdateProportion)                                                         # 
    UpPropUnits=Label(SetWin,text='%')                                                                 # 
    HeatLabel=Label(SetWin,text='Thermal efficiency:')                                                 # 
    HeatEntry=Entry(SetWin)                                                                            # 
    HeatEntry.insert(0,100*(1-Heat))                                                                   # 
    HeatUnits=Label(SetWin,text='%')                                                                   # 
    RackLabel=Label(SetWin,text='Rack MTBF:')                                                          # 
    RackEntry=Entry(SetWin)                                                                            # 
    RackEntry.insert(0,RackMTBF)                                                                       # 
    RackUnits=Label(SetWin,text='hours')                                                               # 
    SubmitButton=Button(SetWin,text='Save & return to menu',command=lambda:(GetSet(),CloseSettings())) # 

    ## Grid (using r so more can be added):
    r=0
    EarthLinkLabel.grid(row=r,column=0,sticky='e') # 
    EarthLinkEntry.grid(row=r,column=1)            # 
    EarthLinkUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    MarsLinkLabel.grid(row=r,column=0,sticky='e') # 
    MarsLinkEntry.grid(row=r,column=1)            # 
    MarsLinkUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    NoiseAmpLabel.grid(row=r,column=0,sticky='e') # 
    NoiseAmpEntry.grid(row=r,column=1)            # 
    NoiseAmpUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    StorUtilLabel.grid(row=r,column=0,sticky='e') # 
    StorUtilEntry.grid(row=r,column=1)            # 
    StorUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    CompUtilLabel.grid(row=r,column=0,sticky='e') # 
    CompUtilEntry.grid(row=r,column=1)            # 
    CompUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    SpinUtilLabel.grid(row=r,column=0,sticky='e') # 
    SpinUtilEntry.grid(row=r,column=1)            # 
    SpinUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    LeafUtilLabel.grid(row=r,column=0,sticky='e') # 
    LeafUtilEntry.grid(row=r,column=1)            # 
    LeafUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    PowrUtilLabel.grid(row=r,column=0,sticky='e') # 
    PowrUtilEntry.grid(row=r,column=1)            # 
    PowrUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    CoolUtilLabel.grid(row=r,column=0,sticky='e') # 
    CoolUtilEntry.grid(row=r,column=1)            # 
    CoolUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    RackUtilLabel.grid(row=r,column=0,sticky='e') # 
    RackUtilEntry.grid(row=r,column=1)            # 
    RackUtilUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    MTTRLabel.grid(row=r,column=0,sticky='e') # 
    MTTREntry.grid(row=r,column=1)            # 
    MTTRUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    RunOutLabel.grid(row=r,column=0,sticky='e') # 
    RunOutEntry.grid(row=r,column=1)            # 
    RunOutUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    HumErrLabel.grid(row=r,column=0,sticky='e') # 
    HumErrEntry.grid(row=r,column=1)            # 
    HumErrUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    UpPropLabel.grid(row=r,column=0,sticky='e') # 
    UpPropEntry.grid(row=r,column=1)            # 
    UpPropUnits.grid(row=r,column=2,sticky='w') # 
    r+=1
    HeatLabel.grid(row=r,column=0,sticky='e')    # 
    HeatEntry.grid(row=r,column=1)               # 
    HeatUnits.grid(row=r,column=2,sticky='w')    # 
    r+=1
    RackLabel.grid(row=r,column=0,sticky='e')    # 
    RackEntry.grid(row=r,column=1)               # 
    RackUnits.grid(row=r,column=2,sticky='w')    # 
    SubmitButton.grid(row=r,column=3)            # 
    r+=1
    SetWin.mainloop()

def OutputWindow():       # Main Menu,display calculated values & provide options

    ## Set up window:
    Main=Tk()                     # Initialise
    Main.title('Mars Datacenter') # Title


    ## Close window:
    def CloseMain():   # 
        Main.destroy() # 


    ## Strings for output:
    StringDay=('%.0f'%Date[2]).zfill(2)                                                                            # \
    StringMonth=('%.0f'%Date[3]).zfill(2)                                                                          #  \
    StringYear=('%.0f'%Date[4]).zfill(4)                                                                           #    Normalise date
    StringHour=('%.0f'%Date[1]).zfill(2)                                                                           #  /
    StringMinute=('%.0f'%Date[0]).zfill(2)                                                                         # /
    StringDate=StringDay+'/'+StringMonth+'/'+StringYear+'  '+StringHour+':'+StringMinute                           # Date string
    StringDistance=f'{round(Distance):,} km (%.5f'%(Distance/AU)+' AU)'                                            # Distance to Mars
    Sign=''                                                                                                        # \
    StringDirection='towards Earth:'                                                                               #  \
    if EffectiveDistance>Distance:                                                                                 #   Direction of Mars velocity
        Sign='+'                                                                                                   #  /
        StringDirection='away from Earth:'                                                                         # /
    StringEffDist=f'{round(EffectiveDistance):,} km ('+Sign+f'{round((EffectiveDistance-Distance)):,} km)'         # Effective distance travelled by wave
    StringVel='%.2f'%abs(RelVel)+' km/s'                                                                           # Radial velocity of Mars w.r.t. Earth
    StringDelay='%.0f'%(PropDelay//60)+' minutes, %.0f'%(PropDelay%60)+' seconds'                                  # Split delay into minutes & seconds
    StringBandwidth='%.0f'%Bandwidth+' Mbps'                                                                       # Bandwidth
    StringCodeRate='%.2f'%(CodeRate*100)+' %'                                                                      # Coding rate
    StringMessage='%.1f'%MessageSize+' MB'                                                                         # Message size
    StringLatency='%.0f'%(Latency//60)+' minutes, %.0f'%(Latency%60)+' seconds'                                    # Split latency into minutes & seconds
    StringSentFreq = f'{round(SentFreq/1000):,} kHz'                                                               # Sent frequency
    StringFreqShift=f'{round(FreqShift/1000,2):,} kHz (%.3f'%(100*FreqShift/SentFreq)+'%)'                         # Doppler shift
    StringSentPower='%.2f'%(SentAmps/1000)+' kW'                                                                   # Amplitude of sent signal from Earth
    StringNoisePower=str(NoiseAmp)+' W'                                                                            # Amplitude recieved noise on Mars
    try:                                                                                                           # I.e. if blocked
        StringAtten='inf dB (Blocked by '+SNR+')'                                                                  # \
        StringSNR='0 dB (Blocked by '+SNR+')'                                                                      #  \
        StringDelay+=' (Blocked by '+SNR+')'                                                                       #   Blocking planet
        StringLatency+=' (Blocked by '+SNR+')'                                                                     #  /
        StringFreqShift+=' (Blocked by '+SNR+')'                                                                   # /
    except:                                                                                                        # I.e. if unblocked
        StringAtten=f'{round(10*log10(Attenuation),1):,} dB'                                                       # Attenuation between planets
        StringSNR=f'{round(10*log10(SNR),1):,} dB'                                                                 # SNR recieved
    StringUptime='%.5f'%(Uptime*100)+'%'                                                                           # Uptime
    for i in TierBoundaries:                                                                                       # \
        if Uptime>i:                                                                                               #  Equivalent tier based on uptime
            StringTier=TierBoundaries[i]                                                                           # /
    Downtime=(1-Uptime)*29*Month                                                                                   # Downtime in 29 months
    hours='%.0f'%floor(Downtime)+' hours, '                                                                        # \
    if Downtime<1:                                                                                                 #  \
        hours=''                                                                                                   #   Downtime hours
    elif Downtime<2:                                                                                               #  /
        hours='%.0f'%floor(Downtime)+' hour, '                                                                     # /
    StringDowntime=hours+'%.0f'%floor(60*(Downtime%1))+' minutes'+', %.0f'%(60*((60*Downtime)%1))+' seconds'       # Normalise output
    StringCriteria='(for highest MTBF)'                                                                            # \
    if Criteria=='tPC':                                                                                            #  Criteria used to determine demand
        StringCriteria='(for lowest power consumption)'                                                            # /
    CReq=' cores (%.0f'%DeviceParameters[BestDevices['Compute']['tMTBF'][0]]['Number']+' required + '              #  Compute demand (cores) (using C for compute)
    StringDemandC='%.0f'%Demand['Compute']+CReq+'%.0f'%Replacements['Compute'][0]+' replacements)'                 # /
    SReq=' TB (%.0f'%DeviceParameters[BestDevices['Storage']['tMTBF'][0]]['Number']+' required + '                 #  Storage Demand (TB)
    StringDemandSt='%.0f'%Demand['Storage']+SReq+'%.0f'%Replacements['Storage'][0]+' replacements)'                # /
    SReq=' Switches (%.0f'%DeviceParameters[BestDevices['Spine']['tMTBF'][0]]['Number']+' required + '             #  Spine demand (Switches)
    StringDemandSp='%.0f'%Demand['Spine']+SReq+'%.0f'%Replacements['Spine'][0]+' replacements)'                    # /
    LReq=' Ports (%.0f'%DeviceParameters[BestDevices['Leaf']['tMTBF'][0]]['Number']+' required + '                 #  Leaf demand (Ports)
    StringDemandL='%.0f'%Demand['Leaf']+LReq+'%.0f'%Replacements['Leaf'][0]+' replacements)'                       # /
    PReq=' Ports (%.0f'%DeviceParameters[BestDevices['Power']['tMTBF'][0]]['Number']+' required + '                #  Power Demand (Ports)
    StringDemandP='%.0f'%Demand['Power']+PReq+'%.0f'%Replacements['Power'][0]+' replacements)'                     # /
    CReq=' m\u00B3/s (%.0f'%DeviceParameters[BestDevices['Cooling']['tMTBF'][0]]['Number']+' required + '          #  Cooling Demand (m^3/s) (using F for fans)
    StringDemandF='%.2f'%Demand['Cooling']+CReq+'%.0f'%Replacements['Cooling'][0]+' replacements)'                 # /
    RReq=' RU (%.0f'%NumRacks+' required + '                                                                       #  Rack units
    StringDemandR='%.0f'%Demand['Racks']+RReq+'%.0f'%Replacements['Racks'][0]+' replacements)'                     # /
    StringOpResCP=BestDevices['Compute']['tPC'][0]+' ('+f'{round(BestDevices['Compute']['tPC'][1],1):,} W)'        # Compute device with lowest total power consumption
    StringOpResCM=BestDevices['Compute']['tMTBF'][0]+' ('+f'{round(BestDevices['Compute']['tMTBF'][1]):,} hours)'  # Compute device with highest total MTBF
    StringOpResStP=BestDevices['Storage']['tPC'][0]+' ('+f'{round(BestDevices['Storage']['tPC'][1],1):,} W)'       # Storage device with lowest total power consumption
    StringOpResStM=BestDevices['Storage']['tMTBF'][0]+' ('+f'{round(BestDevices['Storage']['tMTBF'][1]):,} hours)' # Storage device with highest total MTBF
    StringOpResSpP=BestDevices['Spine']['tPC'][0]+' ('+f'{round(BestDevices['Spine']['tPC'][1],1):,} W)'           # Spine switch with lowest total power consumption
    StringOpResSpM=BestDevices['Spine']['tMTBF'][0]+' ('+f'{round(BestDevices['Spine']['tMTBF'][1]):,} hours)'     # Spine switch with highest total MTBF
    StringOpResLP=BestDevices['Leaf']['tPC'][0]+' ('+f'{round(BestDevices['Leaf']['tPC'][1],1):,} W)'              # Leaf switch with lowest total power consumption
    StringOpResLM=BestDevices['Leaf']['tMTBF'][0]+' ('+f'{round(BestDevices['Leaf']['tMTBF'][1]):,} hours)'        # Leaf switch with highest total MTBF
    BestPower=BestDevices['Power']['tPC'][1]*SysPower/(1+BestDevices['Power']['tPC'][1])                           # Power consumption of best power distribution unit
    StringOpResPP=BestDevices['Power']['tPC'][0]+' ('+f'{round(BestPower,1):,} W)'                                 # Power distribution unit with lowest total power consumption
    StringOpResPM=BestDevices['Power']['tMTBF'][0]+' ('+f'{round(BestDevices['Power']['tMTBF'][1]):,} hours)'      # Power distribution unit with highest total MTBF
    StringOpResFP=BestDevices['Cooling']['tPC'][0]+' ('+f'{round(BestDevices['Cooling']['tPC'][1],1):,} W)'        # Cooling unit with lowest total power consumption
    StringOpResFM=BestDevices['Cooling']['tMTBF'][0]+' ('+f'{round(BestDevices['Cooling']['tMTBF'][1]):,} hours)'  # Cooling unit with highest total MTBF
    StringSysPower='%.2f'%(SysPower/1000)+' kW'                                                                    # Total system power consumption
    if SysMTBF>Month:                                                                                              # \
        StringSysMTBF='%.0f'%SysMTBF+' hours ( \u2248%.1f'%(SysMTBF/Month)+' months)'                              #  |
        StringSysMTBFRcsv='%.0f'%SysMTBF+' hours ( =%.1f'%(SysMTBF/Month)+' months)'                               #  |
    elif SysMTBF>Week:                                                                                             #   \
        StringSysMTBF='%.0f'%SysMTBF+' hours ( \u2248%.1f'%(SysMTBF/Week)+' weeks)'                                #    Total system MTBF (without approx for report)
        StringSysMTBFRcsv='%.0f'%SysMTBF+' hours ( =%.1f'%(SysMTBF/Week)+' weeks)'                                 #   /
    else:                                                                                                          #  |
        StringSysMTBF='%.0f'%SysMTBF+' hours ( \u2248%.1f'%(SysMTBF/Day)+' days)'                                  #  |
        StringSysMTBFRcsv='%.0f'%SysMTBF+' hours ( =%.1f'%(SysMTBF/Day)+' days)'                                   # /

    ## Output to Report.csv:
    def Report():
        try:
            with open(str(datetime.now())[0:13]+'-'+str(datetime.now())[14:16]+' Report .csv','w',newline='') as ReportCSV: # Open [datetime] Report.csv
                Writer=writer(ReportCSV)                                                                                    # Generate writer


                Writer.writerow(['Date:',StringDate])                                          # 
                Writer.writerow(['Distance from Earth to Mars:',StringDistance])               # 
                Writer.writerow(['Effective distance travelled by signal:',StringEffDist])     # 
                Writer.writerow(['Velocity of Mars '+StringDirection,StringVel])               # 
                Writer.writerow(['Propogation delay between Earth and Mars:',StringDelay])     # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Bandwidth:',StringBandwidth])                                # 
                Writer.writerow(['Coding Rate:',StringCodeRate])                               # 
                Writer.writerow(['Message Size:',StringMessage])                               # 
                Writer.writerow(['Total Latency:',StringLatency])                              # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Signal power sent:',StringSentPower])                        # 
                Writer.writerow(['Communcation Frequency:',StringSentFreq])                    # 
                Writer.writerow(['Frequency shift:',StringFreqShift])                          # 
                Writer.writerow(['Attenuation of signal:',StringAtten])                        # 
                Writer.writerow(['Noise power recieved:',StringNoisePower])                    # 
                Writer.writerow(['SNR recieved:',StringSNR])                                   # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Compute utilisation',str(100*Utilisation['Compute'])+'%'])   # 
                Writer.writerow(['Storage utilisation',str(100*Utilisation['Storage'])+'%'])   # 
                Writer.writerow(['Spine utilisation',str(100*Utilisation['Spine'])+'%'])       # 
                Writer.writerow(['Leaf utilisation',str(100*Utilisation['Leaf'])+'%'])         # 
                Writer.writerow(['PDU utilisation',str(100*Utilisation['Power'])+'%'])         # 
                Writer.writerow(['Cooling utilisation',str(100*Utilisation['Cooling'])+'%'])   # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Storage Demand (not including redundancy):',StringDemandSt]) # 
                Writer.writerow(['Compute Demand (not including redundancy):',StringDemandC])  # 
                Writer.writerow(['Spine switch Demand:',StringDemandSp])                       # 
                Writer.writerow(['Leaf switch Demand '+StringCriteria+':',StringDemandL])      # 
                Writer.writerow(['Power Demand '+StringCriteria+':',StringDemandP])            # 
                Writer.writerow(['Cooling Demand '+StringCriteria+':',StringDemandF])          # 
                Writer.writerow(['Rack Demand '+StringCriteria+':',StringDemandR])             # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Lowest total system power consumption:',StringSysPower])     # 
                Writer.writerow(['Storage:',StringOpResStP])                                   # 
                Writer.writerow(['Compute:',StringOpResCP])                                    # 
                Writer.writerow(['Spine switch:',StringOpResSpP])                              # 
                Writer.writerow(['Leaf switch:',StringOpResLP])                                # 
                Writer.writerow(['Power:',StringOpResPP])                                      # 
                Writer.writerow(['Cooling:',StringOpResFP])                                    # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Highest total system MTBF:',StringSysMTBFRcsv])              # 
                Writer.writerow(['Storage:',StringOpResStM])                                   # 
                Writer.writerow(['Compute:',StringOpResCM])                                    # 
                Writer.writerow(['Spine switch:',StringOpResSpM])                              # 
                Writer.writerow(['Leaf switch:',StringOpResLM])                                # 
                Writer.writerow(['Power:',StringOpResPM])                                      # 
                Writer.writerow(['Cooling:',StringOpResFM])                                    # 
                Writer.writerow(['',''])                                                       # 
                Writer.writerow(['Percentage Uptime:',StringUptime])                           # 
                Writer.writerow(['Equivalent Tier (based on uptime):',StringTier])             # 
                Writer.writerow(['Expected downtime in 29 months:',StringDowntime])            # 

        ## Error message if Report.csv inaccessable
        except:
            ErrorWin=Tk()
            ErrorWin.title('Error')
            def KillError():
                ErrorWin.destroy()
            ErrorLabel=Label(ErrorWin,text='Error: Unable to access Report.csv\nEnsure it is not open before saving')
            ErrorButton=Button(ErrorWin,text='ok',command=KillError)
            ErrorLabel.pack()
            ErrorButton.pack()
            ErrorWin.mainloop()

    ## Labels:
    DateLabel1=Label(Main,text='Date:',justify='left')                                               # 
    DateLabel2=Label(Main,text=StringDate,justify='left')                                            # 
    DistLabel1=Label(Main,text='Distance from Earth to Mars:',justify='left')                        # 
    DistLabel2=Label(Main,text=StringDistance,justify='left')                                        # 
    EfDiLabel1=Label(Main,text='Effective distance travelled by signal:',justify='left')             # 
    EfDiLabel2=Label(Main,text=StringEffDist,justify='left')                                         # 
    VelLabel1=Label(Main,text='Velocity of Mars '+StringDirection,justify='left')                    # 
    VelLabel2=Label(Main,text=StringVel,justify='left')                                              #  
    DelayLabel1=Label(Main,text='Time delay between Earth and Mars:',justify='left')                 # 
    DelayLabel2=Label(Main,text=StringDelay,justify='left')                                          # 
    SentFLabel1=Label(Main,text='Communcation Frequency:',justify='left')                            # 
    SentFLabel2=Label(Main,text=StringSentFreq,justify='left')                                       # 
    ShiftLabel1=Label(Main,text='Frequency shift:',justify='left')                                   # 
    ShiftLabel2=Label(Main,text=StringFreqShift,justify='left')                                      # 
    SPowLabel1=Label(Main,text='Signal power sent:',justify='left')                                  # 
    SPowLabel2=Label(Main,text=StringSentPower,justify='left')                                       # 
    NPowLabel1=Label(Main,text='Noise power recieved:',justify='left')                               # 
    NPowLabel2=Label(Main,text=StringNoisePower,justify='left')                                      # 
    AttenLabel1=Label(Main,text='Attenuation of signal:',justify='left')                             # 
    AttenLabel2=Label(Main,text=StringAtten,justify='left')                                          # 
    BandwLabel1=Label(Main,text='Bandwidth:',justify='left')                                         # 
    BandwLabel2=Label(Main,text=StringBandwidth,justify='left')                                      # 
    CodeRLabel1=Label(Main,text='Coding Rate:',justify='left')                                       # 
    CodeRLabel2=Label(Main,text=StringCodeRate,justify='left')                                       # 
    MessaLabel1=Label(Main,text='Message Size:',justify='left')                                      # 
    MessaLabel2=Label(Main,text=StringMessage,justify='left')                                        # 
    LatenLabel1=Label(Main,text='Total Latency:',justify='left')                                     # 
    LatenLabel2=Label(Main,text=StringLatency,justify='left')                                        # 
    SNRLabel1=Label(Main,text='SNR recieved:',justify='left')                                        # 
    SNRLabel2=Label(Main,text=StringSNR,justify='left')                                              # 
    UptimeLabel1=Label(Main,text='Percentage Uptime:',justify='left')                                # 
    UptimeLabel2=Label(Main,text=StringUptime,justify='left')                                        # 
    TierLabel1=Label(Main,text='Equivalent Tier (based on uptime):',justify='left')                  # 
    TierLabel2=Label(Main,text=StringTier,justify='left')                                            # 
    DowntimeLabel1=Label(Main,text='Expected downtime in 29 months:',justify='left')                 # 
    DowntimeLabel2=Label(Main,text=StringDowntime,justify='left')                                    # 
    DemandCLabel1=Label(Main,text='Compute Demand (not including redundancy):',justify='left')       # 
    DemandCLabel2=Label(Main,text=StringDemandC,justify='left')                                      # 
    DemandStLabel1=Label(Main,text='Storage Demand (not including redundancy):',justify='left')      # 
    DemandStLabel2=Label(Main,text=StringDemandSt,justify='left')                                    # 
    DemandSpLabel1=Label(Main,text='Spine switch Demand (not including redundancy):',justify='left') # 
    DemandSpLabel2=Label(Main,text=StringDemandSp,justify='left')                                    # 
    DemandLLabel1=Label(Main,text='Leaf switch Demand '+StringCriteria+':',justify='left')           # 
    DemandLLabel2=Label(Main,text=StringDemandL,justify='left')                                      # 
    DemandPLabel1=Label(Main,text='Power Demand '+StringCriteria+':',justify='left')                 # 
    DemandPLabel2=Label(Main,text=StringDemandP,justify='left')                                      # 
    DemandFLabel1=Label(Main,text='Cooling Demand '+StringCriteria+':',justify='left')               # 
    DemandFLabel2=Label(Main,text=StringDemandF,justify='left')                                      # 
    DemandRLabel1=Label(Main,text='Rack Demand '+StringCriteria+':',justify='left')                  # 
    DemandRLabel2=Label(Main,text=StringDemandR,justify='left')                                      # 
    SysLowPCLabel1=Label(Main,text='Lowest total system power consumption:',justify='left')          # 
    SysLowPCLabel2=Label(Main,text=StringSysPower,justify='left')                                    # 
    OpResCPLabel1=Label(Main,text='Compute:',justify='left')                                         # 
    OpResCPLabel2=Label(Main,text=StringOpResCP,justify='left')                                      # 
    OpResStPLabel1=Label(Main,text='Storage:',justify='left')                                        # 
    OpResStPLabel2=Label(Main,text=StringOpResStP,justify='left')                                    # 
    OpResSpPLabel1=Label(Main,text='Spine switch:',justify='left')                                   # 
    OpResSpPLabel2=Label(Main,text=StringOpResSpP,justify='left')                                    # 
    OpResLPLabel1=Label(Main,text='Leaf switch:',justify='left')                                     # 
    OpResLPLabel2=Label(Main,text=StringOpResLP,justify='left')                                      # 
    OpResPPLabel1=Label(Main,text='Power distribution:',justify='left')                              # 
    OpResPPLabel2=Label(Main,text=StringOpResPP,justify='left')                                      # 
    OpResFPLabel1=Label(Main,text='Cooling:',justify='left')                                         # 
    OpResFPLabel2=Label(Main,text=StringOpResFP,justify='left')                                      # 
    SysMTBFLabel1=Label(Main,text='Highest total system MTBF:',justify='left')                       # 
    SysMTBFLabel2=Label(Main,text=StringSysMTBF,justify='left')                                      # 
    OpResCMLabel1=Label(Main,text='Compute:',justify='left')                                         # 
    OpResCMLabel2=Label(Main,text=StringOpResCM,justify='left')                                      # 
    OpResStMLabel1=Label(Main,text='Storage:',justify='left')                                        # 
    OpResStMLabel2=Label(Main,text=StringOpResStM,justify='left')                                    # 
    OpResSpMLabel1=Label(Main,text='Spine switch:',justify='left')                                   # 
    OpResSpMLabel2=Label(Main,text=StringOpResSpM,justify='left')                                    # 
    OpResLMLabel1=Label(Main,text='Leaf switch:',justify='left')                                     # 
    OpResLMLabel2=Label(Main,text=StringOpResLM,justify='left')                                      # 
    OpResPMLabel1=Label(Main,text='Power distribution:',justify='left')                              # 
    OpResPMLabel2=Label(Main,text=StringOpResPM,justify='left')                                      # 
    OpResFMLabel1=Label(Main,text='Cooling:',justify='left')                                         # 
    OpResFMLabel2=Label(Main,text=StringOpResFM,justify='left')                                      # 
    SmallEmptyLabel=Label(Main,text='')                                                              # 
    BigEmptyLabel=Label(Main,text='\t\t\t\t')                                                        # 


    ## Buttons:
    DateButton=Button(Main,text='Change Date & Time',justify='left',command=lambda:(CloseMain(),ChangeDate(),OutputWindow()))     # Change Date
    AttenButton=Button(Main,text='Recalculate SNR',justify='left',command=lambda:(CloseMain(),SignalNoiseRatio(),OutputWindow())) # Change Attenuation
    DemandButton=Button(Main,text='Change Demand',justify='left',command=lambda:(CloseMain(),ChangeDemand(),OutputWindow()))      # Change Demand
    DeviceButton=Button(Main,text='See Devices',justify='left',command=lambda:(CloseMain(),DeviceOutputWindow(),OutputWindow()))  # View devices
    BandButton=Button(Main,text='Change Message',justify='left',command=lambda:(CloseMain(),Delay(),OutputWindow()))              # Change Bandwidth
    OutButton=Button(Main,text='Save all to Report.csv',justify='left',command=lambda:(CloseMain(),Report(),OutputWindow()))      # Output data to csv
    SetButton=Button(Main,text='Settings',justify='left',command=lambda:(CloseMain(),SettingWindow(),Startup(),OutputWindow()))   # Change settings
    QuitButton=Button(Main,text='Quit',justify='left',command=CloseMain)                                                          # Change settings


    ## Grid (using r so new labels can be added easily at any point):

    # First column (comms)
    r=0
    DateLabel1.grid(row=r,column=0,sticky='w') # 
    DateLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    DistLabel1.grid(row=r,column=0,sticky='w') # 
    DistLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    EfDiLabel1.grid(row=r,column=0,sticky='w') # 
    EfDiLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    VelLabel1.grid(row=r,column=0,sticky='w') # 
    VelLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    DelayLabel1.grid(row=r,column=0,sticky='w') # 
    DelayLabel2.grid(row=r,column=1,sticky='w') #  
    r+=1
    SmallEmptyLabel.grid(row=r,column=0)       # 
    DateButton.grid(row=r,column=2,sticky='w') #
    r+=1
    BandwLabel1.grid(row=r,column=0,sticky='w') # 
    BandwLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    CodeRLabel1.grid(row=r,column=0,sticky='w') # 
    CodeRLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    MessaLabel1.grid(row=r,column=0,sticky='w') # 
    MessaLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    LatenLabel1.grid(row=r,column=0,sticky='w') # 
    LatenLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    SmallEmptyLabel.grid(row=r,column=0)       # 
    BandButton.grid(row=r,column=2,sticky='w') #
    r+=1
    SPowLabel1.grid(row=r,column=0,sticky='w') # 
    SPowLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    SentFLabel1.grid(row=r,column=0,sticky='w') # 
    SentFLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    ShiftLabel1.grid(row=r,column=0,sticky='w') # 
    ShiftLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    AttenLabel1.grid(row=r,column=0,sticky='w') # 
    AttenLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    NPowLabel1.grid(row=r,column=0,sticky='w') # 
    NPowLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    SNRLabel1.grid(row=r,column=0,sticky='w') # 
    SNRLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    SmallEmptyLabel.grid(row=r,column=0)        # 
    AttenButton.grid(row=r,column=2,sticky='w') # 
    r+=1
    UptimeLabel1.grid(row=r,column=0,sticky='w') # 
    UptimeLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    TierLabel1.grid(row=r,column=0,sticky='w') # 
    TierLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1
    DowntimeLabel1.grid(row=r,column=0,sticky='w') # 
    DowntimeLabel2.grid(row=r,column=1,sticky='w') # 
    r+=1

    # Second column (devices):
    r=0
    DemandStLabel1.grid(row=r,column=3,sticky='w') # 
    DemandStLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    DemandCLabel1.grid(row=r,column=3,sticky='w') # 
    DemandCLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    DemandSpLabel1.grid(row=r,column=3,sticky='w') # 
    DemandSpLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    DemandLLabel1.grid(row=r,column=3,sticky='w') # 
    DemandLLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    DemandPLabel1.grid(row=r,column=3,sticky='w') # 
    DemandPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    DemandFLabel1.grid(row=r,column=3,sticky='w') # 
    DemandFLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    DemandRLabel1.grid(row=r,column=3,sticky='w') # 
    DemandRLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    SmallEmptyLabel.grid(row=r,column=3)         # 
    DemandButton.grid(row=r,column=5,sticky='w') # 
    r+=1
    SysLowPCLabel1.grid(row=r,column=3,sticky='w') # 
    SysLowPCLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResStPLabel1.grid(row=r,column=3,sticky='w') # 
    OpResStPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResCPLabel1.grid(row=r,column=3,sticky='w') # 
    OpResCPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResSpPLabel1.grid(row=r,column=3,sticky='w') # 
    OpResSpPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResLPLabel1.grid(row=r,column=3,sticky='w') # 
    OpResLPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResPPLabel1.grid(row=r,column=3,sticky='w') # 
    OpResPPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResFPLabel1.grid(row=r,column=3,sticky='w') # 
    OpResFPLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    SmallEmptyLabel.grid(row=r,column=3)         # 
    DeviceButton.grid(row=r,column=5,sticky='w') # 
    r+=1
    SysMTBFLabel1.grid(row=r,column=3,sticky='w') # 
    SysMTBFLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResStMLabel1.grid(row=r,column=3,sticky='w') # 
    OpResStMLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResCMLabel1.grid(row=r,column=3,sticky='w') # 
    OpResCMLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResSpMLabel1.grid(row=r,column=3,sticky='w') # 
    OpResSpMLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResLMLabel1.grid(row=r,column=3,sticky='w') # 
    OpResLMLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResPMLabel1.grid(row=r,column=3,sticky='w') # 
    OpResPMLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1
    OpResFMLabel1.grid(row=r,column=3,sticky='w') # 
    OpResFMLabel2.grid(row=r,column=4,sticky='w') # 
    r+=1

    # Extras:
    BigEmptyLabel.grid(row=0,column=2)           # Separates columns
    OutButton.grid(row=r-1,column=0,sticky='w')  # Output to Report [datetime].csv
    SetButton.grid(row=r-1,column=2,sticky='w')  # Change settings
    QuitButton.grid(row=r-1,column=5,sticky='w') # Close menu
    Main.mainloop()

def DeviceOutputWindow(): # Display device parameters
    global DeviceParameters

    ## Set up window:
    DevOutWin=Tk()             # 
    DevOutWin.title('Devices') # 

    ## Close Window to return to main menu:
    def CloseDev():         # 
        DevOutWin.destroy() # 

    ## Sort order marker:
    def o(Par):                   # Return sort arrow
        if SortOrder==Par:        # If sorted by given parameter
            if Reverse==0:        # If sorted in order
                return('\u2193 ') # Down arrow (higher values at bottom)
            else:                 # If sorted in reverse
                return('\u2191 ') # Up arrow (higher values at top)
        else:                     # If not sorted by this parameter
            return('')            # Blank
        
    ## Column titles:
    SortNameButton=Button(DevOutWin,text=o('Name')+'Device Name:',width=30,command=lambda:(CloseDev(),SortI('Name'),DeviceOutputWindow()))          # 
    SortTypeButton=Button(DevOutWin,text=o('Type')+'Device Type:',command=lambda:(CloseDev(),SortI('Type'),DeviceOutputWindow()))                   # 
    SortSizeButton=Button(DevOutWin,text=o('Size')+'Device Size:',command=lambda:(CloseDev(),SortI('Size'),DeviceOutputWindow()))                   # 
    SortPowerButton=Button(DevOutWin,text=o('iPC')+'Individual Power (W):',command=lambda:(CloseDev(),SortI('iPC'),DeviceOutputWindow()))           # 
    SortFailButton=Button(DevOutWin,text=o('iMTBF')+'Individual MTBF (hours):',command=lambda:(CloseDev(),SortI('iMTBF'),DeviceOutputWindow()))     # 
    SortNumButton=Button(DevOutWin,text=o('Number')+'Number Required:',command=lambda:(CloseDev(),SortI('Number'),DeviceOutputWindow()))            # 
    SortTPowButton=Button(DevOutWin,text=o('tPC')+'Total Power (W):',command=lambda:(CloseDev(),SortI('tPC'),DeviceOutputWindow()))                 # 
    SortMTBFButton=Button(DevOutWin,text=o('tMTBF')+'Total MTBF (hours):',command=lambda:(CloseDev(),SortI('tMTBF'),DeviceOutputWindow()))          # 
    Fail29Button=Button(DevOutWin,text=o('tMTBF')+'Average Failures in 29 months:',command=lambda:(CloseDev(),SortI('tMTBF'),DeviceOutputWindow())) # 

    ## Size units:
    def SizeString(Device):
        if Device['Type']=='Compute':                 # Compute
            return '%.0f'%Device['Size']+' cores'     # Int + unit
        elif Device['Type']=='Storage':               # Storage
            return '%.2f'%Device['Size']+' TB'        # Float + unit
        elif Device['Type']in['Spine','Leaf']:        # Spine & Leaf
            return '%.0f'%Device['Size']+' ports'     # Int + unit
        elif Device['Type']=='Power':                 # Power dist.
            return '%.0f'%Device['Size']+' ports'     # Int + unit
        elif Device['Type']=='Cooling':               # Cooling
            return '%.2f'%Device['Size']+' m\u00B3/s' # Float + unit

    ## Device Parameter Labels:
    ci=1                                                                                  # Counter for row for grid
    #PrevType='Storage'                                                                    # Previous type
    for i in DeviceParameters:                                                            # i iterates through device names
    #    if DeviceParameters[i]['Type']!=PrevType:                                         # \
    #        PrevType=DeviceParameters[i]['Type']                                          #  \
    #        EmptyLabel=Label(DevOutWin,text='')                                           #   Adds blank rows between types
    #        EmptyLabel.grid(row=ci,column=0)                                              #  /
    #        ci+=1                                                                         # /
        cj=1                                                                              # Counter for column for grid
        DevName=Label(DevOutWin,text=i)                                                   # Name label
        DevName.grid(row=ci,column=0,sticky='w')                                          # Grid (cith row,0th column)
        for j in DeviceParameters[i]:                                                     # j iterates through parameter names
            if j in ['iMTBF','tMTBF']:                                                    # \
                DevPar=Label(DevOutWin,text=f'{round(DeviceParameters[i][j]):,}')         #  \
            elif j in ['iPC','tPC']:                                                      #   \
                if DeviceParameters[i]['Type']=='Power':                                  #    Round MTBF & power values for output
                    DevPar=Label(DevOutWin,text='%.1f'%(DeviceParameters[i][j]*100)+' %') #   /
                else:                                                                     #  /
                    DevPar=Label(DevOutWin,text='%.1f'%DeviceParameters[i][j])            # /
            elif j=='Size':                                                               # Add units to device size
                DevPar=Label(DevOutWin,text=SizeString(DeviceParameters[i]))              # Using SizeString function aboc
            else:                                                                         # Leave other values
                DevPar=Label(DevOutWin,text=str(DeviceParameters[i][j]))                  # Parameter label
            DevPar.grid(row=ci,column=cj)                                                 # Grid (cith row,cjth column)
            cj+=1                                                                         # Incriment cj (column)
        DevPar=Label(DevOutWin,text='%.2f'%(21170/DeviceParameters[i]['tMTBF']))          # Final column (predicted failures in 29 months)
        DevPar.grid(row=ci,column=cj)                                                     # Grid
        ci+=1                                                                             # Increment ci (row)


    ## Buttons:
    AddDeviceButton=Button(DevOutWin,text='Add Device',command=lambda:(CloseDev(),AddDevice(),DeviceOutputWindow()))               # Add device,re-sort & return
    BackButton=Button(DevOutWin,text='Back to Main Menu',command=lambda:(CloseDev()))                                              # Return to menu
    OutputCSVButton=Button(DevOutWin,text='Save all to Devices.csv',command=lambda:(CloseDev(),DevicesCSV(),DeviceOutputWindow())) # Output devices to csv

    ## Grid:
    SortNameButton.grid(row=0,column=0)   # 
    SortTypeButton.grid(row=0,column=1)   # 
    SortSizeButton.grid(row=0,column=2)   # 
    SortPowerButton.grid(row=0,column=3)  # 
    SortFailButton.grid(row=0,column=4)   # 
    SortNumButton.grid(row=0,column=5)    # 
    SortTPowButton.grid(row=0,column=6)   # 
    SortMTBFButton.grid(row=0,column=7)   # 
    Fail29Button.grid(row=0,column=8)     # 
    OutputCSVButton.grid(row=ci,column=0) # 
    AddDeviceButton.grid(row=ci,column=7) # 
    BackButton.grid(row=ci,column=8)      # 
    DevOutWin.mainloop()                  # 



#################### Date-based functions: ####################

def ChangeDate():          # Changes date & recalculates previously calculated values based on new dates
    global Date,Distance,PlanetsDict,RelVel,RelAcc,EffectiveDistance,RecievedFreq,FreqShift,PlanetsDictDel,PropDelay,Obstacles,SNR
    DateWindow()        # Change date
    DistanceToMars()    # \
    Doppler()           #  \
    PlanetDistance()    #   Recalculate everything depending on date
    Delay(1)            #  /
    SignalNoiseRatio(1) # /

def DistanceToMars():      # Calculates coordinates of Sun & every planet from Mercury to Mars
    global Distance,PlanetsDict

    ## Get planet locations:
    Cartesian=Heliocentric(year=Date[4],month=Date[3],day=Date[2],hour=Date[1],minute=Date[0],view='rectangular') # Using solarsystem module
    PlanetsDict=Cartesian.planets()                                                                               # /

    PlanetsDict['Sun']=(0,0,0)                                        # Add Sun to PlanetsDict
    Distance=0                                                        # Initialise distance
    for i in range(3):                                                # Calculate distance between Earth & Mars
        Distance+=(PlanetsDict['Earth'][i]-PlanetsDict['Mars'][i])**2 # Add 1D distance squared for pythag
    Distance=(Distance**0.5)*AU                                       # Square root & convert to km

def Doppler():             # Calculates relative speed of Earth & Mars when signal recieved
    global RelVel,RelAcc,PropDelay,EffectiveDistance,RecievedFreq,FreqShift,PlanetsDictDel

    ## Get planet locations:
    CartesianPrev=Heliocentric(year=Date[4],month=Date[3],day=Date[2],hour=Date[1],minute=Date[0]-1,view='rectangular') # \
    PlanetsDictPrev=CartesianPrev.planets()                                                                             #  |
    CartesianNext=Heliocentric(year=Date[4],month=Date[3],day=Date[2],hour=Date[1],minute=Date[0]+1,view='rectangular') #  Using solarsystem module
    PlanetsDictNext=CartesianNext.planets()                                                                             # /

    ## Get distance
    DistancePrev=0                                                                #  Initialise distances
    DistanceNext=0                                                                # /
    for i in range(3):                                                            # Calculate distance between Earth & Mars
        DistancePrev+=(PlanetsDictPrev['Earth'][i]-PlanetsDictPrev['Mars'][i])**2 #  Add 1D distance squared for pythag
        DistanceNext+=(PlanetsDictNext['Earth'][i]-PlanetsDictNext['Mars'][i])**2 # /
    DistancePrev=(DistancePrev**0.5)*AU                                           #  Square root & convert to km
    DistanceNext=(DistanceNext**0.5)*AU                                           # /

    ## Get relative speed & acceleration (finite difference)
    RelVel=(DistancePrev-DistanceNext)/120                  # Relative velocity of Mars w.r.t. Earth (km/s)
    RelAcc=(DistancePrev-(2*Distance)+DistanceNext)/(60**2) # Relative acceleration of Mars w.r.t. Earth (km/s^2)

    ## Calculate time delay (Assuming constant acceleration of Mars relative to Earth during propogation delay)
    S=Distance                      # Distance between Earth and Mars
    U=c+RelVel                      # Initial speed of light from Earth relative to Mars in km/s
    V=((U**2)+(2*RelAcc*S))**0.5    # Final speed of light from Earth relative to Mars in km/s
    A=RelAcc                        # Acceleration of Mars away from Earth
    T=((((2*A*S)+(U**2))**0.5)-U)/A # Time taken to for light reach mars

    ## Calculate signal travel distance
    EffectiveDistance=T*c # Distance light travels
    PropDelay=T           # Propogation Delay

    ## Calculate location of planets after delay
    CartesianDel=Heliocentric(year=Date[4],month=Date[3],day=Date[2],hour=Date[1],minute=Date[0]+T,view='rectangular') # \
    PlanetsDictDel=CartesianDel.planets()                                                                              #  Using solarsystem module
    PlanetsDictDel['Sun']=(0,0,0)                                                                                      # /

    ## Calculate 
    RecievedFreq=SentFreq*c/V       # Velocity ratio for recieved light
    FreqShift=RecievedFreq-SentFreq # 

def Delay(s=0):            # Calculates total latency
    global Latency,Bandwidth

    if s==0:
        BandWindow()

    ## Calculate total latency
    TransDelay=MessageSize*8/Bandwidth/CodeRate
    Latency=MarsLink+PropDelay+TransDelay+EarthLink

def PlanetDistance():      # Calculates distance between Mercury,Venus & Sun and the Earth-Mars line
    global Obstacles

    ## Find Earth and Mars:
    EarthVect=array(PlanetsDict['Earth'])       # Get location of Earth in space
    EarthVectDel=array(PlanetsDictDel['Earth']) # Get location of Earth in space
    MarsVect=array(PlanetsDictDel['Mars'])      # Get location of Mars in space after delay
    MarsVectDel=array(PlanetsDictDel['Mars'])   # Get location of Mars in space after delay

    Rs=Radii['Sun']

    ## Assume all planets out of range:
    for i in ['Sun','Mercury','Venus']:            # Iterate through planets
        Obstacles[i]='Outside range'               # Assume planet behind Earth or Mars
        PlanetVect=array(PlanetsDict[i])           # Vector location of planet
        PlanetVectDel=array(PlanetsDictDel[i])     # Vector location of planet after delay

        ## Check if planet is between Earth & Mars (extending range by the diameter of the Sun):
        if MarsVect[0]-(2*Rs)<=PlanetVect[0]<=EarthVect[0]+(2*Rs) or MarsVect[0]+(2*Rs)>=PlanetVect[0]>=EarthVect[0]-(2*Rs):         # \ 
            if MarsVect[1]-(2*Rs)<=PlanetVect[1]<=EarthVect[1]+(2*Rs) or MarsVect[1]+(2*Rs)>=PlanetVect[1]>=EarthVect[1]-(2*Rs):     #  Check if planet is between Earth & Mars
                if MarsVect[2]-(2*Rs)<=PlanetVect[2]<=EarthVect[2]+(2*Rs) or MarsVect[2]+(2*Rs)>=PlanetVect[2]>=EarthVect[2]-(2*Rs): # /

                    ## Iterate through planet locations & signal directions:
                    Directions=[] # To compare distance to line from Earth to Mars & vice versa (because of delay)
                    for PV in [PlanetVect,PlanetVectDel]:
                        for EM in [{'Earth':EarthVect,'Mars':MarsVectDel},{'Earth':EarthVectDel,'Mars':MarsVect}]:

                            ## Calculate distance from Earth-Mars line at present and after delay:
                            EarthPlanet=EM['Earth']-PV                                          # Vector from Earth to planet
                            EarthMars=EM['Earth']-EM['Mars']                                    # Vector from Earth to Mars
                            CrossProd=cross(EarthPlanet,EarthMars)                              # Cross product
                            Directions.append(AU*linalg.norm(CrossProd)/linalg.norm(EarthMars)) # Normalise

                    Obstacles[i]=min(Directions) # Choose closest option

def SignalNoiseRatio(s=0): # Calculates SNR 
    global SNR,SentAmps,SentFreq,Attenuation

    if s==0:
        SNRWindow()

    try: # Try & except in case SNR window closed prematurely

        ## Check if blocked:
        SNR=-1                              # Default value (true value calculated if unchanged)
        for i in ['Sun','Venus','Mercury']: # Iterate through planets
            try:                            # I.e. if planet within range
                if Obstacles[i]<=Radii[i]:  # If planet close enough to block signal
                    SNR=i                   # Name of blocking planet
                    break                   # End check,signal blocked
            except:                         # I.e. if planet outside range
                pass                        # Do nothing

        ## Calculate SNR:
        Attenuation=((4*SentFreq*pi*EffectiveDistance)/c)**2 # Attenuation (FSPL)
        if SNR==-1:                                          # I.e. if not blocked (unchanged from before)
                RecPow=SentAmps/Attenuation                  # Recieved Power
                SNR=RecPow/NoiseAmp                          # Signal power / noise power
    
    ## Only error caused by SNR window closing with invalid or empty inputs
    except:  # I.e. if SNR window closed without input
        pass # Do nothing (return to menu)



#################### Demand-based functions: ####################

def ChangeDemand():                # Changes demand & recalculates below functions
    global Demand,DeviceParameters,Reverse,BestDevices

    DemandWindow()     # Enter new demand
    NumberRequired()   # Recalculate number required
    MTBF()             # Recalculate MTBF
    OptimalResources() # Recalculate optimal resources based on new demand
    Reverse=1-Reverse  # Flip reverse as it will be flipped again when sort applied
    SortI(SortOrder)   # Sort devices for output
    CalculateDemand()  # Calculate demand for leaf, power & cooling
    Online()           # Calculate expected uptime
    NumReplace()       # Calculate number of replacements needed
    DevicesCSV()       # Save DeviceParameters

def CalculateDemand(Crit='tMTBF'): #Calculates demand for leaf, power & cooling based on BestDevices (default by MTBF) then recalculates
    global Demand,DeviceParameters,Reverse,BestDevices,Criteria

    ## Get criteria:
    Criteria=Crit # Required to globalise value

    ## Select best devices:
    BestStor=DeviceParameters[BestDevices['Storage'][Criteria][0]] # Choose best storage device for given criteria
    BestComp=DeviceParameters[BestDevices['Compute'][Criteria][0]] # Choose best compute device for given criteria

    ## Calculate Leaf demand & find best switch:
    Demand['Leaf']=BestStor['Number']+BestComp['Number']                      # 1 port per device
    NumberRequired()                                                          # Recaluclate number of leaf devices
    MTBF()                                                                    # Recalculate MTBF
    OptimalResources()                                                        # Recalculate optimal resources based on new demand
    BestLeaf=DeviceParameters[BestDevices['Leaf'][Criteria][0]]               # Select best switch
    NumberRequired()                                                          # Recalculate number required
    MTBF()                                                                    # Recalculate MTBF
    OptimalResources()                                                        # Recalculate optimal resources based on new demand

    ## Calculate cooling demand & find best cooling device:
    BestPow=DeviceParameters[BestDevices['Power'][Criteria][0]]                                         # Best power device
    Demand['Cooling']=Heat*(1+BestPow['tPC'])*(BestStor['tPC']+BestComp['tPC']+BestLeaf['tPC'])/AirHeat # Air flow rate required
    NumberRequired()                                                                                    # Recalculate number of devices required
    MTBF()                                                                                              # Recalculate MTBF
    OptimalResources()                                                                                  # Recalculate optimal resources based on new demand
    BestCool=DeviceParameters[BestDevices['Cooling'][Criteria][0]]                                      # Select best cooling device

    ## Calculate power demand:
    Demand['Power']=BestStor['Number']+BestComp['Number']+BestLeaf['Number']+BestCool['Number'] # Calculate power demand (number of ports) (spine switches have their own power distribution)

    ## Recalculate everything:
    NumberRequired()   # Recalculate number required
    MTBF()             # Recalculate MTBF
    OptimalResources() # Recalculate optimal resources based on new demand
    Reverse=1-Reverse  # Flip reverse as it will be flipped again when sort applied
    SortI(SortOrder)   # Sort devices for output

def AddDevice():                   # Adds a new device to the DeviceParameters dictionary
    global DeviceParameters,Reverse,BestDevices

    AddDeviceWindow()  # Enter new device
    NumberRequired()   # Recalculate number required
    MTBF()             # Recalculate MTBF
    Reverse=1-Reverse  # Flip reverse as it will be flipped again when sort applied
    SortI(SortOrder)   # Sort devices for output
    OptimalResources() # Recalculate optimal resources based on new device
    DevicesCSV()       # Saves data to Devices.csv

def RemoveDevice(DeviceName):      # Removes device from DeviceParameters (unused)
    global DeviceParameters
    del DeviceParameters[DeviceName]
    DevicesCSV()

def NumberRequired():              # Calculates number of each device required if it were used
    global DeviceParameters

    for i in DeviceParameters:                                                                                            # Iterate through parameters
        TypeDemand=Demand[DeviceParameters[i]['Type']]                                                                    # Demand in i-type device
        DeviceSize=DeviceParameters[i]['Size']                                                                            # Size of device
        if DeviceParameters[i]['Type']=='Leaf':                                                                           # If leaf switch
            DeviceParameters[i]['Number']=int(ceil(TypeDemand/(DeviceSize-Demand['Spine'])))                              # Leave 1 port open for each connection to spine
        elif DeviceParameters[i]['Type']=='Spine':                                                                        # If spine switch
            DeviceParameters[i]['Number']=TypeDemand                                                                      # Spine demand is the number of switches
        else:                                                                                                             # For most devices calculate normally
            DeviceParameters[i]['Number']=max([int(ceil(TypeDemand/Utilisation[DeviceParameters[i]['Type']]/DeviceSize)), # Multiply by redundancy and round up
                                              int(ceil(TypeDemand/DeviceSize)+1)])                                        # Minimum of 1 extra for redundancy
        if DeviceParameters[i]['Type']=='Power':                                                                          # \
            DeviceParameters[i]['tPC']=DeviceParameters[i]['iPC']                                                         #  Power consumption of PDN is multiplicative not additive
        else:                                                                                                             # /
            DeviceParameters[i]['tPC']=DeviceParameters[i]['iPC']*DeviceParameters[i]['Number']                           # Calculate total power consumption

def MTBF():                        # Calculates total MTBF
    global DeviceParameters
    for i in DeviceParameters:                                                                  # Iterate through devices
        DeviceParameters[i]['tMTBF']=DeviceParameters[i]['iMTBF']/DeviceParameters[i]['Number'] # Paralell addition of MTBF (homogeneous)

def SortI(SortKey):                # Sorts devices
    global DeviceParameters,SortOrder,Reverse

    ## Initialisation:
    if SortOrder==SortKey:   # If already sorted in this order
        Reverse=1-Reverse    # Sort in reverse order to previous
    else:                    # If first time sorting in this order
        SortOrder=SortKey    # Remember last sort order
        Reverse=0            # Sort in ascending order
    srtd=[]                  # Array to sort by
    SrtdDeviceParameters={}  # Empty dictionary to add sorted devices

    ## Order of types
    TypeOrder={'Storage':1,'Compute':2,'Spine':3,'Leaf':4,'Power':5,'Cooling':6} # Order to sort types into

    ## Select parameter to sort by:
    if SortKey!='Name':                            # I.e. Sort by specific parameter
        unsrtd={}                                  # Dictionary to map parameter back to name
        for i in DeviceParameters:                 # Iterate through DeviceParameters
            Parameter=DeviceParameters[i][SortKey] # Select parameter to be sorted by (from n)
            if Parameter in TypeOrder:             # If type
                Parameter=TypeOrder[Parameter]     # Replace with number as above so sorted in order

            ## Get parameter & device name
            while Parameter in srtd:               # Add to parameter until it is unique to prevent overwriting
                if type(Parameter) is str:         # I.e. if parameter is a string
                    Parameter+='0'                 # Add '0' to end (does not affect actual value)
                else:                              # I.e. if parameter is a number
                    Parameter*=(1+10**-10)         # Increase by tiny proportion (does not affect actual value)
            unsrtd[Parameter]=i                    # Add chosen (& altered) parameter to dict to get name back
            srtd.append(Parameter)                 # Add chosen parameter to array to be sorted

        ## Create sorted version
        srtd.sort()                                                     # Sort by chosen 
        if Reverse==1:                                                  #  Reverse if necessary
            srtd.reverse()                                              # /
        for i in srtd:                                                  # Go through sorted parameters
            SrtdDeviceParameters[unsrtd[i]]=DeviceParameters[unsrtd[i]] # Add devices in new order (getting name back from unsrt)

    ## Sort by Name:
    else:                                               # I.e. if Key=='Name' (Sort by device name)
        srtd=(sorted(DeviceParameters))                 # Sort by name
        if Reverse==1:                                  #  Reverse if necessary
            srtd.reverse()                              # /
        for i in srtd:                                  # Go through sorted names
            SrtdDeviceParameters[i]=DeviceParameters[i] # Add devices in new order

    ## Replace DeviceParameters with sorted version:
    DeviceParameters=SrtdDeviceParameters # 

    ## Rerun to split into types:
    if SortKey!='Type':          # Unless already using type
        temp=[Reverse,SortOrder] # Store Reverse
        Reverse=0                # Reset Reverse
        SortI('Type')            # Separate into compute (measured in cores),storage (measured in TB),etc.
        SortOrder=temp[1]        # Reset SortOrder to Size as above changes it to 'Type'
        Reverse=temp[0]          # Reset Reverse to previous value as above changes it to 0

def OptimalResources():            # Calculates optimal resources (highest MTBF & lowest power consumption)
    global BestDevices,SysPower,SysMTBF,NumRacks,Demand

    ## Setup:
    BestDevices={}             # Reset BestDevices
    for i in DeviceParameters: # Iterate through DeviceParameters

        ## Get ith device parameters:
        iType=DeviceParameters[i]['Type']                        # Type of device
        tMTBF=DeviceParameters[i]['tMTBF']                       # MTBF of device
        tPC=DeviceParameters[i]['tPC']                           # Power consumption of N devices
        if iType not in BestDevices:                             # If no other devices of that type found yet
            BestDevices[iType]={'tPC':[i,tPC],'tMTBF':[i,tMTBF]} # Create empty best device

        ## Get parameters to compate to best avaliable device
        else:
            BDtMTBF=BestDevices[iType]['tMTBF'][1] # Current highest MTBF 
            BDtPC=BestDevices[iType]['tPC'][1]     # Current lowest power consumption

            ## Compare to best:
            if tMTBF>BDtMTBF:                         # If higher MTBF
                BestDevices[iType]['tMTBF']=[i,tMTBF] # Replace best MTBF
            if tPC<BDtPC:                             # If lower power consumption
                BestDevices[iType]['tPC']=[i,tPC]     # Replace best power consumption

    ## Calculate total system power & MTBF:
    SysPower=0                                  # Reset total system power
    SysMTBF=0                                   # Reset total system MTBF
    for i in BestDevices:                       # Get best devices for each
        if i!='Power':                          # Power consumption of PDN is assumed proportional to total power consumption
            SysPower+=BestDevices[i]['tPC'][1]  # Series addition for power
        SysMTBF+=(1/BestDevices[i]['tMTBF'][1]) #  Paralell addition for MTBF
    SysMTBF=1/SysMTBF                           # /
    SysPower*=1+BestDevices['Power']['tPC'][1]  # Power consumption of PDN is assumed to be proportional to total power consumption

    ## Number of racks:
    StRU=ceil(DeviceParameters[BestDevices['Storage']['tMTBF'][0]]['Number']/2)                                  # Storage rack units
    CRU=ceil(DeviceParameters[BestDevices['Compute']['tMTBF'][0]]['Number']/2)                                   # Compute rack units
    SpRU=({'Cisco Nexus 9516 (X9736C-EX)':21,'Cisco Nexus 9516 (X97160YC-EX)':21,                                # \
         'Cisco Nexus 9508 (X9736C-EX)':13,'Cisco Nexus 9508 (X97160YC-EX)':13,'Cisco Nexus 9504 (X9736C-EX)':7, #  Spine switch rack units
         'Cisco Nexus 9504 (X97160YC-EX)':7}[BestDevices['Spine']['tMTBF'][0]])*Demand['Spine']                  # /
    LRU=DeviceParameters[BestDevices['Leaf']['tMTBF'][0]]['Number']                                              # Leaf switch rack units
    PRU=DeviceParameters[BestDevices['Power']['tMTBF'][0]]['Number']*2                                           # PDU rack units
    Demand['Racks']=StRU+CRU+SpRU+LRU+PRU                                                                        # Total rack units (cooling not in racks)
    NumRacks=ceil(Demand['Racks']/(42*Utilisation['Racks']))                                                     # Total number of racks

def Online():                      # Calculates uptime
    global Uptime

    Downtime=0

    ## Failure modes: (Fail rate defined as expected number of failures within MTTR)
    CritFail={'Storage':[3,MTTR/BestDevices['Compute']['tMTBF'][1],                           # MTTR & fail rate for storage devices
                         floor(DeviceParameters[BestDevices['Storage']['tMTBF'][0]]['Number'] #  Number of storage devices for crit fail
                               *(1-Utilisation['Storage']))+1],                               # /
              'Compute':[3,MTTR/BestDevices['Compute']['tMTBF'][1],                           # MTTR & fail rate for compute devices
                         floor(DeviceParameters[BestDevices['Compute']['tMTBF'][0]]['Number'] #  Number of compute devices for crit fail
                               *(1-Utilisation['Compute']))+1],                               # /
              'Spine':[4,MTTR/BestDevices['Spine']['tMTBF'][1],ceil(Demand['Spine']/2)],      # MTTR, fail rate & number of spine switches
              'Leaf':[2,MTTR/BestDevices['Leaf']['tMTBF'][1],3],                              # MTTR, fail rate & number of leaf
              'Power':[2,MTTR/BestDevices['Power']['tMTBF'][1],3],                            # MTTR, fail rate & number of PDUs
              'Cooling':[4,MTTR/BestDevices['Cooling']['tMTBF'][1],                           # MTTR & fail rate for cooling devices
                         floor(DeviceParameters[BestDevices['Cooling']['tMTBF'][0]]['Number'] #  Number of cooling devices for crit fail
                               *(1-Utilisation['Cooling']))+1]}                               # /

    for i in CritFail:                                                        # Iterate through device types
        DeviceUp=0                                                            # Chance of non-critical numbers of failures
        for j in range(int(CritFail[i][2])):                                  # iterate through non-critical numbers of failures
            DeviceUp+=(exp(-CritFail[i][1])*(CritFail[i][1]**j))/factorial(j) # Poisson distribution
        Downtime+=CritFail[i][0]*(1-DeviceUp)                                 # Expectation for downtime per hour

    Uptime=1-(Downtime*(1+(6*RunOutChance))/(1-UpdateProportion)/(1-HumanError)) # Scaling for chance of running out of devices, updates & human error
    Uptime=1-(Downtime/(1-UpdateProportion)/(1-HumanError)) # Scaling for chance of running out of devices, updates & human error

def NumReplace():                  # Calculates required number of replacements
    global Replacements

    Failures={'Storage':29*Month/DeviceParameters[BestDevices['Compute']['tMTBF'][0]]['iMTBF'], # Number of expected storage failures
              'Compute':29*Month/DeviceParameters[BestDevices['Compute']['tMTBF'][0]]['iMTBF'], # Number of expected compute failures
              'Spine':29*Month/DeviceParameters[BestDevices['Spine']['tMTBF'][0]]['iMTBF'],     # Number of expected spine switch failures
              'Leaf':29*Month/DeviceParameters[BestDevices['Leaf']['tMTBF'][0]]['iMTBF'],       # Number of expected leaf switch failures
              'Power':29*Month/DeviceParameters[BestDevices['Power']['tMTBF'][0]]['iMTBF'],     # Number of expected pdu failures
              'Cooling':29*Month/DeviceParameters[BestDevices['Cooling']['tMTBF'][0]]['iMTBF'], # Number of expected cooling unit failures
              'Racks':29*Month/(RackMTBF/NumRacks)}                                             # Number of expected rack failures

    
    for i in Failures:
        N=0                                                     # Number of failures
        P=(exp(-Failures[i])*(Failures[i]**N))/factorial(N)     # Probability of 0 failures
        while P>RunOutChance:                                   # Increase number of failures until maximum probability reached
            N+=1                                                # Number of failures
            P=(exp(-Failures[i])*(Failures[i]**N))/factorial(N) # Probability of N failures
        Replacements[i]=[N/(1-HumanError),P]                    # Scaling for human error

def DevicesCSV():                  # Saves DeviceParameters to Devices.csv

    ## Write to Devices.csv
    try:
        with open('Devices.csv','w',newline='') as DevicesCSV: # Open Devices.csv
            Writer=writer(DevicesCSV)                            # Generate writer
            Writer.writerow(FancyFieldNames)                     # Write column headers
            for i in DeviceParameters:                           # Iterate through DeviceParameters
                Row=[i]+list(DeviceParameters[i].values())       # Row=name followed by parameters
                Writer.writerow(Row)                             # Write row
    
    ## Error message if Devices.csv inaccessable
    except:
        ErrorWin=Tk()
        ErrorWin.title('Error')
        def KillError():
            ErrorWin.destroy()
        ErrorLabel=Label(ErrorWin,text='Error: Unable to access Devices.csv\nEnsure it is not open before saving')
        ErrorButton=Button(ErrorWin,text='ok',command=KillError)
        ErrorLabel.pack()
        ErrorButton.pack()
        ErrorWin.mainloop()



#################### Startup functions: ####################

def Variables():   # Everything is global for simplicity
    ## Constants
    global AU,c,inf,Radii,Month,Week,Day,AirHeat,FieldNames,FancyFieldNames,TierBoundaries
    AU=149597870.69                                                                         # 1 AU in km
    c=299792.458                                                                            # Light speed in km/s
    inf=1e999                                                                               # An arbitrary large number
    Radii={'Sun':7.978*696340,'Mercury':1*2439.7,'Venus':1*6051.8}                          # Radii of celestial bodies (km)
    Month=730                                                                               # Hours in a month
    Week=168                                                                                # Hours in a week
    Day=24                                                                                  # Hours in a day
    DeltaT=25                                                                               # Difference in temp between air in and out (K)
    SpecificVolume=0.886                                                                    # m^3 kg^-1
    SpecificHeat=1014                                                                       # J kg^−1 K^−1
    AirHeat=DeltaT*SpecificHeat/SpecificVolume                                              # Heat stored in air (J/m^3)
    FieldNames=['Name','Type','Size','iPC','iMTBF','Number','tPC','tMTBF']                  # Names of fields in DeviceParameters
    FancyFieldNames=['Name','Type','Size','Individual Power Consumption','Individual MTBF', #  Legible field names
                     'Number Required','Total Power Consumption','Total MTBF']              # /
    TierBoundaries={0:'< Tier 1',0.99671:'Tier I',0.997:'Tier I-II',                        # \
                    0.99741:'Tier II',0.99861:'Tier II-III',0.99982:'Tier III',             #  Tier boundaries based on uptime
                    0.99988:'Tier III-IV',0.99995:'Tier IV'}                                # /

    ## Date-based Variables:
    global Date,RelVel,RelAcc,PlanetsDict,Distance,PropDelay,EffectiveDistance,SentFreq,Bandwidth,CodeRate,FreqShift,RecievedFreq,MessageSize,Obstacles,SentAmps,SNR
    Now=datetime.now()                # Current date and time
    Date=[Now.minute,Now.hour,        #  Date & Time in ascending magnitude [Minute,Hour,Day,Month,Year]
          Now.day,Now.month,Now.year] # /
    #Date=[37,13,12,1,2025]            # Date & time of next close approach: 13:37 12/01/25
    RelVel=0                          # Velocity at which Mars approaches Earth
    RelAcc=0                          # Acceleration at which Mars approaches Earth
    PlanetsDict={}                    # Planet locations in 3D space (Origin=Sun)
    Distance=0                        # Distance between Earth & Mars
    PropDelay=0                       # Delay in minutes & seconds
    EffectiveDistance=0               # Distance light travels between Earth & Mars
    SentFreq=7.5*(10**9)              # X-band frequency (7-8GHz)
    Bandwidth=500                     # Approx bandwidth (Mbps)
    CodeRate=1/8                      # Coding rate (dimensionless b/b)
    FreqShift=0                       # Shift in frequency due to doppler effect
    RecievedFreq=0                    # Recieved frequency due to doppler effect
    MessageSize=100                   # Size of message (MB)
    Obstacles={}                      # Distance between Mercury,Venus & Sun and the Earth-Mars line 
    SentAmps=1000                     # Amplitude of signal sent (W)
    SNR=0                             # Recieved SNR

    ## Demand-based Variables
    global Demand,Uptime,Replacements
    Demand={'Storage':500,'Compute':500,'Spine':3,'Leaf':1,'Power':1,'Cooling':1} # Required total: storage (TB), compute (cores), spine (switches), etc.
    Uptime=0                                                                      # Uptime (0<Uptime<1)
    Replacements={'Storage':[0,1],'Compute':[0,1],'Spine':[0,1],                  #  Required replacements & chance of running out
                  'Leaf':[0,1],'Power':[0,1],'Cooling':[0,1]}                     # /

    ## Other Variables:
    global SortOrder,Reverse,MarsLink,EarthLink,NoiseAmp,Utilisation,Heat,MTTR,RunOutChance,HumanError,UpdateProportion,RackMTBF
    SortOrder='Name'                             # Devices initially unsorted
    Reverse=1                                    # Initially sort in ascending order
    MarsLink=0                                   # Time for signal at Mars orbit to get to surface (s)
    EarthLink=0                                  # Time for signal at Earth Orbit to get to surface (s)
    NoiseAmp=10**-24                             # Amplitude of noise recieved (W) (assumed)
    Utilisation={'Storage':6/8,'Compute':3/4,    # \
                 'Spine':1,'Leaf':1,'Power':3/4, #  Proportion non-redundant devices
                 'Cooling':3/4,'Racks':3/4}      # /
    Heat=0.1                                     # Average heat production per unit input power
    MTTR=1.5                                     # Mean time to fix non-critical failure
    RunOutChance=0.000001                        # Acceptable chance of running out of replacements
    HumanError=0.7                               # Percentage of failures caused by human error
    UpdateProportion=0.2                         # Percentage of downtime caused by updates & maintenance
    RackMTBF=2500000                             # Rack MTBF

def ReadDevices(): # Reads DeviceParameters from Devices.csv
    global DeviceParameters

    ## Setup:
    DeviceParameters={}                                                      # Empty dictionary to store all device parameters

    ## Read Devices.csv:
    with open('Devices.csv',newline='') as DevicesCSV: # Open Devices.csv
        Reader=reader(DevicesCSV)                       # Generate reader

        ## Convert to DeviceParameters format {'Device A Name':{'Type':'','Size':0.0,'iPC':0.0,'iMTBF':0.0,'Number':0,'tPC':0.0,'tMTBF':0.0},'Device B Name':{...},...}
        ci=0                                                  # Row counter
        for i in Reader:                                      # Iterate through csv structure (i is an array with row elements as strings)
            if ci>0:                                          # Ignore first row (field names)
                Parameters={}                                 # Empty dictionary to store parameters
                for j in range(1,len(i)):                     # Iterate through fields (ignoring first column (name)) (j is an index)
                    if i[j]=='':                              # If empty (i.e. Number-tMTBF uncalculated)
                        Parameters[FieldNames[j]]=0           # Store as 0,will be calculated soon
                    elif FieldNames[j] in ['Type']:           # 'Type' is a string
                        Parameters[FieldNames[j]]=i[j]        # Leave as string
                    elif FieldNames[j] in ['Number']:         # 'Number' is an int
                        Parameters[FieldNames[j]]=int(i[j])   # Convert to int
                    else:                                     # Everything else is a float
                        Parameters[FieldNames[j]]=float(i[j]) # Convert to float
                DeviceParameters[i[0]]=Parameters             # Add device to full dictionary under device name
            else:                                             # After first row (field names)
                ci+=1                                         # Increment row counter

def Startup():     # Runs all functions in order to start calculations
    DistanceToMars()    # Calculate distance to Mars
    Doppler()           # Claculate frequency shift
    PlanetDistance()    # Determine whether planets or sun are in the way
    SignalNoiseRatio(1) # Calculate SNR recieved (1 for no window)
    Delay(1)            # Calculate total latency (1 for no window)
    NumberRequired()    # Calculate number of devices required to meet demand
    MTBF()              # Calculate MTBF for a set of devices
    OptimalResources()  # Calculate optimal devices
    CalculateDemand()   # Calculate demand for leaf, power & cooling 
    Online()            # Calculate uptime
    NumReplace()        # Calculate number of replacements
    SortI('Name')       # Sort devices


#################### Initiate Algorithm: ####################

Variables()    # Initiates main variables
ReadDevices()  # Reads Devices.csv to get device parameters
Startup()      # Runs all calculation functions
OutputWindow() # All commands in OutputWindow reopen OutputWindow

