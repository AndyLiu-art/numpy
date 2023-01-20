import streamlit as st
# 目录
st.sidebar.markdown("## 创建矩阵")
st.sidebar.markdown("### 创建向量")
st.sidebar.markdown("#### 列表元组创建向量")
st.sidebar.markdown("#### 特殊函数创建向量")
st.sidebar.markdown("### 向量重构数组")
st.sidebar.markdown("### 二维列表创建矩阵")
st.sidebar.markdown("### 特殊函数创建矩阵")
st.sidebar.markdown("### 单位阵")
# 一级标题
st.markdown("# 矩阵的创建和基本运算")
# 二级标题
st.markdown("## 创建矩阵")
# 小字
st.caption("Numpy库就是基于数组来运算的，正是因为这个，使得Python做数值计算的速度非常快。所谓数组，在代数运算中就可以理解为矩阵。一般而言，我们的矩阵是一个二维的，由行列指标组成的。")
# 小字
st.caption("Numpy的数组不仅仅支持二维的数组，还可以创建更高维度的数组，比如三维的图像数据就是使用三维数组来存储的。下面提到的矩阵，不加一般说明，就是指二维数组。")
# 文本
st.markdown("学会使用Python做矩阵计算的前提是创建矩阵，下面就给出几种不同创建矩阵的方式。")
# 文本
st.markdown("""
- 创建向量，再重构行列数，得到二维的数组。使用二维列表创建矩阵。
- 通过特殊函数创建特殊矩阵。""")
# 文本
st.markdown("上面所提到的向量，不会区分行向量还是列向量，可以理解为一行元素或者一列元素。原因有二：")
# 小字
st.caption("其一，向量不参与代数运算时，作出区分是无意义的。其二，代数运算中，向量可以直接与矩阵作运算的，但是在Python程序中是不可以的，必须是矩阵与矩阵之间作运算，也就是说，要将向量“显示地”转化为1行$n$列或者$n$行一列的矩阵。如何“显示地”转换，就是对它进行行列数重构。")
# 三级标题
st.markdown("### 创建向量")
# 文本
st.markdown("我们所说的第一种创建矩阵的方式，是先要创建向量，那么如何创建向量呢？也有两种方式：")
# 文本
st.markdown("""
- 使用列表或者元组创建向量。
- 使用特殊函数来创建向量。""")
# 文本
st.markdown("#### 列表元组创建向量")
# 文本
st.markdown("先看第一种简单的方式，使用列表或者元组来创建向量，执行下面的代码：")
# 代码
st.code(r"""
import numpy as np # 导入必要的包，这是必要的，后面书写上可能会省略
lst = [1,2,3,4,5,0,9,8,7,6]
vec = np.array(lst) # 使用np.array()函数来创建向量，同时也可以创建矩阵
print(vec)
""")
# 文本
st.markdown("程序输出的结果如下：")
# 程序
import numpy as np # 导入必要的包，这是必要的，后面书写上可能会省略
options = st.multiselect("请选择数组的元素：", [i for i in range(100)], default=[1,2,3,4,5,0,9,8,7,6])
st.write("你选的元素是：", options)
vec = np.array(options) # 使用np.array()函数来创建向量，同时也可以创建矩阵
vec
# 查看函数的帮助
if st.checkbox("是否显示函数np.array的帮助信息？"):
    st.text_area(st.help(np.array))
# 四级标题
st.markdown("#### 特殊函数创建向量")
# 文本
st.markdown("下面使用几个特殊的函数来创建几个特殊的向量，执行下面的代码：")
# 代码
st.code(r"""
vec1 = np.arange(10) # 默认从0开始，步长为1，截止到9
vec2 = np.ones(10) # 创建10个1的向量
vec3 = np.zeros(5) # 创建5个0的向量
start = 1
end = 11
vec4 = np.arange(start, end) # 创建10个元素的向量，1，2，...，10
vec5= np.empty(5) # 创建5个元素的空向量
length = 10
value = 3
vec6 = np.full(shape=length,fill_value=value)
print(vec1, vec2, vec3, vec4, vec5, vec6, sep="\n")
""")
# 文本
st.markdown("程序输出的结果如下：")
# 程序
vec1_start = st.slider("选择vec1的起始点", 0, 10, step=1, value=0)
st.caption("选择vec1的起始点为{}".format(vec1_start))
vec1_end = st.slider("选择vec1的结束点", 0, 20, step=1, value=10)
st.caption("选择vec1的结束点为{}".format(vec1_end))
vec1 = np.arange(vec1_start, vec1_end) # 默认从0开始，步长为1，截止到9
vec1
# 查看函数的帮助
if st.checkbox("是否显示函数np.arange的帮助信息？"):
    st.text_area(st.help(np.arange))

vec2_num = st.number_input("请输入要创建的向量vec2元素个数", 1, 10, value=10, step=1)
vec2 = np.ones(vec2_num) # 创建10个1的向量
vec2
# 查看函数的帮助
if st.checkbox("是否显示函数np.ones的帮助信息？"):
    st.text_area(st.help(np.ones))

