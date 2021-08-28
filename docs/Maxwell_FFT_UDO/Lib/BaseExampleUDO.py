##############################################################
#                           Imports
##############################################################
import sys 

from Ansys.Ansoft.ModulePluginDotNet.Common.API import *
from Ansys.Ansoft.ModulePluginDotNet.Common.API.Interfaces import *
from Ansys.Ansoft.ModulePluginDotNet.UDO.API.Interfaces import *
from Ansys.Ansoft.ModulePluginDotNet.UDO.API.Data import *


###############################################################
class ExtensionData:
	# list of strings
	_categories = []

	# {string => [string,..]
	_categoryQuantityMap = {}

	# { string -> QuantityInfo }
	_quantityTypeMap = {}

	# list of strings
	_sweepNames = []

	# list of UDSProbeParams
	_probes = []

	# Add a category if not already added.
	def AddCategory(self, catName):		
		self._ensureCategory(catName)

	def Categories(self):
		return self._categories

	# add the name of a sweep to the definition
	def AddSweep(self, sweepName):
		self._sweepNames.append(sweepName)

	def Sweeps(self):
		return self._sweepNames

	# Add a quantity to the category.
	# Possible list of params: catName, paramType
	#                          catName, paramType, FullUnitType
	def AddDoubleQuantity(self, catName, quantName, quantUnits=""):
		self._addQuantity(catName, quantName, Constants.kDoubleParamStr, quantUnits)

	def AddComplexQuantity(self, catName, quantName, quantUnits=""):
		self._addQuantity(catName, quantName, Constants.kComplexParamStr, quantUnits)

	# return the quantity names for the given category. The empty
	# list will be returned if the category is not found
	def QuantitiesForCategory(self, catName):
		if catName in self._categoryQuantityMap:
			return self._categoryQuantityMap[catName]
		else:
			return []

	# Return the quantity info for the quantity name of None if
	# not found
	def QuantInfo(self, quantName):
		if quantName in self._quantityTypeMap:
			return self._quantityTypeMap[quantName]
		else:
			return None

	# add probe definitions supplying the optional description, 
	# report type and component expression
	def AddDoubleProbe(self, probeName, probeDesc="", reportType="", componentExpression=""):
		self._addProbe( probeName, 
				probeDesc, 
				Constants.kDoubleParamStr, 
				reportType, 
				componentExpression)

	def AddComplexProbe(self, probeName, probeDesc="", reportType="", componentExpression=""):
		self._addProbe( probeName, 
				probeDesc, 
				Constants.kComplexParamStr, 
				reportType, 
				componentExpression)

	# Returns a list of UDSProbeParam objecs representing the 
	# registered probes.
	def Probes(self):
		return self._probes

	# helper methods ----------------------------------
	def _ensureCategory(self, catName):
		if catName not in self._categoryQuantityMap:
			self._categories.append(catName)
			self._categoryQuantityMap[catName] = []

	def _addQuantity(self, catName, qName, qType, qUnits):
		self._ensureCategory(catName)		
		self._categoryQuantityMap[catName].append(qName)
		self._quantityTypeMap[qName] = QuantityInfo(qType, qUnits)

	def _addProbe(self, pNm, pDesc, pType, rType, expr):
		self._probes.append( UDSProbeParams(pNm, pDesc, pType, rType, expr))



##############################################################
# The base Class
# 
# 1. Derive from this and call the class UDOExtension: like so
#    class UDOExtension(BaseExampleUDO):
#
# 2. in the __init__ method, 
#    -- Setup the outputs ------
#    // for each double quantity in a category, call
#    self.Data.AddDoubleQuantity("qtyCatName", "qtyName", "qtyUnitString")
#
#    // for each Complex quantity in a category call,
#    self.Data.AddComplexQuantity("qtyCatName", "qtyName", "qtyUnitString")
#
#    // for each sweep you want, in the order of primary/secondary: call
#    self.Data.AddSweep("sweepName")
#
#    -- setup the probes --------
#    // for each double probe, call
#    self.Data.AddDoubleProbe("probeName", "probeDesc")
#
#    // for each complex probe, call
#    self.Data.AddComplexprobe("probeName", "probeDesc")
#
# 3. override the GetUDSDescription(self) -> string method 
#
# 4. override the GeUDSName(self) -> string method 
#
# 5. If you want to add properties, override GetInputUDSParams
#    and after calling BaseExampleUDO.GetInputUDSParams(..)
#    add the needed properties to the propList.
#
# 6. Implement your Compute method.
#  
##############################################################
class BaseExampleUDOClass(IUDOPluginExtension):

	Data = ExtensionData()	


	#--- ISA IPlugin ------------------------------------
	# IPlugin API Implementation.
	def GetDescription(self):
		return self.GetUDSDescription()

	#--- ISA IUDOPluginExtension ------------------------
	# Returns list of category names
	def GetCategoryNames(self):
		return self.Data.Categories()

	#--- ISA IUDOPluginExtension ------------------------
	# returns a list of quantity names for the supplied category name
	# Remember to call self.Data.AddDoubleQuantity or
	#                  self.Data.AddComplexQuantity during __init__
	def GetQuantityNames(self, catName):
		return self.Data.QuantitiesForCategory(catName)

	#--- ISA IUDOPluginExtension ------------------------
	# Returns an instance of QuantityInfo for the qtyName supplied or None if such a 
	#   quantity could not be found
	# Remember to call self.Data.AddDoubleQuantity or
	#                  self.Data.AddComplexQuantity during __init__
	def GetQuantityInfo(self, qtyName):
		return self.Data.QuantInfo(qtyName)

	#--- ISA IUDOPluginExtension ------------------------
	# Returns list of UDSParams and list of dynamic properties
	# Adds setup time properties to the propList
	def GetInputUDSParams(self, udsParams, propList, userSelectedDynamicProbes):
 
		for param in self.Data.Probes():
			udsParams.Add(param)

		return True

	#--- ISA IUDOPluginExtension ------------------------
	# Returns list of UDSParams and list of dynamic properties
	# output UDSDynamicProbeCollection probes
	def GetDynamicProbes(self, probes):
		pass

	#--- ISA IUDOPluginExtension ------------------------
	# Returns list of sweeps names
	# Note: Remember to call self.Data.AddSweep("swpName")
	def GetUDSSweepNames(self):
		return self.Data.Sweeps()


