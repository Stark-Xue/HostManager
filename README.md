# HostManager
主机管理

功能：
1、登录验证
2、主机管理
  i、查看所有主机的信息
  ii、增加主机
3、查看主机的详细信息
4、删除

两张表：
mysql> select * from host;
+----+-----------+----------+--------+-------+------------------+
| id | ip        | hostname | status | flags | description      |
+----+-----------+----------+--------+-------+------------------+
|  1 | 10.0.0.1  | fireman  |      1 |     1 | seth's computer  |
|  2 | 10.0.0.2  | qwer     |      1 |     1 | seth's computer  |
|  3 | 10.0.0.3  | asdf     |      2 |     0 | bob's computer   |
|  5 | 10.0.0.5  | uiop     |      2 |     0 | rain's computer  |
|  7 | 10.0.0.7  | vbnm     |      1 |     0 | one's computer   |
|  8 | 10.0.0.8  | abcd     |      2 |     0 | hello's computer |
| 10 | 10.0.0.11 | awe      |      1 |     1 | dsdsdds          |
| 11 | 10.0.0.2  | qwer     |      1 |     1 | seth's computer  |
| 12 | 10.0.0.3  | asdf     |      2 |     0 | bob's computer   |
| 15 | 10.0.0.6  | hjkl     |      3 |     1 | seven's computer |
+----+-----------+----------+--------+-------+------------------+
mysql> select * from user;
+----+-------+----------+
| id | name  | password |
+----+-------+----------+
|  1 | bob   | 123      |
|  2 | jack  | 1234     |
|  3 | RAIN  | 12345    |
|  4 | peter | 123456   |
+----+-------+----------+
