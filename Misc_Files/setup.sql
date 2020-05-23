INSERT INTO Customer
(name, email_address, telephone_number, "type")
VALUES('Jan', 'jan@vanverkoop.nl', '0652112536', 'Company');

INSERT INTO Address
(street, street_number, postal_code, city)
VALUES('Van Verkoopstraat', '12', '3023AD', 'Zeist');


INSERT INTO Company
(name, kvk_number, contact_person)
VALUES('Van Verkoop', '57438975894', 'Pieter');

INSERT INTO Customer_Data
(customer_id, address_id, company_id, consumer_id)
VALUES(1, 1, 1, 1);

---

INSERT INTO Customer
(name, email_address, telephone_number, "type")
VALUES('Kees', 'kees@gmail.com', '04674698746', 'Consumer');

INSERT INTO Address
(street, street_number, postal_code, city)
VALUES('De Kaasstraat', '112', '3523AD', 'Rotterdam');


INSERT INTO Customer_Data
(customer_id, address_id, company_id, consumer_id)
VALUES(2, 2, 2, 2);

---