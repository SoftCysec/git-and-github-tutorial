# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:35:00 2022

@author: 25471
"""

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal as sp


def ambient():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 20 # You can change the time . it is calculationg second 
    WAVE_OUTPUT_FILENAME = "ambientnoise1.wav"

    p = pyaudio.PyAudio() 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")
    

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


    a, b = scipy.io.wavfile.read("")
    n = np.arange(len(b))/float(a)
    plt.xticks(np.arange(0, 25000))
    plt.tittle("Raw Ambient Noise in an Outside \n Environment Trial 1")
    plt.xlabel("seconds")
    plt.ylabel("ambientnoise1.wav")
    plt.plot(n, b)
    plt.grid()
    plt.show()

def voice():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 20 # You can change the time . it is calculationg second 
    WAVE_OUTPUT_FILENAME = "ambientwithvoice1.wav"

    p = pyaudio.PyAudio() 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    a, b = scipy.io.wavfile.read("ambientwithvoice1.wav")
    n = np.arange(len(b))/float(a)
    plt.xticks(np.arange(0, 25000))
    plt.tittle("Raw Ambient Noise in an Outside \n Environment Trial 1")
    plt.xlabel("seconds")
    plt.ylabel("ambientwithnoise1.wav")
    plt.plot(n, b)
    plt.grid()
    plt.show()

def combination():
    rate1,Data1 = scipy.io.wavfile.read('ambientnoise1.wav')
    rate2,Data2 = scipy.io.wavfile.read('ambientwithvoice1.wav')
    new_Data = [0]*len(Data1)
    for i in range(0,len(Data1)):
        Data1[i] -(Data1[i])
        new_Data[i] = Data2[i] + Data1[i]
        new_Data = np.array(new_Data)
        scipy.io.wavfile.write('filtered.wav', rate1,new_Data)
        
        a, b = scipy.io.wavfile.read("filtered1.wav")
        n = np.arange(len(b))/float(a)
        plt.xticks(np.arange(0, 25000))
        plt.tittle("Filtered Audio in an Outside \n Environment Trial 1")
        plt.xlabel("seconds")
        plt.ylabel("filtered1.wav")
        plt.plot(n, b)
        plt.grid()
        plt.show()
        
def ambient2():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 20 # You can change the time . it is calculationg second 
    WAVE_OUTPUT_FILENAME = "ambientnoise2.wav"

    p = pyaudio.PyAudio() 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    a, b = scipy.io.wavfile.read("ambientnoise2.wav")
    n = np.arange(len(b))/float(a)
    plt.xticks(np.arange(0, 25000))
    plt.tittle("Raw Ambient Noise in an Outside \n Environment Trial 1")
    plt.xlabel("seconds")
    plt.ylabel("ambientnoise2.wav")
    plt.plot(n, b)
    plt.grid()
    plt.show()
    
    
    
        
def voice2():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 20 # You can change the time . it is calculationg second 
    WAVE_OUTPUT_FILENAME = "ambientwithnoise2.wav"

    p = pyaudio.PyAudio() 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    a, b = scipy.io.wavfile.read("ambientwithnoise2.wav")
    n = np.arange(len(b))/float(a)
    plt.xticks(np.arange(0, 25000))
    plt.tittle("Raw Ambient Noise in an Outside \n Environment Trial 2")
    plt.xlabel("seconds")
    plt.ylabel("ambientwithnoise2.wav")
    plt.plot(n, b)
    plt.grid()
    plt.show()
    
def combination2():
        rate1,Data1 = scipy.io.wavfile.read('ambientnoise2.wav')
        rate2,Data2 = scipy.io.wavfile.read('ambientwithvoice2.wav')
        new_Data = [0]*len(Data1)
        for i in range(0,len(Data1)):
            Data1[i] -(Data1[i])
            new_Data[i] = Data2[i] + Data1[i]
            new_Data = np.array(new_Data)
            scipy.io.wavfile.write('filtered2.wav', rate1,new_Data)
            
            a, b = scipy.io.wavfile.read("filtered2.wav")
            n = np.arange(len(b))/float(a)
            plt.xticks(np.arange(0, 25000))
            plt.tittle("Filtered Audio in an Outside \n Environment Trial 1")
            plt.xlabel("seconds")
            plt.ylabel("filtered2.wav")
            plt.plot(n, b)
            plt.grid()
            plt.show()
            
def ambient3():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 20 # You can change the time . it is calculationg second 
    WAVE_OUTPUT_FILENAME = "ambientnoise3.wav"

    p = pyaudio.PyAudio() 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    a, b = scipy.io.wavfile.read("ambientnoise3.wav")
    n = np.arange(len(b))/float(a)
    plt.xticks(np.arange(0, 25000))
    plt.tittle("Raw Ambient Noise in an Outside \n Environment Trial 3")
    plt.xlabel("seconds")
    plt.ylabel("ambientnoise3.wav")
    plt.plot(n, b)
    plt.grid()
    plt.show()
    
def voice3():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 20 # You can change the time . it is calculationg second 
    WAVE_OUTPUT_FILENAME = "ambientwithnoise3.wav"

    p = pyaudio.PyAudio() 

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    a, b = scipy.io.wavfile.read("ambientwithnoise3.wav")
    n = np.arange(len(b))/float(a)
    plt.xticks(np.arange(0, 25000))
    plt.tittle("Raw Ambient Noise in an Outside \n Environment Trial 3")
    plt.xlabel("seconds")
    plt.ylabel("ambientwithnoise3.wav")
    plt.plot(n, b)
    plt.grid()
    plt.show()
    
def combination3():
    rate1,Data1 = scipy.io.wavfile.read('ambientnoise3.wav')
    rate2,Data2 = scipy.io.wavfile.read('ambientwithvoice3.wav')
    new_Data = [0]*len(Data1)
    for i in range(0,len(Data1)):
        Data1[i] -(Data1[i])
        new_Data[i] = Data2[i] + Data1[i]
        new_Data = np.array(new_Data)
        scipy.io.wavfile.write('filtered3.wav', rate1,new_Data)
        
        a, b = scipy.io.wavfile.read("filtered3.wav")
        n = np.arange(len(b))/float(a)
        plt.xticks(np.arange(0, 25000))
        plt.tittle("Filtered Audio in an Outside \n Environment Trial 1")
        plt.xlabel("seconds")
        plt.ylabel("filtered3.wav")
        plt.plot(n, b)
        plt.grid()
        plt.show()
        
    
    
    
        
    
    
    
    
    
        
    
    
























