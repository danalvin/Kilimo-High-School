BEGIN;
--
-- Create model Student
--
CREATE TABLE "students_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "date_of_birth" date NOT NULL, "grade_level" integer NOT NULL, "enrollment_date" date NOT NULL);
COMMIT;
