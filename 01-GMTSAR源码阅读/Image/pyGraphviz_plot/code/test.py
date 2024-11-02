import pygraphviz as pgv

G = pgv.AGraph(directed=True, rankdir="TB")

# 设置节点标签
Root_1 = "主影像"
Root_2 = "辅影像"
negative_1 = "影像配准"
Root_3 = "外部DEM"
negative_2 = "去平地效应"
negative_3 = "滤波"
negative_4 = "相位解缠"
negative_5 = "地表形变"
negative_6 = "地理编码"

# 添加节点
for Root in [eval(_) for _ in dir() if _.startswith("Root")]:
    G.add_node(Root, style="filled", shape="box3d", color="#feb64d")

for negative in [eval(_) for _ in dir() if _.startswith("negative")]:
    G.add_node(negative, style="filled", shape="box", color="#CFDBF6")


# 添加边
G.add_edges_from(
    [
        [Root_1, negative_1],
        [Root_2, negative_1],
        [negative_1, negative_2],
        [negative_2, negative_3],
        [negative_3, negative_4],
        [negative_4, negative_5],
        [negative_5, negative_6],
        [Root_3, negative_2],
    ],
    color="#B4DBFF",
    style="dashed",
    penwidth=1.5,
)


# 导出图形
G.layout()
G.draw("DInSAR.svg", format="svg", prog="dot")
