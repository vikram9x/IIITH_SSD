DELIMITER //
CREATE PROCEDURE q4( INOUT opList varchar(6000) ) 
BEGIN

DECLARE c1 CURSOR FOR 
SELECT CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE FROM customer WHERE AGENT_CODE LIKE "A00%";

OPEN c1;

getInfo: LOOP
FETCH c1 into x;
IF done = 1
THEN LEAVE getInfo;
END IF;


DELIMITER ;
