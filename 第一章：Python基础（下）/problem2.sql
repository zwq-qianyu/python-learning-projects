# 1）
select * from users order by cdate limit 10;

# 2）
select b.id,b.title,b.pcount,u.name from blog b left join users u on b.uid=u.id order by pcount desc limit 5;

# 3）两种方式，一行一种
select u.id,u.name,count(*) as blog_num from users u,blog b where b.uid=u.id group by b.uid order by blog_num desc;
select u.id,u.name,count(*) as blog_num from users u right join blog b on b.uid=u.id group by b.uid order by blog_num desc;

# 4）
select u.id,u.name,avg(pcount) as avg_pcount from users u left join blog b on b.uid=u.id group by b.uid order by avg_pcount desc limit 3;

# 5）
delete from users where id not in(select uid from blog group by uid);