
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Outer_Diameter",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "100mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Inner_Diameter",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "50mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Core_Length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Poles",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "8"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Angle",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "120deg"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Offset_Angle1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "15deg"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Offset_Angle2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "8deg"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Depth",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Fillet1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Fillet2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Notch_Fillet3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Magnet_Thickness",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "4mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Magnet_Gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.1mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Magnet_Fillet",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.3mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Magnet_Step",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5deg"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:V_Angle",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "135deg"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Magnet_Lip_in",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Magnet_Lip_out",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:CenterBrige_Width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:CenterBrige_Length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Pole_Arc_Angle",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "120deg"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.2mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:OuterBrige_Width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:OuterBrige_Length",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "3mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:w2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "1.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:w3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "2mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet0",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.3mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Duct_Fillet6",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.5mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:Friction",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateUserDefinedPart(
	[
		"NAME:UserDefinedPrimitiveParameters",
		"DllName:="		, "V_Shape_IPM_Rotor.py",
		"Version:="		, "1.0",
		"NoOfParameters:="	, 36,
		"Library:="		, "PersonalLib",
		[
			"NAME:ParamVector",
			[
				"NAME:Pair",
				"Name:="		, "Outer_Diameter",
				"Value:="		, "Outer_Diameter"
			],
			[
				"NAME:Pair",
				"Name:="		, "Inner_Diameter",
				"Value:="		, "Inner_Diameter"
			],
			[
				"NAME:Pair",
				"Name:="		, "Core_Length",
				"Value:="		, "Core_Length"
			],
			[
				"NAME:Pair",
				"Name:="		, "Poles",
				"Value:="		, "Poles"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Angle",
				"Value:="		, "Notch_Angle"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Offset_Angle1",
				"Value:="		, "Notch_Offset_Angle1"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Offset_Angle2",
				"Value:="		, "Notch_Offset_Angle2"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Depth",
				"Value:="		, "Notch_Depth"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Fillet1",
				"Value:="		, "Notch_Fillet1"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Fillet2",
				"Value:="		, "Notch_Fillet2"
			],
			[
				"NAME:Pair",
				"Name:="		, "Notch_Fillet3",
				"Value:="		, "Notch_Fillet3"
			],
			[
				"NAME:Pair",
				"Name:="		, "Magnet_Thickness",
				"Value:="		, "Magnet_Thickness"
			],
			[
				"NAME:Pair",
				"Name:="		, "Magnet_Gap",
				"Value:="		, "Magnet_Gap"
			],
			[
				"NAME:Pair",
				"Name:="		, "Magnet_Fillet",
				"Value:="		, "Magnet_Fillet"
			],
			[
				"NAME:Pair",
				"Name:="		, "Magnet_Step",
				"Value:="		, "Magnet_Step"
			],
			[
				"NAME:Pair",
				"Name:="		, "V_Angle",
				"Value:="		, "V_Angle"
			],
			[
				"NAME:Pair",
				"Name:="		, "Magnet_Lip_in",
				"Value:="		, "Magnet_Lip_in"
			],
			[
				"NAME:Pair",
				"Name:="		, "Magnet_Lip_out",
				"Value:="		, "Magnet_Lip_out"
			],
			[
				"NAME:Pair",
				"Name:="		, "CenterBrige_Width",
				"Value:="		, "CenterBrige_Width"
			],
			[
				"NAME:Pair",
				"Name:="		, "CenterBrige_Length",
				"Value:="		, "CenterBrige_Length"
			],
			[
				"NAME:Pair",
				"Name:="		, "w1",
				"Value:="		, "w1"
			],
			[
				"NAME:Pair",
				"Name:="		, "Pole_Arc_Angle",
				"Value:="		, "Pole_Arc_Angle"
			],
			[
				"NAME:Pair",
				"Name:="		, "h1",
				"Value:="		, "h1"
			],
			[
				"NAME:Pair",
				"Name:="		, "OuterBrige_Width",
				"Value:="		, "OuterBrige_Width"
			],
			[
				"NAME:Pair",
				"Name:="		, "OuterBrige_Length",
				"Value:="		, "OuterBrige_Length"
			],
			[
				"NAME:Pair",
				"Name:="		, "w2",
				"Value:="		, "w2"
			],
			[
				"NAME:Pair",
				"Name:="		, "w3",
				"Value:="		, "w3"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet0",
				"Value:="		, "Duct_Fillet0"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet1",
				"Value:="		, "Duct_Fillet1"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet2",
				"Value:="		, "Duct_Fillet2"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet3",
				"Value:="		, "Duct_Fillet3"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet4",
				"Value:="		, "Duct_Fillet4"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet5",
				"Value:="		, "Duct_Fillet5"
			],
			[
				"NAME:Pair",
				"Name:="		, "Duct_Fillet6",
				"Value:="		, "Duct_Fillet6"
			],
			[
				"NAME:Pair",
				"Name:="		, "InfoCore",
				"Value:="		, "0",
				"ParamType:="		, "IntParam"
			],
			[
				"NAME:Pair",
				"Name:="		, "Friction",
				"Value:="		, "Friction"
			]
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "V_Shape_IPM_Rotor1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"V_Shape_IPM_Rotor1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "Rotor"
				]
			]
		]
	])
oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Rotor"
	])
oEditor.Paste()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rotor1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Name",
					"Value:="		, "PM"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"PM:CreateUserDefinedPart:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:InfoCore",
					"Value:="		, "1"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"Rotor"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 192,
					"G:="			, 192,
					"B:="			, 192
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"PM"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 0
				]
			]
		]
	])
	
oEditor.SeparateBody(
	[
		"NAME:Selections",
		"Selections:="		, "PM",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"CreateGroupsForNewObjects:=", False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"PM_Separate1", 
				"PM"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Color",
					"R:="			, 255,
					"G:="			, 128,
					"B:="			, 0
				]
			]
		]
	])
oEditor.CreateObjectCS(
	[
		"NAME:ObjectCSParameters",
		[
			"NAME:Origin",
			"IsAttachedToEntity:="	, True,
			"EntityID:="		, 228,
			"FacetedBodyTriangleIndex:=", -1,
			"TriangleVertexIndex:="	, -1,
			"PositionType:="	, "EdgeCenter",
			"UParam:="		, 0,
			"VParam:="		, 0,
			"XPosition:="		, "0",
			"YPosition:="		, "0",
			"ZPosition:="		, "0"
		],
		"MoveToEnd:="		, False,
		"ReverseXAxis:="	, False,
		"ReverseYAxis:="	, False,
		[
			"NAME:xAxisPos",
			"IsAttachedToEntity:="	, True,
			"EntityID:="		, 224,
			"FacetedBodyTriangleIndex:=", -1,
			"TriangleVertexIndex:="	, -1,
			"PositionType:="	, "EdgeCenter",
			"UParam:="		, 0,
			"VParam:="		, 0,
			"XPosition:="		, "0",
			"YPosition:="		, "0",
			"ZPosition:="		, "0"
		],
		[
			"NAME:yAxis",
			"DirectionType:="	, "AbsoluteDirection",
			"EdgeID:="		, -1,
			"FaceID:="		, -1,
			"xDirection:="		, "-0.707106781186545",
			"yDirection:="		, "0.70710678118655",
			"zDirection:="		, "0",
			"UParam:="		, 0,
			"VParam:="		, 0
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ObjectCS1",
		"PartName:="		, "PM_Separate1"
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"PM_Separate1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Orientation",
					"Value:="		, "ObjectCS1"
				]
			]
		]
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global",
		"RegionDepCSOk:="	, False
	])
oEditor.CreateObjectCS(
	[
		"NAME:ObjectCSParameters",
		[
			"NAME:Origin",
			"IsAttachedToEntity:="	, True,
			"EntityID:="		, 214,
			"FacetedBodyTriangleIndex:=", -1,
			"TriangleVertexIndex:="	, -1,
			"PositionType:="	, "EdgeCenter",
			"UParam:="		, 0,
			"VParam:="		, 0,
			"XPosition:="		, "0",
			"YPosition:="		, "0",
			"ZPosition:="		, "0"
		],
		"MoveToEnd:="		, False,
		"ReverseXAxis:="	, False,
		"ReverseYAxis:="	, False,
		[
			"NAME:xAxisPos",
			"IsAttachedToEntity:="	, True,
			"EntityID:="		, 218,
			"FacetedBodyTriangleIndex:=", -1,
			"TriangleVertexIndex:="	, -1,
			"PositionType:="	, "EdgeCenter",
			"UParam:="		, 0,
			"VParam:="		, 0,
			"XPosition:="		, "0",
			"YPosition:="		, "0",
			"ZPosition:="		, "0"
		],
		[
			"NAME:yAxis",
			"DirectionType:="	, "AbsoluteDirection",
			"EdgeID:="		, -1,
			"FaceID:="		, -1,
			"xDirection:="		, "-0.707106781186545",
			"yDirection:="		, "-0.70710678118655",
			"zDirection:="		, "0",
			"UParam:="		, 0,
			"VParam:="		, 0
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ObjectCS2",
		"PartName:="		, "PM"
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DAttributeTab",
			[
				"NAME:PropServers", 
				"PM"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Orientation",
					"Value:="		, "ObjectCS2"
				]
			]
		]
	])
oEditor.SetWCS(
	[
		"NAME:SetWCS Parameter",
		"Working Coordinate System:=", "Global",
		"RegionDepCSOk:="	, False
	])

oEditor.FitAll()