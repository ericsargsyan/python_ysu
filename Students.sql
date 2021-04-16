use master
go
create database Students
go
use Students
go
create table Faculties(
FacultyID int not null Identity(1,1),
FacultyName nvarchar(100)
)
Insert into Faculties(FacultyName) values('Faculty1'),('Faculty2'),('Faculty3'),('Faculty4'),('Faculty5')
create table Genders(
GenderID int not null Identity(1,1),
GenderName nvarchar(100)
)
Insert into Genders(GenderName) values('Male'),('Female'),('Other')
create table Subjects(
SubjectID int not null Identity(1,1),
SubjectName nvarchar(100)
)
Insert into Subjects(SubjectName) values('Subject1'),('Subject2'),('Subject3'),('Subject4')
create table Teachers(
TeacherID int not null Identity(1,1),
TeacherName nvarchar(100)
)
Insert into Teachers(TeacherName) values('Teacher1'),('teacher2'),('Teacher3'),('Teacher4')


create table Students(
StudentID int not null Identity(1,1),
FirstName nvarchar(100),
LastName nvarchar(100),
FacultyID int,
GenderID int,
BirthDate date)
Insert into Students(FirstName,LastName,FacultyID,GenderID,BirthDate)Values
('FirstName','LastName',1,1,'2000-01-01'),
('FirstName1','LastName',2,2,'2000-01-01'),
('FirstName2','LastName',3,1,'2000-01-01'),
('FirstName3','LastName',4,1,'2000-01-01'),
('FirstName4','LastName',1,1,'2000-01-01'),
('FirstName5','LastName',2,1,'2000-01-01'),
('FirstName6','LastName',3,2,'2000-01-01'),
('FirstName7','LastName',4,1,'2000-01-01'),
('FirstName8','LastName',NULL,1,'2000-01-01'),
('FirstName9','LastName',100,1,'2000-01-01'),
('FirstName10','LastName',1,10,'2000-01-01'),
('FirstName11','LastName',2,1,'2000-01-01'),
('FirstName12','LastName',3,1,'2000-01-01'),
('FirstName13','LastName',4,2,'2000-01-01'),
('FirstName14','LastName',1,1,'2000-01-01'),
('FirstName15','LastName',2,1,'2000-01-01'),
('FirstName16','LastName',3,1,'2000-01-01'),
('FirstName17','LastName',4,1,'2000-01-01'),
('FirstName18','LastName',1,2,'2000-01-01'),
('FirstName19','LastName',2,2,'2000-01-01'),
('FirstName20','LastName',3,2,'2000-01-01'),
('FirstName21','LastName',1,2,'2000-01-01'),
('FirstName22','LastName',1,5,'2000-01-01'),
('FirstName23','LastName',2,1,'2000-01-01'),
('FirstName24','LastName',3,1,'2000-01-01'),
('FirstName25','LastName',4,1,'2000-01-01'),
('FirstName26','LastName',1,1,'2000-01-01'),
('FirstName27','LastName',2,1,'2000-01-01'),
('FirstName28','LastName',2,1,'2000-01-01'),
('FirstName29','LastName',3,1,'2000-01-01'),
('FirstName30','LastName',3,NULL,'2000-01-01'),
('FirstName31','LastName',3,1,'2000-01-01'),
('FirstName32','LastName',1,1,'2000-01-01'),
('FirstName33','LastName',1,1,'2000-01-01')
update Students set LastName=LastName+cast(StudentID as varchar(10)),
BirthDate=cast(BirthDate as datetime)+cast(RAND(StudentID*1000)*1000 as int)
create table Exams(
StudentID int,SubjectID int,TeacherID int,Score int,ExamDate Date)


insert into exams(StudentID,SubjectID,TeacherID,ExamDate,score)
select StudentID,SubjectID,TeacherID,c as examdate,
cast(substring(cast(round(rand(ROW_NUMBER() over (order by studentid))*1000000,0) as varchar(100)),5,2) as int) as score 
from (values(cast('2018-01-01' as date)),('2019-01-01'),('2020-01-01'),('2021-01-01')) as t(c )
cross join Students
cross join Subjects
cross join Teachers
where teacherid=subjectid

