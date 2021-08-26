# encoding: utf-8
##############################################################
#						   Imports
# hongtao.tan@ansys.com   2020-06-15
##############################################################
from BaseExampleUDO import BaseExampleUDOClass
from math import *


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


class UDOExtension(BaseExampleUDOClass):
    # self.Data.AddSweep("Freq")
    _kOutputs = [['FFT_mag', '']]
    _kDynamicProbes = []
    _kInputs = []

    def __init__(self):
        for vName, unit in self._kOutputs:
            self.Data.AddDoubleQuantity("FFT Mag Value", vName, unit)

        self.Data.AddDoubleProbe("Solution", "Select a transient field quantity", "Transient", "")
        self._kInputs = ["Harmonic order", '5', 'input Harmonic order']

    # -- ISA IUDOPluginExtension --------------
    def GetUDSDescription(self):
        return "FFT1D"

    # -- ISA IUDOPluginExtension --------------
    def GetUDSName(self):
        return "FFT"

    # -- ISA IUDOPluginExtension --------------
    def GetInputUDSParams(self, udsParams, propList, userSelectedDynamicProbes):
        # call base class to fill in the uds params
        BaseExampleUDOClass.GetInputUDSParams(self, udsParams, propList, userSelectedDynamicProbes)

        prop = propList.AddNumberProperty(self._kInputs[0], self._kInputs[1])
        prop.Description = self._kInputs[2]

    def Compute(self, inData, outData, params, progMon):
        sweeps = inData.GetSweepNamesForProbe("Solution")
        data = inData.GetDoubleProbeData("Solution")

        data_fft = [abs(a) * 2.0 / len(data[:-1]) for a in dft(data[:-1])]
        data_fft[0] = data_fft[0] / 2.0

        order = int(params.GetNumberProperty(self._kInputs[0]).ValueSI)
        Outputs = [data_fft[order]]

        for vName, value in zip(zip(*self._kOutputs)[0], Outputs):
            outData.SetDoubleQuantityData(vName, [value])

        return True
