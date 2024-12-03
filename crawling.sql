insert into category_tb 
values
	(default, '냉장고'),
	(default, 'TV'),
	(default, '노트북');
    
select * from category_tb;


insert into product_tb
values
	(default, '삼성 냉장고', 100000, 1),
	(default, 'LG 냉장고', 100000, 1),
	(default, '삼성 TV', 100000, 2),
	(default, 'LG TV', 100000, 2),
	(default, '삼성 노트북', 100000, 3),
	(default, 'LG 노트북', 100000, 3);
    
select * 
from 
	product_tb pt 
    left outer join category_tb ct on(ct.category_id = pt.category_id);
    
-- 트리거 시 보통 insert는 after / delete는 before    

delete 
from
	category_tb
where
	category_name = 'TV';