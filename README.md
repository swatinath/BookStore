# BookStore - an online bookstore (for a single shop)
Parties involved - Admin/Seller + Users/Customers

The project can be divided into following categories :
1. User -  1.1. Admin
           1.2. Customer
2. Functionalities -
2.1. Admin - i. Login
   ii. Category (CRUD)
   iii. Book(CRUD)
   iv. Orders (RU)
   v. Logout
   vi. Profile management
2.2. Customer- i. View all Books
   ii. View books category wise
   iii. Check details
   iv. Sign up
   v. Sign in
   vi. Cart (CRUD)
   vii. Address (CRUD)
   viii. Order (CRUD)
   ix. Profile management
   x. Logout
   xi. Product review (CR)
3. Apps/ Modules - i. Admin
   ii.User
   iii. Book
   iv. Pages (Index, About, Contact)
4. Database Tables -
   4.1. User (structure given by Django)
   4.2. Category (id[pk], category )
   4.3. Book (id[pk], category_id (fk), title, author, publisher, publication_year, description, price, image, is_available)
   4.4.        
