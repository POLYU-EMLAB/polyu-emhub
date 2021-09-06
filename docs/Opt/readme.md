## 3.3 电机优化 / Optimal design of electric machines

### 3.3.1 Tutorials

- [如何进行永磁同步电机全局优化设计](https://zhuanlan.zhihu.com/p/43476298)
  知乎老哥写的挺好的，可以作为入门教程学习一下流程

### 3.3.2 优化算法

- [The Reed Research Group](https://reed.cee.cornell.edu)
  康奈尔大学Reed博士课题组，里面的优化算法资源非常全面好用。
- [Platypus](https://github.com/Project-Platypus/Platypus)
  一个简单好用的进化算法库，编程语言python，可用于电机优化
- [jMetalPy](https://github.com/jMetal/jMetalPy) A framework for
  single/multi-objective optimization with metaheuristics. 知名算法库
- [scipy.fft](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html)
  scipy包中的fft模块，可用于谐波分析、寻找功角、 计算功率因数等。AEDT程序目录中自带。具体路径在
  ```C:\Program Files\AnsysEM\AnsysEM21.1\Win64\commonfiles\CPython\3_7\winx64\Release\python\Lib\site-packages```
  ， 其中 AnsysEM的版本必须是21.x，如果是之前版本，则不包含scipy。也可以使用python自带的math库实现dft，详见下一个工具。

### 3.3.3 优化时用的小工具

- [Maxwell傅里叶分析UDO](../Maxwell_FFT_UDO/Readme.md)
  电机的优化设计问题永远也绕不开对谐波的优化，虽然Maxwell后处理中自带了快速FFT功能，
  但是该功能无法直接输出某次谐波的幅值作为优化的目标函数，很多工程师一直认为Maxwell无法实现这个功能，事实上，Maxwell的后处理程序中包含了
  丰富的数学函数库，我们在理解了FFT理论的基础上，可利用这些数学函数库编写表达式抽取出任意次数的谐波幅值并作为优化的目标，
  另外还有一种方法是编写UDO脚本，输出任意阶次的谐波幅值。本次教程通过反电势、气隙磁密、电磁力三个例子介绍上述两种方法，希望对各位有所帮助。
  [[1]](https://mp.weixin.qq.com/s/2TduEvN2K7TRVHnyYjFl1w)
- [Maxwell UDO 脚本：输出二维傅里叶分析结果](../FFT2D/Readme.md)  电机振动噪声的主要激励源是定子受到的时变电磁力，它与结构模态叠加，
  在某些频段引起谐振。削弱电机振动幅度的关键是削弱对应阶次电磁力幅值，电机中的电磁力是非常复杂的，它是时间和空间的函数，包含了时间和空间谐波。
  为了提取某一时间空间次数的电磁力谐波，必须用到二维傅里叶分析，Maxwell目前没有这个功能，为此，我们基于AEDT的UDO框架开发了专用于二维傅里叶分析的脚本。
  利用该脚本，用户可轻松提取电磁力时空谐波幅值，并将其作为优化设计的目标函数，进而从源头上实现电机的减振降噪优化设计
  [[2]](https://mp.weixin.qq.com/s/v7qDxoEzgOW3OOCqA1tnmg)
- [Maxwell 自定义 UDP：V_Shape_IPM_Rotor](../CustomizedVShapeRotor_UDP/Readme.md)
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
  of density based topology optimization methods. 丹麦DTU的拓扑结构优化组，牛。
- [TopOpt_in_PETSc](https://github.com/topopt/TopOpt_in_PETSc) A 3D large-scale
  topology optimization code using PETSc. The code (or framework) presented on
  this page is a fully parallel framework for conducting very large scale
  topology optimziation on structured grids. For more details
  see www.topopt.dtu.dk/PETSc.
- [topy](https://github.com/williamhunter/topy) Topology Optimization using
  Python, DTU的作品
- [Engineering Design Research Laboratory](https://edrl.et.iupui.edu/)
  印第安纳大学与普渡大学印第安纳波利斯联合分校的工程设计组。值得关注
- [top3d](https://www.top3d.app/) 3D拓扑结果优化程序，EDRL组作品。
- [TopOpt-MMA-Python](https://github.com/arjendeetman/TopOpt-MMA-Python)
  Example application of the GCMMA-MMA-Python repo in topology optimization.
- [topopt参考代码](https://github.com/AJJLagerweij/topopt) Topology
  optimization，开源的参考代码。非知名作者。
- [ezdxf](https://github.com/mozman/ezdxf) Python interface to DXF,
  似乎有autodesk支持
- [potrace](https://github.com/tatarize/potrace) Pure Python Port of Potrace
