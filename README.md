# emTools

Resources and tools for electric machines and wireless power transfer systems

常用简写 / Abbreviations ：

- AEDT: ANSYS Electronics Desktop，ANSYS推出的电磁套件，包含Maxwell，HFSS，Simplorer等。
- TBD: TBD常指“有待讨论（To Be Discussed）”、“有待完善（To Be Done）”、“有待定义（To Be Defined）”及“有待决定（To Be Decided或To Be Determined）”。

# 1. 论文相关 / Papers

## 1.1 期刊 / Journals

- [TIE](http://www.ieee-ies.org/pubs/transactions-on-industrial-electronics) IEEE Transactions on Industrial Electronics
- [TPE](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=63) IEEE Transactions on Power Electronics
- [TII](http://www.ieee-ies.org/pubs/transactions-on-industrial-informatics) IEEE Transactions on Industrial Informatics
- [TMAG](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=20) IEEE Transactions on Magnetics
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

### 1.3.2 世 界范围 / Worldwide

- [Thomas A. Lipo](https://scholar.google.com/citations?user=tqHzsE0AAAAJ&hl=zh-CN&oi=ao)
- [K.T. Chau](https://scholar.google.com/citations?user=5wptXfQAAAAJ&hl=zh-CN)

持续收集中……
TBD

# 2. 文档 / Useful documents

- [中国电机标准(GB electrical machinery standards)](http://www.msckobe.com/links/electrical_machinery/gb.htm)
- [IEC电机标准(IEC electrical machinery standards)](http://www.msckobe.com/links/electrical_machinery/iec.htm)

# 3. 特别主题 / Special issue

## 3.1 冻结磁导率 / Frozen Permeability

- [Frozen Permeability](docs/FrozenPermeability) 毕言鼎整理，姜霁芙正在预备整理。

## 3.2 双转子电机 /

## 3.3 电机优化 / Optimal design of electric machines

- [如何进行永磁同步电机全局优化设计](https://zhuanlan.zhihu.com/p/43476298) 知乎老哥写的挺好的，可以作为入门教程学习一下流程
- [Platypus](https://github.com/Project-Platypus/Platypus) 一个简单好用的进化算法库，编程语言python，可用于电机优化
- [scipy.fft](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html) scipy包中的fft模块，可用于谐波分析、寻找功角、
  计算功率因数等。AEDT程序目录中自带。具体路径在
  ```C:\Program Files\AnsysEM\AnsysEM21.1\Win64\commonfiles\CPython\3_7\winx64\Release\python\Lib\site-packages```， 其中
  AnsysEM的版本必须是21.x，如果是之前版本，则不包含scipy。也可以使用python自带的math库实现dft，详见下一个工具。
- [Maxwell傅里叶分析UDO](docs/Maxwell_FFT_UDO)  电机的优化设计问题永远也绕不开对谐波的优化，虽然Maxwell后处理中自带了快速FFT功能，
  但是该功能无法直接输出某次谐波的幅值作为优化的目标函数，很多工程师一直认为Maxwell无法实现这个功能，事实上，Maxwell的后处理程序中包含了
  丰富的数学函数库，我们在理解了FFT理论的基础上，可利用这些数学函数库编写表达式抽取出任意次数的谐波幅值并作为优化的目标，
  另外还有一种方法是编写UDO脚本，输出任意阶次的谐波幅值。本次教程通过反电势、气隙磁密、电磁力三个例子介绍上述两种方法，希望对各位有所帮助。
  [[1]](https://mp.weixin.qq.com/s/2TduEvN2K7TRVHnyYjFl1w)
- [Maxwell UDO 脚本：输出二维傅里叶分析结果](docs/FFT2D)  电机振动噪声的主要激励源是定子受到的时变电磁力，它与结构模态叠加，
  在某些频段引起谐振。削弱电机振动幅度的关键是削弱对应阶次电磁力幅值，电机中的电磁力是非常复杂的，它是时间和空间的函数，包含了时间和空间谐波。
  为了提取某一时间空间次数的电磁力谐波，必须用到二维傅里叶分析，Maxwell目前没有这个功能，为此，我们基于AEDT的UDO框架开发了专用于二维傅里叶分析的脚本。
  利用该脚本，用户可轻松提取电磁力时空谐波幅值，并将其作为优化设计的目标函数，进而从源头上实现电机的减振降噪优化设计
  [[2]](https://mp.weixin.qq.com/s/v7qDxoEzgOW3OOCqA1tnmg)
- [Maxwell 自定义 UDP：V_Shape_IPM_Rotor](docs/CustomizedVShapeRotor_UDP) 对于一些特定领域的电机产品来说，几何模型往往十分复杂
  且千变万化，内置UDP库往往无法满足实际需求，为此ANSYS中国技术团队陆续定制开发了一系列UDP模型，帮助工程师更方便的实现快速参数化建模。
  本次发布的是一个IPM转子UDP模型，该模型支持V、一、双V、双一、V一等组合的磁钢结构，同时支持转子表面辅助槽
  [[3]](https://mp.weixin.qq.com/s/VoS69h_77vRAndxsIJejzQ)

## 3.x 无线传能 / Wireless Power Transfer

TBD

## 3.x 电机控制 / Control Methods for Electrical Machines

TBD

## 3.x 机器学习与电机 / Machine learning and electric machines

TBD

# 4. 视频资源 / Video resources

## 4.1 可以关注的up主 / The people you can follow

- [我是大鳄鱼](https://space.bilibili.com/37260118) 据说来自华中
- [豪底狄](https://space.bilibili.com/7132537/dynamic) 浙大博士[陈嘉豪](https://horychen.github.io)，
  目前方向为无轴承感应电机、控制、电机设计相关软件等，目前在NTU。
- [Mark Weng](https://mark-weng.com) Mark Weng, 电机设计工程师&程序员，目前在台湾“國家高速網路與計算中心”工作。最近似乎在开发基于 AI的电机设计系统。

## 4.2 Maxwell 操作 / Maxwell Hints

- 效率、功率因数计算
  [b站链接](https://www.bilibili.com/video/BV1MZ4y1F7dv)

- 【学习分享】ANSYS Maxwell中如何提取磁场轴向分量与径向分量丨场计算器的简单应用
  [b站链接](https://www.bilibili.com/video/BV1c5411e7Yr)

- 最大转矩/电流角丨内置V型转子丨Maxwell电机仿真丨罗小黑战记
  [b站链接](https://www.bilibili.com/video/BV1yA411g7oK)

# 5. 工具 / Tools

- [pyaedt](https://github.com/pyansys/PyAEDT) ANSYS官方推出的基于.net和python的脚本工具，用于操作ANSYS Electronics Desktop。
- [AutoWinding](https://github.com/POLYU-EMLAB/AutoWinding) 在ANSYS Maxwell
  2D/3D中为交流/直流电机排绕组及计算槽星型矢量图、相关参数。作者江明远，欢迎发送邮件至nmyjiang@foxmail.com或直接找他debug。
- [getPF](https://github.com/POLYU-EMLAB/getPF) 用C++和matlab写的求功率因数的程序，作者吴会欢，2017年写的，如果有问题请至issue留言。
- [Electrical Machines Design Automation by Ansys Maxwell Script](https://github.com/MarkWengSTR/ansys-maxwell-EM-design-online)
  It is a Electrical Machines Design Automation by Ansys Maxwell Script. 从事电机设计的台湾小哥Mark Weng写的，搞得很好。
- [Platypus](https://github.com/Project-Platypus/Platypus) 一个简单好用的进化算法库，编程语言python，可用于电机优化
- [scipy.fft](https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html) scipy包中的fft模块，可用于谐波分析、寻找功角、
  计算功率因数等。AEDT程序目录中自带。具体路径在
  ```C:\Program Files\AnsysEM\AnsysEM21.1\Win64\commonfiles\CPython\3_7\winx64\Release\python\Lib\site-packages```， 其中
  AnsysEM的版本必须是21.x，如果是之前版本，则不包含scipy。也可以使用python自带的math库实现dft，详见下一个工具。
- [Maxwell傅里叶分析UDO](docs/Maxwell_FFT_UDO)  电机的优化设计问题永远也绕不开对谐波的优化，虽然Maxwell后处理中自带了快速FFT功能，
  但是该功能无法直接输出某次谐波的幅值作为优化的目标函数，很多工程师一直认为Maxwell无法实现这个功能，事实上，Maxwell的后处理程序中包含了
  丰富的数学函数库，我们在理解了FFT理论的基础上，可利用这些数学函数库编写表达式抽取出任意次数的谐波幅值并作为优化的目标，
  另外还有一种方法是编写UDO脚本，输出任意阶次的谐波幅值。本次教程通过反电势、气隙磁密、电磁力三个例子介绍上述两种方法，希望对各位有所帮助。
  [[1]](https://mp.weixin.qq.com/s/2TduEvN2K7TRVHnyYjFl1w)
- [Maxwell UDO 脚本：输出二维傅里叶分析结果](docs/FFT2D)  电机振动噪声的主要激励源是定子受到的时变电磁力，它与结构模态叠加，
  在某些频段引起谐振。削弱电机振动幅度的关键是削弱对应阶次电磁力幅值，电机中的电磁力是非常复杂的，它是时间和空间的函数，包含了时间和空间谐波。
  为了提取某一时间空间次数的电磁力谐波，必须用到二维傅里叶分析，Maxwell目前没有这个功能，为此，我们基于AEDT的UDO框架开发了专用于二维傅里叶分析的脚本。
  利用该脚本，用户可轻松提取电磁力时空谐波幅值，并将其作为优化设计的目标函数，进而从源头上实现电机的减振降噪优化设计
  [[2]](https://mp.weixin.qq.com/s/v7qDxoEzgOW3OOCqA1tnmg)
- [Maxwell 自定义 UDP：V_Shape_IPM_Rotor](docs/CustomizedVShapeRotor_UDP) 对于一些特定领域的电机产品来说，几何模型往往十分复杂
  且千变万化，内置UDP库往往无法满足实际需求，为此ANSYS中国技术团队陆续定制开发了一系列UDP模型，帮助工程师更方便的实现快速参数化建模。
  本次发布的是一个IPM转子UDP模型，该模型支持V、一、双V、双一、V一等组合的磁钢结构，同时支持转子表面辅助槽
  [[3]](https://mp.weixin.qq.com/s/VoS69h_77vRAndxsIJejzQ)
