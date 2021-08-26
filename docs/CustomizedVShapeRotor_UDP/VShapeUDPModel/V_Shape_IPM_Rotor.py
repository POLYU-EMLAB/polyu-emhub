# encoding: utf-8

##############################################################
# 作者：王杨(ANSYS China)于2019年8月
# 联系方式：wang.yang@ansys.com
# 使用过程中，如果有问题或者改进建议，欢迎联系我！
##############################################################
#                           Imports
##############################################################
import sys 
from math import *
##############################################################
#                           Constants
##############################################################
primitiveInfo = UDPPrimitiveTypeInfo(
	name = "V_Shape_IPM_Rotor",
	purpose = "Create a Rotor in XY plane",
	company = "ANSYS China wang.yang@ansys.com",
	date = "8-5-2019",
	version = "1.0")

defaultPrimitiveParams = [
	"100.0", 
	"50.0",
	"20.0",
	"8",
	"120.0",
	"15.0",
	"8.0",
	"0.5",
	"5.0",
	"1.0",
	"3.0",
	"4.0",
	"0.1",
	"0.3",
	"1.5",
	"135.0",
	"0.5",
	"0.5",
	"1.5",
	"3.5",
	"1.5",
	"120.0",
	"1.2",
	"1.5",
	"3.0",
	"1.5",
	"2.0",
	"0.3",
	"0.5",
	"0.5",
	"0.5",
	"0.5",
	"0.5",
	"0.5",
	"0",
	"0"]

primitiveParamDefs = [  UDPPrimitiveParameterDefinition2(
							"Outer_Diameter", 
							"Core diameter on gap side", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double,defaultPrimitiveParams[0])), #1 parameter
						
						UDPPrimitiveParameterDefinition2(
							"Inner_Diameter", 
							"Core diameter on yoke side", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[1])), #2 parameter
									
						UDPPrimitiveParameterDefinition2(
							"Core_Length", 
							"Core length", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double,defaultPrimitiveParams[2])), #3 parameter
							
							
						UDPPrimitiveParameterDefinition2(
							"Poles", 
							"Number of Poles", 
							UnitType.NoUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeInt, 
							UDPParam(ParamDataType.Int, defaultPrimitiveParams[3])), #4 parameter	
									
						UDPPrimitiveParameterDefinition2(
							"Notch_Angle", 
							"", 
							UnitType.AngleUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[4])), #4 NA
							
						UDPPrimitiveParameterDefinition2(
							"Notch_Offset_Angle1", 
							"", 
							UnitType.AngleUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double,defaultPrimitiveParams[5])), #5 NOA1							
							

						UDPPrimitiveParameterDefinition2(
							"Notch_Offset_Angle2", 
							"", 
							UnitType.AngleUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[6])), #4 NOA2	
							
						UDPPrimitiveParameterDefinition2(
							"Notch_Depth", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[7])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Notch_Fillet1", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[8])), #4 ND	

						UDPPrimitiveParameterDefinition2(
							"Notch_Fillet2", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[9])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Notch_Fillet3", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[10])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Magnet_Thickness", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[11])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Magnet_Gap", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[12])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Magnet_Fillet", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[13])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Magnet_Step", 
							"", 
							UnitType.AngleUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[14])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"V_Angle", 
							"",  
							UnitType.AngleUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[15])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"Magnet_Lip_in", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[16])), #4 ND	
							
							
						UDPPrimitiveParameterDefinition2(
							"Magnet_Lip_out", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[17])), #4 ND	
							
						UDPPrimitiveParameterDefinition2(
							"CenterBrige_Width", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[18])), #4 ND	

						UDPPrimitiveParameterDefinition2(
							"CenterBrige_Length", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[19])), #4 parameter	

						UDPPrimitiveParameterDefinition2(
							"w1", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[20])), #4 parameter


						UDPPrimitiveParameterDefinition2(
							"Pole_Arc_Angle", 
							"",  
							UnitType.AngleUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[21])), #4 parameter

						UDPPrimitiveParameterDefinition2(
							"h1", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[22])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"OuterBrige_Width", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[23])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"OuterBrige_Length", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[24])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"w2", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[25])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"w3", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[26])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet0", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[27])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet1", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[28])), #4 parameter
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet2", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[29])), #4 parameter
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet3", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[30])), #4 parameter
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet4", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[31])), #4 parameter
																									
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet5", 
							"",  
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[32])), #4 parameter
							
						UDPPrimitiveParameterDefinition2(
							"Duct_Fillet6", 
							"", 
							UnitType.LengthUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeReal, 
							UDPParam(ParamDataType.Double, defaultPrimitiveParams[33])), #4 parameter
						UDPPrimitiveParameterDefinition2(
							"InfoCore", 
							"0: Rotor only; 1: Magnet only; 2: Duct only; 3: Notch only", 
							UnitType.NoUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeInt, 
							UDPParam(ParamDataType.Int, defaultPrimitiveParams[34])), #4 parameter	
							
						UDPPrimitiveParameterDefinition2(
							"Friction", 
							"0: One pole model; 1: Full model", 
							UnitType.NoUnit, 
							ParamPropType.Value, 
							ParamPropFlag.MustBeInt, 
							UDPParam(ParamDataType.Int, defaultPrimitiveParams[35])) #4 parameter	
							


]									
numParams = 36
lengthUnits = "mm"
angleUnits = "deg"

