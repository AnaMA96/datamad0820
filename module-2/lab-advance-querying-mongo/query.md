1. {name:"Babelgum"}
2. {"number_of_employees":{$gt:5000}} (limit 20)
3. {$and:[ {"number_of_employees":{$gte:2000}} , {"number_of_employees":{$lte:2005}}]}
(project: {name:1, founded_year:1})
4. {$and:[ {"ipo.valuation_amount":{$gt:100000}}, {founded_year:{$lt:2010}}]}
(project: {ipo:1,name:1} )
5. {$and:[ {"number_of_employees":{$lt:1000}}, {founded_year:{$lt:2005}}]}
(sort: {number_of_employees:1}, limit = 10)
6. project: {partners:0}
7. {"category_field":null}
8. {$and:[ {"number_of_employees":{$gt:100}}, {"number_of_employees:{$lt:1000}}]}
(project: {name:1,number_of_employees:1})
9. sort: {"ipo":-1}
10. sort: {"number_of_employees":-1}, limit= 10
11. {"founded_month":{$gt:6}}}, limit= 1000
12. {$and: [ {"founded_year":{$lt:2000}}, {"acquisition.price_amount":{$lt:10000000}}]}
13. {$and: [ {"acquisition.acquired_year":{$gt:2010}}]}, project: {name:1, acquisition:1}, sort: {"acquisition.price_amount":1}
14. {"name":1, "founded_year":1}, {"founded_year":1}
15. {"founded_day":{$lt:7}}, sort: {"acquisition.price_amount":-1}, limit=10
16. {$and:[ {"category_code": "web"}, {"number_of_employees":{$gt:4000}}]}, sort: {"number_of_employees":-1}
17. {$and: [ {"acquisition.price_amount":{$gt:10000000}}, {"acquisition.price_currency_code":"EUR"}]}
18. {"founded_month":{$lte:3}}, sort:{name:1, acquisition:1}
19. {$and:[ {"founded_year":{$gte:2000}} , {"founded_year":{$lte:2010}}, {"acquisition.acquired_year":{$gt:2011}}]}
20. { founded_year: {$gt: 0}, $where: "this.deadpooled_year >= this.founded_year + 3 " }


