# encoding: utf-8
##############################################################
#						   Imports
# hongtao.tan@ansys.com
# wang.yang@ansys.com
##############################################################
import os, sys,clr
from BaseExampleUDO import BaseExampleUDOClass
from math import *
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import *
from System.Drawing import *
import datetime

# 定义输出FFT_data的数据类型，0：幅值， 1：复数
data_type = 0


def dft(x, inverse=False):
    N = len(x)
    inv = -1 if not inverse else 1
    X = [0] * N
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * e ** (inv * 2j * pi * k * n / N)
        if inverse:
            X[k] /= N
    return X


def dft2(x):
    y = [dft(a) for a in x]
    y = [dft(a) for a in zip(*y)]
    y = zip(*y)
    return y

def myfun(aaa):
    aaa = list(aaa)
    for j in range(len(aaa)):
        for i, a in enumerate(aaa):
            try:
                if a.isdigit() and aaa[i + 1].isalpha():
                    del aaa[i + 1]
            except:
                break
    return ''.join(aaa)

class UDOExtension(BaseExampleUDOClass):
    _kOutputs = [['Mag', '']]
    _kDynamicProbes = []
    _kInputs = []
    reportName = "FieldReport"

    def __init__(self):
        for vName, unit in self._kOutputs:
            self.Data.AddDoubleQuantity("FFT2D", vName, unit)

        sweepNames = ["Distance", "Time"]
        self.Data._sweepNames = sweepNames
        self.Data.AddDoubleProbe(self.reportName, "Select a transient field quantity", "Fields", "AirgapLine")
        self._kInputs.append(["Order of time domain", '0', 'Multiples of fundamental electric frequency'])
        self._kInputs.append(["Order of space domain", '0', 'Number of spatial modes, can be positive or negative'])
        self._kInputs.append(["Export FFT2D datatable ?", ['Yes', 'No'], 'Select Yes or No'])
        self._kInputs.append(
            ["Maximum time order", '0', 'The largest number of time domain order to export, input 0 for all orders'])
        self._kInputs.append(
            ["Maximum space order", '0', 'The largest number of space domain order to export, input 0 for all orders'])


    # -- ISA IUDOPluginExtension --------------
    def GetUDSDescription(self):
        return "FFT2D"

    # -- ISA IUDOPluginExtension --------------
    def GetUDSName(self):
        return "FFT2D"

    # -- ISA IUDOPluginExtension --------------
    def GetInputUDSParams(self, udsParams, propList, userSelectedDynamicProbes):
        # call base class to fill in the uds params
        BaseExampleUDOClass.GetInputUDSParams(self, udsParams, propList, userSelectedDynamicProbes)

        for name, value, description in self._kInputs:
            if isinstance(value, list):
                prop = propList.AddMenuProperty(name, value)
            else:
                prop = propList.AddNumberProperty(name, value)
            prop.Description = description

    def Compute(self, inData, outData, params, progMon):
        sweepNames1 = inData.GetSweepNamesForProbe(self.reportName)
        time = inData.GetSweepsDataForProbe(self.reportName, sweepNames1[1])
        distance = inData.GetSweepsDataForProbe(self.reportName, sweepNames1[0])
        data = inData.GetDoubleProbeData(self.reportName)

        distance = list(set(distance))
        distance.sort()
        distance = distance[:-1]

        time = list(set(time))
        time.sort()
        time = time[:-1]

        data = zip(*([iter(data)] * (len(distance) + 1)))
        data = [a[:-1] for a in data[:-1]]
        fft2_data = dft2(data)
        factor = len(time) * len(distance) / 2.0
        fft2_abs = [[abs(b) / factor for b in a] for a in fft2_data]
        fft2_abs[0][0] /= 2.0

        if data_type == 1:
            fft2_data = dft2(data)
            fft2_Complex = [[b / factor for b in a] for a in fft2_data]
            fft2_Complex[0][0] /= 2.0

        Order1 = params.GetNumberProperty(self._kInputs[0][0]).ValueSI
        Order2 = params.GetNumberProperty(self._kInputs[1][0]).ValueSI

        if Order2 < 0:
            Order2 += len(distance)
        Outputs = [fft2_abs[(len(time) - int(Order1)) % len(time)][int(Order2)]]

        outData.SetSweepsData("Distance", [0.0])
        outData.SetSweepsData("Time", [0.0])

        for vName, value in zip(zip(*self._kOutputs)[0], Outputs):
            outData.SetDoubleQuantityData(vName, [value])

        export = params.GetMenuProperty(self._kInputs[2][0]).SelectedMenuChoice
        if export == 'Yes':
            max_time_order = params.GetNumberProperty(self._kInputs[3][0]).ValueSI
            max_space_order = params.GetNumberProperty(self._kInputs[4][0]).ValueSI
            path = os.getcwd()
            csv_path = os.path.join(path, 'FFT2D_data.csv')

            if data_type == 1:
                fft2_abs = list(fft2_Complex)

            new_fft2_abs = fft2_abs[1:]
            new_fft2_abs.append(fft2_abs[0])
            export_data = list(reversed(new_fft2_abs))
            new_export_data = []
            if int(max_space_order) == 0:
                if len(distance) % 2 == 1:
                    max_space_order = (len(distance) - 1) / 2
                else:
                    max_space_order = (len(distance)) / 2 - 1

            if int(max_time_order) == 0:
                if len(time) % 2 == 1:
                    max_time_order = (len(time) - 1) / 2
                else:
                    max_time_order = (len(time)) / 2 - 1

            for each in export_data[0:int(max_time_order) + 1]:
                aa = []
                aa = (each[-int(max_space_order) + len(distance):])
                aa = aa + (each[0:int(max_space_order) + 1])
                new_export_data.append(aa)

            length = len(new_export_data)
            with open(csv_path, 'w') as file:
                file.write(
                    r'Time\Space,' + str(list(range(-int(max_space_order), int(max_space_order) + 1, 1))).strip(
                        '[').strip(']') + '\n')
                for i in range(length):
                    file.write(str(i) + ',' + str(new_export_data[i]).strip('[').strip(']') + '\n')
        return True