vec3_num = st.number_input("请输入要创建的向量vec3元素个数", 1, 10, value=5, step=1)
vec3 = np.zeros(vec3_num) # 创建5个0的向量
vec3
# 查看函数的帮助
if st.checkbox("是否显示函数np.zeros的帮助信息？"):
    st.text_area(st.help(np.zeros))

start = st.number_input("向量vec4的起始点：",0, 10, step=1, value=1)
end = st.number_input("向量vec4的结束点：",0, 100, step=1, value=11)
vec4 = np.arange(start, end) # 创建10个元素的向量，1，2，...，10
vec4

vec5_num = st.slider("向量vec5的元素个数：", 1, 10, value=5, step=1)
vec5= np.empty(vec5_num) # 创建5个元素的空向量
vec5
# 查看函数的帮助
if st.checkbox("是否显示函数np.empty的帮助信息？"):
    st.text_area(st.help(np.empty))

vec6_length = st.number_input("向量vec6的元素个数：", 1, 10, value=10, step=1)
vec6_value = st.number_input("向量vec6的元素值：", 1, 10, value=3, step=1)
vec6 = np.full(shape=vec6_length,fill_value=vec6_value)
vec6
# 查看函数的帮助
if st.checkbox("是否显示函数np.full的帮助信息？"):
    st.text_area(st.help(np.full))
# 文本
st.markdown("需要注意的是，empty函数得到的“空向量”是一个非常小的数组成的向量，而这些非常小的数是随机生成的。")
# 三级标题
st.markdown("### 向量重构数组")
# 文本
st.markdown("现在来创建矩阵，先看第一种方法。创建向量再重构行列，重构是使用方法reshape。")
# 代码
st.code(r"""
row = 4
col = 5 # 行、列只需要指定一个即可，另一个写成-1
mat1 = np.arange(20).reshape(row, -1)
mat2 = np.reshape(np.arange(1,21), (row, col))
print(mat1, mat2, sep="\n")
""")
# 文本
st.markdown("程序输出的结果如下：")
# 程序
mat1_start = st.slider("矩阵mat1的起始点：", 0, 10, value=0, step=1)
mat1_end = st.slider("矩阵mat1的结束点：", 0, 100, value=20, step=1)

row1 = st.number_input("请输入矩阵mat1的行数：", 1, 10, value=4, step=1)
st.caption("行数和列数只需要指定其中之一即可！")

mat1 = np.arange(mat1_start, mat1_end).reshape(row1, -1)
mat1

mat2_start = st.slider("矩阵mat2的起始点：", 0, 10, value=1, step=1)
mat2_end = st.slider("矩阵mat2的结束点：", 0, 100, value=21, step=1)

row2 = st.number_input("请输入矩阵mat2的行数：", 1, 10, value=4, step=1)
st.caption("行数和列数只需要指定其中之一即可！")

mat2 = np.reshape(np.arange(mat2_start, mat2_end), (5, -1))
mat2

st.markdown("### 二维列表创建矩阵")

st.markdown("第二种方式，使用二维列表创建矩阵，执行下面的代码：")
st.code(r"""
lst = [[1,2,3], [3,2,1], [4,5,6]]
mat = np.array(lst)
print(mat)
""")


st.markdown("程序输出的结果如下：")

lst = [[1,2,3], [3,2,1], [4,5,6]]
mat = np.array(lst)
mat

st.markdown("### 特殊函数创建矩阵")

st.markdown("第三种生成矩阵的方式，是使用特殊函数直接生成矩阵。")

st.code(r"""
row = 3
col = 5
mat1 = np.ones((row, col)) # 1矩阵，直接生成必须填写一个元组作为参数
mat2 = np.zeros((row, col)) # 0矩阵，元组作参数
mat3 = np.full(shape=(row, col), fill_value=5) # 全值矩阵
print(mat1, mat2, mat3, sep="\n")
""")

st.markdown("程序输出的结果如下：")
row = st.number_input("矩阵mat1-3的行数：", 1, 10, value=3, step=1)
col = st.number_input("矩阵mat1-3的列数：", 1, 10, value=5, step=1)

mat1 = np.ones((row, col)) # 1矩阵，直接生成必须填写一个元组作为参数
mat1

mat2 = np.zeros((row, col)) # 0矩阵，元组作参数
mat2

fill_value = st.number_input("矩阵mat3的元素为：", 0, 100, value=5, step=1)
mat3 = np.full(shape=(row, col), fill_value=fill_value) # 全值矩阵
mat3

st.markdown("### 单位阵")

st.markdown("下面使用一个最实用的函数来创建单位矩阵：")
st.code(r"""
mat = np.identity(4) # 创建一个4×4的单位阵
print(mat)
""")

st.markdown("程序输出的结果如下：")
n = st.slider("单位矩阵的行数：", 1, 10, value=4, step=1)
mat = np.identity(n) # 创建一个4×4的单位阵
mat