##############################################################
#                       Class Implementation
##############################################################
class UDPExtension(IUDPExtension):
	def __init__(self):
		m_StartPt = UDPPosition(0,0,0)
		m_EndPt = UDPPosition(0,0,0)


	def CreatePrimitive2(self, funcLib, paramValues):
		ret = self._Createrotor(funcLib, paramValues)
		if (ret < 0):
			funcLib.AddMessage(MessageSeverity.ErrorMessage, "Could not create UDP")
			bRet = False
		else:
			bRet = True
		return bRet



	def GetPrimitiveTypeInfo(self):
		return primitiveInfo


		
	def GetLengthParameterUnits(self):
		return lengthUnits


		
	def GetPrimitiveParametersDefinition2(self):
		return primitiveParamDefs
	

		
	def AreParameterValuesValid2(self, error, udpParams):
		return True


		
	def _Createrotor(self, funcLib, paramValues):
		OD = paramValues[0].Data
		YD = paramValues[1].Data
		Le = paramValues[2].Data
		Poles = paramValues[3].Data
		NA = paramValues[4].Data
		NOA1 = paramValues[5].Data
		NOA2 = paramValues[6].Data		
		ND = paramValues[7].Data
		NFL1 = paramValues[8].Data
		NFL2 = paramValues[9].Data		
		NFL3 = paramValues[10].Data	

		mag_thick = paramValues[11].Data
		mag_gap = paramValues[12].Data
		mag_fillet = paramValues[13].Data
		mag_step1 = paramValues[14].Data
		V_angle = paramValues[15].Data
		lip1 = paramValues[16].Data
		lip2= paramValues[17].Data
		
		CenterBrige_wide = paramValues[18].Data
		CenterBrige_len = paramValues[19].Data
		w1 = paramValues[20].Data
		pole_angle = paramValues[21].Data
		h1 = paramValues[22].Data
		
		OutBrige_wide = paramValues[23].Data
		OutBrige_len = paramValues[24].Data
		w2 = paramValues[25].Data
		w3 = paramValues[26].Data
		duct_fillet0 = paramValues[27].Data
		duct_fillet1 = paramValues[28].Data
		duct_fillet2 = paramValues[29].Data
		duct_fillet3 = paramValues[30].Data
		duct_fillet4 = paramValues[31].Data
		duct_fillet5 = paramValues[32].Data
		duct_fillet6 = paramValues[33].Data
		Info = paramValues[34].Data
		friction = paramValues[35].Data

		# test_pra = paramValues[12].Data	

		if Info == 0:
			if friction == 0:
				id_rotor,id_rotor1 = self._rotor(funcLib, OD, YD, Le, Poles, NA, NOA1, NOA2, ND, NFL1,NFL2,NFL3)
				id_duct,id_duct1 = self._duct(funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,duct_fillet0,duct_fillet1,duct_fillet2,duct_fillet3,duct_fillet4,duct_fillet5,duct_fillet6)
				funcLib.Subtract([id_rotor,id_rotor1],[id_duct,id_duct1])
			elif friction == 1:
				id_rotor,id_rotor1 = self._rotor(funcLib, OD, YD, Le, Poles, NA, NOA1, NOA2, ND, NFL1,NFL2,NFL3)
				id_duct,id_duct1 = self._duct(funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,duct_fillet0,duct_fillet1,duct_fillet2,duct_fillet3,duct_fillet4,duct_fillet5,duct_fillet6)
				funcLib.Subtract([id_rotor],[id_duct])
				funcLib.Subtract([id_rotor1],[id_duct1])
				funcLib.DuplicateAroundAxis(id_rotor,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,444)
				funcLib.DuplicateAroundAxis(id_rotor1,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,445)
		if Info == 2:
			if friction == 0:
				id_duct,id_duct1 = self._duct(funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,duct_fillet0,duct_fillet1,duct_fillet2,duct_fillet3,duct_fillet4,duct_fillet5,duct_fillet6)
			elif friction == 1:
				id_duct,id_duct1 = self._duct(funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,duct_fillet0,duct_fillet1,duct_fillet2,duct_fillet3,duct_fillet4,duct_fillet5,duct_fillet6)
				funcLib.DuplicateAroundAxis(id_duct,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,446)
				funcLib.DuplicateAroundAxis(id_duct1,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,447)
		if Info == 1:	
			if friction == 0:
				id_magnet,id_magnet1 = self._magnet(funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,mag_fillet,mag_gap)
			elif friction == 1:
				id_magnet,id_magnet1 = self._magnet(funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,mag_fillet,mag_gap)
				funcLib.DuplicateAroundAxis(id_magnet,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,448)
				funcLib.DuplicateAroundAxis(id_magnet1,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,449)
		if Info == 3:	
			if friction == 0:
				id_base,id_base1 = self._base(funcLib, OD, YD, Le, Poles)
				id_rotor,id_rotor1 = self._rotor(funcLib, OD, YD, Le, Poles, NA, NOA1, NOA2, ND, NFL1,NFL2,NFL3)

				funcLib.Subtract([id_base,id_base1],[id_rotor,id_rotor1])
				
			elif friction == 1:
				id_base,id_base1 = self._base(funcLib, OD, YD, Le, Poles)
				id_rotor,id_rotor1 = self._rotor(funcLib, OD, YD, Le, Poles, NA, NOA1, NOA2, ND, NFL1,NFL2,NFL3)
				
				funcLib.Subtract([id_base],[id_rotor])
				funcLib.Subtract([id_base1],[id_rotor1])
				funcLib.DuplicateAroundAxis(id_base,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,555)
				funcLib.DuplicateAroundAxis(id_base1,CoordinateSystemAxis.ZAxis,360.0/Poles,Poles,556)

											
		ret = 1
		return ret
		

		
	def _rotor(self, funcLib, OD, YD, Le, Poles, NA, NOA1, NOA2, ND, NFL1,NFL2,NFL3):		
		thePointArray = []
		#pp = Poles/2
		point0_x = 0.0
		point0_y = 0.5*OD
		
		point1_x = 0.5*OD*sin(pi*((NA-NOA1)/180.0)/Poles/2.0)
		point1_y = 0.5*OD*cos(pi*((NA-NOA1)/180.0)/Poles/2.0)

		point2_x = 0.5*OD*sin(pi*((NA-NOA1)/180.0)/Poles)
		point2_y = 0.5*OD*cos(pi*((NA-NOA1)/180.0)/Poles)
		
		point3_x = 0.5*(OD-2.0*ND)*sin(pi*(NA/180.0)/Poles)
		point3_y = 0.5*(OD-2.0*ND)*cos(pi*(NA/180.0)/Poles)
		
		point4_x = 0.5*OD*sin(pi*((NA+NOA2)/180.0)/Poles)
		point4_y = 0.5*OD*cos(pi*((NA+NOA2)/180.0)/Poles)	
		
		point5_x = 0.5*OD*sin((pi*((NA+NOA2)/180.0)/Poles+pi/Poles)/2.0)
		point5_y = 0.5*OD*cos((pi*((NA+NOA2)/180.0)/Poles+pi/Poles)/2.0)	

		point6_x = 0.5*OD*sin(pi/Poles)
		point6_y = 0.5*OD*cos(pi/Poles)
	
		point7_x = 0.5*YD*sin(pi/Poles)
		point7_y = 0.5*YD*cos(pi/Poles)	
		
		point8_x = 0.5*YD*sin(pi/Poles/2.0)
		point8_y = 0.5*YD*cos(pi/Poles/2.0)	
		
		point9_x = 0.0
		point9_y = 0.5*YD	

		# point7_x = YD/2.0*sin(pi/Poles)
		# point7_y = YD/2.0*cos(pi/Poles)			
		
		# point8_x = sqrt(point3_x**2.0+point3_y**2.0)*cos(pi/Poles-atan(-point3_x/point3_y))*sin(pi/Poles)
		# point8_y = sqrt(point3_x**2.0+point3_y**2.0)*cos(pi/Poles-atan(-point3_x/point3_y))*cos(pi/Poles)

		# point9_x = BP/2.0
		# point9_y = 0.5*sqrt(OD**2.0-BP**2.0)-HP2	
		
		thePointArray = []
		thePointArray.append(UDPPosition(point0_x,point0_y,0.0))
		thePointArray.append(UDPPosition(point1_x,point1_y,0.0))
		thePointArray.append(UDPPosition(point2_x,point2_y,0.0))
		thePointArray.append(UDPPosition(point3_x,point3_y,0.0))
		thePointArray.append(UDPPosition(point4_x,point4_y,0.0))
		thePointArray.append(UDPPosition(point5_x,point5_y,0.0))		
		thePointArray.append(UDPPosition(point6_x,point6_y,0.0))
		thePointArray.append(UDPPosition(point7_x,point7_y,0.0))
		thePointArray.append(UDPPosition(point8_x,point8_y,0.0))
		thePointArray.append(UDPPosition(point9_x,point9_y,0.0))
		thePointArray.append(UDPPosition(point0_x,point0_y,0.0))	
		#
		theSegArray = []
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.ArcSegment,0,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,2,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,3,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.ArcSegment,4,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,6,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.ArcSegment,7,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,9,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		# theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,9,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		# theSegArray.append(theSegDefinition)
        
		id_rotor1 = funcLib.CreatePolyline(UDPPolylineDefinition(thePointArray, theSegArray, 1, 1))
		
		funcLib.SweepAlongVector(id_rotor1,UDPVector(0.0,0.0,100.0), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
		
		blendElem = UDPBLNDElements(id_rotor1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point2_x,point2_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, NFL1, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		
		blendElem = UDPBLNDElements(id_rotor1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point3_x,point3_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, NFL2, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		
		blendElem = UDPBLNDElements(id_rotor1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point4_x,point4_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, NFL3, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)	

		id_rotor = funcLib.Section(id_rotor1,CoordinateSystemPlane.XYPlane) 
		funcLib.DeletePart(id_rotor1) 
		
		id_rotor1 = funcLib.DuplicateAndMirror(id_rotor,UDPPosition(0.0,0.0,0.0),UDPVector(-1.0,0.0,0.0))	
		# id_duct1 = self._duct(funcLib, OD, YD, Le, Poles, BM, HM, BP, HP, HP2, BLJ, RLJ)
		
		# a,b = funcLib.DuplicateAlongLine(id_duct1 , UDPVector(-BLJ-BM,0.0,0.0), 4 ,3) 
		# id_ducts = [id_duct1] + [id for id in b]
		

		# funcLib.Subtract([id_rotor],id_ducts[:])
		
		if Le != 0.0:
			funcLib.SweepAlongVector(id_rotor,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_rotor,UDPVector(0.0,0.0,-Le/2.0)) 
			funcLib.SweepAlongVector(id_rotor1,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_rotor1,UDPVector(0.0,0.0,-Le/2.0)) 
						
		return id_rotor,id_rotor1
		

	def _base(self, funcLib, OD, YD, Le, Poles):	
		point0_x = 0.0
		point0_y = 0.5*OD
		
		# point1_x = 0.5*OD*sin(pi*((NA-NOA1)/180.0)/Poles/2.0)
		# point1_y = 0.5*OD*cos(pi*((NA-NOA1)/180.0)/Poles/2.0)

		# point2_x = 0.5*OD*sin(pi*((NA-NOA1)/180.0)/Poles)
		# point2_y = 0.5*OD*cos(pi*((NA-NOA1)/180.0)/Poles)
		
		# point3_x = 0.5*(OD-2.0*ND)*sin(pi*(NA/180.0)/Poles)
		# point3_y = 0.5*(OD-2.0*ND)*cos(pi*(NA/180.0)/Poles)
		
		# point4_x = 0.5*OD*sin(pi*((NA+NOA2)/180.0)/Poles)
		# point4_y = 0.5*OD*cos(pi*((NA+NOA2)/180.0)/Poles)	
		
		# point5_x = 0.5*OD*sin((pi*((NA+NOA2)/180.0)/Poles+pi/Poles)/2.0)
		# point5_y = 0.5*OD*cos((pi*((NA+NOA2)/180.0)/Poles+pi/Poles)/2.0)	
		
		point1_x = 0.5*OD*sin(pi/Poles/2.0)
		point1_y = 0.5*OD*cos(pi/Poles/2.0)

		point2_x = 0.5*OD*sin(pi/Poles)
		point2_y = 0.5*OD*cos(pi/Poles)
	
		point3_x = 0.5*YD*sin(pi/Poles)
		point3_y = 0.5*YD*cos(pi/Poles)	
		
		point4_x = 0.5*YD*sin(pi/Poles/2.0)
		point4_y = 0.5*YD*cos(pi/Poles/2.0)	
		
		point5_x = 0.0
		point5_y = 0.5*YD	
		
		
		thePointArray = []
		thePointArray.append(UDPPosition(point0_x,point0_y,0.0))
		thePointArray.append(UDPPosition(point1_x,point1_y,0.0))
		thePointArray.append(UDPPosition(point2_x,point2_y,0.0))
		thePointArray.append(UDPPosition(point3_x,point3_y,0.0))
		thePointArray.append(UDPPosition(point4_x,point4_y,0.0))
		thePointArray.append(UDPPosition(point5_x,point5_y,0.0))		
		# thePointArray.append(UDPPosition(point6_x,point6_y,0.0))
		# thePointArray.append(UDPPosition(point7_x,point7_y,0.0))
		# thePointArray.append(UDPPosition(point8_x,point8_y,0.0))
		# thePointArray.append(UDPPosition(point9_x,point9_y,0.0))
		thePointArray.append(UDPPosition(point0_x,point0_y,0.0))	
		
		
		theSegArray = []
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.ArcSegment,0,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,2,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.ArcSegment,3,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,5,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
        
		id_base = funcLib.CreatePolyline(UDPPolylineDefinition(thePointArray, theSegArray, 1, 1))
		id_base1 = funcLib.DuplicateAndMirror(id_base,UDPPosition(0.0,0.0,0.0),UDPVector(-1.0,0.0,0.0))	
		
		
		
		if Le != 0.0:
			funcLib.SweepAlongVector(id_base,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_base,UDPVector(0.0,0.0,-Le/2.0)) 
			funcLib.SweepAlongVector(id_base1,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_base1,UDPVector(0.0,0.0,-Le/2.0)) 
						
		return id_base,id_base1
		
		
	def _solvefun1(self,a,b,c,d,e,f):
	
		x=-d*tan(1/360*f*pi) + e + ((d*tan(1/360*f*pi) - e)*tan(1/360*f*pi)/(tan(1/360*f*pi)**2 + 1.0) + 0.5*sqrt(a**2*tan(1/360*f*pi)**2 + a**2 - 4.0*a*b*tan(1/360*f*pi)**2 - 4.0*a*b - 4.0*a*c*tan(1/360*f*pi)**2 - 4.0*a*c + 4.0*b**2*tan(1/360*f*pi)**2 + 4.0*b**2 + 8.0*b*c*tan(1/360*f*pi)**2 + 8.0*b*c + 4.0*c**2*tan(1/360*f*pi)**2 + 4.0*c**2 - 4.0*d**2*tan(1/360*f*pi)**2 + 8.0*d*e*tan(1/360*f*pi) - 4.0*e**2)/(tan(1/360*f*pi)**2 + 1.0))*tan(1/360*f*pi)

		y=(d*tan(1/360*f*pi) - e)*tan(1/360*f*pi)/(tan(1/360*f*pi)**2 + 1.0) + 0.5*sqrt(a**2*tan(1/360*f*pi)**2 + a**2 - 4.0*a*b*tan(1/360*f*pi)**2 - 4.0*a*b - 4.0*a*c*tan(1/360*f*pi)**2 - 4.0*a*c + 4.0*b**2*tan(1/360*f*pi)**2 + 4.0*b**2 + 8.0*b*c*tan(1/360*f*pi)**2 + 8.0*b*c + 4.0*c**2*tan(1/360*f*pi)**2 + 4.0*c**2 - 4.0*d**2*tan(1/360*f*pi)**2 + 8.0*d*e*tan(1/360*f*pi) - 4.0*e**2)/(tan(1/360*f*pi)**2 + 1.0)

	
		return x,y
		
		
	def _solvefun2(self,a,b,k):
	# solve Intersection of line and circle in First quadrant
		x = (-b + b/(k**2 + 1) + k*sqrt(a**2*k**2 + a**2 - b**2)/(k**2 + 1))/k
		y = b/(k**2 + 1) + k*sqrt(a**2*k**2 + a**2 - b**2)/(k**2 + 1)
		return x,y
		
	def _solvefun3(self,pt1x, pt1y, k1,pt2x,pt2y,k2):
	# solve Intersection of two lines, line def by ptx pty and k
		x = (k1*pt1x - k2*pt2x - pt1y + pt2y)/(k1 - k2)
		y = (k1*(k2*pt1x - k2*pt2x + pt2y) - k2*pt1y)/(k1 - k2)
		return x,y
		
	def _magnet(self, funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,mag_fillet,mag_gap):
	
		beta = (90.0-180.0/Poles)/180.0*pi

		pp = Poles/2.0
		betaM = pole_angle/pp/2.0/180.0*pi
		point3_x = (OD/2.0-OutBrige_wide)*sin(betaM)
		point3_y = (OD/2.0-OutBrige_wide)*cos(betaM)
		
		point2_x = point3_x - cos(beta)*w2
		point2_y = point3_y - sin(beta)*w2


		OutBrige_angle = 2*asin(OutBrige_len/(OD-OutBrige_wide*2.0))
		
		
		alpha = betaM + OutBrige_angle
		point4_x = (OD/2.0-OutBrige_wide)*sin(alpha)
		point4_y = (OD/2.0-OutBrige_wide)*cos(alpha)
		
		point5_x = point4_x - cos(beta)*w3
		point5_y = point4_y - sin(beta)*w3
		
		mag_angle = (90.0-V_angle/2.0)/180.0*pi
		
		point22_x = point2_x - cos(mag_angle)*lip2
		point22_y = point2_y - sin(mag_angle)*lip2
		
		point7_x = point22_x + sin(mag_angle)*mag_thick
		point7_y = point22_y - cos(mag_angle)*mag_thick
				
		point6_x = point22_x + sin(mag_angle)*(mag_thick-mag_step1)
		point6_y = point22_y - cos(mag_angle)*(mag_thick-mag_step1)
		
		point1_x = w1+CenterBrige_wide/2.0
		point1_y = point2_y-(point2_x - w1-CenterBrige_wide/2.0)*tan(mag_angle)
		
		point0_x = CenterBrige_wide/2.0
		point0_y = point1_y + h1


		point11_x = point1_x + cos(mag_angle)*lip1
		point11_y = point1_y + sin(mag_angle)*lip1
		
		point8_x = point11_x + sin(mag_angle)*mag_thick
		point8_y = point11_y - cos(mag_angle)*mag_thick
		
		point9_x = point11_x + sin(mag_angle)*(mag_thick - mag_step1)
		point9_y = point11_y - cos(mag_angle)*(mag_thick - mag_step1)
		
		point10_x = point0_x
		point10_y = point0_y - CenterBrige_len
		
		point33_x = point22_x + sin(mag_angle)*(mag_thick-mag_gap)
		point33_y = point22_y - cos(mag_angle)*(mag_thick-mag_gap)
		
		point44_x = point11_x + sin(mag_angle)*(mag_thick-mag_gap)
		point44_y = point11_y - cos(mag_angle)*(mag_thick-mag_gap)

		thePointArray = []
		thePointArray.append(UDPPosition(point11_x,point11_y,0.0))
		thePointArray.append(UDPPosition(point22_x,point22_y,0.0))
		thePointArray.append(UDPPosition(point33_x,point33_y,0.0))
		thePointArray.append(UDPPosition(point44_x,point44_y,0.0))
		thePointArray.append(UDPPosition(point11_x,point11_y,0.0))
		
		theSegArray = []
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,0,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,1,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,2,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,3,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		
		
		id_magnet1 = funcLib.CreatePolyline(UDPPolylineDefinition(thePointArray, theSegArray, 1, 1))
		
		funcLib.SweepAlongVector(id_magnet1,UDPVector(0.0,0.0,100.0), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
		
		blendElem = UDPBLNDElements(id_magnet1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point11_x,point11_y,50.0)))
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point22_x,point22_y,50.0)))
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point33_x,point33_y,50.0)))
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point44_x,point44_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, mag_fillet, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		
		id_magnet = funcLib.Section(id_magnet1,CoordinateSystemPlane.XYPlane) 
		funcLib.DeletePart(id_magnet1) 
		
		id_magnet1 = funcLib.DuplicateAndMirror(id_magnet,UDPPosition(0.0,0.0,0.0),UDPVector(-1.0,0.0,0.0))
		
		if Le != 0.0:
			funcLib.SweepAlongVector(id_magnet,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_magnet,UDPVector(0.0,0.0,-Le/2.0)) 
			funcLib.SweepAlongVector(id_magnet1,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_magnet1,UDPVector(0.0,0.0,-Le/2.0)) 
						
		return id_magnet,id_magnet1

	def _duct(self, funcLib, OD, YD, Le, Poles, CenterBrige_wide,CenterBrige_len,w1,pole_angle,h1,OutBrige_wide, OutBrige_len, w2,lip1,lip2,mag_thick,mag_step1,V_angle,w3,duct_fillet0,duct_fillet1,duct_fillet2,duct_fillet3,duct_fillet4,duct_fillet5,duct_fillet6):
		
	
		beta = (90.0-180.0/Poles)/180.0*pi

		pp = Poles/2.0
		betaM = pole_angle/pp/2.0/180.0*pi
		point3_x = (OD/2.0-OutBrige_wide)*sin(betaM)
		point3_y = (OD/2.0-OutBrige_wide)*cos(betaM)
		
		point2_x = point3_x - cos(beta)*w2
		point2_y = point3_y - sin(beta)*w2


		OutBrige_angle = 2*asin(OutBrige_len/(OD-OutBrige_wide*2.0))
		
		
		alpha = betaM + OutBrige_angle
		point4_x = (OD/2.0-OutBrige_wide)*sin(alpha)
		point4_y = (OD/2.0-OutBrige_wide)*cos(alpha)
		
		point5_x = point4_x - cos(beta)*w3
		point5_y = point4_y - sin(beta)*w3
		
		mag_angle = (90.0-V_angle/2.0)/180.0*pi
		
		point22_x = point2_x - cos(mag_angle)*lip2
		point22_y = point2_y - sin(mag_angle)*lip2
		
		point7_x = point22_x + sin(mag_angle)*mag_thick
		point7_y = point22_y - cos(mag_angle)*mag_thick
				
		point6_x = point22_x + sin(mag_angle)*(mag_thick-mag_step1)
		point6_y = point22_y - cos(mag_angle)*(mag_thick-mag_step1)
		
		point1_x = w1+CenterBrige_wide/2.0
		point1_y = point2_y-(point2_x - w1-CenterBrige_wide/2.0)*tan(mag_angle)
		
		point0_x = CenterBrige_wide/2.0
		point0_y = point1_y + h1


		point11_x = point1_x + cos(mag_angle)*lip1
		point11_y = point1_y + sin(mag_angle)*lip1
		
		point8_x = point11_x + sin(mag_angle)*mag_thick
		point8_y = point11_y - cos(mag_angle)*mag_thick
		
		point9_x = point11_x + sin(mag_angle)*(mag_thick - mag_step1)
		point9_y = point11_y - cos(mag_angle)*(mag_thick - mag_step1)
		
		point10_x = point0_x
		point10_y = point0_y - CenterBrige_len
		
		thePointArray = []
		thePointArray.append(UDPPosition(point0_x,point0_y,0.0))
		thePointArray.append(UDPPosition(point1_x,point1_y,0.0))
		thePointArray.append(UDPPosition(point2_x,point2_y,0.0))
		thePointArray.append(UDPPosition(point3_x,point3_y,0.0))
		thePointArray.append(UDPPosition(point4_x,point4_y,0.0))
		thePointArray.append(UDPPosition(point5_x,point5_y,0.0))		
		thePointArray.append(UDPPosition(point6_x,point6_y,0.0))
		thePointArray.append(UDPPosition(point7_x,point7_y,0.0))
		thePointArray.append(UDPPosition(point8_x,point8_y,0.0))
		thePointArray.append(UDPPosition(point9_x,point9_y,0.0))
		thePointArray.append(UDPPosition(point10_x,point10_y,0.0))	
		thePointArray.append(UDPPosition(point0_x,point0_y,0.0))	
		#
		theSegArray = []
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,0,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,1,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,2,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,3,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,4,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,5,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,6,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,7,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,8,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,9,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		theSegDefinition = UDPPolylineSegmentDefinition(PolylineSegmentType.LineSegment,10,0,0.0,UDPPosition(0,0,0),CoordinateSystemPlane.XYPlane)
		theSegArray.append(theSegDefinition)
		
		
		id_duct1 = funcLib.CreatePolyline(UDPPolylineDefinition(thePointArray, theSegArray, 1, 1))
		
		funcLib.SweepAlongVector(id_duct1,UDPVector(0.0,0.0,100.0), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
		#0
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point0_x,point0_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet0, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)

		#2
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point1_x,point1_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet1, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		#3
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point2_x,point2_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet2, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		#4
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point3_x,point3_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet3, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		#5
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point4_x,point4_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet4, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		#6
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point5_x,point5_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet5, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		
				#1
		blendElem = UDPBLNDElements(id_duct1)
		listOfEdges = []		
		listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(point10_x,point10_y,50.0)))
		blendElem.ListOfEdges = listOfEdges
		blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, duct_fillet6, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		funcLib.Fillet(blendElem,  blendOpts)
		

		
		id_duct = funcLib.Section(id_duct1,CoordinateSystemPlane.XYPlane) 
		funcLib.DeletePart(id_duct1) 
		
		id_duct1 = funcLib.DuplicateAndMirror(id_duct,UDPPosition(0.0,0.0,0.0),UDPVector(-1.0,0.0,0.0))
		 
		if Le != 0.0:
			funcLib.SweepAlongVector(id_duct,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_duct,UDPVector(0.0,0.0,-Le/2.0)) 
			funcLib.SweepAlongVector(id_duct1,UDPVector(0.0,0.0,Le), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
			funcLib.Translate(id_duct1,UDPVector(0.0,0.0,-Le/2.0)) 
						
		return id_duct,id_duct1
		# id_duct = funcLib.CreateRectangle(CoordinateSystemPlane.XYPlane,UDPPosition(BLJ*1.5 + BM,OD/2.0-HP-HM,0.0),(BM,HM),1)
		
		# funcLib.SweepAlongVector(id_duct,UDPVector(0.0,0.0,10.0), UDPSweepOptions(SweepDraftType.RoundDraft,0.0,0.0))
		# blendElem = UDPBLNDElements(id_duct)
		
		# listOfEdges = []		
		# listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(BLJ*1.5 + BM,OD/2.0-HP-HM,5.0)))
		# listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(BLJ*1.5 + BM*2.0,OD/2.0-HP-HM,5.0)))
		# listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(BLJ*1.5 + BM,OD/2.0-HP,5.0)))
		# listOfEdges.append(funcLib.GetEdgeIDFromPosition(UDPPosition(BLJ*1.5 + BM*2.0,OD/2.0-HP,5.0)))
		
		# blendElem.ListOfEdges = listOfEdges
		# blendOpts = UDPBLNDFilletOptions(True, BLNDFilletRadiusLaw.BLNDConstantRadius, RLJ, 0.0, True, BLNDFilletType.BLNDRound, 0.0, 0.0)		
		# funcLib.Fillet(blendElem,  blendOpts)	
		# id_duct1 = funcLib.Section(id_duct,CoordinateSystemPlane.XYPlane) 
		# funcLib.DeletePart(id_duct) 		
		

		
		
	
