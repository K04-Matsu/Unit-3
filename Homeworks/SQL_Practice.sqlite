```.sqlite
-- Nagisa City with the most murders
select city from crime_scene_report where type like 'murder';

-- Reiji Benz driver
select count(car_make) from drivers_license where car_make like 'Mercedes-Benz';

-- Bee frequency of people living on same street
select address_street_name, count(address_street_name) 'Frequency'
from person group by address_street_name order by count(address_street_name) desc;

-- Elia Theft reports in SQL city
select count(city) from crime_scene_report where type like 'theft' and city like 'SQL City';

-- Kojiro Facebook events on July 2017
select count(date) from facebook_event_checkin where date > 20170700 and date < 20170800;

-- David Gold member, annual income range
select membership_status, annual_income from person
inner join income i on person.ssn inner join get_fit_now_member g
on person.name like g.name order by annual_income;

-- Michael cautious month
select date, count(date) 'Frequency'
from crime_scene_report group by date order by count(date) desc;

-- Aup Nudism crimes
select count(type) from crime_scene_report where type like 'arson';
```
