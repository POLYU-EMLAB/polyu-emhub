# emTools

Resources and tools for electric machines and wireless power transfer systems

## 目录 Index

* [1. 论文相关 / Papers](#1-论文相关--papers)
* [2. 文档 / Useful documents](#2-文档--useful-documents)
* [3. 特别主题 / Special topics](#3-特别主题--special-topics)
* [4. 资源 / Resources](#4-资源--resources)
* [5. 工具 / Tools](#5-工具--tools)
* [6. 讨论区 / Discussion](#6-讨论区--Discussion)

常用简写 / Abbreviations ：

- AEDT: ANSYS Electronics Desktop，ANSYS推出的电磁套件，包含Maxwell，HFSS，Simplorer等。
- TBD: TBD常指“有待讨论（To Be Discussed）”、“有待完善（To Be Done）”、“有待定义（To Be
  Defined）”及“有待决定（To Be Decided或To Be Determined）”。

# [1. 论文相关 / Papers](#目录-index)

## 1.1 期刊 / Journals

- [TIE](http://www.ieee-ies.org/pubs/transactions-on-industrial-electronics)
  IEEE Transactions on Industrial Electronics
- [TPE](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=63) IEEE
  Transactions on Power Electronics
- [TII](http://www.ieee-ies.org/pubs/transactions-on-industrial-informatics)
  IEEE Transactions on Industrial Informatics
- [TMAG](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=20) IEEE
  Transactions on Magnetics
- [ENERGIES](https://www.mdpi.com/journal/energies) Energies

## 1.2 会议 / Conferences

- COMPUMAG
- Intermag
- CEFC

## 1.3作者 / Authors

### 1.3.1 实验室 / Lab

- [Weinong Fu](https://scholar.google.com/citations?user=itDH2QIAAAAJ&hl=zh-CN&oi=sra)
- [Shuangxia Niu](https://scholar.google.com/citations?user=lIH-GZIAAAAJ&hl=zh-CN&oi=ao)
- [Xing Zhao](https://scholar.google.com/citations?user=CvpxdLgAAAAJ&hl=zh-CN&oi=sra)

### 1.3.2 世界范围 / Worldwide

- [Thomas A. Lipo](https://scholar.google.com/citations?user=tqHzsE0AAAAJ&hl=zh-CN&oi=ao)
- [K.T. Chau](https://scholar.google.com/citations?user=5wptXfQAAAAJ&hl=zh-CN)

持续收集中…… TBD

# [2. 文档 / Useful documents](#目录-index)

- [中国电机标准(GB electrical machinery standards)](http://www.msckobe.com/links/electrical_machinery/gb.htm)
- [IEC电机标准(IEC electrical machinery standards)](http://www.msckobe.com/links/electrical_machinery/iec.htm)
- [各类电机教程、教材](https://github.com/POLYU-EMLAB/useful-resources)

# [3. 特别主题 / Special topics](#目录-index)

## 3.1 冻结磁导率 / Frozen Permeability

- [Frozen Permeability](docs/FrozenPermeability) 毕言鼎整理，姜霁芙正在预备整理。

## 3.2 双转子电机 /

## 3.3 电机优化 / Optimal design of electric machines

### 3.3.1 Tutorials

- [如何进行永磁同步电机全局优化设计](https://zhuanlan.zhihu.com/p/43476298)
  知乎老哥写的挺好的，可以作为入门教程学习一下流程

### 3.3.2 优化算法

- [Platypus](https://github.com/Project-Platypus/Platypus)
  一个简单好用的进化算法库，编程语言python，可用于电机优化
- [jMetalPy](https://github.com/jMetal/jMetalPy) A framework for
  single/multi-objective optimization with metaheuristics. 知名算法库
- [scipy.fft](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html)
  scipy包中的fft模块，可用于谐波分析、寻找功角、 计算功率因数等。AEDT程序目录中自带。具体路径在
  ```C:\Program Files\AnsysEM\AnsysEM21.1\Win64\commonfiles\CPython\3_7\winx64\Release\python\Lib\site-packages```
  ， 其中 AnsysEM的版本必须是21.x，如果是之前版本，则不包含scipy。也可以使用python自带的math库实现dft，详见下一个工具。

### 3.3.3 优化时用的小工具

- [Maxwell傅里叶分析UDO](docs/Maxwell_FFT_UDO)
  电机的优化设计问题永远也绕不开对谐波的优化，虽然Maxwell后处理中自带了快速FFT功能，
  但是该功能无法直接输出某次谐波的幅值作为优化的目标函数，很多工程师一直认为Maxwell无法实现这个功能，事实上，Maxwell的后处理程序中包含了
  丰富的数学函数库，我们在理解了FFT理论的基础上，可利用这些数学函数库编写表达式抽取出任意次数的谐波幅值并作为优化的目标，
  另外还有一种方法是编写UDO脚本，输出任意阶次的谐波幅值。本次教程通过反电势、气隙磁密、电磁力三个例子介绍上述两种方法，希望对各位有所帮助。
  [[1]](https://mp.weixin.qq.com/s/2TduEvN2K7TRVHnyYjFl1w)
- [Maxwell UDO 脚本：输出二维傅里叶分析结果](docs/FFT2D)  电机振动噪声的主要激励源是定子受到的时变电磁力，它与结构模态叠加，
  在某些频段引起谐振。削弱电机振动幅度的关键是削弱对应阶次电磁力幅值，电机中的电磁力是非常复杂的，它是时间和空间的函数，包含了时间和空间谐波。
  为了提取某一时间空间次数的电磁力谐波，必须用到二维傅里叶分析，Maxwell目前没有这个功能，为此，我们基于AEDT的UDO框架开发了专用于二维傅里叶分析的脚本。
  利用该脚本，用户可轻松提取电磁力时空谐波幅值，并将其作为优化设计的目标函数，进而从源头上实现电机的减振降噪优化设计
  [[2]](https://mp.weixin.qq.com/s/v7qDxoEzgOW3OOCqA1tnmg)
- [Maxwell 自定义 UDP：V_Shape_IPM_Rotor](docs/CustomizedVShapeRotor_UDP)
  对于一些特定领域的电机产品来说，几何模型往往十分复杂
  且千变万化，内置UDP库往往无法满足实际需求，为此ANSYS中国技术团队陆续定制开发了一系列UDP模型，帮助工程师更方便的实现快速参数化建模。
  本次发布的是一个IPM转子UDP模型，该模型支持V、一、双V、双一、V一等组合的磁钢结构，同时支持转子表面辅助槽
  [[3]](https://mp.weixin.qq.com/s/VoS69h_77vRAndxsIJejzQ)
- [aedtfile](https://github.com/POLYU-EMLAB/aedtfile) aedtfile是用于解析Ansys
  Electronics文件的库，目前可用于优化时修改变量。
- [SALib](https://github.com/SALib/SALib) Sensitivity Analysis Library in
  Python. Contains Sobol, Morris, FAST, and other methods. 用于做敏感度分析的库，可以用于电机优化。

### 3.3.4 拓扑结构优化

- [DTU topopt group](https://www.topopt.mek.dtu.dk) The TopOpt group at DTU
  Mechanical Engineering is world leading within development and applications
  of density based topology optimization methods. TopOpt is an acronym for
  Topology Optimization and the group is a joined research effort between the
  departments of DTU Mechanical Engineering and DTU Compute with the aim of
  promoting theoretical extensions and practical applications of the topology
  optimization method. The group is involved in a number of multidisciplinary
  research projects sponsored from national and international sources.
- [TopOpt_in_PETSc](https://github.com/topopt/TopOpt_in_PETSc) A 3D large-scale
  topology optimization code using PETSc. The code (or framework) presented on
  this page is a fully parallel framework for conducting very large scale
  topology optimziation on structured grids. For more details
  see www.topopt.dtu.dk/PETSc.
- [topy](https://github.com/williamhunter/topy) Topology Optimization using
  Python, DTU的作品
- [TopOpt-MMA-Python](https://github.com/arjendeetman/TopOpt-MMA-Python)
  Example application of the GCMMA-MMA-Python repo in topology optimization.
- [topopt参考代码](https://github.com/AJJLagerweij/topopt) Topology
  optimization，开源的参考代码。非知名作者。
- [ezdxf](https://github.com/mozman/ezdxf) Python interface to DXF,
  似乎有autodesk支持
- [potrace](https://github.com/tatarize/potrace) Pure Python Port of Potrace

## 3.4 电磁计算 / Computational electromagnetics

### 3.4.1 网格

- [trimesh](https://github.com/mikedh/trimesh) Python library for loading and
  using triangular meshes.
- [triangle](https://github.com/libigl/triangle) A Two-Dimensional Quality Mesh
  Generator and Delaunay Triangulator.
- [gmsh](https://gmsh.info) A three-dimensional finite element mesh generator
  with built-in pre- and post-processing facilities.
- [netgen](https://ngsolve.org) Netgen is a part of high performance
  multiphysics finite element software. 网格是好的，据我观察ANSYS Maxwell似乎时用netgen。
- [tetgen](https://github.com/libigl/tetgen) A Quality Tetrahedral Mesh
  Generator and a 3D Delaunay Triangulator.

### 3.4.2 求解器

- [FEMM](https://github.com/cenit/FEMM) Finite Element Method Magnetics: A
  Windows finite element solver for 2D and axisymmetric magnetic,
  electrostatic, heat flow, and current flow problems with graphical pre- and
  post-processors.
- [ONELAB](https://onelab.info) Open Numerical Engineering LABoratory
  相对好用的通用FEM软件。
- [fealpy](https://github.com/weihuayi/fealpy) Finite Element Analysis Library
  in Python. 作者：湘潭大学 魏华祎
- [FEMFX](https://github.com/GPUOpen-Effects/FEMFX) FEMFX is a multithreaded
  CPU library for deformable material physics, using the Finite Element
  Method (FEM). AMD写的

### 3.4.3 可视化

- [FastCAE](https://github.com/DISOGitHub/FastCAE) FastCAE，是一套开源国产CAE软件集成开发平台。
- [pyvista](https://github.com/pyvista/pyvista) 3D plotting and mesh analysis
  through a streamlined interface for the Visualization Toolkit (VTK)
- [OCCT](https://github.com/Open-Cascade-SAS/OCCT) Open CASCADE Technology (
  OCCT) is an open-source software development platform for 3D CAD, CAM, CAE.
- [pyocc](https://github.com/tpaviot/pythonocc-core) Python package for 3D
  CAD/BIM/PLM/CAM

### 3.4.4 专用软件

- [ACMSimPy](https://github.com/horychen/ACMSimPy) 作者horychen, AC Machine
  Simulation in Python

### 3.4.5 Input/Output

- [meshio](https://github.com/nschloe/meshio) input/output for many mesh
  formats

## 3.5 电机控制 / Control Methods for Electrical Machines

### 3.5.1 软件

- [Simulink](https://www.mathworks.com/help/simulink/getting-started-with-simulink.html)
  Simulink, yyds.
- [emachinery](https://github.com/horychen/emachinery) A package for analysis
  of electric machinery.
- [ACMSIMC_TUT](https://github.com/horychen/ACMSIMC_TUT) AC Machine Simulation
  in C (Tutorial Version)

### 3.5.2 硬件方案

- [dSPACE](https://www.dspace.com) 位于德国帕德博恩的dSPACE
  GmbH是用于开发电子控制单元的工具的世界领先供应商之一。
- [RTUnit](http://www.rtunit.com) dSPACE的国产替代，网站不行，淘宝购买方便。
- [Xilinx IIoT-EDDP](https://github.com/Xilinx/IIoT-EDDP) Xilinx的电机驱动方案
- [FpOC](https://github.com/WangXuan95/FpOC) FPGA-based Field Oriented
  Control (FOC) for driving PMSM motor. 中文Readme，写的非常详细。
- [Creeper](https://github.com/ChenJin0927/Creeper) 基于DRV8301的开源无刷电机矢量控制器

## 3.6 机器学习与电机 / Machine learning and electric machines

### 3.6.1 平台

- [tensorflow](https://www.tensorflow.org)
  TensorFlow是一个开源软件库，用于各种感知和语言理解任务的机器学习。Google主力
- [pytorch](https://pytorch.org)
  PyTorch是一个开源的Python机器学习库，基于Torch，底层由C++实现，应用于人工智能领域，如自然语言处理。
  它最初由Facebook的人工智能研究团队开发

### 3.6.2 Models

- [Onnx Model](https://github.com/onnx/models) A collection of pre-trained,
  state-of-the-art models in the ONNX format

## 3.7 无线传能 / Wireless Power Transfer

TBD

# [4. 资源 / Resources](#目录-index)

## 4.1 可以关注的up主 / The people you can follow

- [我是大鳄鱼](https://space.bilibili.com/37260118) 据说来自华中
- [豪底狄](https://space.bilibili.com/7132537/dynamic)
  浙大博士[陈嘉豪](https://horychen.github.io)， 目前方向为无轴承感应电机、控制、电机设计相关软件等，目前在NTU。
- [Mark Weng](https://mark-weng.com) Mark Weng,
  电机设计工程师&程序员，目前在台湾“國家高速網路與計算中心”工作。最近似乎在开发基于 AI的电机设计系统。

## 4.2 模型资源 / Model resources

- [电机模型](https://github.com/POLYU-EMLAB/motor_lib) 不同电机结构的模型，包括SPM、IPM等常见电机。

## 4.3 视频资源 / Video resources

### 4.3.1 Maxwell 操作 / Maxwell Hints

- 效率、功率因数计算
  [b站链接](https://www.bilibili.com/video/BV1MZ4y1F7dv)

- 【学习分享】ANSYS Maxwell中如何提取磁场轴向分量与径向分量丨场计算器的简单应用
  [b站链接](https://www.bilibili.com/video/BV1c5411e7Yr)

- 最大转矩/电流角丨内置V型转子丨Maxwell电机仿真丨罗小黑战记
  [b站链接](https://www.bilibili.com/video/BV1yA411g7oK)

## 4.4 编程学习资源 / Learning program language resources

- [Sololearn](www.sololearn.com) Courses designed by experts with real-world
  practice. 一个适合初学者的编程学习网站，里面有大量免费的课程，非常实用。只要学习一遍，非计算机专业编程基本没有问题了。
- [Jetbrains免费教育许可证](https://www.jetbrains.com/community/education/#students)
  软件开发者和团队的必备工具。JetBrains开发工具免费提供学生和教师使用。取得授权后只需要使用相同的 JetBrains
  帐号就可以激活其他产品，不需要重复申请。
- [GitHub 学生开发包](https://docs.github.com/cn/education/explore-the-benefits-of-teaching-and-learning-with-github-education/use-github-for-your-schoolwork/apply-for-a-student-developer-pack)
  作为学生，可以申请 GitHub Student Developer Pack，其中包括 GitHub 合作伙伴的特惠和福利。

# [5. 工具 / Tools](#目录-index)

- [pyaedt](https://github.com/pyansys/PyAEDT)
  ANSYS官方推出的基于.net和python的脚本工具，用于操作ANSYS Electronics Desktop。
- [AutoWinding](https://github.com/POLYU-EMLAB/AutoWinding) 在ANSYS Maxwell
  2D/3D中为交流/直流电机排绕组及计算槽星型矢量图、相关参数。作者江明远，欢迎发送邮件至nmyjiang@foxmail.com或直接找他debug。
- [getPF](https://github.com/POLYU-EMLAB/getPF)
  用C++和matlab写的求功率因数的程序，作者吴会欢，2017年写的，如果有问题请至issue留言。
- [Electrical Machines Design Automation by Ansys Maxwell Script](https://github.com/MarkWengSTR/ansys-maxwell-EM-design-online)
  It is a Electrical Machines Design Automation by Ansys Maxwell Script.
  从事电机设计的台湾小哥Mark Weng写的，搞得很好。

# [6. 讨论区 / Discussion](#目录-index)

点[这里](https://github.com/POLYU-EMLAB/emTools/discussions)进入讨论区。请勿发与学科无关内容。
