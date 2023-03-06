## Text2SQL

1. 配置参数
模型配置/大模型API、数据库连接信息
2. 连接到数据库，获取所有表的列名和数据类型，作为prompt的一部分
3. 用户输入自然语言查询
3.1 大模型基于"数据库信息+自然语言查询"生成sql语句
3.2 验证sql的有效性
1) 能否执行: 大模型check/数据库执行测试/建模判断
2) 是否是用户想要的: 执行一次大模型，给当前sql的一个注释，判断注释和用户输入是否一致
3.3 支持用户修改，用户确认后执行，返回结果


参考: 
1. https://github.com/HarryVolek/aisql/blob/main/aisql.go
2. langchain sql: https://langchain.readthedocs.io/en/latest/modules/chains/examples/sqlite.html?highlight=sql
3. gpt-index, sql解决方案, https://gpt-index.readthedocs.io/en/latest/guides/sql_guide.html
